import random
import time

secenekler = ["Taş", "Kağıt", "Makas"]
baslat = input("Başlayalım mı? (e/h): ")
tekrar = "e"

while baslat == "e":

    if tekrar in "e":
        karar = random.randint(0,2)
        print("Taş")
        time.sleep(0.7)
        print("Kağıt")
        time.sleep(0.7)
        print("Makas")
        time.sleep(0.2)
        print("\nSonucum:",secenekler[karar])

    elif tekrar in "h":
        print("\nPeki! bb :)")
        break

    else:
        print("Hata Aldım!!")

    tekrar = input("\nTekrar? (e/h): ")


