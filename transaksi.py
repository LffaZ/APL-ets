# tarik tunai, transfer (di bank yg sama aja), riwayat transaksi (dibuat ringkas di paging 1-5), detail riwayat transaksi
import utils as ut
import time
from datetime import datetime
class Transaksi:
    def __init__(self):
        self = self

    def menu_utama(self):
        while True:
            ut.cprint("MENU PENARIKAN CEPAT")
            ut.cprint("SILAHKAN PILIH JUMLAH PENARIKAN")
            ut.cprint('(PILIH "MENU LAIN")')
            ut.cprint("=================================")
            ut.cprint("TEKAN <0> UNTUK BATAL\n")
            ut.cprint("1. 100.000")
            ut.cprint("2. 200.000")
            ut.cprint("3. 300.000")
            ut.cprint("4. 500.000")
            ut.cprint("5. 1.000.000")
            ut.cprint("6. PENARIKAN JUMLAH LAIN")
            ut.cprint("7. MENU LAINNYA")
            ut.cprint("8. KELUAR")

            pilihan = input("\nPILIHAN: ")
            if pilihan == "0" or pilihan == "8":
                self.keluar()
                break
            elif pilihan == "1":
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
                try:
                    jumlah = int(input("Masukkan jumlah penarikan (minimal 50.000): "))
                    ut.clear_screen()
                    self.tarik_tunai(jumlah)
                except:
                    print("Input tidak valid.")
                    time.sleep(2)
                    ut.clear_screen()
            elif pilihan == "7":
                    self.menu_lainnya()
            else:
                print("Pilihan tidak tersedia.")
                time.sleep(2)
                ut.clear_screen()

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
            
    def menu_rekeninglain(self):
        while True:
            ut.cprint("TRANSFER KE REKENING LAIN")
            ut.cprint("=================================")
            ut.cprint("MASUKKAN NOMOR REKENING TUJUAN")
            ut.cprint("1 <-- BENAR          SALAH --> 2")

    def menu_rekeningbenar(self):
        while True:
            ut.cprint("TRANSFER KE REKENING LAIN")
            ut.cprint("=================================")
            ut.cprint("MASUKKAN JUMLAH TRANSFER")
            ut.cprint("(MINIMUM 50.000)")
            ut.cprint("1 <-- BENAR          SALAH --> 2")
    
    def konfirmasi_transfer(self, rek_tujuan, nama, jumlah, rek_asal):
        while True:
            ut.cprint("KONFIRMASI TRANSFER")
            ut.cprint("=================================")
            print("REK. TUJUAN  :{rek_tujuan}")
            print("NAMA         :{nama}")
            print("JUMLAH       :Rp.{jumlah},00")
            print("DARI REK.    :{rek_asal}")
            ut.cprint("1 <-- BENAR          SALAH --> 2")

    def bukti_transfer(self):
        while True:
            ut.cprint("---------------------------------")
            ut.cprint("BUKTI TRANSFER")
            ut.cprint("---------------------------------")
            print("Tanggal      : {tanggal}")
            print("Waktu         : {waktu}")
            print("TRANSFER ATM")
            print("DARI REK.    : {rek_asal}")
            print("NAMA         : {nama_asal}")
            print("KE REK.      : {rek_tujuan}")
            print("KEPADA       : {nama}")
            print("JUMLAH       : Rp.{jumlah},00")
            ut.cprint("---------------------------------")
            ut.cprint("TERIMAKASIH! ☺️❤️")

# MANAJEMEN SALDO

    def cek_saldo(self):
        ut.cprint("INFORMASI SALDO")
        ut.cprint("=================================")
        print("SALDO ANDA SEKARANG :")
        ut.cprint("{self.saldo}")
        ut.cprint("=================================")
        ut.cprint("APAKAH ANDA INGIN MELAKUKAN TRANSAKSI LAIN?")
        ut.cprint("1 <-- YA          TIDAK --> 2")
