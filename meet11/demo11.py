import sqlite3
from sqlite3.dbapi2 import Cursor

with sqlite3.connect("alpro-praktik/db/akademik_db.db") as db:
    Cursor = db.cursor()
  
Cursor.execute('''DROP TABLE IF EXISTS `mahasiswa`;''')  
  
Cursor.execute('''CREATE TABLE IF NOT EXISTS `mahasiswa` (
	`npm` INTEGER PRIMARY KEY AUTOINCREMENT,
	`nama` TEXT,
	`jenis_kelamin` TEXT,
	`jenis_sekolah` CHAR,
	`status_sekolah` CHAR,
	`ipk_semester_1` REAL,
	`ipk_semester_2` REAL
);''')

Cursor.execute('''INSERT INTO `mahasiswa` VALUES ('521001', 'Budi Setiawan', 'L', 'SMA', 'N', 2.60, 3.90);''')
db.commit()

Cursor.execute('''INSERT INTO `mahasiswa` (`nama`, `jenis_kelamin`, `jenis_sekolah`, `status_sekolah`, `ipk_semester_1`, `ipk_semester_2`) VALUES
('Joni Hermawan', 'L', 'SMA', 'N', 2.99, 3.30),
('Endah Sulastri', 'P', 'SMA', 'N', 3.56, 2.90),
('Akmal Laksmana', 'L', 'SMA', 'S', 3.25, 3.45),
('Nugroho', 'L', 'SMK', 'N', 2.75, 3.15),
('Rini Nuraeni', 'P', 'SMA', 'N', 2.85, 2.9),
('Farida', 'P', 'SMK', 'S', 3.81, 3.60);''')
db.commit()

#menampilkan data
Cursor.execute('''SELECT * FROM `mahasiswa`;''')
for row in Cursor.fetchall():
    print(row)
    
    
Cursor.execute('''UPDATE mahasiswa SET ipk_semester_1 = 3.00 WHERE npm = 521006;''')
db.commit()

#menampilkan data
Cursor.execute('''SELECT * FROM `mahasiswa`;''')
for row in Cursor.fetchall():
    print(row)
    
    
nama_baru = str(input("Nama baru : "))
nama_lama = str(input("Nama lama : "))

#update
Cursor.update('''UPDATE mahasiswa SET nama = ? WHERE nama = ?;''', (nama_baru, nama_lama))
db.commit()

#menampilkan data
Cursor.execute('''SELECT * FROM `mahasiswa`;''')
for row in Cursor.fetchall():
    print(row)
  
# hapus data
Cursor.execute('''DELETE FROM mahasiswa WHERE ipk_semester_1 < 3.00 OR ipk_semester_2 < 3.00;''')  

print()
Cursor.execute('''SELECT nama, ipk_semester_1, ipk_semester_2, (ipk_semester_1 + ipk_semester_2) / 2 AS rata-rata FROM `mahasiswa`''')
for row in Cursor.fetchall():
    print(row)
    
db.close()