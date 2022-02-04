import random
olasılık = ["YAZI", "TURA", "DİK"]
while True:
    karar = input("\nYazı tura atılsın mı? (e/h) : ")
    if karar == 'e':
        para = random.randint(0,2)
        print("Yazı tura sonucu",olasılık[para],"geldi..")
    elif karar == 'h':
        break
    else:
        print("Yazı tura atılamadı...")
