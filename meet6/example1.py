def klasifikasiSkor():
    global listening, written, reading

    jumlahSkor = (listening+written+reading)
    skor =jumlahSkor * 10
    skor_akhir = skor/3

    if skor_akhir >= 310 and skor_akhir <= 420:
        print("Elementary")
    elif skor_akhir >= 421 and skor_akhir <= 480:
        print("Low intermediate")
    elif skor_akhir >= 481 and skor_akhir <= 520:
        print("High intermediate")
    elif skor_akhir >= 521 and skor_akhir <= 677:
        print("Advance")
    
listening = 63
written = 63
reading = 63

klasifikasiSkor()