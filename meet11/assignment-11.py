import sqlite3
import os
from colorama import Fore,Style

# changes tuple to dict
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Init Database
with sqlite3.connect("alpro-praktik/db/human_resource_db_5210411144.db") as db:
        db.row_factory = dict_factory
        cursor = db.cursor()

#Membuat Tabel
tbl1 = '''CREATE TABLE IF NOT EXISTS tbl_pegawai(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    full_name TEXT, 
    division TEXT);'''
cursor.execute(tbl1)

# Insert data
def input_data(db):
    insert_data = 'Y'
    while (insert_data == 'Y' or insert_data == 'y'):
        full_name = input("Masukan nama lengkap: ")
        division = input("Masukan divisi anda: ")   
        cursor = db.cursor()
        cursor.execute('''INSERT INTO tbl_pegawai(full_name, division) VALUES (?, ?)''',( full_name.title(), division.title()))
        db.commit() 
        print(Fore.GREEN+"data berhasil disimpan"+Style.RESET_ALL)
        
        insert_data = input("Ingin menambah data lainnya (Y/N) ")
    print('_'*50,'\n')
    
# Show Data
def show_data(db):
    cursor = db.cursor()
    Tampilkan_Data = "SELECT * FROM tbl_pegawai"
    cursor.execute(Tampilkan_Data)
    results = cursor.fetchall()
    print('_'*25,'Tampilkan Data','_'*25,'\n')
  
    for data in results:
        print(data)
    print('_'*66,'\n')

# update data  
def update_data(db):
    cursor = db.cursor()
    sql = '''SELECT employee_id FROM `tbl_pegawai`;'''
    cursor.execute(sql)
    print('_'*25,'Employee ID','_'*25,'\n')
    
    for row in cursor.fetchall():
        print('->',row['employee_id'])
        
    print('_'*63,'\n')
    employee_id = int(input("pilih id: "))
    cursor.execute('''SELECT employee_id FROM tbl_pegawai;''')
    row = cursor.fetchall()
    for x in row:
        if employee_id == x['employee_id']:    
            full_name = input("Nama baru: ")
            division = input("Divisi baru: ")

            cursor.execute('''UPDATE tbl_pegawai SET full_name=?, division=? WHERE employee_id=?''', (full_name.title(), division.title(), employee_id))
            db.commit()
            
            print(Fore.GREEN+"data berhasil diubah"+Style.RESET_ALL)
        else:
            print(Fore.RED+"Maaf, Nomor pegawai", str(employee_id) ," tidak ditemukan."+Style.RESET_ALL)
        print('_'*63,'\n')
   
# delete data  
def del_data(db):
    cursor = db.cursor()
    cursor.execute('''SELECT full_name FROM tbl_pegawai''')
    print('_'*25,'Hapus Data','_'*25,'\n')
    
    for row in cursor.fetchall():
        print('->',row['full_name'])
    print('_'*62)  
    full_name = input("pilih nama : ")
    cursor.execute('''SELECT full_name FROM tbl_pegawai''')
    row = cursor.fetchall()
    for i in row:
        if full_name.title() == i['full_name']:
            sql = '''DELETE FROM tbl_pegawai WHERE full_name=?'''
            cursor.execute(sql, [full_name.title()])
            db.commit()
        
            print(Fore.GREEN+"data berhasil dihapus"+Style.RESET_ALL)
        else:
            print(Fore.RED+"Maaf, Nama pegawai", str(full_name.title()) ,"tidak ditemukan."+Style.RESET_ALL)
    print('_'*62,'\n')
# Menu     
def show_menu(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    os.system('clear')
    
    if menu == "1":
        input_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        del_data(db)
    elif menu == "0":
        db.close()
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)
