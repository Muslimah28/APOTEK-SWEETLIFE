import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "APOTEK_SWEETLIFE"
)

cursor = connection.cursor()

# data_to_insert = [
#     {"id_obat": "A001", "nama_obat": "Paracetamol", "jenis_obat": "Antipiretik", "harga" : 15000, "stok": 20},
#     {"id_obat": "A002", "nama_obat": "Ibuprofen", "jenis_obat": "Antipiretik", "harga" : 10000, "stok": 15},
#     {"id_obat": "B001", "nama_obat": "Ketorolac", "jenis_obat": "Analgesik", "harga" : 12000, "stok": 10},
#     {"id_obat": "C001", "nama_obat": "Amoxicilin", "jenis_obat": "Antibiotik", "harga" : 5000, "stok": 30},
#     {"id_obat": "C002", "nama_obat": "Ciprofloxacin", "jenis_obat": "Antibiotik", "harga" : 6000, "stok": 17},
#     {"id_obat": "D001", "nama_obat": "Diclofenac", "jenis_obat": "Antiinflamasi Nonsteroid(AINS)", "harga" : 5000, "stok": 8},
#     {"id_obat": "D002", "nama_obat": "Naproxen", "jenis_obat": "Antiinflamasi Nonsteroid(AINS)", "harga" : 7000, "stok": 6},
#     {"id_obat": "E001", "nama_obat": "Cetirizine", "jenis_obat": "Antihistamin", "harga" : 9000, "stok": 12},
#     {"id_obat": "E002", "nama_obat": "Loratadine", "jenis_obat": "Antihistamin", "harga" : 6000, "stok": 18},
#     {"id_obat": "F001", "nama_obat": "Fluconazole", "jenis_obat": "Antifungal", "harga" : 8000, "stok": 5},
#     {"id_obat": "F002", "nama_obat": "Nystatin", "jenis_obat": "Antifungal", "harga" : 1000, "stok": 0},
#     {"id_obat": "G001", "nama_obat": "Acyclovir", "jenis_obat": "Antiviral", "harga" : 7000, "stok": 15},
#     {"id_obat": "G002", "nama_obat": "Oseltamivir", "jenis_obat": "Antiviral", "harga" : 8500, "stok": 14},
#     {"id_obat": "H001", "nama_obat": "Metformin", "jenis_obat": "Antidiabetik", "harga" : 7000, "stok": 15},
#     {"id_obat": "H002", "nama_obat": "Glibenclamide", "jenis_obat": "Antidiabetik", "harga" : 10000, "stok": 20},
#     {"id_obat": "I001", "nama_obat": "Furosemide", "jenis_obat": "Diuretik", "harga" : 8000, "stok": 16},
#     {"id_obat": "I002", "nama_obat": "Spironolactone", "jenis_obat": "Diuretik", "harga" : 7000, "stok": 17},
#     {"id_obat": "J001", "nama_obat": "Aluminium Hydroxide", "jenis_obat": "Antasida", "harga" : 5000, "stok": 19},
#     {"id_obat": "J002", "nama_obat": "Magnesium Hydroxide", "jenis_obat": "Antasida", "harga" : 25000, "stok": 50},
#     {"id_obat": "K001", "nama_obat": "Salbutamol", "jenis_obat": "Bronkodilator", "harga" : 13000, "stok": 14},
#     {"id_obat": "K002", "nama_obat": "Ipratropium Bromide", "jenis_obat": "Bronkodilator", "harga" : 15000, "stok": 8},
# ]
# insert_query = "INSERT INTO obat (id_obat, nama_obat, jenis_obat, harga, stok) VALUES (%s, %s, %s, %s, %s)"

# cursor.executemany(insert_query, [(data["id_obat"], data["nama_obat"], data["jenis_obat"], data["harga"], data["stok"]) for data in data_to_insert])

# query = "SELECT * FROM obat"
# cursor.execute(query)
# results = cursor.fetchall()
# for row in results:
#     print(row)

# connection.commit()
# cursor.close()
# connection.close()

# data_to_insert = [
#     {"id_pegawai": "P001", "nama_pegawai": "Najwa", "jenis_kelamin": "Perempuan", "alamat": "Aceh Besar", "no_telepon": "081210893423"},
#     {"id_pegawai": "P002", "nama_pegawai": "Muslimah", "jenis_kelamin": "Perempuan", "alamat": "Aceh Selatan", "no_telepon": "085260353198"},
#     {"id_pegawai": "P003", "nama_pegawai": "Ismulianur", "jenis_kelamin": "Perempuan", "alamat": "Pidie Jaya", "no_telepon": "087896532106"},
#     {"id_pegawai": "P004", "nama_pegawai": "Hafsah", "jenis_kelamin": "Perempuan", "alamat": "Aceh Barat Daya", "no_telepon": "082345231980"}
# ]

# insert_query = "INSERT INTO pegawai (id_pegawai, nama_pegawai, jenis_kelamin, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"

# cursor.executemany(insert_query, [(data["id_pegawai"], data["nama_pegawai"], data["jenis_kelamin"], data["alamat"], data["no_telepon"]) for data in data_to_insert])

# query = "SELECT * FROM pegawai"
# cursor.execute(query)
# results = cursor.fetchall()
# for row in results:
#     print(row)

# connection.commit()
# cursor.close()

data_to_insert = [
    # {"id_pelanggan": 1, "nama_pelanggan": "Ana", "Alamat": "Batoh"},
    # {"id_pelanggan": 2, "nama_pelanggan": "Alice", "Alamat": "Rukoh"},
    {"id_pelanggan": 3, "nama_pelanggan": "Angel", "Alamat": "Batoh"},
    {"id_pelanggan": 4, "nama_pelanggan": "Siti", "Alamat": "Batoh"},

]

insert_query = "INSERT INTO pelanggan (id_pelanggan, nama_pelanggan, Alamat) VALUES (%s, %s, %s)"

cursor.executemany(insert_query, [(data["id_pelanggan"], data["nama_pelanggan"], data["Alamat"]) for data in data_to_insert])

query = "SELECT * FROM pelanggan"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)

connection.commit()
cursor.close()