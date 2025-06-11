import os
import random
from datetime import datetime
from filelog import FileLogger
import faker

fake = faker.Faker('id_ID')
folder_name = "data_atm"
os.makedirs(folder_name, exist_ok=True)

num_users = 30
user_data = []
saldo_data = []
logger = FileLogger()

for i in range(1, num_users + 1):
    user_id = random.randint(10**9, 10**10 - 1)
    pin = random.randint(1000, 9999)
    nama = fake.name()
    saldo = random.randint(100_000, 10_000_000)
    login_fail = 0

    user_data.append([user_id, pin, nama, saldo, login_fail])

logger.tulis_csv("data/nasabah.txt", ["userID", "PIN", "Nama", "NamaIbu", "Saldo", "LoginFail"], user_data)

# with open(os.path.join(folder_name, "transaksi.txt"), "w", newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["TanggalWaktu", "UserID_Pengirim", "Tipe_Transaksi", "Jumlah", "UserID_Tujuan", "Status", "Sisa_Saldo"])