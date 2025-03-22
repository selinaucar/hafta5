class hesap:
        def __init__(self, say1, say2):
        self.say1= say1
        self.say2 = say2
        def carp (self):
            carpma sonuc=self.say1 * self.say2
            return sonuc
        def bol(self):
            bolme sonuc=return self.say1 / self.say2
            return sonuc
        def topla(self):
            toplama sonuc=self.say1 + self.say2
            return sonuc
        def cikar(self):
            cikarma sonuc=self.say1 - self.say2
            return sonuc

        def yazdir(self):
            toplam= self.topla()
            carpma= self.carp()
            cikarma= self.cikar()
            bolme= self.bol()

            print('sayilarin toplami:', toplam)
            print('sayilarin carpimi:', carpma)
            print('sayilarin cikarmami:', cikarma)
            print('sayilarin bolme:', toplam)
