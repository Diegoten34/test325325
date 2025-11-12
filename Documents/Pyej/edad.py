n = input("¿Cual es tu nombre? ")
a_n = int(input("¿En que año naciste? "))
año_actual = 2025
edad = a

es_mayor = edad >= 18

print(f"Hola {n}, tienes aproximadamente {edad} años.")
if es_mayor:
    print("Eres mayor de edad.")     
else:
    print("Eres menor de edad.")