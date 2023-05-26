def baslangicbitisartis():
    baslangic=int(input("Başlangıç değeri:"))
    bitis=int(input("Bitiş değeri:"))
    artis=int(input("Artış değeri:"))
    for i in range(baslangic,bitis,artis):
        print(i)

def ciftsayilar():
    baslangic=int(input("Başlangıç değeri:"))
    bitis=int(input("Bitiş değeri:"))
    for i in range(baslangic,bitis):
        if i%2==0:
            print(i)

def harfharfisim():
    isim=str(input("İsim:"))
    for i in a:
        print(i)

def carpimtablosu():
    for i in range(1,10):
        print("----------")
        for a in range(1,10):
            print(i*a)

def ucunkatitopla():
    a=int(input("Sayı:"))
    if a<1 or a>10:
        a=int(input("Sayı:"))
    import random
    b=random.randint(11,50)
    print(b)
    t=0
    for i in range(a,b):
        if i%3==0:
            print(i)
            t=t+i
    print(t)

def kare():
    x=str(input("Harf:"))
    y=int(input("Sayı:"))
    for i in range(y):
        print(x*y) # Üçgen için ise print(x*i)








    
