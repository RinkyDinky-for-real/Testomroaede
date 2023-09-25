src_list = ['Farmer Giles of Ham', 'Lord of The Rings: The Fellowship of The Ring', 
'Lord of The Rings: The Return of the King', 'Lord of The Rings: The Two Towers', 
'The Adventures of Tom Bombadil', 'The Hobbit',
'The Silmarillion', 'Tree and Leaf', 'Unfinished Tales']

den_list = list()

den_list.insert(0,src_list[1])
den_list.insert(1,src_list[2])
den_list.insert(2,src_list[3])
print("metode nr:1")
for i in den_list:
    print(i)
print("metode nr:2")
for x in range(len(den_list)):
    print(den_list[x])
for i in range (len(den_list)):
    print("{}.{}".format(i + 1, den_list[i]))#med denne får man nummererte
print("metode nr:3")
for i in range (len(den_list)):
    print("{}.{}".format(i + 1, den_list[i]))#med denne får man nummererte    print(den_list[x])
print("metode nr:4")
for index, element in enumerate(den_list):#annen metode for å nummerere
  print(index, ":", element)