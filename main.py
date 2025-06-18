from account import Account
from atm import ATM
from bank import Bank
from receipt import ReceiptPrinter
import shutil, os, time, sys

def cls():
    os.system('cls' if os.name == 'nt' else 'cls')
def cprint(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))
def cinput(prompt):
    columns = shutil.get_terminal_size().columns
    prompt_len = len(prompt)
    start_pos = (columns - prompt_len) // 2
    print(' ' * start_pos + prompt, end='', flush=True)
    return input()

def close(atm, bank, msg='TRANSAKSI ANDA TELAH SELESAI'):
    cls()
    print('\n\n')
    cprint(msg)
    cprint("=================================")
    cprint(f'SISA SALDO ANDA:')
    cprint(f'{atm.check_balance()}')
    cprint('APAKAH ANDA INGIN MELAKUKAN TRANSAKSI LAINNYA?\n')
    cprint("1 <-- YA          TIDAK --> 2")
    pilihan = cinput('')
    if pilihan == "1":
        print()
        main(atm, bank)
    elif pilihan == "2":
        cls()
        start()

def confirm(atm, bank, target_number, amount):
    while True:
        target_account = bank.find_account(target_number)
        cprint("KONFIRMASI TRANSFER")
        cprint("=================================")
        print(f"REK. TUJUAN  : {target_number}")
        print(f"NAMA         : {target_account.owner_name}")
        print(f"JUMLAH       : Rp.{amount},00")
        print(f"DARI REK.    : {atm.current_account.owner_name}")
        cprint("1 <-- BENAR          SALAH --> 2")
        pilihan = cinput('')
        if pilihan == "1":
            atm.transfer(target_number, amount, cprint)
            close(atm, bank)
        elif pilihan == "2":
            target_account = None
            transfer(atm,bank)

def transfer(atm, bank):
    while True:
        cls()
        print('\n\n')

        cprint("MENU TRANSFER UANG")
        cprint("=================================")
        cprint("1 <-- TRANSFER KE REKENING LAIN ")
        pilihan = cinput('')
        if pilihan == "1":
            cls()
            print('\n\n')
            cprint("TRANSFER UANG")
            cprint("=================================")
            cprint("MASUKKAN NOMOR REKENING TUJUAN")
            target = cinput('')
            cprint("1 <-- BENAR          SALAH --> 2")
            pilihan = cinput('')
            if pilihan == "1":
                cls()
                print('\n\n')
                cprint("TRANSFER UANG")
                cprint("=================================")
                cprint("MASUKKAN JUMLAH TRANSFER")
                cprint("(MINIMUM 50.000)")
                amount = int(cinput(''))
                if amount < 50000:
                    cls()
                    print('\n\n')
                    cprint('NOMINAL TIDAK MENCUKUPI. HARUS KELIPATAN 50.000.')
                    continue
                cprint("1 <-- BENAR          SALAH --> 2")
                pilihan = cinput('')
                if pilihan == "1":
                    cls()
                    print('\n\n')
                    confirm(atm, bank, target, amount)
                elif pilihan == "2":
                    amount = None
                    continue
            elif pilihan == "2":
                target = None
                continue
        else:
            cls()
            print('\n\n')
            cprint('PILIHAN TIDAK TERSEDIA')
            continue

def menu_lainnya(atm, bank):
    while True:
        cprint("PILIH TRANSAKSI YANG")
        cprint("ANDA INGINKAN")
        cprint("=================================")
        cprint("1 <-- TRANSFER UANG         CEK SALDO --> 2")
        cprint("3 <-- GANTI PIN                KELUAR --> 4")

        pilihan = cinput('')
        if pilihan == "1":
            transfer(atm, bank)
        elif pilihan == "2":
            close(atm, bank)
        elif pilihan == "3":
            change_pin(atm, bank)
        elif pilihan == "4":
            cls()
            start()
        else:
            cls()
            print('\n\n')
            cprint('PILIHAN TIDAK TERSEDIA')
            time.sleep(2)
            continue

def language():
    while True:
        cprint('SILAHKAN PILIH BAHASA')
        cprint('---------------------------')
        cprint('PLEASE SELECT YOUR LANGUAGE')

        print('1 <-------- BAHASA INDONESIA')
        choice = cinput('')
        if choice != '1':
            cprint("TRANSAKSI TIDAK DAPAT DIPROSES.")
            continue
        return 


def start():
    bank = Bank()
    bank.load_accounts("nasabah.txt")
    printer = ReceiptPrinter()

    atm = ATM(bank, printer)

    try:
        cprint("SELAMAT DATANG DI BANK JALI")
        cprint("------------------------------------------")
        cprint("WELCOME TO BANK JALI")
        print('\n\n\n')
        cprint("MASUKKAN KARTU ATM ANDA")
        cprint("------------------------")
        cprint("PLEASE INSERT YOUR CARD")
        print('\n\n')
        acc_number = cinput("")
        if not atm.insert_card(acc_number):
            cls()
            print('\n\n')
            cprint("TRANSAKSI TIDAK DAPAT DIPROSES.\nDATA AKUN TIDAK VALID ATAU TIDAK TERDAFTAR")
            return
        cls()
        print('\n\n')
        language()

        cls()
        cprint('MASUKKAN NOMOR PIN ANDA:')
        pin = cinput("")
        # print(atm.current_account.isbanned)
        # if atm.current_account.isbanned == True:
        #     print('sip')
            
        if not atm.enter_pin(pin, cprint):
            cls()
            print('\n\n')
            cprint("TRANSAKSI TIDAK DAPAT DIPROSES")
            return
        
        main(atm, bank)
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user (Ctrl+C). Keluar...")
        sys.exit()
        
def main(atm, bank):
    try:
        while True:
            cls()
            print('\n\n')
            cprint("MENU PENARIKAN CEPAT")
            cprint("SILAHKAN PILIH ATAU MASUKKAN JUMLAH PENARIKAN")
            cprint('(PECAHAN RP.50.000)')
            cprint("=====================================")
            cprint("1 <-------- 100.000               200.000 ----------> 2")
            cprint("3 <-------- 300.000               500.000 ----------> 4")
            cprint("5 <-------- 1.000.000          PEMBAYARAN ----------> 6")
            cprint("7 <-------- LAINNYA                KELUAR ----------> 8")

            choice = cinput('')

            if choice == '1':
                cls()
                amount = 100000
                atm.withdraw(amount, cprint)
                close(atm, bank)
            elif choice == '2':
                cls()
                amount = 200000
                atm.withdraw(amount, cprint)
                close(atm, bank)
            elif choice == '3':
                cls()
                amount = 300000
                atm.withdraw(amount, cprint)
                close(atm, bank)
            elif choice == '4':
                cls()
                amount = 500000
                atm.withdraw(amount, cprint)
                close(atm, bank)
            elif choice == '5':
                cls()
                amount = 1000000
                atm.withdraw(amount, cprint)
                close(atm, bank)
            elif choice == '6':
                cls()
                print('\n\n\n')
                cprint('FITUR BELUM TERSEDIA')
                cprint("1 <-------- KEMBALI                KELUAR ----------> 2")
                choice = cinput('')
                if choice == '1': 
                    main(atm, bank)
                else:
                    cls()
                    start()

            elif choice == '7':
                cls()
                menu_lainnya(atm, bank)
            elif choice == '8':
                cls()
                atm.eject_card()
                cprint("KARTU DIKELUARKAN, SAMPAI JUMPA!")
                cls()
                start()
            else:
                cls()
                amount = int(choice)
                cprint(f'PENARIKAN SEBESAR RP.{amount}')
                cprint("1 <-- BENAR          SALAH --> 2")
                choice = cinput('')
                if choice == "1":
                    cls()
                    print('\n\n\n')
                    atm.withdraw(amount, cprint)
                    close(atm, bank)
                elif choice == "2":
                    continue
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh user (Ctrl+C). Keluar...")
        sys.exit()

def change_pin(atm, bank):
    cls()
    print('\n\n')
    cprint("===================================")
    cprint("---------  GANTI PIN ATM  ---------")
    cprint("===================================\n")
    cprint('MASUKKAN PIN LAMA ANDA')
    old_pin_input = cinput('')

    cls()
    print('\n\n')
    cprint("===================================")
    cprint("---------  GANTI PIN ATM  ---------")
    cprint("===================================\n")
    cprint('MASUKKAN PIN BARU (4 DIGIT):')
    new_pin = cinput('')

    cls()
    print('\n\n')
    cprint("===================================")
    cprint("---------  GANTI PIN ATM  ---------")
    cprint("===================================\n")
    cprint('KONFIRMASI PIN BARU:')
    confirm_pin = cinput('')
    if new_pin != confirm_pin:
        print("\nPIN BARU YANG ANDA MASUKKAN TIDAK COCOK. SILAKAN COBA LAGI.")
        change_pin(atm, bank)

    atm.change_pin(old_pin_input, new_pin)
    cls()

if __name__ == "__main__":
    start()