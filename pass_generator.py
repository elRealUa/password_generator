import random

long = int(input("ingrese la longitud de la contraseña: "))
cont = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

for i in range(long):
    password += random.choice(cont)

print(password)
