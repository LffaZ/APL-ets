class ReceiptPrinter:
    def print_receipt(self, sender, target, amount, cprint):
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

            for line in isi_struk:
                cprint(line)

            with open("struk_transfer.txt", "w", encoding="utf-8") as file:
                for line in isi_struk:
                    file.write(line + "\n")
            break
