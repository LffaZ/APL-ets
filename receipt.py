class ReceiptPrinter:
    def print_receipt(self, sender, target, amount, cprint):
        # print("\n===== ATM RECEIPT =====")
        # print(f"Account: {account.account_number}")
        # print(f"Owner  : {account.owner_name}")
        # print(f"Balance: {account.get_balance()}")
        # print("\n--- Transaction History ---")
        # if not account.get_transaction_log():
        #     print("No recent transactions.")
        # else:
        #     for txn in account.get_transaction_log()[-5:]:  # tampilkan 5 terakhir
        #         print(f"{txn['time']} - {txn['type']} - {txn['amount']}")
        # print("=========================\n")

        while True:
            isi_struk = []
            isi_struk.append("---------------------------------")
            isi_struk.append("BUKTI TRANSFER")
            isi_struk.append("---------------------------------")
            isi_struk.append("TRANSFER ATM")
            isi_struk.append(f"DARI REK.    : {sender.account_number}")
            isi_struk.append(f"NAMA         : {sender.owner_name}")
            isi_struk.append(f"KE REK.      : {target.account_number}")
            isi_struk.append(f"KEPADA       : {target.owner_name}")
            isi_struk.append(f"JUMLAH       : Rp.{amount},00")
            isi_struk.append("---------------------------------")
            isi_struk.append("TERIMAKASIH! ☺️❤️")

            # Cetak ke terminal (opsional)
            for line in isi_struk:
                cprint(line)

            # Simpan ke file TXT
            with open("struk_transfer.txt", "w", encoding="utf-8") as file:
                for line in isi_struk:
                    file.write(line + "\n")
            break
