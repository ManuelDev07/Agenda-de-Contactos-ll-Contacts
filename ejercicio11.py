'''

Ejercicio Nro11 - Realizar un programa que simule una agenda de contactos.Crear un
diccionario donde la clave sea el nombre del contacto y el valor sea el número
de teléfono, el programa tendrá el siguiente menú de opciones:

1.- Nuevo contacto
2.- Borrar contacto
3.- Ver contacto
4.- Salir

'''

print("AGENDA DE CONTACTOS")
print("Opciones:")
print("1 para NUEVO CONTACTO")
print("2 para BORRAR CONTACTO")
print("3 para MOSTRAR CONTACTOS existentes de la agenda")
print("4 para SALIR")

diccionario = {}

while True:
    opc = int(input('¿Que desea realizar? '))
    if opc == 1:
        name = input('Ingrese el nombre del nuevo contacto: ')
        tlf = int(input('Ingrese el numero de telefono: '))
        diccionario[name] = tlf
        print('Datos Guardados con exito')
    elif opc == 2:
        name = input('Ingrese el nombre del contacto a eliminar: ')
        if name in diccionario:
            del(diccionario[name])
            print('Contacto Eliminado')
        else:
            print('Contacto Inexistente')
    elif opc == 3:
        print('LISTA DE CONTACTOS')
        for name, tlf in diccionario.items():
            print(f'Nombre: {name} | Telefono: {tlf}') 
    elif opc == 4:
        print('Agenda Cerrada.')
        break
    else:
        print('ERROR Opcion inexistente')