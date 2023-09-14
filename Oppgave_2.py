print("for løkke nå")
for n in range(9, 101):
    if n/2 != n//2:
        print(n)
print("while løkke nå")
n = 9
while n < 101:
    if n/2 != n//2:
        print(n)
        n += 1
    else:
        n += 1