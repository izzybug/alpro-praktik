import sqlite3

# Init Database
db = sqlite3.connect("alpro-praktik/db/human_resource_db_5210411144.db")
cursor = db.cursor()

#Membuat Tabel
tbl1 = '''CREATE TABLE IF NOT EXISTS tbl_pegawai(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    full_name TEXT, 
    division TEXT);'''
cursor.execute(tbl1)

#insert table
insrt_tbl = '''INSERT INTO tbl_pegawai(employee_id, full_name, division) VALUES (980987, "Tammara Z. Gysbers", "Information Technology")'''
cursor.execute(insrt_tbl)
db.commit()
