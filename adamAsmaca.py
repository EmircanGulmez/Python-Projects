import random

adam = [
    """
      +-----+
      |     |
            |
            |
            |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
            |
            |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
      |     |
            |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
     /|     |
            |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
     /|\    |
            |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
     /|\    |
      |     |
            |
    ----------
    ""","""
      +-----+
      |     |
      O     |
     /|\    |
      |     |
     /      |
    ----------
    ""","""
      +-----+
      |     |
      O     |
     /|\    |
      |     |
     / \    |
    ----------
    """]

while True:
    print("********** Adam Asmaca Oyunu **********")

    kelime = random.choice(["python", "django", "java", "terminal", "linux", "windows"])
    adim = 0
    tahmin = []

    while True:
        print(adam[adim])
        print(kelime)

        for i, char in enumerate(kelime):
            print(char if i in tahmin else "_"),

        cevap = input("Tahmin: ")

        if tahmin == kelime:
            print("Tebrikler Kazandınız..")
            break
        else:
            adim += 1
            while True:
                rastgele = random.randint(0, len(kelime))
                if not rastgele in tahmin:
                    tahmin.append(rastgele)
                    break

        if adim >= len(adam) or adim >= len(kelime):
            print("Cevap: '"+kelime+"' Kaybettiniz! :(")
            break

    if not "e" == input("Tekrar Oynamak İSter misiniz? (e/h): "):
        break



