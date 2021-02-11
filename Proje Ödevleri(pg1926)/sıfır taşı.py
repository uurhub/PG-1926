#Sıfır Taşı

girdi = None
dizi = []

print("Çıkmak için 'q'tuşuna basınız!")

while True:
    girdi = input("Sayi gir :")
    
    try:
        if girdi == "q":
            break
        elif girdi == "0":
            dizi.insert(0,int(girdi))
        else:
            dizi.append(int(girdi))

    except:
        print("Lütfen sayi giriniz")

print("Dizi :",dizi)