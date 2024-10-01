# Napisz funkcję, która przyjmuje liste zawierającą liczby i zwraca nową liste z tymi 
# samymi liczbami posortowanymi w porządku rosnącym lub malejacym, w zaleznosci od argumentu podanego do funckji.
import sys

def pobrana_lista():
  lista = []
  for i in range(5):
    pobierz = int(input("Podaj liczby do listy: "))
    lista.append(pobierz)
  sortowanie = input("Chcesz posortowac liste malejaco czy rosnaco?: ")
  if sortowanie in ["rosnaco", "Rosnaco", "rosnąco", "Rosnąco"]:
    lista.sort()
    return lista
  elif sortowanie in ["Malejąco", "malejąco", "malejaco", "Malejaco"]:
    lista.sort(reverse=True)
    return lista
  else:
    sys.exit(1)

x = pobrana_lista()
print(x)