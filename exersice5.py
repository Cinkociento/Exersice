# Napisz funkcję, która przyjmuje liste zawierającą liczby i zwraca nową liste z tymi 
# samymi liczbami posortowanymi w porządku rosnącym lub malejacym, w zaleznosci od argumentu podanego do funckji.
import sys
import time

def pobrana_lista():
  lista = []
  try:
      pobierz = int(input("Podaj liczby do listy: "))
  except ValueError:
      print("ERROR! - Wpisz liczbe!")
      time.sleep(2)
      sys.exit(1)

  for i in range(4):
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
    print("ERROR! - Wybrano nieprawidłowa! fraze Wybierz pomiedzy sortowaniem malejacym lub rosnacym")
    time.sleep(2)
    sys.exit(1)

x = pobrana_lista()
print(x)