# algoritmo que pregune al usuario su edad y muestre en pantalla si es mayor de edad o no
# si el usuario tiene entre 14-17 años es adolecente
# y si el usuario tiene 6-13 años es niño

edad = int(input("ingrese la edad: "))

if edad >= 18:
    print("es mayor de edad")
elif edad >= 14 and edad <=17:
    print("es adolecente")
elif edad >= 5 and edad <=13:
    print("es niño")
