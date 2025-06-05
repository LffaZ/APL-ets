# tarik tunai, transfer (di bank yg sama aja), riwayat transaksi (dibuat ringkas di paging 1-5), detail riwayat transaksi 
import uuid
import datetime


class Transaksi:
    def __init__(self, tipe, jumlah, dari=None, ke=None):
        self.id = str(uuid.uuid4())
        self.tipe = tipe  # 'tarik' atau 'transfer'
        self.jumlah = jumlah
        self.dari = dari
        self.ke = ke
        self.waktu = datetime.datetime.now()

    def ringkas(self):
        return f"[{self.waktu.strftime('%Y-%m-%d %H:%M:%S')}] {self.tipe.upper()} - Rp{self.jumlah:,}"

    def detail(self):
        return {
            "id": self.id,
            "waktu": self.waktu.strftime('%Y-%m-%d %H:%M:%S'),
            "tipe": self.tipe,
            "jumlah": self.jumlah,
            "dari": self.dari,
            "ke": self.ke
        }


class AkunBank:
    def __init__(self, nama, saldo_awal=0):
        self.nama = nama
        self.saldo = saldo_awal
        self.riwayat_transaksi = []

    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak mencukupi.")
        self.saldo -= jumlah
        trx = Transaksi(tipe="tarik", jumlah=jumlah, dari=self.nama)
        self.riwayat_transaksi.append(trx)
        return trx.id

    def transfer(self, penerima: 'AkunBank', jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak mencukupi.")
        self.saldo -= jumlah
        penerima.saldo += jumlah
        trx = Transaksi(tipe="transfer", jumlah=jumlah, dari=self.nama, ke=penerima.nama)
        self.riwayat_transaksi.append(trx)
        penerima.riwayat_transaksi.append(trx)
        return trx.id

    def tampilkan_ringkasan_riwayat(self, halaman=1, per_halaman=5):
        start = (halaman - 1) * per_halaman
        end = start + per_halaman
        return [trx.ringkas() for trx in self.riwayat_transaksi[start:end]]

    def tampilkan_detail_transaksi(self, id_transaksi):
        for trx in self.riwayat_transaksi:
            if trx.id == id_transaksi:
                return trx.detail()
        return "Transaksi tidak ditemukan."


# =====================
# === CONTOH UJI COBA ===
# =====================

akun1 = AkunBank("Rudi", 2_000_000)
akun2 = AkunBank("Dina", 1_000_000)

id1 = akun1.tarik_tunai(500_000)
id2 = akun1.transfer(akun2, 300_000)

print("=== Ringkasan Riwayat Akun Rudi (Halaman 1) ===")
for r in akun1.tampilkan_ringkasan_riwayat(halaman=1):
    print(r)

print("\n=== Detail Transaksi ===")
print(akun1.tampilkan_detail_transaksi(id1))
