import utils as ut

class LanguageSelector:
    def __init__(self, supported_languages):
        self.supported_languages = supported_languages
        self.selected_language = None

    def show_menu(self):
        ut.cprint("SILAHKAN PILIH BAHASA")
        ut.cprint("----------------------")
        ut.cprint("PLEASE SELECT YOUR LANGUAGE")
        print()
        for i, lang in enumerate(self.supported_languages, 1):
            print(f"{i}. {lang}")
        choice = ut.cinput("")
        try:
            choice = int(choice)
            if 1 <= choice <= len(self.supported_languages):
                self.selected_language = self.supported_languages[choice - 1]
            else:
                ut.cprint("Pilihan tidak valid.")
        except ValueError:
            ut.cprint("Input harus angka.")

    def get_language(self):
        return self.selected_language
