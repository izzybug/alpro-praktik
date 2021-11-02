def getBMI(tb,bb):
    tb_meter = tb / 100
    tb_square = tb_meter * tb_meter
    
    
    # hitung bmi
    bmi = bb / tb_square
    
    return bmi

def getResiko(bmi):
    if bmi >= 18.5 and bmi <= 25.0:
        return "Normal"
    elif bmi > 25.0 and bmi <= 30.0:
        return "Average"
    elif bmi > 30.0 and bmi <= 40.0:
        return "Important"
    elif bmi > 40:
        return "Severe"   
    
    
# input
beratBadan = float(input("Input Berat badan (kg) :"))
tinggiBadan = float(input("Input tinggi badan (cm) :"))

print("BMI = ", round(getBMI(tinggiBadan,beratBadan),3))


# cetak resikoKesehatan
print("Resiko Kesehatan =", getResiko(getBMI(tinggiBadan,beratBadan)))