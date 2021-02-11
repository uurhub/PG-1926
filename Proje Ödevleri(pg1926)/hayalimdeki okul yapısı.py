# Hayalimde'ki Okul Yapısı

class Okul():
    tip="Okul"
    
    def __init__(self,calisan=3,bina=1,ekbina=0,bahce=True):
        self.calisan=calisan
        self.bina=bina
        self.ekbina=ekbina
        self.bahce=bahce

okul1 = Okul(30,2,1,True)
okul2 = Okul(80,3,2,False)
okul3 = Okul(calisan=35,ekbina=2)
print(okul3.calisan)
print(okul1.__class__.tip)