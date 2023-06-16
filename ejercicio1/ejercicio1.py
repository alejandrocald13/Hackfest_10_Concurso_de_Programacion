import sys
lista_departamentos = {"16": "Alta Verapaz",
                       "15": "Baja Verapaz", "04": "Chimaltenango", "01": "Guatemala", "02": "El Progreso",
                       "03": "Sacatepequez", "05": "Escuintla", "06": "Santa Rosa", "07": "Sololá", "08": "Totonicapán",
                       "09": "Quetzaltenango", "10": "Suchitepequez", "11": "Retalhuleu", "12": "San Marcos",
                       "13": "Huehuetenango", "14": "Quiché", "17": "Petén", "18": "Izabal", "19": "Zacapa",
                       "20": "Chiquimula", "21": "Jalapa", "22": "Jutiapa"}
lista_municpios = {"09001": "Quetzaltenango", "09004": "San Carlos Sija", "09006": "Cabricán", "09007": "Cajolá",
                   "09030": "El Eden Palestina De Los Altos", "21002": "San Pedro Pinula"}
while True:
    print('ELECCIONES GENERALES 2023')
    posicion = 0
    cadena_dia = ''
    cadena_mes = ''
    cadena_anio = ''
    edad_votar = False
    fecha = input('Ingrese su fecha de nacimiento en formato (DDMMAAAA): ')
    if len(fecha) != 8:
        print('Vuelva a intentarlo, no coincide al formato solicitado.')
        continue
    else:
        for digito in fecha:
            posicion += 1
            if posicion <= 2:
                cadena_dia += digito
            elif posicion <= 4:
                cadena_mes += digito
            elif posicion <= 8:
                cadena_anio += digito
        try:
            cadena_dia = int(cadena_dia)
            cadena_mes = int(cadena_mes)
            cadena_anio = int(cadena_anio)
            print('Formato ingresado exitosamente.')
        except ValueError:
            print('Vaya, parece que ingresaste un formato erróneo.')

        if cadena_dia > 31:
            print('Dia no válido.')
            continue
        if cadena_mes > 12:
            print('Mes no válido.')
            continue

        if 2023 - cadena_anio >= 18:
            if cadena_anio == 18 and cadena_mes <= 6 and cadena_dia <= 15:
                if 2023 - cadena_anio == 18:
                    print('Tienes 18 años, pero no aún no los has cumplido.')
            else:
                print('Tienes edad para votar.')
                edad_votar = True
        else:
            print(f'Aún no puede votar, cuenta con {2023 - cadena_anio} años.')

        mesa = ''
        centro = ''
        departamento = ''
        municipio = ''

        if edad_votar:
            while True:
                try:
                    dpi = int(input('Ingrese el número de DPI: '))
                    dpi = str(dpi)
                    if len(dpi) != 13:
                        print('Vaya, ese no es un número de DPI, vuelve a intentarlo.')
                        continue
                    else:
                        break
                except ValueError:
                    print('Ingresaste una letra, no puedo ayudarte.')

            for i in range(len(dpi)):
                if i <= 3:
                    mesa = mesa + dpi[i]
                elif i <= 8:
                    centro += dpi[i]
                elif i <= 10:
                    departamento += dpi[i]
                elif i <= 12:
                    municipio += dpi[i]
            print('Datos del Centro de Votación')
            print(f'Departamento: {lista_departamentos[departamento]}')
            print(f'Municipio: {lista_municpios[departamento + "0" + municipio]} ')
            print(f'Centro de Votación: {centro}')
            print(f'Mesa: {mesa}')
        while True:
            decision = input('¿Desea realizar otra consulta? (S/N):\n')
            if decision == 'S':
                break
            elif decision == 'N':
                sys.exit('Espero haberte ayudado.')
            else:
                continue
        continue

# Los municipios funcionan 6 de Quetzaltenango y 1 de Jalapa
# Todos los departamentos funcionan!
