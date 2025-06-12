import utils as ut
from transaksi import Transaksi
class Saldo:
    def __init__(self, no_rek):
        file_nasabah = 'data/nasabah.txt'
        self.daftar_akun = ut.load_akun(file_nasabah)
        self.akun = self.daftar_akun.get(no_rek)
        self.transaksi = Transaksi()

    # def cek_saldo(self):
    #     try:
    #         with open("data_atm/saldo.txt", "r") as f:
    #             next(f)
    #             for line in f:
    #                 data = line.strip().split(", ")
    #                 if data[0] == self.user_id_aktif:
    #                     return int(data[1])
    #     except FileNotFoundError:
    #         self.cprint("❌ File saldo.txt tidak ditemukan.")
    #     return None
    
    def cek_saldo(self):
        saldo = self.akun['Saldo']
        while True:
            if saldo is not None:
                ut.cprint("INFORMASI SALDO")
                ut.cprint("=================================")
                print("SALDO ANDA SEKARANG :")
                ut.cprint(f"{saldo}")
                ut.cprint("=================================")
                ut.cprint("APAKAH ANDA INGIN MELAKUKAN TRANSAKSI LAIN?")
                ut.cprint("1 <-- YA          TIDAK --> 2")
                pilihan = ut.cinput('')
                if pilihan == '1':
                    self.transaksi.menu_utama()
                elif pilihan == '2':
                    break
                else:
                    ut.cprint("INPUT TIDAK VALID")

            else:
                self.cprint("❌ Gagal mengambil saldo.")
