import random
def printtall (x):
    x = random.randrange(100)
    print("**********")
    print("***", x, "***")
    print("**********")
tall = 0
for n in range(5):
    printtall(tall)