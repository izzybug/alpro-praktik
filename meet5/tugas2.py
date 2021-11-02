def getDataPetinju():
    #Main program untuk mengambil data petinju
    NamaPetinju =input("Input nama anda: ") 
    Usia =input("Input usia anda: ") 
    TinggiBadan =input("Input tinggi badan anda: ") 
    BeratBadan =int(input("Input berat badan anda: "))
    Kebangsaan =input("Input kebangsaan anda: ") 
    
    print("="*5,"DATA PETINJU","="*5)
    print("Nama: ",NamaPetinju,"\n"
          "Usia: ",Usia,"\n"
          "Tinggi Badan: ",TinggiBadan,"cm\n"
          "Berat Badan: ",BeratBadan,"kg\n"
          "Kebanggsaan: ",Kebangsaan,)
    tampilKelasPetinju(BeratBadan)
    
def cekKelasPetinju(beratBadanPetinju):
    #Menghitung Kelas Petinju Berdasarkan Berat Badan
    # namaKelas = ''
    if beratBadanPetinju >= 41 and beratBadanPetinju <= 54:
        namaKelas= "Kelas Terbang"
    elif beratBadanPetinju >= 55 and beratBadanPetinju <= 59:
        namaKelas= "Kelas Bulu"
    elif beratBadanPetinju >= 60 and beratBadanPetinju <= 66:
        namaKelas= "Kelas Ringan"
    elif beratBadanPetinju >= 67 and beratBadanPetinju <= 77:
        namaKelas= "Kelas Menengah"
    elif beratBadanPetinju >= 78 and beratBadanPetinju <= 87:
        namaKelas= "Kelas Berat"
    else:
        namaKelas= "Bukan petinju"
    return namaKelas
        
def tampilKelasPetinju(beratPetinju):
    #Menampilkan Kelas Petinju 
    beratPetinju = cekKelasPetinju(beratPetinju)
    print("Kelas Petinju: ",beratPetinju)
    
#Call  
getDataPetinju()

print("\nNama: Mohammad Izza Iqbal\n",
      "NPM: 5210411144")