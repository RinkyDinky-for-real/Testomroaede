#oppgave 5.1
filmer = [#A
    {"name" : "Inception", "year" : 2010, "rating" : 8.7},
    {"name" : "Inside Out", "year" : 2015, "rating" : 8.1},
    {"name" : "Con Air", "year" : 1997, "rating" : 6.9}]
def add_film(x,y,z):#B
    if z is not float :#C, del 1
        z = 5.0
    filmer.append({"name" : x,"year" : y,"rating" : z})
for n in filmer:
    print(n)
print("**********neste**********")
add_film("Independence Day","1996", 6.6 )
add_film("Jurassic Park","1993", 8.5 )
add_film("Tenet","2020", 6.9 )
add_film("Barbie","2023", )#C, del 2
for n in filmer:
    print(n)
