from tkinter import * # Tkinter kütüphanesi

main = Tk() # Tkinter obje tanımlama
main.geometry("350x430") # Ekran boyutu
main.title("Hesap Makinesi") # Ekran İsmi

def yazi(z): # label'a yazdırma
    global yaz
    yaz = yaz + z
    yazma.config(text=yaz)

def islem(): # İşlemin sonucu bulma ve hata mesajı ayıklama
    try:
        global yaz
        z = eval(yaz)
        yazma.config(text=z)
        yaz = ""
    except Exception as ex:
        labelHata.config(text=ex)

def silme(): # Label'ı tek tek silme
    global yaz
    yaz = yaz[0:-1]
    yazma.config(text=yaz)

def temizle(): # Label'ı komple silme
    global yaz
    yazma.config(text="0")
    yaz = ""

yaz = ""

cerceveLabel = Frame(main,bg="#3399FF", pady=10, padx=11) # Label'ları gruplandırma
cerceveLabel.pack(side="top")

yazma = Label(cerceveLabel, text="0", bd=1, relief=SUNKEN, font=("Vertana",24), width=16, anchor=E)
yazma.pack(pady=10)

labelHata = Label(cerceveLabel, text="Hata Mesajı", fg="black", font=("Vertana",15), bg="#3399FF")
labelHata.pack(side=RIGHT)

cerceveButon = Frame(main,bg="blue") # Butonları gruplandırma
cerceveButon.pack()

x = 3
y = 0
for a in range(1,10): # 1-9 numarları oluşturma ve sıralama
    Button(cerceveButon, text=a, font="Times 12 bold", padx="25", pady="10", bg="black", fg="white",
           cursor="hand2", activeforeground="white", activebackground="gray",
           command=(lambda a=a: yazi(str(a)))).grid(row=x, column=y, pady=5, padx=5)
    y += 1
    if y == 3:
        x -= 1
        y = 0
# Diğer butonları oluşturma ve gruplandırma
Button(cerceveButon, text="(", font="Times 12 bold", padx="26", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("("))).grid(row=0, column=0, pady=5, padx=5) # row = Satır , column = Sütun

Button(cerceveButon, text=")", font="Times 12 bold", padx="26", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi(")"))).grid(row=0, column=1, pady=5, padx=5) # row = Satır , column = Sütun

Button(cerceveButon, text="AC", font="Times 12 bold", padx="21", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=temizle).grid(row=0, column=2, pady=5, padx=5) # row = Satır , column = Sütun

Button(cerceveButon, text="/", font="Times 12 bold", padx="27", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("/"))).grid(row=0, column=3, pady=5, padx=5)

Button(cerceveButon, text="x", font="Times 12 bold", padx="25", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("*"))).grid(row=1, column=3, pady=5, padx=5)

Button(cerceveButon, text="-", font="Times 12 bold", padx="27", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("-"))).grid(row=2, column=3, pady=5, padx=5)

Button(cerceveButon, text="+", font="Times 12 bold", padx="25", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("+"))).grid(row=3, column=3, pady=5, padx=5)

Button(cerceveButon, text="C", font="Times 12 bold", padx="25", pady="10", bg="black", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=silme).grid(row=4, column=0, pady=5, padx=5) # row = Satır , column = Sütun

Button(cerceveButon, text="0", font="Times 12 bold", padx="25", pady="10", bg="black", fg="white",
       cursor="hand2", activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("0"))).grid(row=4, column=1, pady=5, padx=5)

Button(cerceveButon, text=".", font="Times 12 bold", padx="27", pady="10", bg="black", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=(lambda a=a: yazi("."))).grid(row=4, column=2, pady=5, padx=5) # row = Satır , column = Sütun

Button(cerceveButon, text="=", font="Times 12 bold", padx="25", pady="10", bg="green", fg="white", cursor="hand2",
       activeforeground="white", activebackground="gray",
       command=islem).grid(row=4, column=3, pady=5, padx=5) # row = Satır , column = Sütun

main.mainloop()
