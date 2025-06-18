from account import Account
class Bank:
    def __init__(self):
        self.accounts = {}  # key: account_number, value: Account object

    def add_account(self, account):
        self.accounts[account.account_number] = account
    def find_account(self, account_number):
        return self.accounts.get(account_number)
    def validate_user(self, account_number, pin):
        account = self.find_account(account_number)
        if account and account.verify_pin(pin):
            return account
        return None
    def load_accounts(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) != 5:
                        continue  
                    account_number, pin, owner_name, balance, failed = parts
                    try:
                        balance = float(balance)
                        failed = int(failed)
                        account = Account(account_number, pin, owner_name, balance, failed)
                        self.add_account(account)
                    except ValueError:
                        print(f"Invalid balance for account {account_number}")
        except FileNotFoundError:
            print(f"File {filename} not found.")
    def save_accounts(self, filename):
        with open(filename, 'w') as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.pin},{account.owner_name},{account.balance},{account.failed}\n")