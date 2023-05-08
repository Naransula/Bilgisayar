def sayiuretyaz():
    import random
    t=0
    sayac=0
    while sayac<3:
        x=random.randint(0,5)
        print(x)
        t=t+x
        sayac=sayac+1
    print(x)

def girilendegertopla():
    t=0
    sayac=0
    while sayac<4:
        x=int(input("Sayı:"))
        t=t+x
        sayac=sayac+1
    print(t)

def teksayitopla():
    x=int(input("Sayı:"))
    i=0
    t=0
    while i<x:
        if i%2==1:
            print(i)
            t=t+i
        i=i+1
    print(t)

def whiletrue():
    while True:
        a=str(input("Sınıf:"))
        if a=="9-D":
            print("Döngü sonlanıyor.")
            break

def whiletruetahmin():
    import random
    x=random.randint(0,30)
    print(x)
    while True:
        y=int(input("Sayı tahmin edin:"))
        if y==x:
            print("Tebrikler!")
            break

def azaltarakyaz():
    x=int(input("Sayı:"))
    i=0
    while i<x:
        x=x-2
        print(x)




















