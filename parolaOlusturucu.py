import random

kucukHarf = "abcdefghijklmnopqrstuvwxyz"
buyukHarf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayi = "0123456789"
ozelKarakter = "!@#$%^&*()"

karakterAdet = int(input("Parolanız kaç karakterden oluşturulsun: "))
adet = int(input("Kaç tane şifre oluşturulsun: "))
hersey = input("Parolanızda bütün karakterler olsun mu? (e/h): ")
print("")

if hersey == "e":
    karakterler = kucukHarf + buyukHarf + sayi + ozelKarakter
    for x in range(0,adet):
        sifre = ""
        for y in range(0,karakterAdet):
            rastgele = random.choice(karakterler)
            sifre = rastgele + sifre
        print("Şifreniz: ", sifre)

elif hersey == "h":
    sayilar = input("Parolanızda sayı olsun mu? (e/h): ")
    ozel = input("Parolanızda özel karakterler olsun mu? (e/h): ")
    buyuk = input("Parolanızda büyük karakterler olsun mu? (e/h): ")
    kucuk = input("Parolanızda küçük karakterler olsun mu? (e/h): ")
    karakterler = ""

    if sayilar == "e":
        karakterler = karakterler + sayi
    if ozel == "e":
        karakterler = karakterler + ozelKarakter
    if buyuk == "e":
        karakterler = karakterler + buyukHarf
    if kucuk == "e":
        karakterler = karakterler + kucukHarf

    if sayilar == "h" and ozel == "h" and buyuk == "h" and kucuk == "h":
        adet = 0
        print("Şifreniz oluşturulmadı.")

    for x in range(0,adet):
        sifre = ""
        for y in range(0,karakterAdet):
            rastgele = random.choice(karakterler)
            sifre = rastgele + sifre
        print("Şifreniz: ", sifre)
