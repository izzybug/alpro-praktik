import sqlite3

# Init Database
db = sqlite3.connect("human_resource_db_5210411144.db")
cursor = db.cursor()

#Membuat Tabel
tbl1 = '''CREATE TABLE IF NOT EXISTS tbl_pegawai(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    full_name TEXT, 
    division TEXT);'''
cursor.execute(tbl1)

# Insert data
def input_data(db):
    employee_id = int(input("Masukkan ID: "))
    full_name = input("Masukan nama lengkap: ")
    division = input("Masukan divisi anda: ")   
    cursor = db.cursor()
    cursor.execute('''INSERT INTO tbl_pegawai(employee_id, full_name, division) VALUES (?, ?, ?)''',(employee_id, full_name.title(), division.title()))
    db.commit() 
    print("data berhasil disimpan")
    
# Show Data
def show_data(db):
    cursor = db.cursor()
    Tampilkan_Data = "SELECT * FROM tbl_pegawai"
    cursor.execute(Tampilkan_Data)
    results = cursor.fetchall()
  
    for data in results:
        print(data)
   
# Menu     
def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    
    if menu == "1":
        input_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)