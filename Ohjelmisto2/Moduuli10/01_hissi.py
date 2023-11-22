class Hissi:
    def __init__(self):
        self.sijainti = 1  # hissi aloittaa pohjakerroksesta

    def kerros_ylös(self):
        if self.sijainti < 6:  # talossa on kuusi kerrosta
            self.sijainti += 1
            print(f"Hissi on nyt {self.sijainti}. kerroksessa.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.sijainti > 1:
            self.sijainti -= 1
            print(f"Hissi on nyt {self.sijainti}. kerroksessa.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

    def siirry_kerrokseen(self, haluttu_kerros):
        while self.sijainti < haluttu_kerros:
            self.kerros_ylös()
        while self.sijainti > haluttu_kerros:
            self.kerros_alas()
        if self.sijainti == 6:
            print(f"Hissi on nyt {self.sijainti}. kerroksessa, jonne se kutsuttiin.")

# testi
elevator_G = Hissi()
elevator_G.siirry_kerrokseen(6)  # Move the elevator to the 6th floor.

# kutsu hissiä haluttuun kerrokseen
elevator_G.siirry_kerrokseen(1)
