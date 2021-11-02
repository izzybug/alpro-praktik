def getXdanY():
    global x,y
    x = int(input("Masukan nilai x: "))
    y = int(input("Masukan nilai y: "))
    tampilInfo(x,y)
    
def getKuadran(x,y):
    kuadran = ''
    if x>0 and y >0:
        kuadran = 'Kuadran I'
    elif x<0 and y >0:
        kuadran = 'Kuadran II'
    elif x<0 and y <0:
        kuadran = 'Kuadran III'
    elif x>0 and y <0:
        kuadran = 'Kuadran IV'
    else:
        kuadran = 'Bukan Kuadran'
    return kuadran

def tampilInfo(x,y):
    print("Nilai x = ",x)
    print("Nilai y = ",y)
    print("koordinat(",x,",",y,")","berada pada kuadran",getKuadran(x,y))
    
getXdanY()

print("\nNama: Mohammad Izza Iqbal\n",
      "NPM: 5210411144")