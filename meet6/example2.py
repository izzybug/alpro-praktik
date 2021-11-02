def convC2F(cel):
    return ((9/5)*cel)+32

def getGasMark(fah):
    if fah >= 225 and fah < 250:
        return 0.25
    elif fah >= 250 and fah < 275:
        return 0.5
    elif fah >= 275 and fah < 300:
        return 1
    elif fah >= 300 and fah < 325:
        return 2
    elif fah >= 325 and fah < 350:
        return 3
    elif fah >= 350 and fah < 375:
        return 4
    elif fah >= 375 and fah < 400:
        return 5
    elif fah >= 400 and fah < 425:
        return 6
    elif fah >= 425 and fah < 450:
        return 7
    elif fah >= 450 and fah < 475:
        return 8
    elif fah >= 475:
        return 9

def getDeskripsi(gm):
    if gm == 0.25 or gm == 0.5:
        return "Very slow"
    elif gm == 1 or gm == 2:
        return "Slow"
    elif gm == 3 or gm == 4:
        return "Moderate"
    elif gm == 5 or gm == 6:
        return "Moderately Hot"
    elif gm == 7 or gm == 8:
        return "Hot"
    elif gm == 9:
        return "Very Hot"
    
    
#TODO: Program start here
c = int(input("Input suhu (celcius): "))
print("Suhu (celcius):", c)

#celcius to fahrenheit
f = convC2F(c)
print("Suhu (fahrenheit):", f)

#Gas Mark
gas_mark = getGasMark(f)
print("Gas Mark =", getGasMark(f))
#Deskripsi
print("Deskripsi =", getDeskripsi(gas_mark))