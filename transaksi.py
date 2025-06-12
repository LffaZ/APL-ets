# tarik tunai, transfer (di bank yg sama aja), riwayat transaksi (dibuat ringkas di paging 1-5), detail riwayat transaksi
import utils as ut
from manajemen_saldo import Saldo
from filelog import FileLogger
from keamanan import Security
import time
from datetime import datetime
class Transaksi:
    def __init__(self, no_rek, start_callback=None):
        file_nasabah = 'data/nasabah.txt'
        self.daftar_akun = ut.load_akun(file_nasabah)
        self.akun = self.daftar_akun.get(no_rek)
        self.saldo = Saldo()
        self.logger = FileLogger()
        self.currsaldo = 0
        self.keamanan = Security(no_rek)
        self.start_callback = start_callback
        self.nominaltarik = 0

        self.norek_tujuan = ''
        self.tujuan = self.daftar_akun.get(self.norek_tujuan)

        self.nominal_tf = 0
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
                self.nominaltarik = int(pilihan)
                return None

    def tarik_tunai_cust(self):
        while True:
            if self.nominaltarik < 50000 or self.nominaltarik % 50000 != 0:
                print("NOMINAL TIDAK MENCUKUPI. HARUS KELIPATAN 50.000.")
                break
            elif self.akun['saldo'] <= self.nominaltarik:
                ut.cprint('SALDO TIDAK MENCUKUPI')
                break

            self.akun['saldo'] -= self.nominaltarik
            
            self.logger.log_per_akun(self.akun['no_rek'], f"Tarik tunai sebesar Rp{self.nominaltarik}")

            ut.cprint('TRANSAKSI ANDA TELAH SELESAI')
            ut.cprint('APAKAH ANDA INGIN TRANSAKSI LAINNYA?')
            print()
            ut.cprint(f'SISA SALDO ANDA: {self.akun['saldo']}')

    def tarik_tunai(self, nominal):
        while True:
            if self.akun['saldo'] <= nominal:
                ut.cprint('SALDO TIDAK MENCUKUPI')
                break
            
            self.akun['saldo'] -= nominal
            self.logger.log_per_akun(self.akun['no_rek'], f"Tarik tunai sebesar Rp{nominal}")
            
            self.log_aktivitas(f"{self.akun['nama']} melakukan penarikan Rp {nominal}")

            ut.cprint('TRANSAKSI ANDA TELAH SELESAI')
            ut.cprint('APAKAH ANDA INGIN TRANSAKSI LAINNYA?')
            print()
            ut.cprint(f'SISA SALDO ANDA: {self.akun['saldo']}')
            ut.clear_screen()

    def menu_lainnya(self):
        while True:
            ut.cprint("PILIH TRANSAKSI YANG")
            ut.cprint("ANDA INGINKAN")
            ut.cprint("=================================")
            ut.cprint("1 <-- TRANSFER UANG         CEK SALDO --> 2")
            ut.cprint("3 <-- GANTI PIN                KELUAR --> 4")

            pilihan = ut.cinput('')
            if pilihan == "1":
                self.menu_transfer()
            elif pilihan == "2":
                self.saldo.cek_saldo()
            elif pilihan == "3":
                self.keamanan.ganti
            elif pilihan == "4":
                break
            else:
                ut.cprint('PILIHAN TIDAK TERSEDIA')
                time.sleep(5)
                ut.clear_screen()

    def menu_transfer(self):
        while True:
            ut.cprint("MENU TRANSFER UANG")
            ut.cprint("=================================")
            ut.cprint("1 <-- TRANSFER KE REKENING LAIN ")
            ut.cinput('')
            
            
    def menu_rekeninglain(self):
        while True:
            ut.cprint("TRANSFER UANG")
            ut.cprint("=================================")
            ut.cprint("MASUKKAN NOMOR REKENING TUJUAN")
            self.norek_tujuan = ut.cinput('')
            ut.cprint("1 <-- BENAR          SALAH --> 2")
            pilihan = ut.cinput('')

    def menu_rekeningbenar(self):
        while True:
            ut.cprint("TRANSFER UANG")
            ut.cprint("=================================")
            ut.cprint("MASUKKAN JUMLAH TRANSFER")
            ut.cprint("(MINIMUM 50.000)")
            self.nominal_tf = int(ut.cinput(''))
            ut.cprint("1 <-- BENAR          SALAH --> 2")
            pilihan = ut.cinput('')
    
    def konfirmasi_transfer(self):
        while True:
            ut.cprint("KONFIRMASI TRANSFER")
            ut.cprint("=================================")
            print(f"REK. TUJUAN  :{self.norek_tujuan}")
            print(f"NAMA         :{self.akun['nama']}")
            print(f"JUMLAH       :Rp.{self.nominal_tf},00")
            print(f"DARI REK.    :{self.akun['no_rek']}")
            ut.cprint("1 <-- BENAR          SALAH --> 2")
            pilihan = ut.cinput('')

    def bukti_transfer(self):
        while True:
            ut.cprint("---------------------------------")
            ut.cprint("BUKTI TRANSFER")
            ut.cprint("---------------------------------")
            print(f"Tanggal      : {tanggal}")
            print(f"Waktu         : {waktu}")
            print("TRANSFER ATM")
            print(f"DARI REK.    : {self.akun['no_rek']}")
            print(f"NAMA         : {self.akun['nama']}")
            print(f"KE REK.      : {self.norek_tujuan}")
            print(f"KEPADA       : {self.tujuan['nama']}")
            print(f"JUMLAH       : Rp.{self.nominal_tf},00")
            ut.cprint("---------------------------------")
            ut.cprint("TERIMAKASIH! ☺️❤️")