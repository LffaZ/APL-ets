import os
from datetime import datetime
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class User:
    def __init__(self, user_id, nama, saldo):
        self.user_id = user_id
        self.nama = nama
        self.saldo = saldo

class Transaksi:
    def __init__(self, current_user, users_dict):
        self.current_user = current_user
        self.users = users_dict  # Semua user untuk cek transfer
        self.struk_folder = "struk"
        if not os.path.exists(self.struk_folder):
            os.mkdir(self.struk_folder)

    def _buat_struk(self, isi_struk):
        waktu = datetime.now().strftime("%Y%m%d_%H%M%S")
        nama_file = f"{self.struk_folder}/struk_{self.current_user.user_id}_{waktu}.txt"
        with open(nama_file, "w") as f:
            f.write(isi_struk)

    def tarik_tunai(self):
        clear_screen()
        print("==== Tarik Tunai ====")
        print("Pilih nominal cepat atau masukkan nominal custom (minimal 50.000, kelipatan 50.000):")
        print("1. 100.000")
        print("2. 200.000")
        print("3. 300.000")
        print("4. 500.000")
        print("5. 1.000.000")
        print("6. Nominal lain")
        print("0. Batal")

        pilihan = input("Pilihan: ")
        clear_screen()

        nominal_map = {
            "1": 100_000,
            "2": 200_000,
            "3": 300_000,
            "4": 500_000,
            "5": 1_000_000
        }

        if pilihan == "0":
            print("Transaksi dibatalkan.")
            time.sleep(2)
            clear_screen()
            return

        if pilihan in nominal_map:
            nominal = nominal_map[pilihan]
        elif pilihan == "6":
            try:
                nominal = int(input("Masukkan jumlah penarikan (min 50.000, kelipatan 50.000): "))
                clear_screen()
            except:
                print("Input tidak valid.")
                time.sleep(2)
                clear_screen()
                return
        else:
            print("Pilihan tidak valid.")
            time.sleep(2)
            clear_screen()
            return

        # Validasi nominal
        if nominal < 50_000 or nominal % 50_000 != 0:
            print("Nominal harus minimal 50.000 dan kelipatan 50.000.")
            time.sleep(2)
            clear_screen()
            return

        if nominal > self.current_user.saldo:
            print("Saldo tidak cukup untuk penarikan.")
            time.sleep(2)
            clear_screen()
            return

        # Proses tarik tunai
        self.current_user.saldo -= nominal
        print(f"Silakan ambil uang Anda: Rp {nominal:,}")
        print(f"Sisa saldo: Rp {self.current_user.saldo:,}")

        # Buat struk
        isi_struk = (
            "=== STRUK PENARIKAN TUNAI ===\n"
            f"Nama: {self.current_user.nama}\n"
            f"Rekening: {self.current_user.user_id}\n"
            f"Tanggal: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Nominal Penarikan: Rp {nominal:,}\n"
            f"Sisa Saldo: Rp {self.current_user.saldo:,}\n"
            "=============================\n"
            "Terima kasih telah menggunakan ATM kami."
        )
        self._buat_struk(isi_struk)
        time.sleep(4)
        clear_screen()
        self.page_akhir_transaksi()

    def transfer(self):
        clear_screen()
        print("==== Transfer Antar Rekening ====")
        tujuan = input("Masukkan nomor rekening tujuan: ")
        clear_screen()

        if tujuan == self.current_user.user_id:
            print("Tidak bisa transfer ke rekening sendiri.")
            time.sleep(2)
            clear_screen()
            return

        if tujuan not in self.users:
            print("Nomor rekening tujuan tidak ditemukan.")
            time.sleep(2)
            clear_screen()
            return

        penerima = self.users[tujuan]
        print(f"Tujuan transfer: {penerima.nama} (Rek: {penerima.user_id})")

        try:
            nominal = int(input("Masukkan nominal transfer (minimal 50.000): "))
            clear_screen()
        except:
            print("Input nominal tidak valid.")
            time.sleep(2)
            clear_screen()
            return

        if nominal < 50_000:
            print("Minimal transfer adalah 50.000.")
            time.sleep(2)
            clear_screen()
            return

        if nominal > self.current_user.saldo:
            print("Saldo tidak cukup untuk transfer.")
            time.sleep(2)
            clear_screen()
            return

        # Konfirmasi ulang data transfer
        print("Konfirmasi data transfer:")
        print(f"Rekening asal   : {self.current_user.user_id}")
        print(f"Rekening tujuan : {penerima.user_id}")
        print(f"Nama penerima   : {penerima.nama}")
        print(f"Nominal         : Rp {nominal:,}")

        konfirmasi = input("Lanjutkan transfer? (y/n): ").lower()
        clear_screen()
        if konfirmasi != "y":
            print("Transfer dibatalkan.")
            time.sleep(2)
            clear_screen()
            return

        # Proses transfer
        self.current_user.saldo -= nominal
        penerima.saldo += nominal
        print("Transfer berhasil.")
        print(f"Sisa saldo Anda: Rp {self.current_user.saldo:,}")

        # Buat struk transfer
        isi_struk = (
            "=== STRUK TRANSFER ===\n"
            f"Nama Pengirim: {self.current_user.nama}\n"
            f"Rekening Pengirim: {self.current_user.user_id}\n"
            f"Nama Penerima: {penerima.nama}\n"
            f"Rekening Penerima: {penerima.user_id}\n"
            f"Tanggal: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Nominal Transfer: Rp {nominal:,}\n"
            f"Sisa Saldo Pengirim: Rp {self.current_user.saldo:,}\n"
            "=====================\n"
            "Terima kasih telah menggunakan ATM kami."
        )
        self._buat_struk(isi_struk)

        time.sleep(4)
        clear_screen()
        self.page_akhir_transaksi()

    def page_akhir_transaksi(self):
        print("=== Transaksi Selesai ===")
        print(f"Sisa saldo Anda: Rp {self.current_user.saldo:,}")
        print("\nPilih menu berikut:")
        print("1. Pembayaran (belum tersedia)")
        print("2. Menu Utama")
        print("3. Selesai")

        pilihan = input("Pilih: ")
        clear_screen()
        if pilihan == "1":
            print("Fitur pembayaran belum tersedia.")
            time.sleep(2)
            clear_screen()
            self.page_akhir_transaksi()
        elif pilihan == "2":
            # Kembali ke menu utama (caller harus handle ini)
            pass
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami.")
            time.sleep(2)
            clear_screen()
            # Caller bisa handle keluar atau kembali ke awal
        else:
            print("Pilihan tidak valid.")
            time.sleep(2)
            clear_screen()
            self.page_akhir_transaksi()

# Contoh penggunaan

users = {
    "1001": User("1001", "Ahmad", 1_500_000),
    "1002": User("1002", "Budi", 2_000_000)
}

current_user = users["1001"]

transaksi = Transaksi(current_user, users)

# Panggil fungsi tarik tunai
transaksi.tarik_tunai()

# Panggil fungsi transfer
transaksi.transfer()

# Setelah transaksi, caller (misal main ATM) yang atur kembali ke menu utama atau keluar
