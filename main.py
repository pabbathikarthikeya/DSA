class Books:
    def __init__(self, name, author, pages):  # Corrected __int__ to __init__
        self.name = name
        self.author = author
        self.pages = pages
    def __getitem__(self, item):
        if item=='name':
            return self.name
        if item=='author':
            return self.author
    def __add__(self, other):
        return self.pages+other.pages
    def 

book1 = Books('Operating System', 'Kaya', 264)
book2 = Books('DS', 'Anil', 45)
book3 = Books('CN', 'Mani', 69)

print(book2['name'])
print(book2['author'])
print(book2+book3)
