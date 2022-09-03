import random

print("")
print("*"*15," Çarpım Tablosuna Hoşgeldiz ","*"*15)

def derece():
    print("\nBir Zorluk Derecesi Seçiniz:")
    print("0 - Çıkış\n1 - Kolay\n2 - Normal\n3 - Zor\n4 - Çok Zor\n")

    secim = int(input("Seçim: "))
    if secim == 0:
        return 0

    adet = int(input("Kaç adet soru olsun?: "))

    if secim == 1:
        islem(0,10,adet)

    elif secim == 2:
        islem(10,20,adet)

    elif secim == 3:
        islem(20,50,adet)

    elif secim == 4:
        islem(50, 1000,adet)

def islem(min,max,adet):
    # noinspection PyGlobalUndefined
    global i
    d = 0
    y = 0
    for i in range(1,adet+1):
        sayi1 = random.randint(min,max)
        sayi2 = random.randint(min,max)

        sonuc = int(input(f"\nSoru {i}: {sayi1} x {sayi2} sonucu kaçtır? : "))
        if sonuc == sayi1 * sayi2:
            d += 1
            print("Sonucunuz Doğru :)\n")
        else:
            y += 1
            print("Sonuç yanlış :( \nDoğru Cevap:",sayi1 * sayi2)

    if i == adet:
        print(f"\n{adet} sorudan {d} doğru, {y} yanlış")

while True:
    if derece() == 0:
        break
