from datetime import datetime
import os

class Account:
    def __init__(self, account_number, pin, owner_name, balance=0, failed=0):
        self.account_number = account_number
        self.pin = pin
        self.owner_name = owner_name
        self.balance = balance
        self.failed = failed
        self.transaction_log = []  
        self.isbanned = self.failed >= 3

    def verify_pin(self, input_pin):
        return self.pin == input_pin
        # gadi pake depo
        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                self._add_transaction("Deposit", amount)
                return True
            return 
    def failed_login(self):
        self.failed += 1
        self.isbanned = self.failed >= 3
        return
    def transfer(self, target_account, amount):
        if 50000 <= amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self._add_transaction("Transfer Out", amount, target_account)
            target_account._add_transaction("Transfer In", amount, self)
            return True
        return False
    def withdraw(self, amount):
        if 50000 <= amount <= self.balance:
            self.balance -= amount
            self._add_transaction("Withdrawal", amount)
            return True
        return False
    def get_balance(self):
        return self.balance
    def _add_transaction(self, transaction_type, amount, account=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = {
                "type": transaction_type,
                "amount": amount,
                "time": timestamp
            }
        if account != None:
            transaction = {
                "type": transaction_type,
                "amount": amount,
                "time": timestamp,
                "num": account.account_number,
                "name": account.owner_name
            }
        self.transaction_log.append(transaction)
        self.save_transaction_log() 
    def get_transaction_log(self):
        return self.transaction_log
    def save_transaction_log(self):
        log_file_path = f"log/{self.account_number}.txt"
    
        with open(log_file_path, 'a') as file:
            for txn in self.transaction_log[-1:]: 
                if txn['type'] == 'Withdrawal':
                    msg = f"[{txn['time']}] - Tarik tunai Sebesar Rp.{txn['amount']}\n"
                elif txn['type'] == 'Transfer In':
                    msg = f"[{txn['time']}] - Menerima transfer Rp.{txn['amount']} dari {txn['num']} ({txn['name']})\n"
                elif txn['type'] == 'Transfer Out':
                    msg = f"[{txn['time']}] - Transfer Rp{txn['amount']} ke {txn['num']} ({txn['name']}\n"
                file.write(f'\n{msg}')
    def log_action(self, action, additional_info=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs('log', exist_ok=True)
        log_file_path = f"log/{self.account_number}.txt"
        if action == 'Login':
            msg = 'Login Berhasil'
        elif action == 'Login Failed':
            msg = 'Login gagal: PIN salah'
        elif action == 'Change PIN':
            msg = f'PIN diubah. PIN baru: {additional_info}'
        with open(log_file_path, 'a') as file:
            file.write(f"\n[{timestamp}] - {msg}")
