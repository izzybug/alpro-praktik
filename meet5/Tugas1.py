def getBilanganBulat():
    nilai = int(input("Masukan nilai: "))
    cekGanjilGenap(nilai)
    
    
def cekGanjilGenap(nilai):
    if nilai % 2 == 0:
        print ("%i adalah bilangan genap" % nilai)
    else:
        print ("%i adalah bilangan ganjil" % nilai)
        
getBilanganBulat()

# print("\nNama: Mohammad Izza Iqbal\n",
#       "NPM: 5210411144")