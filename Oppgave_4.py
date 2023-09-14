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
for n in den_list:
    print(n)
print("metode nr:3")
for x in range(3):
    print(den_list[x])