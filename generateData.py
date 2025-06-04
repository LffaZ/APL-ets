import csv
import random
from datetime import datetime
import faker

fake = faker.Faker()

# Generate dummy data for 30 users
num_users = 30
user_data = []
saldo_data = []

for i in range(1, num_users + 1):
    user_id = f"user{i:03d}"
    pin = f"{random.randint(1000, 9999)}"
    nama = fake.name()
    nama_ibu = fake.first_name_female()
    tanggal_buat = fake.date_between(start_date='-5y', end_date='today').strftime("%Y-%m-%d")
    status = random.choice(["aktif", "nonaktif"])
    terakhir_transaksi = fake.date_time_between(start_date='-30d', end_date='now').strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to user data
    user_data.append([user_id, pin, nama, nama_ibu, tanggal_buat, status, terakhir_transaksi])
    
    # Generate saldo antara 100rb s/d 10jt
    saldo = random.randint(100_000, 10_000_000)
    saldo_data.append([user_id, saldo])

# Write akun.txt
with open("akun.txt", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["userID", "PIN", "Nama", "NamaIbu", "TanggalBuatAkun", "StatusAkun", "TerakhirTransaksi"])
    writer.writerows(user_data)

# Write saldo.txt
with open("saldo.txt", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["userID", "Saldo"])
    writer.writerows(saldo_data)

# Write transaksi.txt (empty for now, only header)
with open("transaksi.txt", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["TanggalWaktu", "UserID_Pengirim", "Tipe_Transaksi", "Jumlah", "UserID_Tujuan", "Status", "Sisa_Saldo"])
