def getDataNasabah():
    namaNasabah = input("Masukkan nama anda: ")
    noRekening = input("Masukkan nomor rekening anda: ")
    saldo = int(input("Masukkan saldo anda: "))
    bunga = int(input("Masukkan suku bunga per tahun: "))
    
    print("="*5,"DATA NASABAH","="*5)
    print(" Nama      :",namaNasabah,"\n",
          "NO. Rek   :",noRekening,"get\n",
          "Saldo     :Rp.",saldo,"\n",
          "Suku Bunga:",bunga,"%\n")
    print("Bunga yang diterima:Rp.", hitungBungaNetto(saldo,bunga),"\n")
    
def hitungBungaBruto(saldo,bunga):
    bunga_bruto = saldo * 1/365 * bunga
    return bunga_bruto
 
def hitungBungaNetto(saldo,bunga):
    bungaNetto = hitungBungaBruto(saldo,bunga) - 0.2 * hitungBungaBruto(saldo,bunga)
    return bungaNetto
    
getDataNasabah()
print("\nNama: Mohammad Izza Iqbal\n",
      "NPM: 5210411144")
