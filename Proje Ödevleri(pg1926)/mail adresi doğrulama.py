# Mail Adresi Doğrulama

import re
a=True
while a==True:
    len_uz=int(input("Uzantı uzunluğunu giriniz:"))
    if len_uz > 3:
        a=True
        print("Yanlış uzunluk girdiniz.")
    else:
        a=False
mail=input("Mail adresinizi giriniz:")

def dogrula(mail):
    sartlar=[False,False,False,False,False]
    if re.search("[@]",mail) is not None:
        sartlar[4]=True
    else:
        sartlar[4]=False
    pattern="[@,.]"
    temp=re.split(pattern,mail)
    if len(temp)!= 4:
        return False
    else:
        pass
    if re.search("[a-zA-Z0-9_-]" ,temp[0]) is not None:
        sartlar[0]=True
    else: 
        sartlar[0]=False 
    if re.search("[a-zA-Z0-9]",temp[1]) is not None:
        sartlar[1]=True
    else: 
        sartlar[1]=False
    global len_uz
    uzunluk="^[a-zA-Z]{{{}}}$".format(len_uz)
    if re.search(uzunluk,temp[2]) is not None:
        sartlar[2]=True
    else: 
        sartlar[2]=False
    if re.search("^[a-zA-Z]{2,4}$",temp[3]) is not None:
        sartlar[3]=True
    else: 
        sartlar[3]=False
    if sartlar[0]==True and sartlar[1]==True and sartlar[2]==True and sartlar[3]==True and sartlar[4]==True:
        return True
    else:
        return False

dogrula(mail)
if dogrula(mail) == False:
    print("Mail Adresiniz yanlış")
else:
    print("Mail Adresiniz doğru")