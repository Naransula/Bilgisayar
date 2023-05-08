# Fonksiyon içine yazılmış komutların çağırılarak tekrar tekrar kullanılmasını sağlar.

# Kullanıcıdan istenen sayının çift mi tek mi olduğunu belirler.
def cifttek():
    import random
    a=random.randint(1,50)
    print(a)
    if a%2==0:
        print("Sayı çift.")
    else:
        print("Sayı tek.")

# Kullanıcının girdiği not değerlerinin ortalamasını alır ve geçtiğini veya kaldığını yazar.
def ortalama():
    not1=int(input("İlk not:"))
    not2=int(input("İkinci not:"))
    ortalama=(not1+not2)/2
    print(ortalama)
    if ortalama>=50:
        print("Geçti.")
    else:
        print("Kaldı.")

# Kayıt ve giriş sistemi oluşturur.
def kayit():
    kayitisim=str(input("Kullanıcı adı belirleyiniz:"))
    kayitsifre=int(input("Şifre belirleyiniz:"))
    print("Kayıt yapıldı.")
    girisisim=str(input("Kullanıcı adınız:"))
    girissifre=int(input("Şifreniz:")

    if kayitisim==girisisim and kayitsifre=girissifre:
                   print("Başarıyla giriş yaptınız.")
    else:
        print("Kullanıcı adınız veya şifreniz yanlış.")

# Bir tahmin oyunu oynamanızı sağlar.
def tahmin():

    cevap=random.randint(1,5)
    sayi=int(input("Tahmininiz:"))

    if sayi == cevap:
        print("Kazandın!")
    else:
        print("Kaybettin...")
        print("Doğru sayı:", cevap)

# Bir hesap makinesi kullanmanızı sağlar.
def hesap():
    sayi1 = int(input("1. sayı"))
    sayi2 = int(input("2. sayı"))
    islem = str(input("Yapılacak işlemin sembolü?"))

    if islem == "+":
        print(sayi1 + sayi2)
    elif islem == "-":
        print(sayi1 - sayi2)
    elif islem == "*":
        print(sayi1*sayi2)
    elif islem == "/":
        print(sayi1/sayi2)
    elif islem == "%":
        print(sayi%sayi2)
    elif islem == "**":
        print(sayi1**sayi2)

# Bir geziye katılıp katılamayacağınızı belirler ve yazdırır.
def gezi():
    devamsizlik = int(input("Devamsızlık yaptığınzı gün sayısı:"))
    ortalama = int(input("Not ortalamanız:"))

    if devamsizlik<5 or ortalama>85:
        print("Geziye gidebilirsin!")
    else:
        print("Maalesef geziye gitmeye uygun değilsin.")

# Stok bilgileri girmenizi ve stoğu kontrol etmenizi sağlar.
def stok():
    urun = str(input("Ürün ismi:"))
    stok = int(input("Stok adedi:"))
    print("Stok kaydı yapıldı.")

    adet = int(input("Üründen kaç adet alacaksınız?"))

    if stok>=adet:
        print("Üründen yeterli sayıda mevcut.")
    elif stok<adet:
        print("Üründen yeterli sayıda yok.")
