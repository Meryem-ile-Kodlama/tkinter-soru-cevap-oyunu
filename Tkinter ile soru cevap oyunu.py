import tkinter as tk
from tkinter import ttk

sorular = ["Türkiye'nin başkenti?",
           "2+2 kaç eder?",
           "Güneş'e en yakın gezegen?"]

secenekler = [["İstanbul","izmir","Ankara"],
             ["3","4","5"],
             ["Mars","Jüpiter","Merkür"]]

cevap = [3,2,3]

skor = 0
toplam_soru = 3
soru_no = 0

def sonraki_soru():
    global skor,soru_no,toplam_soru
    if deger1.get() == 1:
        verilen_cevap = 1
    elif deger2.get() == 1:
        verilen_cevap = 2
    elif deger3.get() == 1:
        verilen_cevap = 3
    else:
        verilen_cevap = -1

    if cevap[soru_no] == verilen_cevap:
        skor += 1

    if verilen_cevap != -1:
        soru_no += 1

    if soru_no >= toplam_soru:
        soru_l.pack_forget()
        secenek1.pack_forget()
        secenek2.pack_forget()
        secenek3.pack_forget()
        sonraki_b.pack_forget()
        skor_l.pack(pady=40)
        skor_l.config(text="Skorunuz: {}".format(str(skor)),font="Arial 15")
    else:
        deger1.set(0)
        deger2.set(0)
        deger3.set(0)
        soru_l.config(text=sorular[soru_no])
        secenek1.config(text=secenekler[soru_no][0])
        secenek2.config(text=secenekler[soru_no][1])
        secenek3.config(text=secenekler[soru_no][2])

def sec(verilen_cevap):
    global deger1,deger2,deger3
    if verilen_cevap == 1:
        deger2.set(0)
        deger3.set(0)
    elif verilen_cevap == 2:
        deger1.set(0)
        deger3.set(0)
    else:
        deger1.set(0)
        deger2.set(0)

pencere = tk.Tk()
pencere.geometry("600x180")
pencere.title("Soru-Cevap Oyunu")

soru_l = ttk.Label(master=pencere,text=sorular[0],font="Arial 15")
soru_l.pack(pady=10)

deger1 = tk.IntVar()
deger2 = tk.IntVar()
deger3 = tk.IntVar()

secenek1 = ttk.Checkbutton(master=pencere,text=secenekler[0][0],variable=deger1,command=lambda:sec(1))
secenek1.pack()
secenek2 = ttk.Checkbutton(master=pencere,text=secenekler[0][1],variable=deger2,command=lambda:sec(2))
secenek2.pack()
secenek3 = ttk.Checkbutton(master=pencere,text=secenekler[0][2],variable=deger3,command=lambda:sec(3))
secenek3.pack()

sonraki_b = ttk.Button(master=pencere,text="Sonraki",command=sonraki_soru)
sonraki_b.pack(pady=20)

skor_l = ttk.Label(master=pencere)
skor_l.pack_forget()

pencere.mainloop()