class Akun:
    def __init__(self, no_rek, nama, pin, saldo, login_fail):
        self.no_rek = no_rek
        self.nama = nama
        self.pin = pin
        self.saldo = saldo
        self.login_fail = login_fail
    def __getitem__(self, key):
        return getattr(self, key)
    def __setitem__(self, key, value):
        setattr(self, key, value)
        self._dirty = True