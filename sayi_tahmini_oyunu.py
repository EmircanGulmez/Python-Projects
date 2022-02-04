import random
asagi = ["İn in daha", "Daha aşağıda!!", "Aşağı iner misin", "Lütfen aşağı in...", "in daha", "Aşağıdaa...", "aha, bilemedin aşağıdaaa", "ehehe, aşağıda"]
yukari = ["Çık çık daha", "Ohoo yukarıda!!", "Yukar çıkar mısın", "Lütfen yukarı lütfeenn", "Çık yukarı", "Yukarıdaa...", "ehehe, bilemedin yukarıdaa", "aha, bildin şaka şaka yukarı :)"]
sayi = random.randint(1,100)
print("\nOyunun Amacı: Bilgisayar bir ile yüz arası bir sayı tutar ve sen istediğin hak kadar bilmeye çalışırsın, her \nsayı tahmininde bilgisayar seni yönlendirecektir iyi şanslar. Oyunu sonlandırmak için 0 gir.\n")
hak = int(input("Ne kadar hak istiyorsun? : "))
if hak >= 10:
    print("Sence de fazla hak almadın mı? Neyse...")
say = 0
while hak > 0:
    print("\n###########################################\n")
    tahmin = int(input("Tahmin : "))
    soylem = random.randint(0,7)
    say += 1
    hak -= 1
    if tahmin == 0:
        print("Oyun sonlandırıldı...")
        break
    if hak == 0:
        print("Tuttuğum sayı :",sayi)
        print("Hakkın : ",hak)
        print("Oyun bitti, hakkın kalmadı...")
        break
    if tahmin < sayi:
        print("Hakkın : ",hak)
        print(yukari[soylem])
    elif tahmin > sayi:
        print("Hakkın : ",hak)
        print(asagi[soylem])
    else:
        print(f"Bildin tebrikler {say}. defada bildiniz...")
        break
