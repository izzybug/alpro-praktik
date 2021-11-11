choice = 0
cars = ["Mercedes", "Toyota", "BMW"]

while True:
    print("*"*6," APLIKASI SEDERHANA ","*"*6)
    print("1. Insert Data Merek Mobil")
    print("2. Lihat Data Merek Mobil")
    print("3. Ubah Data Merek Mobil")
    print("4. Hapus Data Merek Mobil")
    print("5. Hapus Semua Data Merek Mobil")
    print("6. Urutkan Data Merek Mobil")
    print("7. Keluar Aplikasi")
    choice = input("Masukkan pilihan anda:")

    if choice == '1':
        print("*"*6," INSERT DATA ","*"*6)
        new_car = input("Masukkan merek mobil baru :")
        cars.append(new_car)
        print("Data mobil baru", new_car, "berhasil di-insert-kan")

    elif choice == '2':
        print("*"*6," LIHAT DATA ","*"*6)
        print("Data mobil yang tersimpan : ")
        for x in cars:
            print(x)

    elif choice == '3':
        change_car = input("Masukkan nama mobil yang akan diubah :")
        for i, car in enumerate(cars):   
            if car == change_car:
                mobil = i

        new_car = input("Masukkan merek mobil pengganti :")
        cars[mobil] = new_car
        print("Data mobil pengganti", new_car, "berhasil di-insert-kan")

    elif choice == '4':
        print("*"*6," HAPUS DATA ","*"*6)
        del_car = input("Masukkan merek mobil yang akan dihapus :")
        cars.remove(del_car)
        print("Data mobil lama", del_car, "berhasil dihapus")

    elif choice == '5':
        print("*"*6," HAPUS SEMUA DATA ","*"*6)
        clear_data = input("Apakah anda yakin ingin menghapus semua data (YA?TIDAK) :")
        if clear_data == 'YA':
            cars.clear()
        else:
            continue
    
    elif choice == '6':
        cars.sort()
        print("Data anda sudah diurutkan")
        print(cars)
    
    elif choice == '7':
        print("*"*6," KELUAR APLIKASI ","*"*6)
        print("*"*6," CREATED BY IZZA IQBAl ","*"*6)
        break

    else:
        print("*"*6," ERROR APLIKASI ","*"*6)
        print("Menu yang anda pilih tidak ada...")