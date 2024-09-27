max = int(input("Podaj max'a: "))

lista = [i for i in range(0, max)]

for i in range(0, max, 2):
  print(i)

lista.clear()
print(lista)