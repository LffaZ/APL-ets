
import time, sys
class ATM:
    def __init__(self, bank, printer):
        self.bank = bank
        self.printer = printer
        self.current_account = None
        self.accounts = 'nasabah.txt'

    def insert_card(self, account_number):
        account = self.bank.find_account(account_number)

        if account:
            self.current_account = account
            return True
        return False
    def failed(self, cprint):
        self.current_account.log_action("Login Failed")
        self.current_account.failed_login()
        self.bank.save_accounts(self.accounts)
        cprint("AKUN ANDA TELAH DIBLOKIR KARENA TERLALU BANYAK PERCOBAAN LOGIN GAGAL.")
        cprint("SILAKAN KUNJUNGI BANK TERDEKAT ATAU HUBUNGI LAYANAN PELANGGAN UNTUK MEMBUKA BLOKIR.")
        time.sleep(5)
        sys.exit()
    def enter_pin(self, pin, cprint):
        if self.current_account and self.current_account.verify_pin(pin):
            if self.current_account.failed >= 3 :
                self.failed(cprint)
            self.current_account.log_action("Login")
            self.current_account.failed = 0
            return True
        else:
            if self.current_account.failed >= 2 :
                self.failed(cprint)
            cprint('TRANSAKSI TIDAK DAPAT DIPROSES')
            self.current_account = None
        return False
    def change_pin(self, old_input, new_pin):
        if self.current_account:
            old_pin = self.current_account.pin
            if old_input == old_pin:
                self.current_account.pin = new_pin
                self.current_account.log_action("Change PIN", new_pin)
                self.bank.save_accounts(self.accounts)
            return True
        return False
    def withdraw(self, amount, cprint):
        if self.current_account:
            if self.current_account.withdraw(amount):
                self.bank.save_accounts(self.accounts)
                return True
            else:
                cprint("SALDO TIDAK MENCUKUPI")
        return False
    #    Depo ga dipakai
        def deposit(self, amount):
            if self.current_account:
                if self.current_account.deposit(amount):
                    print(f"Deposited: {amount}")
                    return True
            return False
    def transfer(self, target_account_number, amount, cprint):
        if self.current_account:
            target_account = self.bank.find_account(target_account_number)
            if target_account:
                if self.current_account.transfer(target_account, amount):
                    self.bank.save_accounts(self.accounts)
                    self.printer.print_receipt(self.current_account, target_account, amount, cprint)
                    return True
                else:
                    print("TRANSAKSI TIDAK DAPAT DIPROSES.")
            else:
                cprint("TRANSAKSI TIDAK DAPAT DIPROSES. NOMOR REKENING PENERIMA TIDAK VALID ATAU TIDAK TERDAFTAR")
        return False
    def check_balance(self):
        if self.current_account:
            balance = self.current_account.get_balance()
            return balance
        return None
    def eject_card(self):
        self.current_account = None


