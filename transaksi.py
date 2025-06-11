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