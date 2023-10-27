class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin


    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
        print(f"Hissi on nyt {self.sijaini}. kerroksessa.")
        return


    def siirry_kerrokseen(self, haluttu_kerros):
        if self.sijainti < haluttu_kerros:

            while self.sijainti < haluttu_kerros:
                self.kerros_ylös()
        elif self.sijainti < haluttu_kerros:
            while self.sijainti < haluttu_kerros:
                self.kerros_alas()
        print("Hissi on nyt halutussa kerroksessa.")


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [] #lista, joka sisältää talon hissit
        #luodaan tarvittavat hissit ja talletetaan ne listaan
        for i in range (hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)


    def aja_hissia(self, hissin_nro, kohdekerros):
        #oletus: käyttäjä antaa hissin numeron 1, 2, 3, ...
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"Hissi {hissin_nro} on nyt halutussa kerroksessa {kohdekerros}.")
        return


    # metodi toiminnan tarkistamiseksi
    def kerro_hissien_sijainnit(self):
        for i in self.hissit:
         print(f"Hissi {i+1} on kerroksessa {i.sijainti}")



#pääohjelma
talo = Talo(1,12,3)
talo.aja_hissia(3, 10)
talo.kerro_hissien_sijainnit()

talo.palohalytys()

print("Hissien sijainnit {kerro_hissien_sijainnit}")