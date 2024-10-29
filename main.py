#odwoływanie się do jednego znaku stringa. Zachowuje się jak lista
tekst = "Hello world"
print(tekst[2])


#doklejanie podanego stringa do każdego elementu listy
print(",-- ".join(["a", "b", "c"]))

#podmiana wyrazow
print("Witaj Swiecie".replace("Swiecie", "Mario"))
print("Witaj Swiecie".replace("e", "a"))

wyraz = 'Mercedes'
print(id(wyraz))
wyraz = wyraz.replace('ced', 'BMW') #wymaga przypisania do zmiennej, żeby zmiana się zapisała
wyraz.replace('BMW', 'aa') #nie zapisze wyniku replace. String jest niemutowalny i dlatego tak się dzieje
print(wyraz)
print(id(wyraz))

#sprawdzanie czy dany string zaczyna sie od podanego argumentu
print("To jest zdanie".startswith("To"))
print("To jest zdanie".endswith("ale"))
#czy dane wyrązenie jest w ciągu
print("j" in "To jest zdanie")

#Zmiana rozmiaru string
print("To jest zdanie".upper())
print("To jest ZDANIE".lower())


#tworzenie krotek jako par z numeracja
lista = [10, 20, 24, 33, 40]
lista_krotek = []
for i in enumerate(lista):
    print(i)
    print(i[0], i[1])
    lista_krotek.append(i)
print(lista_krotek)