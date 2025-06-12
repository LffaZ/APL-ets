# tarik tunai, transfer (di bank yg sama aja), riwayat transaksi (dibuat ringkas di paging 1-5), detail riwayat transaksi
import utils as ut
from manajemen_saldo import Saldo
from keamanan import Security
import time
from datetime import datetime
class Transaksi:
    def __init__(self, no_rek, start_callback=None):
        file_nasabah = 'data/nasabah.txt'
        self.daftar_akun = ut.load_akun(file_nasabah)
        self.akun = self.daftar_akun.get(no_rek)
        self.saldo = Saldo()
        self.keamanan = Security(no_rek)
        self.start_callback = start_callback
        # print(f"# DEBUG: daftar_akun keys = {list(daftar_akun.keys())}")  # DEBUG
        self.keluar = 0

    def menu_utama(self):
        while True:
            ut.cprint("MENU PENARIKAN CEPAT")
            ut.cprint("SILAHKAN PILIH JUMLAH PENARIKAN")
            ut.cprint('(PECAHAN RP.50.000)')
            ut.cprint("=====================================")
            ut.cprint("1 <-------- 100.000               200.000 ----------> 2")
            ut.cprint("3 <-------- 300.000               500.000 ----------> 4")
            ut.cprint("5 <-------- 1.000.000          PEMBAYARAN ----------> 6")
            ut.cprint("7 <-------- LAINNYA                KELUAR ----------> 8")
            pilihan = ut.cinput('')

            # if pilihan == "8":
            #     self.keluar()
            #     break
            if pilihan == "1":
                self.tarik_tunai(100000)
            elif pilihan == "2":
                self.tarik_tunai(200000)
            elif pilihan == "3":
                self.tarik_tunai(300000)
            elif pilihan == "4":
                self.tarik_tunai(500000)
            elif pilihan == "5":
                self.tarik_tunai(1000000)
            elif pilihan == "6":
                ut.cprint('Fitur belum tersedia')
                # try:
                #     jumlah = int(input("Masukkan jumlah penarikan (minimal 50.000): "))
                #     ut.clear_screen()
                #     self.tarik_tunai(jumlah)
                # except:
                #     print("Input tidak valid.")
                #     time.sleep(2)
                #     ut.clear_screen()
            elif pilihan == "7":
                self.menu_lainnya()
            elif pilihan == '8':
                if self.start_callback:
                    self.start_callback()
                break
            else:
                jumlah = pilihan

    def tarik_tunai_cust(self, jumlah):
        if jumlah < 50000 or jumlah % 50000 != 0:
            print("Nominal tidak valid. Harus kelipatan 50.000.")
        elif self.akun['saldo'] <= jumlah:
            ut.cprint('SALDO TIDAK MENCUKUPI')
            return None

    def tarik_tunai(self, jumlah):
        ut.cprint('TRANSAKSI ANDA TELAH SELESAI')
        ut.cprint('APAKAH ANDA INGIN TRANSAKSI LAINNYA?')
        print()
        ut.cprint(f'SISA SALDO ANDA: {self.akun['saldo']}')


        if jumlah < 50000 or jumlah % 50000 != 0:
            print("Nominal tidak valid. Harus kelipatan 50.000.")
        elif self.akun['saldo'] >= jumlah:
            self.akun['saldo'] -= jumlah
            isi_struk = f"TRANSAKSI PENARIKAN\nNama: {self.akun['nama']}\nJumlah: Rp {jumlah}\nSisa Saldo: Rp {self.akun['saldo']}"
            write_struk("tarik_tunai", isi_struk)
            print(f"Silakan ambil uang Anda: Rp {jumlah}")
            print(f"Sisa saldo: Rp {self.akun['saldo']}")
            self.log_aktivitas(f"{self.akun['nama']} melakukan penarikan Rp {jumlah}")
            self.setelah_transaksi()
        else:
            print("Saldo tidak mencukupi.")
            time.sleep(3)
        ut.clear_screen()

    def lainnya(self):
        print('1. TRANSFER UANG')
        print('2. CEK SALDO')
        print('3. GANTI PIN')
        pilihan = input('')

        if pilihan == '1':
            transfer()
        elif pilihan == '2':
            x.cek_saldo
        elif pilihan == '3':
            
        else:
            print('Input anda tidak valid')
            break

    def menu_lainnya(self):
        while True:
            ut.cprint("PILIH TRANSAKSI YANG")
            ut.cprint("ANDA INGINKAN")
            ut.cprint("=================================")
            ut.cprint("TEKAN <0> UNTUK BATAL\n")
            ut.cprint("1 <-- GANTI PIN             PENARIKAN TUNAI --> 2")
            ut.cprint("3 <-- TRANSFER              CEK SALDO --> 4")
            ut.cprint("5 <-- PEMBAYARAN            MENU SEBELUMNYA --> 6")
            ut.cprint("7 <-- KELUAR")

            pilihan = input("\nPILIHAN: ")
            if pilihan == "0" or pilihan == "7":
                self.keluar()
                break
            elif pilihan == "1":
                self.ganti_pin()
            elif pilihan == "2":
                self.menu_utama()
            elif pilihan == "3":
                self.menu_transfer()
            elif pilihan == "4":
                self.cek_saldo()
            elif pilihan == "5":
                self.menu_pembayaran()
            elif pilihan == "6":
                self.menu_lainnya()
            else:
                print("Pilihan tidak tersedia.")
                time.sleep(2)
    def menu_transfer(self):
        while True:
            ut.cprint("MENU TRANSFER")
            ut.cprint("=================================")
            ut.cprint("TEKAN <0> UNTUK BATAL\n")
            ut.cprint("1 <-- TRANSFER KE REKENING LAIN      MENU SEBELUMNYA --> 2")
            ut.cprint("3 <-- KELUAR")
