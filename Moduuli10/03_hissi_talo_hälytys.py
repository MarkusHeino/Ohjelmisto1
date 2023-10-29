class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin


    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti -= 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa.")
        return

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa.")
        return

    def siirry_kerrokseen(self, haluttu_kerros):
        if self.sijainti < haluttu_kerros:
            while self.sijainti < haluttu_kerros:
                self.kerros_ylos()
        elif self.sijainti > haluttu_kerros:
            while self.sijainti > haluttu_kerros:
                self.kerros_alas()
        print("Hissi on nyt halutussa kerroksessa.")


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []  # lista, joka sisältää talon hissit
        # luodaan tarvittavat hissit ja talletetaan ne listaan
        for i in range(hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)


    def aja_hissia(self, hissin_nro, kohdekerros):
        hissi = self.hissit[hissin_nro - 1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"Hissi {hissin_nro} on nyt halutussa kerroksessa {kohdekerros}.")
        return

    # palohälytys, joka siirtää kaikki hissit pohjakerrokseen
    def palohalytys(self):
        self.palohalytys = True
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)  # siirrä kaikki hissit pohjakerrokseen

    # metodi toiminnan tarkistamiseksi
    def kerro_hissien_sijainnit(self):
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i + 1} on kerroksessa {hissi.sijainti}")



# pääohjelma
talo = Talo(1, 12, 3)
talo.aja_hissia(3, 10)
talo.aja_hissia(2, 7)
talo.aja_hissia(1, 11)
talo.kerro_hissien_sijainnit()
print("Talossa on palohälytys..!")
talo.palohalytys()
talo.kerro_hissien_sijainnit()