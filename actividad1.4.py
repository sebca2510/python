from collections import deque

def reinicio_turnos():
    digiturno.clear()
    print("Se reinicio la cola")

digiturno = deque(maxlen= 4)
turno = 1


while True: 
    print("\nSeleccione una opción: " )
    print("1. Agregar Cliente")
    print("2. Proximo turno ")
    print("3. Comprobar si la cola está llena")
    print("4. Comprobar si la cola está vacía")
    print("5. Reinicial cola")
    print("6. Salir")
    
    eleccion = input("Escriba el numero de obcion que requiere: ")

    if eleccion == "1":
        if len(digiturno) < digiturno.maxlen:
            cliente = input("Ingrese nombre del cliente: ")
            digiturno.append((turno, cliente))
            print("El turno para: ", cliente , "El turno es: ", turno)
            turno += 1
        else:
            print("La cola esta llena , espera que se atienda un cleinte para agregar otro turno")

    elif eleccion == "2":
        if len(digiturno) > 0:
            atendido = digiturno.popleft()
            print(f"El proximo cliente es: ", atendido[1], "con el turno: ", atendido[0])
        else:
            print("No hay turnos en la cola")

    elif eleccion == "3": 
        if len(digiturno) == digiturno.maxlen:
            print("La cola esta llena")
        else:
            print("La cola aun no esta llena")

    elif eleccion == "4":
        if len(digiturno) == 0:
            print("La cola esta vacia ")
        else:
            print("La cola aun no esta vacia ")

    elif eleccion == "5":
        reinicio_turnos()

    elif eleccion == "6":
        break
    else:
        print("Obcion no valida, porfavor elija nuevamente")