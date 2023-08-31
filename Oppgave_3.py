#denne koden er en videreutvikling av en eldre kalkulator-kode som jeg har brukt fra videregående
#så mange def
def Add(x,y):#definerer pluss
    return(x+y)
def Minus(x,y):#definerer minus
    return(x-y)
def Times(x,y):#definerer ganger
    return(x*y)
def Divide(x,y):#definerer deling
    return(x/y)
def Divide2(x,y):#definerer deling med nedrunding
    return(x//y)
def Power(x,y):#definerer opphøyning
    return(x**y)
def Modulo(x,y):#definerer modulo
    return(x%y)
#hva er tallene
Num1 = int(input("hva er det første nummeret ditt?"))
Num2 = int(input("hva er det andre nummeret ditt?"))
#kalkulering babyyy
Operation = input("velg hvilken operasjon du vil gjøre med de tallene. velg mellom +,-,*,/,//,**,%")
if Operation == "+":#pluss
    print("resultatet er ", Add(Num1,Num2))
elif Operation == "-":#minus
    print("resultatet er ", Minus(Num1,Num2))
elif Operation == "*":#ganger
    print("resultatet er ", Times(Num1,Num2))
elif Operation == "/":#deler
    print("resultatet er ", Divide(Num1,Num2))
elif Operation == "//":#deler uten desimal
    print("resultatet er ", Divide2(Num1,Num2))
elif Operation == "**":#opphøyer
    print("resultatet er ", Power(Num1,Num2))
elif Operation == "%":#modulo
    print("resultatet er ", Modulo(Num1,Num2))
else:#definerer en error-melding
    raise Exception("Her har du gjort noe galt mann")
