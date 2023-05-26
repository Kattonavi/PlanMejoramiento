# crea un programa donde guarde una conseña en una variable
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña que introduce
# el usuario coincide con la guardada en la variable

clave = "prueba1234567890"

clave_usuario = input("ingrse la contraseña ")

if clave == clave_usuario:
    print("La contraseña coincide ")
else:
    print("La contraseña no coincide ")