class Publication:
    def __init__(self, title, author_or_editor, pages=None):
        self.title = title
        self.author_or_editor = author_or_editor
        self.pages = pages

    def tulosta_tiedot(self):
        print(f"Title: {self.title}")
        print(f"Author/Editor: {self.author_or_editor}")
        if self.pages is not None:
            print(f"Pages: {self.pages}")

class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)

class Magazine(Publication):
    def __init__(self, title, editor):
        super().__init__(title, editor)

# kirjan ja lehden tarkemmat ja toisistaan eroavat tiedot
book = Book("Hytti nro. 6", "Rosa Likson", 200)
magazine = Magazine("Aku Ankka", "Aki Hyyppä")

# metodi tietojen tulostamiseksi
book.tulosta_tiedot()
print("\n")
magazine.tulosta_tiedot()
