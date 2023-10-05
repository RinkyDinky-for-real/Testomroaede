#Oppgave 5.1
filmer = [#A
    {"name" : "Inception", "year" : 2010, "rating" : 8.7},
    {"name" : "Inside Out", "year" : 2015, "rating" : 8.1},
    {"name" : "Con Air", "year" : 1997, "rating" : 6.9}]
def add_film(x,y,z=5.0):#B, Løsningen for C er z = 5.0
    filmer.append({"name" : x,"year" : y,"rating" : z})
add_film("Independence Day","1996",6.6)
add_film("Jurassic Park","1993",8.5)
add_film("Tenet","2020",6.9)
add_film("Barbie","2023",)#C, del 2
#Oppgave 5.2
def fancy_print(x):#A
    print("**********5.2A:**********")
    for i in range(len(x)):
        print(x[i]["name"],"-", x[i]["year"],"has a rating of",x[i]["rating"])
fancy_print(filmer)#A
def avg_rat(x):#B, føler at dette er en tungvint måte å gjøre det på, men whatevs, det funker
    print("**********5.2B:**********")
    movie_ratings = []
    for i in range(len(x)):
        movie_ratings.append(x[i]["rating"])
    avg = sum(movie_ratings) / len(movie_ratings)
    print(f"Gjennomsnitts-ratingen på listen er {avg}")
avg_rat(filmer)#B
def year_check(x):#C
    print("**********5.2C:**********")
    for i in range(len(x)):
        if int(x[i]["year"]) >= 2010:
            print(x[i]["name"],"-", x[i]["year"],"has a rating of",x[i]["rating"])
year_check(filmer)#C