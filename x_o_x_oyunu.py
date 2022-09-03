"""
        3 x 3   3 x 3   3 x 3
......................................
        - - -   x|o|x   1|2|3
                _ _ _   _ _ _
        - - -   o|o|x   4|5|6
                _ _ _   _ _ _
        - - -   x|x|o   7|8|9
......................................
"""

import random

def kart():
    print("\n")
    print(sira[0], "|", sira[1], "|", sira[2],"     1 | 2 | 3")
    print(sira[3], "|", sira[4], "|", sira[5],"     4 | 5 | 6")
    print(sira[6], "|", sira[7], "|", sira[8],"     7 | 8 | 9")
    print("\n\n")

xox = True
while xox:

    sira = ["-","-","-",
            "-","-","-",
            "-","-","-",]

    print()
    print("::::::::::::::::::::::::::''':::::'''::''''''''::'''::::'''::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::'##::::'##::'#######::'##::::'##::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::. ##::'##::'##.... ##:. ##::'##:::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::. ##'##::: ##:::: ##::. ##'##::::::::::::::::::::::::::::::")
    print("'#######:'#######:'#######:::. ###:::: ##:::: ##:::. ###::::'#######:'#######:'#######:")
    print("........:........:........::: ## ##::: ##:::: ##::: ## ##:::........:........:........:")
    print(":::::::::::::::::::::::::::: ##:. ##:: ##:::: ##:: ##:. ##:::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::: ##:::. ##:. #######:: ##:::. ##::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::...::::...::........::...:::::...:::::::::::::::::::::::::::")

    print("\nÇift kişilik için : 1 \nTek  kişilik için : 2")
    kisi = int(input("\nYapmak istediğiniz işlemi seçiniz : "))
    if kisi == 1:
        print("\n---------- Çift Oyunculu ----------")
        oyuncu = "X"
        while True:
            kart()
            print(oyuncu,"sırası : ")
            tabloNo = int(input())

            # tabloda yerleştirme
            if sira[tabloNo-1] == "-":
                sira[tabloNo-1] = oyuncu
                if oyuncu == "O":
                    oyuncu = "X"
                elif oyuncu == "X":
                    oyuncu = "O"
            else:
                print("\n\n\nOrayı seçemezsiniz, tekrar seçiniz!")

            # kazanma kontrolü
            sira1 = sira[0] == sira[1] == sira[2] != "-"
            sira2 = sira[3] == sira[4] == sira[5] != "-"
            sira3 = sira[6] == sira[7] == sira[8] != "-"

            sutun1 = sira[0] == sira[3] == sira[6] != "-"
            sutun2 = sira[1] == sira[4] == sira[7] != "-"
            sutun3 = sira[2] == sira[5] == sira[8] != "-"

            carpraz1 = sira[0] == sira[4] == sira[8] != "-"
            carpraz2 = sira[2] == sira[4] == sira[6] != "-"

            if sira1 or sira2 or sira3 or sutun1 or sutun2 or sutun3 or carpraz1 or carpraz2:
                kart()
                if oyuncu == "O":
                    oyuncu = "X"
                elif oyuncu == "X":
                    oyuncu = "O"
                print("Kazanan oyuncu : ",oyuncu)
                tekrar = input("\nTekrar oynamak ister misiniz? (e/h) : ")
                if tekrar == 'e':
                    break
                else:
                    xox = False
                    break
            
            # berabere kontrolü
            if sira[0] != "-" and sira[1] != "-" and sira[2] != "-" and sira[3] != "-" and sira[4] != "-" and sira[5] != "-" and sira[6] != "-" and sira[7] != "-" and sira[8] != "-":
                print("Kutularda Yer kalmadı Oyun berabere")
                tekrar = input("\nTekrar oynamak ister misiniz? (e/h) : ")
                if tekrar == 'e':
                    break
                else:
                    xox = False
                    break
                
    # bilgisayar kendi hamlesini rastgele koyar
    if kisi == 2:
        print("\n---------- Tek Oyunculu ----------\n")
        xoSecimi = input("X mi, O mu olmak istersin (küçük harfle) : ")
        oyuncu = "X"
        while True:
            kart()
            print(oyuncu,"sırası : ")
            # ilk başlama seçimi ve devamı
            if xoSecimi == "o" and oyuncu == "X" or xoSecimi == "x" and oyuncu == "O":
                tabloNo = random.randint(0,8)
            elif xoSecimi == "x" or xoSecimi == "o":
                tabloNo = int(input())
            
            # tabloda yerleştirme
            if sira[tabloNo-1] == "-":
                sira[tabloNo-1] = oyuncu
                if oyuncu == "O":
                    oyuncu = "X"
                elif oyuncu == "X":
                    oyuncu = "O"
            else:
                print("\n\n\nOrayı seçemezsiniz, tekrar seçiniz!")

            # kazanma kontrolü
            sira1 = sira[0] == sira[1] == sira[2] != "-"
            sira2 = sira[3] == sira[4] == sira[5] != "-"
            sira3 = sira[6] == sira[7] == sira[8] != "-"

            sutun1 = sira[0] == sira[3] == sira[6] != "-"
            sutun2 = sira[1] == sira[4] == sira[7] != "-"
            sutun3 = sira[2] == sira[5] == sira[8] != "-"

            carpraz1 = sira[0] == sira[4] == sira[8] != "-"
            carpraz2 = sira[2] == sira[4] == sira[6] != "-"

            if sira1 or sira2 or sira3 or sutun1 or sutun2 or sutun3 or carpraz1 or carpraz2:
                kart()
                if oyuncu == "O":
                    oyuncu = "X"
                elif oyuncu == "X":
                    oyuncu = "O"
                print("Kazanan oyuncu : ",oyuncu)
                tekrar = input("\nTekrar oynamak ister misin? (e/h) : ")
                if tekrar == 'e':
                    break
                else:
                    xox = False
                    break
            
            # berabere kontrolü
            if sira[0] != "-" and sira[1] != "-" and sira[2] != "-" and sira[3] != "-" and sira[4] != "-" and sira[5] != "-" and sira[6] != "-" and sira[7] != "-" and sira[8] != "-":
                print("Kutularda Yer kalmadı, Oyun berabere")
                tekrar = input("\nTekrar oynamak ister misin? (e/h) : ")
                if tekrar == 'e':
                    break
                else:
                    xox = False
                    break