MAX_SORU = 5
BASARI_PUANI = 30

def puan_hesapla():
    soru = 1
    puan = 0
    yanlis = 0

    
    while soru <= MAX_SORU:
        cevap = int(input(f"{soru}. soru (1=doğru, 0=yanlış): "))

        if cevap == 1:
            puan += 10
        elif cevap == 0:
            yanlis += 1
        else:
            print("Hatalı giriş!")
            continue

        soru += 1

    
    if yanlis >= 2:
        print("\nTelafi hakkı kazandın!")

        for i in range(2):
            telafi = input("Telafi sorusu doğru mu? (e/h): ")
            if telafi == "e":
                puan += 5

    return puan



toplam_puan = puan_hesapla()

print("\nToplam puan:", toplam_puan)

if toplam_puan >= BASARI_PUANI:
    print("Başarılı ")
else:
    print("Başarısız ")
