# if - elif - else koşul içeren durumlarda kullanılırlar.

# Örnek: Kullanıcıdan sayı isteyip pozitif, negatif veya sıfır olduğunu ekrana yazdırınız.
x=int(input("Bir sayı giriniz:"))
if x<0:
    print("Sayı negatif.")
elif x>0:
    print("Sayı pozitif.")
else:
    print("Sayı sıfır.")


# Örnek: 1 ve 50 arasında rastgele sayı üretip sayının 3ün tam katı olup olmadığını ekrana yazdırınız.
import random
x=random.randint(1,50)
if x%3==0:
    print("Sayı 3'ün tam katı.")
else:
    print("Sayı 3'ün tam katı değil.")
