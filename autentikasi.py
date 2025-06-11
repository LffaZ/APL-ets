# Login, Pemanggilan Data Akun, Logout
from filelog import FileLogger
import datetime
import utils as ut
from bahasa import LanguageSelector
from keamanan import Security

bahasa = LanguageSelector(['Bahasa'])

class Authenticator:
    def __init__(self, daftar_akun):
        self.daftar_akun = daftar_akun
        self.logger = FileLogger()
        self.keamanan = Security()
        self.session = None

    def inputnorek(self):
        no_rek = ut.cinput("")
        return no_rek
    
    def inputpin(self):
        ut.cprint('MASUKKAN NOMOR PIN ANDA:')
        pin = ut.cinput("")
        return pin

    def login(self, no_rek, pin):
        # print(f"# DEBUG: Login attempt with no_rek='{no_rek}', pin='{pin}'")  # DEBUG
        akun = self.daftar_akun.get(no_rek)
        # print(f"# DEBUG: akun ditemukan = {akun['nama']}") # DEBUG
        # print(f"# DEBUG: akun ditemukan = {no_rek}") # DEBUG

        self.keamanan = Security(no_rek)
        if self.keamanan.verifikasi(pin):
            self.session = akun
            print(f"\nSelamat datang, {akun.nama}!\n")
            return akun
        else:
            ut.cprint('PIN YANG ANDA MASUKKAN SALAH.')
        return None

    def logout(self):
        if self.session:
            norek = self.session.no_rek
            self.logger.log_per_akun(norek, "Logout")
            print(f"Anda telah logout dari akun {self.session.nama}\n")
            self.session = None