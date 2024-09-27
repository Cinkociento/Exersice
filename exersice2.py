lista = []

for i in range(10):
  number = int(input("Enter 10 numbers: "))
  lista.append(number)

sortowanie = str(input("Do you want to sort your number in Descending or Ascending order?: "))

if sortowanie == "Descending":
  lista.sort(reverse=True)
elif sortowanie == "Ascending":
  lista.sort()
else:
  print("Error: You are stupid!")
print(lista)