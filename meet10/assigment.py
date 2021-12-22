import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Init database
with sqlite3.connect("db/akademik_db.db") as db:
    # Ubah struktur baris jadi dictionary
    db.row_factory = dict_factory
    cursor = db.cursor()


# Drop table -> Hapus tabel dari database
cursor.execute('''DROP TABLE IF EXISTS `mahasiswa`;''')

# Buat tabel
cursor.execute('''CREATE TABLE IF NOT EXISTS `mahasiswa` (
	`npm` INTEGER PRIMARY KEY AUTOINCREMENT,
	`nama` TEXT,
	`jenis_kelamin` CHAR,
	`jenis_sekolah` CHAR,
	`status_sekolah` CHAR,
	`ipk_semester_1` REAL,
	`ipk_semester_2` REAL,
    'rata_rata_ipk' AS ((ipk_semester_1 + ipk_semester_2) / 2) STORED
);''')

# Tambah data 1
cursor.execute('''INSERT INTO `mahasiswa` 
    VALUES ('521001', 'Budi Setiawan', 'L', 'SMA', 'N', 2.60, 3.90);''')
db.commit()

# Tambah data lebih dari 1 -> Insert batch
cursor.execute('''INSERT INTO `mahasiswa` 
    (`nama`, `jenis_kelamin`, `jenis_sekolah`, `status_sekolah`, `ipk_semester_1`, `ipk_semester_2`) VALUES
    ('Joni Hermawan', 'L', 'SMA', 'N', 2.99, 3.30),
    ('Endah Sulastri', 'P', 'SMA', 'N', 3.56, 2.90),
    ('Akmal Laksmana', 'L', 'SMA', 'S', 3.25, 3.45),
    ('Nugroho', 'L', 'SMK', 'N', 2.75, 3.15),
    ('Rini Nuraeni', 'P', 'SMA', 'N', 2.85, 2.9),
    ('Farida', 'P', 'SMK', 'S', 3.81, 3.60)
;''')
db.commit()

# Menampilkan data
cursor.execute('''SELECT * FROM `mahasiswa`;''')
for row in cursor.fetchall():
    print(row)

# Rata-rata ipk kelas
cursor.execute('''SELECT avg(rata_rata_ipk) FROM mahasiswa;''')
for row in cursor.fetchall():
    print("Rata-rata kelas :", row)

cursor.execute('''SELECT max(rata_rata_ipk) FROM mahasiswa;''')
for row in cursor.fetchall():
    print("Rata-rata tertinggi :", row)

cursor.execute('''SELECT min(rata_rata_ipk) FROM mahasiswa;''')
for row in cursor.fetchall():
    print("Rata-rata terendah :", row)


# Update berdasarkan npm atau id
# cursor.execute('''UPDATE mahasiswa SET ipk_semester_1 = 3.00 WHERE npm = 521006;''')
# db.commit()

# Menampilkan data
# print()
# cursor.execute('''SELECT * FROM `mahasiswa`;''')
# for row in cursor.fetchall():
#     print(row)


# nama_baru = str(input("Nama baru : "))
# nama_lama = str(input("Nama Lama : "))

# Update berdasarkan kolom selain id
# cursor.execute('''UPDATE mahasiswa SET nama = ? WHERE nama = ?;''', (nama_baru, nama_lama))
# db.commit()

# js = str(input("Jenis Sekolah : "))

# Update tanpa kondisi -> akan merubah satu kolom
# cursor.execute("UPDATE mahasiswa SET jenis_sekolah = '" + js + "';")
# db.commit()

# Menampilkan data
# print()
# cursor.execute('''SELECT * FROM `mahasiswa`;''')
# for row in cursor.fetchall():
#     print(row)


# Update semua kolom -> tulis tiap kolom yang mau dirubah
# cursor.execute('''UPDATE mahasiswa SET 
#     nama = 'Andrea Wu',
#     jenis_kelamin = 'P',
#     jenis_sekolah = 'SMK',
#     status_sekolah = 'S',
#     ipk_semester_1 = 3.81,
#     ipk_semester_2 = 3.67
#     WHERE npm = 521001
# ;''')
# db.commit()

# Menampilkan data + generate kolom
# print()
# cursor.execute('''SELECT nama, 
#     ipk_semester_1,
#     ipk_semester_2,
#     (ipk_semester_1 + ipk_semester_2) / 2 AS rata_rata 
#     FROM `mahasiswa`;''')
# for row in cursor.fetchall():
#     print(row)


# Hapus data
cursor.execute('''DELETE FROM mahasiswa 
    WHERE ipk_semester_1 < 3.00
    OR ipk_semester_2 < 3.00;''')

print()
cursor.execute('''SELECT nama, 
    ipk_semester_1,
    ipk_semester_2,
    rata_rata_ipk
FROM `mahasiswa`;''')
for row in cursor.fetchall():
    print(row["rata_rata_ipk"])

db.close()