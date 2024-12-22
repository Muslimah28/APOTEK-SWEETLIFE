import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database= "APOTEK_SWEETLIFE"
)

cursor = connection.cursor()
# if connection :
#     print("berhasil terhubung ke database")

#     # cursor.execute('CREATE DATABASE APOTEK_SWEETLIFE')
#     # print('database berhasil dibuat')

# cursor.execute("show databases")
# print(cursor.fetchall())

# result = cursor.fetchall()
# for item in result:
#     print(item)
    

# P E M B U A T A N  T A B L E S

# query = """CREATE TABLE  obat(
#     id_obat INT PRIMARY KEY AUTO_INCREMENT,
#     nama_obat VARCHAR(255) NOT NULL,
#     jenis_obat VARCHAR(255) NOT NULL,
#     harga DECIMAL(10, 2) NOT NULL,
#     stok INT NOT NULL
#     )
#     """

# cursor.execute(query)
# print("Tabel obat Berhasi Dibuat!!")

# query = """ALTER TABLE obat 
#            MODIFY COLUMN id_obat INT"""
# cursor.execute(query)
# print("Kolom 'id_obat' berhasil diubah menjadi INT biasa tanpa AUTO_INCREMENT.")

# cursor.execute("show tables")
# print(cursor.fetchall())

# result = cursor.fetchall()
# for item in result:
#         print(item)


# query = """CREATE TABLE pegawai (
#     id_pegawai INT PRIMARY KEY AUTO_INCREMENT,
#     nama_pegawai VARCHAR(255) NOT NULL,
#     jenis_kelamin VARCHAR(10) NOT NULL,
#     alamat TEXT NOT NULL,
#     no_telepon VARCHAR(20) NOT NULL
#     )
#     """

# query = """ALTER TABLE pegawai 
#            MODIFY COLUMN id_pegawai INT"""
# cursor.execute(query)
# print("Kolom 'id_pegawai' berhasil diubah menjadi INT biasa tanpa AUTO_INCREMENT.")

# cursor.execute(query)
# print("Tabel pegawai Berhasi Dibuat!!")

# cursor.execute("show tables")
# print(cursor.fetchall())

# query = """CREATE TABLE pelanggan (
#     id_pelanggan INT PRIMARY KEY AUTO_INCREMENT ,
#     nama_pelanggan VARCHAR(255) NOT NULL,
#     Alamat varchar(30)             
#     )
#     """

# query = """ALTER TABLE pelanggan
#            MODIFY COLUMN id_pelanggan INT"""
# cursor.execute(query)
# print("Kolom 'id_pelanggan' berhasil diubah menjadi INT biasa tanpa AUTO_INCREMENT.")

# cursor.execute(query)
# print("Tabel pelanggan Berhasi Dibuat!!")

# cursor.execute("show tables")
# print(cursor.fetchall())


# query = """ALTER TABLE obat 
#            MODIFY COLUMN id_obat VARCHAR(30)"""
# cursor.execute(query)
# print("Kolom 'id_obat' berhasil diubah menjadi VARCHAR.")

# cursor.execute("show tables")
# print(cursor.fetchall())


query = """CREATE TABLE transaksi (
    id_transaksi VARCHAR(30) PRIMARY KEY,
    tanggal_transaksi DATE NOT NULL,
    waktu_transaksi TIME NOT NULL,
    id_pelanggan VARCHAR(30),
    jumlah INT,
    beli_obat INT,
    total_harga DECIMAL(10, 2) NOT NULL,
    status_transaksi ENUM('LUNAS', 'BELUM LUNAS') NOT NULL DEFAULT 'BELUM LUNAS',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """

cursor.execute(query)
print("Tabel transaksi Berhasi Dibuat!!")

cursor.execute("show tables")
print(cursor.fetchall())

cursor.execute("DESC transaksi")
result = cursor.fetchall()
for row in result :
    print(row)

query = "ALTER TABLE transaksi ADD CONSTRAINT fk_id_pelanggan FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id_pelanggan)"
cursor.execute(query)
print(cursor.fetchall())

cursor.execute("DESC transaksi")
result = cursor.fetchall()
for row in result :
    print(row)


connection.commit()
cursor.close()
connection.close()
    