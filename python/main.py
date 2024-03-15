def ingresar_puntos_y_comentarios():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        if point.isdigit() and 1 <= int(point) <= 5:
            comment = input('Introduzca sus comentarios: ')
            with open("data.txt", 'a') as file_pc:
                file_pc.write(f'punto: {point} comentario: {comment}\n')
            break
        else:
            print('Por favor, introduzca una puntuación válida entre 1 y 5.')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as read_file:
        print(read_file.read().strip())

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Introducir puntos de evaluación y comentarios')
        print('2: Comprueba los resultados hasta ahora.')
        print('3: Terminar.')
        num = input()

        if num == '1':
            ingresar_puntos_y_comentarios()
        elif num == '2':
            mostrar_resultados()
        elif num == '3':
            print('Terminación.')
            break
        else:
            print('Por favor, introduzca una opción válida (1, 2 o 3).')

if name == "main":
    main()