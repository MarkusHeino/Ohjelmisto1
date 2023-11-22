class Tili:
    def __init__(self, omistaja, saldo=0):
        # Tili-luokan alustusmetodi (__init__)
        self.omistaja = omistaja  # Aseta tilin omistaja
        self.saldo = saldo  # Aseta tilin saldo
        print("Tilejä luotu: {}".format(Tili.laske_tilit()))  # Tulosta luotujen tilien määrä

    @classmethod
    def laske_tilit(cls):
        # Luokkametodi seuraavaa varten, pitää kirjaa luoduista tileistä
        if not hasattr(cls, 'tilit'):
            cls.tilit = 0
        cls.tilit += 1
        return cls.tilit

    def maksa(self, maara):
        # Maksu-metodi, vähentää tililtä annetun määrän, jos saldo riittää
        if self.saldo >= maara:
            self.saldo -= maara
            print("Maksu onnistui")
        else:
            print("Ei tarpeeksi rahaa")

    def tulostus(self):
        # Tulostus-metodi, tulostaa tilin omistajan ja saldon
        print("Omistaja: {}, tilillä rahaa {}".format(self.omistaja, self.saldo))


# Pääohjelma
print("--- tilien luonti ---")
t1 = Tili("Jorma")  # Luo tilin omistajalle "Jorma" ilman alkusaldoa
t2 = Tili("Anne", 100)  # Luo tilin omistajalle "Anne" alkusaldo 100

print("--- maksut ---")
t1.maksa(25)  # Yritä tehdä maksu tililtä, jolla ei ole tarpeeksi rahaa
t2.maksa(25)  # Tee maksu tililtä, jolla on tarpeeksi rahaa

print("--- tilien saldot ---")
t1.tulostus()  # Tulosta tilin tiedot (omistaja ja saldo)
t2.tulostus()  # Tulosta toisen tilin tiedot
