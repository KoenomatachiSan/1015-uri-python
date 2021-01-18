import math

LINHA1 = input("LINHA1").split(" ")
LINHA2 = input("LINHA2").split(" ")

X1,Y1 = LINHA1
X1,Y2 = LINHA2

distancia = math.sqrt(((float(X1) - float(X1))*(float(X1) - float(X1))) + ((float(Y2)-float(Y1)) *(float(Y2)-float(Y1))))

print("%0.4f" %distancia)