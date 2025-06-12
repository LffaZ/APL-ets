import os
import time
from datetime import datetime

class ATM:
    def __init__(self):
        self.users = {}
        self.language = None
        self.user_id = None

    def clear_screen(self):
        """Clear the terminal screen (like clearing the ATM screen)"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_welcome(self):
        """Tampilan Selamat datang dan pilihan bahasa"""
        self.clear_screen()
        print("Selamat datang di Mesin ATM!")
        print("Pilih bahasa / Select Language")
        print("1. Bahasa Indonesia")
        print("2. English")
        choice = input("Pilih: ")

        if choice == "1":
            self.language = "id"
            print("Bahasa Indonesia dipilih.")
        elif choice == "2":
            self.language = "en"
            print("English selected.")
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)
            self.show_welcome()

        time.sleep(2)

    def load_data(self):
        """Memuat data dari akun.txt dan saldo.txt"""
        with open("data_atm/akun.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                line = line.strip()
                if line:
                    data = line.split(",")
                    if len(data) == 7:
                        user_id, pin, nama, nama_ibu, tanggal_buat, status, terakhir_transaksi = data
                        self.users[user_id] = {"pin": pin, "nama": nama, "saldo": 0}

        with open("data_atm/saldo.txt", "r", encoding='utf-8') as file:
            lines = file.readlines()[1:]  # Skip header
            for line in lines:
                line = line.strip()
                if line:
                    user_id, saldo = line.split(",")
                    if user_id in self.users:
                        self.users[user_id]["saldo"] = int(saldo)

    def login(self):
        """Proses login untuk memasukkan userID dan PIN"""
        print("Masukkan UserID dan PIN")
        self.user_id = input("UserID: ")
        pin = input("PIN: ")
        print(self.users)
        print(self.user_id in self.users)
        print(self.users[self.user_id]["pin"] == pin)

        if self.user_id in self.users and self.users[self.user_id]["pin"] == pin:
            print(f"Selamat datang, {self.users[self.user_id]['nama']}!")
            return True
        else:
            print("UserID atau PIN salah!")
            return False

    def main_menu(self):
        """Menu utama ATM"""
        while True:
            self.clear_screen()
            print("1. Cek Saldo / Check Balance")
            print("2. Pengisian Saldo / Deposit")
            print("3. Tarik Tunai / Withdraw")
            print("4. Transfer")
            print("5. Keluar / Exit")
            choice = input("Pilih: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                print("Terima kasih telah menggunakan ATM kami / Thank you for using our ATM!")
                time.sleep(1)
                break
            else:
                print("Pilihan tidak valid!")
                time.sleep(1)

    def check_balance(self):
        """Cek saldo pengguna"""
        self.clear_screen()
        print(f"Saldo Anda saat ini / Your current balance: {self.users[self.user_id]['saldo']}")
        input("Tekan Enter untuk kembali ke menu utama / Press Enter to go back to main menu.")
    
    def deposit(self):
        """Pengisian saldo"""
        self.clear_screen()
        print("Masukkan jumlah pengisian saldo / Enter deposit amount:")
        amount = int(input("Amount: "))
        if amount > 0:
            self.users[self.user_id]['saldo'] += amount
            print(f"Saldo berhasil diisi! / Deposit successful. New balance: {self.users[self.user_id]['saldo']}")
            self.add_transaction_log("Pengisian Saldo", amount)
        else:
            print("Jumlah tidak valid! / Invalid amount!")
        input("Tekan Enter untuk kembali ke menu utama / Press Enter to go back to main menu.")

    def withdraw(self):
        """Tarik tunai"""
        self.clear_screen()
        print("Pilih nominal tarik tunai / Select withdrawal amount:")
        print("1. 100.000")
        print("2. 300.000")
        print("3. 500.000")
        print("4. 1.000.000")
        print("5. Custom (minimal 50.000)")
        choice = input("Pilih: ")

        if choice == "1":
            amount = 100000
        elif choice == "2":
            amount = 300000
        elif choice == "3":
            amount = 500000
        elif choice == "4":
            amount = 1000000
        elif choice == "5":
            amount = int(input("Masukkan jumlah tarik tunai (minimal 50.000): "))
            if amount < 50000:
                print("Jumlah minimal tarik tunai adalah 50.000!")
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        if self.users[self.user_id]['saldo'] >= amount:
            self.users[self.user_id]['saldo'] -= amount
            print(f"Tarik tunai berhasil! / Withdrawal successful. New balance: {self.users[self.user_id]['saldo']}")
            self.add_transaction_log("Tarik Tunai", amount)
        else:
            print("Saldo tidak cukup! / Insufficient balance.")
        input("Tekan Enter untuk kembali ke menu utama / Press Enter to go back to main menu.")

    def transfer(self):
        """Transfer ke akun lain"""
        self.clear_screen()
        print("Masukkan UserID tujuan transfer / Enter recipient UserID:")
        recipient_id = input("UserID Tujuan: ")

        if recipient_id not in self.users:
            print("UserID tujuan tidak ditemukan! / Recipient UserID not found!")
            return

        amount = int(input("Masukkan jumlah transfer / Enter transfer amount (minimum 50.000): "))
        if amount < 50000:
            print("Jumlah transfer minimal adalah 50.000! / Minimum transfer amount is 50,000.")
            return

        if self.users[self.user_id]['saldo'] >= amount:
            # Tampilkan informasi penerima
            print(f"\nInformasi UserID Tujuan: {recipient_id}")
            print(f"Nama: {self.users[recipient_id]['nama']}")
            print(f"Jumlah Transfer: {amount}")
            print(f"UserID Pengirim: {self.user_id}")
            
            confirmation = input("\nKonfirmasi transfer (y/n): ")
            if confirmation.lower() == 'y':
                self.users[self.user_id]['saldo'] -= amount
                self.users[recipient_id]['saldo'] += amount
                print(f"Transfer berhasil! / Transfer successful. Your new balance: {self.users[self.user_id]['saldo']}")
                self.add_transaction_log("Transfer", amount, recipient_id)
            else:
                print("Transfer dibatalkan! / Transfer cancelled.")
        else:
            print("Saldo tidak cukup untuk transfer! / Insufficient balance for transfer.")
        input("Tekan Enter untuk kembali ke menu utama / Press Enter to go back to main menu.")

    def add_transaction_log(self, transaction_type, amount, recipient_id=None):
        """Mencatat log transaksi per pengguna dalam file yang lebih readable"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "Berhasil" if amount > 0 else "Gagal"
        saldo_after = self.users[self.user_id]['saldo']

        # Pastikan direktori untuk log ada
        log_dir = "data_atm/logs"
        os.makedirs(log_dir, exist_ok=True)

        # Menyimpan log transaksi di file per pengguna dengan format yang lebih readable
        log_filename = f"{log_dir}/{self.user_id}_log.txt"
        with open(log_filename, "a", encoding="utf-8") as file:
            file.write(f"\n----------------------------------------\n")
            file.write(f"       STRUK TRANSAKSI ATM\n")
            file.write(f"----------------------------------------\n")
            file.write(f"Tanggal       : {timestamp}\n")
            file.write(f"Tipe Transaksi: {transaction_type}\n")
            file.write(f"Jumlah        : {amount} IDR\n")
            file.write(f"Nama          : {self.users[self.user_id]['nama']}\n")
            file.write(f"Saldo Setelah : {saldo_after} IDR\n")
            file.write(f"----------------------------------------\n")

    def start(self):
        """Memulai aplikasi ATM"""
        self.show_welcome()
        while not self.login():
            self.clear_screen()
            print("Silakan coba lagi / Please try again.")

        self.load_data()  # Memuat data setelah login
        self.main_menu()


# Memulai mesin ATM
atm = ATM()
atm.start()
