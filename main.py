
#doklejanie podanego stringa do każdego elementu listy
print(",-- ".join(["a", "b", "c"]))
print("Witaj Swiecie".replace("Swiecie", "Mario"))
print("Witaj Swiecie".replace("e", "a"))

#sprawdzanie czy dany string zaczyna sie od podanego argumentu
print("To jest zdanie".startswith("To"))
print("To jest zdanie".endswith("ale"))
#czy dane wyrązenie jest w ciągu
print("j" in "To jest zdanie")

print("To jest zdanie".upper())
print("To jest ZDANIE".lower())

print("-----")
#Operacje na listach z liczbami

lista = [10, 20, 24, 33, 40]

if all([i % 2 == 0 for i in lista]):
    print(lista)
    print("Wszystkie parzyste")

if any(i % 2 == 1 for i in lista):
    print("Chociaż jeden nieparzysty")

#tworzenie krotek jako par z numeracja
for i in enumerate(lista):
    print(i)
    print(i[0], i[1])


