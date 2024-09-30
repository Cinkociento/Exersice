# stworz funckje do konwertowania temperatury celcjusza na farenheita i uzyj ich
#F = C * 9/5 + 32
#C = (F - 32) * 5/9

t_c = 30

def konwert_C_F(C):
  F = C *  9/5 + 32
  return F

xd = konwert_C_F(t_c)

print(xd)

def konwert_C_F(F):
  C = (F - 32) * 5/9
  return C