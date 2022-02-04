import random
while 1:
    karar = input("\nZar atılsın mı? (e/h) : ")
    if karar == 'e':
        zar1 = random.randint(1,6)
        zar2 = random.randint(1,6)
        print(f"Zar sonucu : {zar1} / {zar2}")
    elif karar == 'h':
        break
    else:
        print("Zar atılamadı...")
