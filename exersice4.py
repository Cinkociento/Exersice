# popros uzytkownika o dlugosc jendego i drugiego boku prostokata
# oblicz pole i obwod prostokata (uzyj do tego dwie funckje)
# wypisz pole i obwod prostokata
# zabezpiecz program tak zeby uzytkownik nie mogl go popsuc'
def obwod_prostokata(a, b):
  obwod = a + b + a + b
  return obwod
def pole_prostokata(a, b):
  pole = a * b
  return pole

# try:
  
# except:


b1 = int(input("---------------Podaj pierwszy bok prostokąta: ---------------\nLiczbe wpisz tutaj: "))
b2 = int(input("---------------Podaj drugi bok prostokąta: ---------------\nLiczbe wpisz tutaj: "))

b1_finish = obwod_prostokata(b1, b2)
b2_finish = pole_prostokata(b1, b2)

print(f"\n---------------Obwód twojego prostokąta to: {b1_finish}---------------") 
# print(b1_finish)

print(f"-----------Natomiast pole twojego prostokąta to: {b2_finish}-----------")
# print(b2_finish)