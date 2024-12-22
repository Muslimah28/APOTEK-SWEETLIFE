import mysql.connector
from tabulate import tabulate 
from datetime import datetime
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, init
import pyfiglet
import os

init(autoreset=True)

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="APOTEK_SWEETLIFE"
)

cursor = connection.cursor()

def center_text(text):
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    return text.center(terminal_width)

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def tampilkan_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    for i, line in enumerate(ascii_art.splitlines()):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(color + center_text(line) + Style.RESET_ALL)

def tampilkan_menu():
    menu_lines = [
        "+" + "-" * 38 + "+",
        "          |    {:^38}  |".format(f"{Fore.RED} --MENU UTAMA APOTEK SWEETLIFE--{Style.RESET_ALL}"),
        "+" + "-" * 38 + "+",
        "          | {:<2} {:<35}       |".format("[1]", f"{rainbow_colors[1]}Insert Data{Style.RESET_ALL}"),
        "          | {:<3} {:<35}       |".format("[2]", f"{rainbow_colors[2]}Delete Data{Style.RESET_ALL}"),
        "          | {:<3} {:<35}       |".format("[3]", f"{rainbow_colors[3]}Update Data{Style.RESET_ALL}"),
        "          | {:<3} {:<35}       |".format("[4]", f"{rainbow_colors[4]}Search Data{Style.RESET_ALL}"),
        "          | {:<3} {:<35}       |".format("[5]", f"{rainbow_colors[5]}Show Data{Style.RESET_ALL}"),
        "          | {:<3} {:<35}       |".format("[0]", f"{rainbow_colors[0]}Log Out{Style.RESET_ALL}"),
        "+" + "-" * 38 + "+",
    ]
    for line in menu_lines:
        print(center_text(line))

def tampilkan_insert():
        table_width = 40
        print("   ")
        title = "PILIH DATA YANG INGIN DITAMBAHKAN <> "
        data_lines = [
            Fore.RED + "+" + "-" * table_width + "+",  
            Fore.RED + "|{:^{width}}|".format(title, width=table_width),  
            Fore.RED + "+" + "-" * table_width + "+",  
            Fore.RED + "| {:<3} {:<{width}} |".format("[1]", "Data Obat", width=table_width - 6), 
            Fore.RED + "| {:<3} {:<{width}} |".format("[2]", "Data Pegawai", width=table_width - 6), 
            Fore.RED + "| {:<3} {:<{width}} |".format("[3]", "Data Pelanggan", width=table_width - 6), 
            Fore.RED + "| {:<3} {:<{width}} |".format("[4]", "Data Transaksi", width=table_width - 6), 
            Fore.RED + "| {:<3} {:<{width}} |".format("[5]", "Kembali ke Menu Utama", width=table_width - 6), 
            Fore.RED + "+" + "-" * table_width + "+",  
        ]
        for line in data_lines:
            print(center_text(line))

def tampilkan_delete():
        table_width = 40
        print("   ")
        title = "PILIH DATA YANG INGIN DIHAPUS <> "
        data_lines = [
            Fore.YELLOW + "+" + "-" * table_width + "+",
            Fore.YELLOW + "|{:^{width}}|".format(title, width=table_width),
            Fore.YELLOW + "+" + "-" * table_width + "+",
            Fore.YELLOW + "| {:<3} {:<{width}} |".format("[1]", "Data Obat", width=table_width - 6),
            Fore.YELLOW + "| {:<3} {:<{width}} |".format("[2]", "Data Pegawai", width=table_width - 6),
            Fore.YELLOW + "| {:<3} {:<{width}} |".format("[3]", "Kembali ke Menu Utama", width=table_width - 6),
            Fore.YELLOW + "+" + "-" * table_width + "+",
        ]
        for line in data_lines:
            print(center_text(line))

def tampilkan_update():
        table_width = 40
        print("   ")
        title = "PILIH DATA YANG INGIN DIPERBAHARUI <> "
        data_lines = [
            Fore.GREEN + "+" + "-" * table_width + "+",
            Fore.GREEN + "|{:^{width}}|".format(title, width=table_width),
            Fore.GREEN + "+" + "-" * table_width + "+",
            Fore.GREEN + "| {:<3} {:<{width}} |".format("[1]", "Data Obat", width=table_width - 6),
            Fore.GREEN + "| {:<3} {:<{width}} |".format("[2]", "Data Pegawai", width=table_width - 6),
            Fore.GREEN + "| {:<3} {:<{width}} |".format("[3]", "Data Pelanggan", width=table_width - 6),
            Fore.GREEN + "| {:<3} {:<{width}} |".format("[4]", "Data Transaksi", width=table_width - 6),
            Fore.GREEN + "| {:<3} {:<{width}} |".format("[5]", "Kembali ke Menu Utama", width=table_width - 6),
            Fore.GREEN + "+" + "-" * table_width + "+",
        ]
        for line in data_lines:
            print(center_text(line))

def tampilkan_search():
        table_width = 40
        print("   ")
        title = "PILIH DATA YANG INGIN DICARI <> "
        data_lines = [
            Fore.CYAN  + "+" + "-" * table_width + "+",
            Fore.CYAN  + "|{:^{width}}|".format(title, width=table_width),
            Fore.CYAN  + "+" + "-" * table_width + "+",
            Fore.CYAN  + "| {:<3} {:<{width}} |".format("[1]", "Data Obat", width=table_width - 6),
            Fore.CYAN  + "| {:<3} {:<{width}} |".format("[2]", "Data Pegawai", width=table_width - 6),
            Fore.CYAN  + "| {:<3} {:<{width}} |".format("[3]", "Data Pelanggan", width=table_width - 6),
            Fore.CYAN  + "| {:<3} {:<{width}} |".format("[4]", "Data Transaksi", width=table_width - 6),
            Fore.CYAN  + "| {:<3} {:<{width}} |".format("[5]", "Kembali ke Menu Utama", width=table_width - 6),
            Fore.CYAN  + "+" + "-" * table_width + "+",
        ]
        for line in data_lines:
            print(center_text(line))

def tampilkan_show():
        table_width = 40
        print("   ")
        title = "PILIH DATA YANG INGIN DILIHAT <> "
        data_lines = [
            Fore.BLUE + "+" + "-" * table_width + "+",
            Fore.BLUE + "|{:^{width}}|".format(title, width=table_width),
            Fore.BLUE + "+" + "-" * table_width + "+",
            Fore.BLUE + "| {:<3} {:<{width}} |".format("[1]", "Data Obat", width=table_width - 6),
            Fore.BLUE + "| {:<3} {:<{width}} |".format("[2]", "Data Pegawai", width=table_width - 6),
            Fore.BLUE + "| {:<3} {:<{width}} |".format("[3]", "Data Pelanggan", width=table_width - 6),
            Fore.BLUE + "| {:<3} {:<{width}} |".format("[4]", "Data Transaksi", width=table_width - 6),
            Fore.BLUE + "| {:<3} {:<{width}} |".format("[5]", "Kembali ke Menu Utama", width=table_width - 6),
            Fore.BLUE + "+" + "-" * table_width + "+",
        ]
        for line in data_lines:
            print(center_text(line))

# INSERT
def insert_data(connection):
    while True:
        tampilkan_insert()
        choice = input("Select Menu <> ")

        if choice == "1":
            insert_obat(cursor)
        elif choice == "2":
            insert_pegawai(cursor)
        elif choice == "3":
            insert_pelanggan(cursor)
        elif choice == "4":
            insert_transaksi(cursor)
        elif choice == "5":
            main(connection)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def insert_obat(cursor):
    id_obat = input("Masukkan ID obat: ")
    nama_obat = input("Masukkan Nama obat: ")
    jenis_obat = input("Masukkan Jenis obat: ")
    harga = input("Masukkan harga obat: ")
    stok = input("Masukkan stok obat: ")

    query = "INSERT INTO obat (id_obat, nama_obat, jenis_obat, harga, stok) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (id_obat, nama_obat, jenis_obat, harga, stok))
    connection.commit()
    print("{} Data obat berhasil disimpan".format(cursor.rowcount))

def insert_pegawai(cursor):
    id_pegawai = input("Masukkan ID pegawai: ")
    nama_pegawai = input("Masukkan Nama pegawai: ")
    jenis_kelamin = input("Masukkan jenis_kelamin pegawai: ")
    alamat = input("Masukkan alamat pegawai: ")
    no_telepon = input("Masukkan no telepon pegawai: ")

    query_pegawai = "INSERT INTO pegawai (id_pegawai, nama_pegawai, jenis_kelamin, alamat, no_telepon) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_pegawai, (id_pegawai, nama_pegawai, jenis_kelamin, alamat, no_telepon))
    connection.commit()
    print("{} Data pegawai berhasil disimpan". format(cursor.rowcount))

def insert_pelanggan(cursor):
    id_pelanggan = input("Masukkan ID pelanggan: ")  
    nama_pelanggan = input("Masukkan Nama pelanggan: ")
    alamat = input("Masukkan Alamat pelanggan: ")
    
    query_pelanggan = "INSERT INTO pelanggan (id_pelanggan, nama_pelanggan, alamat) VALUES (%s, %s, %s)"
    cursor.execute(query_pelanggan, (id_pelanggan, nama_pelanggan, alamat))
    connection.commit()
    print("{} Data pelanggan berhasil disimpan".format(cursor.rowcount))

def insert_transaksi(cursor) :
    show_data_obat(cursor)
    id_transaksi = input("Masukkan id_transaksi: ")
    id_pelanggan = input("Masukkan ID Pelanggan: ")
    tanggal_transaksi = datetime.now().date()
    waktu_transaksi = datetime.now().time()
    beli_obat = input("Masukkan Obat apa yang ingin dibeli: ")
    jumlah = int(input("Jumlah: "))
    cursor.execute("SELECT harga, stok FROM obat WHERE nama_obat = %s", (beli_obat,))
    harga_satuan_result = cursor.fetchone()

    if harga_satuan_result:
        harga_satuan = harga_satuan_result[0]  
        stok = harga_satuan_result[1]          
    else:
        print(f"Obat {beli_obat} tidak ditemukan!")
        return 

    if jumlah > stok:
        print("Jumlah obat yang diminta melebihi stok yang tersedia.")
        return

    total_harga = harga_satuan * jumlah
    status_transaksi = input("Masukkan status transaksi pelanggan: ")
    query_transaksi = """
    INSERT INTO transaksi (id_transaksi, id_pelanggan, tanggal_transaksi, waktu_transaksi, beli_obat, jumlah, total_harga, status_transaksi)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query_transaksi, (id_transaksi, id_pelanggan, tanggal_transaksi, waktu_transaksi, beli_obat, jumlah, total_harga, status_transaksi))

    query_update_stok = "UPDATE obat SET stok = stok - %s WHERE nama_obat = %s"
    cursor.execute(query_update_stok, (jumlah, beli_obat))

    connection.commit()

    print(f"{cursor.rowcount} Data transaksi berhasil disimpan")

    cetak_struk(cursor, id_transaksi)

# STRUK
from datetime import timedelta

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{days} hari, {hours} jam, {minutes} menit"

def format_date(dt):
    return dt.strftime("%d-%m-%Y") 

def cetak_struk(cursor, id_transaksi):
    try:
        query_struk = """
        SELECT transaksi.id_transaksi, pelanggan.nama_pelanggan, pelanggan.alamat, 
               transaksi.beli_obat, transaksi.jumlah, transaksi.total_harga, 
               transaksi.status_transaksi, transaksi.tanggal_transaksi, transaksi.waktu_transaksi 
          FROM transaksi 
          JOIN pelanggan ON transaksi.id_pelanggan = pelanggan.id_pelanggan 
          WHERE transaksi.id_transaksi = %s
        """
        
        cursor.execute(query_struk, (id_transaksi,))
        result = cursor.fetchone()

        if result:
            id_transaksi, nama_pelanggan, alamat_pelanggan, beli_obat, jumlah, total_harga, status_transaksi, tanggal_transaksi, waktu_transaksi = result

            garis_horizontal = "+" + "-" * 42 + "+"
            print("\n" + garis_horizontal)
            print(f"| {'~ APOTEK SWEETLIFE ~':^42} |")
            print(garis_horizontal)
            print(f"| ID Transaksi    : {id_transaksi:<24} |")
            print(f"| Nama Pembeli    : {nama_pelanggan:<24} |")
            print(f"| Alamat Pelanggan: {alamat_pelanggan:<24} |")
            print(f"| Obat Dibeli     : {beli_obat:<24} |")
            print(f"| Jumlah          : {jumlah:<24} |")
            print(f"| Total Harga     : Rp {total_harga:>21,} |")
            print(f"| Status Transaksi: {status_transaksi:<24} |")
            print(f"| Tanggal         : {format_date(tanggal_transaksi):<24} |")  
            print(f"| Waktu           : {format_timedelta(waktu_transaksi):<24} |")    
            print(garis_horizontal)
            print(f"| {'SEMOGA LEKAS SEMBUH !':^42} |")
            print(garis_horizontal)
        else:
            print("Data transaksi tidak ditemukan!")
    except Exception as e:
        print("Terjadi kesalahan saat mencetak struk:", e)
        
#DELETE
def delete_data(connection):
    cursor = connection.cursor()
    while True:
        tampilkan_delete()
        print("\nPilih data yang ingin dihapus:")
        print("1. Data Obat")
        print("2. Data Pegawai")
        print("3. Kembali ke Menu Utama")
        choice = input("Select Menu <> ")

        if choice == "1":
            delete_data_obat(cursor)
        elif choice == "2":
            delete_data_pegawai(cursor)
        elif choice == "3":
            main(connection)
        else:
            print("Pilihan tidak valid.")

def delete_data_obat (cursor) :
    show_data_obat(cursor)
    id_obat = input("pilih nama id obat yang ingin dihapus > ")
    sql = "DELETE FROM obat WHERE id_obat = %s"
    cursor.execute(sql, (id_obat,))
    connection.commit()
    print("{} Data berhasil dihapus".format(cursor.rowcount))

def delete_data_pegawai(cursor):
    show_data_pegawai(cursor)
    id_pegawai = input("Pilih Id pegawai yang ingin dihapus > ")
    sql = "DELETE FROM pegawai WHERE id_pegawai = %s"
    cursor.execute(sql, (id_pegawai,))
    connection.commit()
    print("{} Data berhasil dihapus".format(cursor.rowcount))

#UPDATE
def update_data(connection):
    while True:
        tampilkan_update()
        choice = input("Select Menu <> ")

        if choice == "1":
            update_obat(cursor)
        elif choice == "2":
            update_pegawai(cursor)
        elif choice == "3":
            update_pelanggan(cursor)
        elif choice == "4":
            update_transaksi(cursor)
        elif choice == "5":
            main(connection)
        else:
            print("Pilihan tidak valid.")

def update_obat(cursor):
    cursor = connection.cursor()
    show_data_obat(cursor)
    id_obat = input("Pilih ID obat : ")
    nama_obat = input("Nama Baru : ")
    jenis_obat = input("Jenis Baru : ")
    stok = input("stok baru : ")
    harga = input("Masukkan Harga Baru : ")

    sql = "UPDATE obat SET nama_obat = %s, jenis_obat = %s, stok = %s, harga= %s WHERE id_obat = %s"
    cursor.execute(sql, (nama_obat, jenis_obat, stok, harga, id_obat))
    connection.commit()
    print("{} Data berhasil diubah".format(cursor.rowcount))


def update_pegawai(cursor):
    cursor = connection.cursor()
    show_data_pegawai(cursor)
    id_pegawai = input ("pilih id pegawai :")
    nama_pegawai = input ("nama pegawai baru : ")
    jenis_kelamin = input ("jenis kelamin baru : ")
    alamat = input ("alamat baru:  ")
    no_telepon = input ("nomor telepon baru : ")

    sql = "UPDATE pegawai SET nama_pegawai = %s, jenis_kelamin = %s, alamat = %s, no_telepon = %s  WHERE id_pegawai = %s"
    cursor.execute(sql, (nama_pegawai, jenis_kelamin, alamat, no_telepon, id_pegawai))
    connection.commit()
    print("{} Data berhasil diubah".format(cursor.rowcount))


def update_pelanggan(cursor):
    cursor = connection.cursor()
    show_data_pelanggan(cursor)
    id_pelanggan = input ("pilih id pelnggan :")
    nama_pelanggan = input ("nama pelanggan baru :")

    sql = "UPDATE pelanggan SET nama_pelanggan = %s, no_antrian = %s WHERE id_pelanggan = %s"
    cursor.execute(sql, (id_pelanggan, nama_pelanggan))
    print("{} Data berhasil diubah".format(cursor.rowcount))


def update_transaksi(cursor):
    cursor = connection.cursor()
    show_data_transaksi(cursor)
    id_transaksi = input ("pilih id transaksi :")
    tanggal_transaksi = input ("tanggal baru :")
    waktu_transaksi = input ("waktu transakasi baru : ")
    jumlah = input ("jumlah baru : ")
    total_harga = input ("total harga yang baru :")
    status_transaksi = input ("status transaksi baru :")

    sql = "UPDATE transaksi SET tanggal_transaksi = %s, waktu_transaksi = %s, jumlah = %s, total_harga = %s, status_transaksi = %s  WHERE id_transaksi = %s"
    cursor.execute(sql, (id_transaksi, tanggal_transaksi, waktu_transaksi, jumlah, total_harga, status_transaksi))
    print("{} Data berhasil diubah".format(cursor.rowcount))

#SEARCH
def search_data(connection):
    cursor = connection.cursor()
    while True:
        tampilkan_search()
        choice = input("Select Menu <> ")

        if choice == "1":
            search_data_obat(cursor)
        elif choice == "2":
            search_data_pegawai(cursor)
        elif choice == "3":
            search_data_pelanggan(cursor)
        elif choice == "4":
            search_data_transaksi(cursor)
        elif choice == "5":
             main(connection)
        else:
            print("Pilihan tidak valid.")

def search_data_obat(cursor):
    cursor = connection.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM obat  WHERE nama_obat LIKE %s OR jenis_obat LIKE %s"
    like_keyword = f"%{keyword}%"
    cursor.execute(sql, (like_keyword, like_keyword))
    result = cursor.fetchall()

    headers = ["id obat", "Nama obat", "Jenis obat", "Harga", "Stok"]

    if len(result) == 0:
        print("Data tidak ditemukan")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))

def search_data_pegawai(cursor):
    cursor = connection.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM pegawai  WHERE nama_pegawai LIKE %s OR jenis_kelamin LIKE %s"
    like_keyword = f"%{keyword}%"
    cursor.execute(sql, (like_keyword, like_keyword))
    result = cursor.fetchall()

    headers = ["id pegawai", "Nama Pegawai", "Jenis Kelamin", "Alamat", "No Telepon"]

    if len(result) == 0:
        print("Data tidak ditemukan")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))

def search_data_pelanggan(cursor):
    cursor = connection.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM pelanggan  WHERE nama_pelanggan LIKE %s OR alamat LIKE %s"
    like_keyword = f"%{keyword}%"
    cursor.execute(sql, (like_keyword, like_keyword))
    result = cursor.fetchall()

    headers = ["id pelanggan", "Nama Pelanggan", "Alamat"]

    if len(result) == 0:
        print("Data tidak ditemukan")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))


def search_data_transaksi(cursor):
    cursor = connection.cursor()
    keyword = input("Kata kunci: ")
    sql = "SELECT * FROM transaksi WHERE id_transaksi LIKE %s OR status_transaksi LIKE %s"
    like_keyword = f"%{keyword}%"
    cursor.execute(sql, (like_keyword, like_keyword))
    result = cursor.fetchall()

    headers = ["id transaksi", "Tanggal transaksi ", "Waktu transaksi", "Total harga", "Status transaksi", "created_at", "updated_at", "Jumlah", "beli obat", "id pelanggan"]

    if len(result) == 0:
        print("Data tidak ditemukan")
    else:
        print(tabulate(result, headers=headers, tablefmt="grid"))
            

# show 
def show_data(connection):
    while True:
        tampilkan_show()
        choice = input("Select Menu <> ")

        if choice == "1":
            show_data_obat(cursor)
        elif choice == "2":
            show_data_pegawai(cursor)
        elif choice == "3":
            show_data_pelanggan(cursor)
        elif choice == "4":
            show_data_transaksi(cursor)
        elif choice == "5":
            main(connection)
        else:
            print("Pilihan tidak valid.")

def show_data_obat(cursor):
    cursor.execute("SELECT id_obat, nama_obat, jenis_obat, harga, stok FROM obat")
    result = cursor.fetchall()
    
    if result:
        console = Console()
        table = Table(title="Data Obat", show_lines=True)
        table.add_column("ID Obat", justify="center")
        table.add_column("Nama Obat", justify="center")
        table.add_column("Jenis Obat", justify="center")
        table.add_column("Harga",  justify="center")
        table.add_column("Stok", justify="center")

        for row in result:
            id_obat = row[0]
            nama_obat = row[1]
            jenis_obat = row[2]
            harga = f"Rp {row[3]:,}"  
            stok = row[4]

            if stok <= 5:
                stok_display = f"[bold red]{stok}[/]"
            else:
                stok_display = f"[bold green]{stok}[/]"

            table.add_row(id_obat, nama_obat, jenis_obat, harga, stok_display)

        console.print(table)
    else:
        print("Tidak ada data obat.")
    
def show_data_pegawai(cursor):
    cursor.execute("SELECT * FROM pegawai")
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers=["ID Pegawai", "Nama Pegawai", "Jenis Kelamin", "Alamat", "No Telepon"], tablefmt="grid"))
    else:
        print("Tidak ada data pegawai.")

def show_data_pelanggan(cursor):
    cursor.execute("SELECT * FROM pelanggan")
    result = cursor.fetchall()
    if result:
        print(tabulate(result, headers=["ID Pelanggan", "Nama Pelanggan", "Alamat"], tablefmt="grid"))
    else:
        print("Tidak ada data pelanggan.")

def show_data_transaksi(cursor):
    cursor = connection.cursor()
    sql = "SELECT * FROM transaksi"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if result:
        for row in result:
            print(f"ID transaksi      : {row[0]}")
            print(f"Tanggal transaksi : {row[1]}")
            print(f"Waktu transaksi   : {row[2]}")
            print(f"Total harga       : {row[3]}")
            print(f"Status            : {row[4]}")
            print(f"Beli obat         : {row[5]}")
            print(f"Jumlah            : {row[6]}")
            print(f"ID pelanggan      : {row[7]}")
            print("=" * 40)  
    else:
        print("Tidak ada data transaksi.")



# === Main Program === #

def main(connection):
    tampilkan_ascii_art("APOTEK SWEETLIFE")

    while True:
        tampilkan_menu()
        pilihan = input(("\n[?] Masukkan pilihan: "))

        if pilihan == "1":
            print("\nAPOTEK SWEETLIFE")
            insert_data(connection)
        elif pilihan == "2":
            print("\nAPOTEK SWEETLIFE")
            delete_data(connection)
        elif pilihan == "3":
            print("\n\nAPOTEK SWEETLIFE")
            update_data(connection)
        elif pilihan == "4":
            print("\n\nAPOTEK SWEETLIFE")
            search_data(connection)
        elif pilihan == "5":
            print("\n\nAPOTEK SWEETLIFE")
            show_data(connection)
        elif pilihan == "0":
            tampilkan_ascii_art("TERIMA KASIH ^^")
            print(center_text(Fore.GREEN + "Terima kasih! SEMOGA LEKAS SEMBUH ^^" + Style.RESET_ALL))
            exit()
            connection.close()
        else:
            print(center_text(Fore.RED + "[!] Pilihan tidak valid. Silakan coba lagi!" + Style.RESET_ALL))

if __name__ == "__main__":
    main(connection)
