import csv
from datetime import datetime
import os

# Definisikan kelas TransactionLog terlebih dahulu
class TransactionLog:
    def __init__(self):
        self.logs = []

    def tambah_log(self, user_id, jumlah, tipe_transaksi):
        waktu_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        saldo_terbaru = self.get_saldo(user_id)
        log = {
            'TanggalWaktu': waktu_transaksi,
            'UserID': user_id,
            'Tipe_Transaksi': tipe_transaksi,
            'Jumlah': jumlah,
            'Sisa_Saldo': saldo_terbaru  # Menyimpan saldo terbaru setelah transaksi
        }
        self.logs.append(log)

    def get_saldo(self, user_id):
        # Ambil saldo berdasarkan user_id yang sesuai
        if user_id in atm.users:
            return atm.users[user_id].saldo
        return 0  # Jika user_id tidak ditemukan

    def tampilkan_log(self, user_id):
        # Menampilkan log transaksi untuk pengguna tertentu
        print(f"Log Transaksi untuk {user_id}:")
        for log in self.logs:
            if log['UserID'] == user_id:
                print(f"{log['TanggalWaktu']} | {log['Tipe_Transaksi']} | {log['Jumlah']} | Sisa Saldo: {log['Sisa_Saldo']}")

    def simpan_log(self, user_id):
        # Menyimpan log transaksi untuk setiap pengguna dalam file .txt terpisah berdasarkan user_id
        with open(f"{user_id}_transaction_log.txt", "a") as file:
            for log in self.logs:
                if log['UserID'] == user_id:
                    file.write(f"{log['TanggalWaktu']} | {log['Tipe_Transaksi']} | {log['Jumlah']} | Sisa Saldo: {log['Sisa_Saldo']}\n")


# Definisikan kelas User setelah TransactionLog
class User:
    def __init__(self, user_id, pin, nama, saldo):
        self.user_id = user_id
        self.pin = pin
        self.nama = nama
        self.saldo = saldo

    def cek_saldo(self):
        return self.saldo

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah  # Update saldo setelah pengisian
            return True
        return False

    def kurangi_saldo(self, jumlah):
        if self.saldo >= jumlah and jumlah > 0:
            self.saldo -= jumlah  # Update saldo setelah penarikan
            return True
        return False


class ATM:
    def __init__(self):
        self.users = {}
        self.transaction_log = TransactionLog()

    def load_data(self):
        # Memuat data pengguna dari akun.txt
        with open("data_atm/akun.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                user_id, pin, nama, nama_ibu, tanggal_buat, status, terakhir_transaksi = line.strip().split(",")
                self.users[user_id] = User(user_id, pin.strip(), nama.strip(), 0)

        # Memuat saldo pengguna dari data_atm/saldo.txt
        with open("data_atm/saldo.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                user_id, saldo = line.strip().split(",")
                if user_id in self.users:
                    self.users[user_id].saldo = int(saldo.strip())  # Hapus spasi ekstra

    def login(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            print(f"Selamat datang, {self.users[user_id].nama}!")
            return self.users[user_id]
        else:
            print("userID atau PIN salah!")
            return None

    def cek_saldo(self, user):
        print(f"Saldo Anda saat ini: {user.cek_saldo()}")

    def tambah_saldo(self, user):
        try:
            jumlah = int(input("Masukkan jumlah pengisian saldo: "))
            if user.tambah_saldo(jumlah):
                print(f"Saldo Anda berhasil diisi. Saldo baru: {user.cek_saldo()}")
                self.transaction_log.tambah_log(user.user_id, jumlah, 'Pengisian Saldo')
                self.simpan_saldo()  # Simpan saldo terbaru setelah transaksi
            else:
                print("Jumlah pengisian saldo tidak valid!")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def kurangi_saldo(self, user):
        try:
            jumlah = int(input("Masukkan jumlah penarikan saldo: "))
            if user.kurangi_saldo(jumlah):
                print(f"Saldo Anda berhasil ditarik. Saldo baru: {user.cek_saldo()}")
                self.transaction_log.tambah_log(user.user_id, jumlah, 'Penarikan Saldo')
                self.simpan_saldo()  # Simpan saldo terbaru setelah transaksi
            else:
                print("Jumlah penarikan saldo tidak valid atau saldo tidak cukup!")
        except ValueError:
            print("Masukkan jumlah yang valid!")

    def tampilkan_log(self, user):
        self.transaction_log.simpan_log(user.user_id)  # Menyimpan log transaksi untuk setiap pengguna dalam file
        self.transaction_log.tampilkan_log(user.user_id)  # Tampilkan log transaksi pengguna

    def simpan_saldo(self):
        # Simpan saldo yang sudah diperbarui ke data_atm/saldo.txt
        with open("data_atm/saldo.txt", "w", encoding='utf-8') as file:
            file.write("userID, Saldo\n")
            for user_id, user in self.users.items():
                file.write(f"{user_id}, {user.saldo}\n")  # Simpan saldo terbaru

    def menu(self, user):
        while True:
            print("\nMenu:")
            print("1. Cek Saldo")
            print("2. Pengisian Saldo")
            print("3. Penarikan Saldo")
            print("4. Lihat Log Transaksi")
            print("5. Keluar")

            pilihan = input("Pilih menu (1/2/3/4/5): ")

            if pilihan == '1':
                self.cek_saldo(user)
            elif pilihan == '2':
                self.tambah_saldo(user)
            elif pilihan == '3':
                self.kurangi_saldo(user)
            elif pilihan == '4':
                self.tampilkan_log(user)
            elif pilihan == '5':
                self.simpan_saldo()  # Simpan saldo sebelum keluar
                print("Terima kasih telah menggunakan ATM!")
                break
            else:
                print("Pilihan tidak valid!")


# Main program
if __name__ == "__main__":

    atm = ATM()
    atm.load_data()

    user_id = input("Masukkan userID: ")
    pin = input("Masukkan PIN: ")

    user = atm.login(user_id, pin)

    if user:
        atm.menu(user)
