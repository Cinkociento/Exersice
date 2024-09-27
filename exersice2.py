
lista = []

for i in range(10):
  number = int(input("Podaj 10 liczb: "))
  lista.append(number)

sortowanie = str(input("czy chcesz posortowac liste malejaco czy rosnaca? Malejaco or Rosnaco: "))

if sortowanie == "Malejaco":
  lista.sort(reverse=True)
elif sortowanie == "Rosnaco":
  lista.sort()
else:
  print("Error: Jestes debilem!")

print(lista)