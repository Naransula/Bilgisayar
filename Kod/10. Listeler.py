#Liste oluştur
liste=["gergin görünüşlü adam","kral ragnar","sultan hakim"]

#Listeden çağar
print(liste[1])

#Liste sonuna eleman ekle
liste.append("kral harlaus")
print(liste)

#Listede eleman değiştirme
liste[0]="kral graveth"
print(liste)

#Listedeki ilk iki elemanı değiştirme
liste[:2]=["sancar han","yaroglek"]
print(liste)

#Listedeki eleman sayısını öğren
print(len(liste))

#Listeden belirtilen elemanı çıkartır.
liste.pop(1)
print(liste)

#Listeyi sıraya sokar
liste.sort()
print(liste)

#Listeyi ters sıraya sokar
liste.sort(reverse=True)
print(liste)
