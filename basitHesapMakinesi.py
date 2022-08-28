print("********************\n\nHESAP MAKİNESİ")
while True:
    print("+-------------------------------------------+")
    print("|\tÇıkmak için \t\t\t -> 0'a basın\t|")
    print("|\tToplama işlemi için \t -> 1'e basın\t|")
    print("|\tÇıkarma işlemi için \t -> 2'ye basın\t|")
    print("|\tÇarpma işlemi için  \t -> 3'e basın\t|")
    print("|\tBölme işlemi için   \t -> 4'e basın\t|")
    print("|\tMod işlemi için     \t -> 5'e basın\t|")
    print("|\tKare alma işlemi için \t -> 6'ya basın\t|")
    print("+-------------------------------------------+\n\n********************\n")

    islem = int(input("İslem Seçiniz: "))
    if islem == 0:
        break

    if islem > 6:
        print("Hatalı İşlem Seçimi Yapıldı!")
        continue

    sayi1 = float(input("1. Sayi Giriniz: "))
    sayi2 = float(input("2. Sayi Giriniz: "))

    if islem == 1:
        print("Sonuç:", sayi1 + sayi2)

    elif islem == 2:
        print("Sonuç:", sayi1 - sayi2)

    elif islem == 3:
        print("Sonuç:", sayi1 * sayi2)

    elif islem == 4:
        print("Sonuç:", sayi1 / sayi2)

    elif islem == 5:
        print("Sonuç:", sayi1 % sayi2)

    elif islem == 6:
        print("Sonuç:", sayi1 ** sayi2)

    else:
        print("Hatalı Giriş Yapıldı!")
    print("\n********************")
