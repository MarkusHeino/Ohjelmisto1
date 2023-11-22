class Person:
    def __init__(self, first_name, last_name):
        # Person-luokan alustusmetodi (__init__)
        self.first_name = first_name  # Aseta etunimi
        self.last_name = last_name  # Aseta sukunimi

    def plot(self):
        # Plot-metodi, tulostaa henkilön nimen
        print("-- My name is {} {}".format(self.first_name, self.last_name))


class Student(Person):
    def __init__(self, first_name, last_name, student_number):
        # Student-luokan alustusmetodi, perii Person-luokan ominaisuudet
        super().__init__(first_name, last_name)
        self.student_number = student_number  # Aseta opiskelijanumero

    def plot(self):
        # Plot-metodi, tulostaa opiskelijan nimen ja opiskelijanumeron
        print("-- My name is {} {} and my student number is {}".format(
            self.first_name, self.last_name, self.student_number))


# Pääohjelma
p1 = Person("James", "Bond")  # Luo henkilö nimeltä "James Bond"
s1 = Student("Johnny", "English", 321)  # Luo opiskelija nimeltä "Johnny English" opiskelijanumerolla 321

p1.plot()  # Tulosta henkilön tiedot
s1.plot()  # Tulosta opiskelijan tiedot
