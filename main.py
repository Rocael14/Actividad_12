def menu():
    print("--- MENU ---")
    print("1. Ingrese Pedidos Repartidos")
    print("2. Ordenar repartidores")
    print("3. Buscar Repartidor")
    print("4. Estadisticas")
    print("5. Salir")

def busqueda_por_valor(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return elemento
    return None


def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores)+iguales+quick_sort(mayores)


while True:
    menu()
    try:
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print("Pedidos Repartidos")
                cantidad_repartidos = int(input("Ingrese la cantidad de repartidores: "))
            case 2:
                print("Ordenar repartidores")
            case 3:
                print("Buscar Repartido")
            case 4:
                print("Estadisticas")
            case 5:
                print("Salir")
            case _:
                print("Opcion invalida")

    except Exception:
        print("Debe ingrear parametros numericos")