import os
import random
from datetime import datetime
from filelog import FileLogger
import faker

# Setup
fake = faker.Faker('id_ID')
folder_name = "data_atm"

# Buat folder jika belum ada
os.makedirs(folder_name, exist_ok=True)

# Dummy data
num_users = 30
user_data = []
saldo_data = []
logger = FileLogger()

for i in range(1, num_users + 1):
    user_id = random.randint(10**9, 10**10 - 1)
    pin = random.randint(1000, 9999)
    nama = fake.name()
    nama_ibu = fake.first_name_female()
    saldo = random.randint(100_000, 10_000_000)

    user_data.append([user_id, pin, nama, nama_ibu, saldo])

logger.tulis_csv("data/nasabah.txt", ["userID", "PIN", "Nama", "NamaIbu", "Saldo"], user_data)

# with open(os.path.join(folder_name, "transaksi.txt"), "w", newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["TanggalWaktu", "UserID_Pengirim", "Tipe_Transaksi", "Jumlah", "UserID_Tujuan", "Status", "Sisa_Saldo"])