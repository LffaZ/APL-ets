class Akun:
    def __init__(self, no_rek, nama, pin, login_fail):
        self.no_rek = no_rek
        self.nama = nama
        self.pin = pin
        self.login_fail = login_fail
    def __getitem__(self, key):
        return getattr(self, key)