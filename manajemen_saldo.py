class ATM:
    def __init__(self):
        self.user_id_aktif = None
        self.nama_aktif = ""

    def cprint(self, text):
        print(text)

    def login(self):
        print("Mencoba login...")
        user_id = input("Masukkan User ID: ").strip()
        pin = input("Masukkan PIN: ").strip()

        try:
            with open("data_atm/akun.txt", "r") as f:
                next(f)  # skip header
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == user_id and data[1] == pin and data[5].strip().lower() == "aktif":
                        self.user_id_aktif = user_id  # Set user_id yang aktif
                        self.nama_aktif = data[2]
                        self.cprint(f"✅ Login berhasil. Selamat datang, {self.nama_aktif}")
                        return True
        except FileNotFoundError:
            self.cprint("❌ File akun.txt tidak ditemukan.")
            return False

        self.cprint("❌ Login gagal. User ID atau PIN salah.")
        return False

    def cek_saldo(self):
        try:
            with open("data_atm/saldo.txt", "r") as f:
                next(f)  # skip header
                for line in f:
                    data = line.strip().split(", ")
                    if data[0] == self.user_id_aktif:
                        return int(data[1])
        except FileNotFoundError:
            self.cprint("❌ File saldo.txt tidak ditemukan.")
        return None

    def menu_utama(self):
        while True:
            print("\n=== MENU UTAMA ATM ===")
            print("1. Cek Saldo")
            print("2. Keluar")
            
            pilihan = input("\nPILIHAN: ")
            if pilihan == "1":
                self.menu_cek_saldo()
            elif pilihan == "2":
                print("👋 Terima kasih telah menggunakan ATM.")
                break
            else:
                print("❌ Pilihan tidak valid.")
    
    def menu_cek_saldo(self):
        saldo = self.cek_saldo()
        if saldo is not None:
            self.cprint(f"\nSaldo Anda: Rp{saldo:,.0f}")
        else:
            self.cprint("❌ Gagal mengambil saldo.")
        input("\nTekan ENTER untuk kembali ke menu utama...")

if __name__ == "__main__":
    atm = ATM()
    if atm.login():  # Kalau login sukses
        atm.menu_utama()  # Panggil menu utama untuk cek saldo
    else:
        print("❌ Login gagal")
