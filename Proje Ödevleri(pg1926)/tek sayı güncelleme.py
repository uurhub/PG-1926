#Tek Sayı Güncelleme

girdi = None
buyuk = -1
dizi = []

print("Çıkmak için 'q' tuşuna basınız!")

while True:

    try:
        girdi = input("Sayi Gir : ")

        if girdi == "q":
            break
        else:
            dizi.append(int(girdi))
    
    except:
        print("Lütfen sayı giriniz!")


print("{0}".format(dizi))


for i in dizi:
    if i % 2 == 1 and i >= buyuk:
        buyuk = i

print("En büyük tek sayi : ",buyuk)