print('CONTEO RAPIDO "ELECCIONES GENERALES 2023"')
partidos = []
while True:
    opcion = int(input('1. Ingresar partidos políticos\n2. Ingresar Actas\n3. Ver Resultados\n'
                       '4. Exportar Resultados\n'))
    if opcion == 1:
        while True:
            partido = {"Codigo": input('Ingrese código del partido: '),
                       "Nombre":  input('Ingrese nombre del partido: '),
                       "Siglas": input('Ingrese siglas del partido: '), "Numero Votos": 0}
            partidos.append(partido)
            decision = input('Desea ingresar otro partido político (s/n):\n')
            if decision == 's':
                continue
            elif decision == 'n':
                break
            else:
                print('Ingresa una opción válida.')
                continue
    if opcion == 2:
        while True:
            partido_encontrado = False
            mesa = input('Ingrese número de mesa: ')
            departamento = input('Ingrese el departamento: ')
            munipicio = input('Ingrese el municipio: ')
            cod = input('Ingrese el código del partido: ')
            cant_votos = int(input('Ingrese la cantidad de exacta de votos válidos: '))
            for i in range(len(partidos)):
                if partidos[i]["Codigo"] == cod:
                    partido_encontrado = True
                    partidos[i]["Numero Votos"] += cant_votos
            if not partido_encontrado:
                print('No se pudo encontrar el partido ingresado, reintentar.')
                continue
            decision = input('Desea ingresar otro partido político (s/n):\n')
            if decision == 's':
                continue
            elif decision == 'n':
                break
            else:
                print('Ingresa una opción válida.')
                continue
    if opcion == 3:
        listado_votos = []
        listado_votos_ordenado = []
        for i in range(len(partidos)):
            listado_votos.append(partidos[i]["Numero Votos"])
        for voto in listado_votos:
            mayor = voto
            if mayor < voto:
                mayor = voto
                listado_votos_ordenado.append(mayor)

        print(listado_votos_ordenado)
    if opcion == 4:
        print('Gracias por usar mi sistema.')
        break


