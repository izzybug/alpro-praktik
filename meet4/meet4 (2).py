def getPanjangLebar():
    panjang=float(input("Masukan nilai panjang: "))
    lebar=float(input("Masukan nilai lebar: "))
    luas = hitungLuasPP(panjang,lebar)
    
    print("="*5,"REKAP INPUTAN","="*5)
    print("Panjang: ",panjang," cm\n",
          "Lebar : ",lebar," cm\n")
    tampilLuasPP(luas)
      
def hitungLuasPP(panjang,lebar):
    perkalian= panjang*lebar
    return perkalian

def tampilLuasPP(luas):
    print("luas bangunan ini adalah: ", luas,"cm")
    
getPanjangLebar()
print("\nNama: Mohammad Izza Iqbal\n",
      "NPM: 5210411144")
