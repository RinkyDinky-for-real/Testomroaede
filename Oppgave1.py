class Film:#A
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score
    def bfunk(self):#B
        print(f"{self.title} was released in {self.year} and currently has a score of {self.score}")

film0 = Film("Inception", 2010, 8.8)
film1 = Film("The Martian", 2015, 8.0)
film2 = Film("Joker", 2019, 8.4)
filmer = [film0, film1, film2]#A

print("A-stil")
for n in filmer:#A
    print (f"{n.title} was released in {n.year} and currently has a score of {n.score}")

print("B-stil")#B
film0.bfunk()
film1.bfunk()
film2.bfunk()