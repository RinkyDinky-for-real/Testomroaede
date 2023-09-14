jrr_bok = ["The Hobbit", "Farmer Giles of Ham",
"The Fellowship of the Ring","The Two Towers", 
"The Return of the King","The Adventures of Tom Bombadil",
"Tree and Leaf"]

print(jrr_bok[0],",",jrr_bok[1],",",jrr_bok[len(jrr_bok)-2],",", jrr_bok[len(jrr_bok)-1])

jrr_bok.append("The Silmarillion")
jrr_bok.append("Unfinished Tales")

jrr_bok[2] = "Lord of The Rings: The Fellowship of The Ring"
jrr_bok[3] = "Lord of The Rings: The Two Towers"
jrr_bok[4] = "Lord of The Rings: The Return of the King"

jrr_bok.sort()
print(jrr_bok)