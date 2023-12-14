import csv

def datos_pokemon(archivo_pokemons):
    """
    Recibe un archivo con todos los pokemons de la forma: numero;imagen;nombre;tipos;hp;atk;def;spa;spd;spe.
    Devuelve un dicionario de la forma: {pokemon: numero_pokemon}
    Devuelve una lista con tuplas de la forma: [('Bulbasaur', {'numero': '1', 'imagen': 'imgs/1.gif', 'tipo': 'Grass,Poison', 'hp': '45', 'atk': '49', 'defe': '49', 'spa': '65', 'spd': '65', 'spe': '45'})...]
    """

    lista = []
    diccionario = {}

    with open(archivo_pokemons) as f:
        csv_reader = csv.reader(f, delimiter = ";")
        encabezado = next(csv_reader)

        for linea in csv_reader:
            numero, imagen, nombre, tipo, hp, atk, defe, spa, spd, spe = linea
            lista.append((nombre, {'numero':numero,'imagen':imagen, 'tipo':tipo, 'hp':hp, 'atk':atk, 'defe': defe, 'spa':spa, 'spd':spd, 'spe':spe}))
            diccionario[nombre] = numero
           
    return lista, diccionario

def movimientos_pokemon(archivo_movimientos):
    """
    Recibe un archivo con los movimientos de los pokemons de la forma: nombre;movimientos
    Devuelve un diccionario de la forma: {pokemon: [movimiento1,movimiento1...], ...}
    """
    
    movimientos_por_pokemon = {}
    
    with open(archivo_movimientos) as archivo_movimientos:
        next(archivo_movimientos)
        for fila in archivo_movimientos:
            nombre, movimientos = fila.rstrip("\n").split(";")
            movimientos_por_pokemon[nombre] = movimientos.split(",")
            
    return movimientos_por_pokemon

def guardar_partida(equipos):
    """
    Recibe una lista de la forma: [{equipo: {pokemon: [movimientos]}}, {equipo: {pokemon: []}, ...}]
    Devuelve un nuevo archivo con toda la informacion del diccionario de la forma equipo;pokemon;movimientos...
    """

    equipos_vacios = []

    with open('partida.csv', 'w') as partida:

        for equipo in equipos:
            
            for nombre_equipo, pokemons in equipo.items():

                if pokemons == {}:
                    equipos_vacios.append(nombre_equipo)
                
                for pokemon, movimientos in pokemons.items():
                    mov = ",".join(movimientos) 
                    partida.write(f"{nombre_equipo};{pokemon};{mov}\n")
                
        for equipos in equipos_vacios:
            partida.write(f"{equipos};\n")

def cargar_partida(archivo_equipos):
    """
    Recibe un archivo de la forma equipo;pokemon;movimiento1,movimiento2...
    Devuelve una lista de la forma: [{equipo: {pokemon: [movimientos]}}, {equipo: {pokemon: []}, ...}]
    """

    resultado = []
    equipos = {}
    
    try:
        with open(archivo_equipos) as f:
            csv_reader = csv.reader(f, delimiter = ";")

            for linea in csv_reader:
                
                if len(linea) == 3:
                    nombre_equipo, pokemon, movimientos = linea
                    movimientos = movimientos.split(",")
                    equipos[nombre_equipo] = equipos.get(nombre_equipo, {})
                    equipos[nombre_equipo][pokemon] = equipos[nombre_equipo].get(pokemon, []) + movimientos
                    
                if len(linea) == 2:
                    nombre_equipo, pokemon = linea
                    equipos[nombre_equipo] = equipos.get(nombre_equipo, {})
                    
        for equipo, pokemons in equipos.items():
            dic = {}
            dic[equipo] = pokemons
            resultado.append(dic)
        
        return resultado
                
    except FileNotFoundError:
        return resultado

def informacion_nombre(pokemons, indices_pokemons, pokemon):
    """
    Recibe una lista ordenada de tuplas de la forma: [(pokemon, {info_pokemon})...].
    Recibe un diccionario de la forma: {pokemon:numero_pokemon}.
    Recibe el nombre del pokemon particular.
    Devuelve un diccionario que contiene la informacion del pokemon.
    """
    
    pokemon_numero = int(indices_pokemons[pokemon])
    return pokemons[pokemon_numero - 1][1]

def obtener_nombre(pokemons, numero):
    """
    Recibe una lista ordenada de la forma [(pokemon, {info_pokemon})].
    Recibe un numero que corresponde a un pokemon.
    Devuelve el pokemon que corresponde dado el numero.
    """

    return pokemons[numero - 1][0]

def esta_pokemon(numero_pokemons, pokemon):
    """
    Recibe un diccionario de la forma: {pokemon:numero_pokemon}.
    Devuelve True si el pokemon se encuentra en el diccionario y devuelve False si el pokemon no se encuentra en el diccionario.
    """

    try:
        numero_pokemons[pokemon]
        return True

    except KeyError:
        return False

def informacion_numero(pokemons, numero_actual):
    """
    Recibe una lista de tuplas de la forma:[(pokemon1, {informacion1}), (pokemon2, {informacion2}), ...]
    Recibe el numero del pokemon actual.
    Devuelve una tupla con la informacion del pokemon.
    """
    
    informacion = pokemons[numero_actual]
    return informacion

def obtener_movimientos(movimientos, pokemon):
    """
    Recibe un diccionario de la forma {nombre: [movimientos],...}
    Devuelve una lista con los movimientos del pokemon que se introduce como parametro.
    """

    return movimientos[pokemon]
    
def agregar_equipo(equipos, nombre_equipo): 
    """
    Recibe una lista de la forma: [{equipo: {pokemon: [movimientos]}}]
    Devuelve la lista equipos con el nuevo equipo.
    """

    equipo_nuevo = {}
    equipo_nuevo[nombre_equipo] = {}
    equipos.append(equipo_nuevo)
    return equipos

def eliminar_equipo(equipos, numero_equipo):
    """
    Recibe un diccionario de la forma: [{equipo: {pokemon: [movimientos]}}]
    Recibe el numero del equipo a borrar.
    Devuelve el diccionario equipos sin el equipo que se introdujo como parametro.
    """

    equipos.pop(numero_equipo)
    return equipos

def agregar_pokemon(equipos, numero_equipo, nombre_equipo, pokemon):
    """
    Recibe una lista de la forma [{equipo: {pokemon: [movimientos]}}]
    Recibe el numero/nombre del equipo donde se agregara el pokemon.
    Recibe el nombre del pokemon que se desea agregar.
    Devuelve el diccionario equipos con el nuevo pokemon en su respectivo equipo y con los movimientos.
    """

    equipo = equipos[numero_equipo]
    equipo[nombre_equipo][pokemon] = equipo[nombre_equipo].get(pokemon, [])
    return equipos

def borrar_pokemon(equipos, numero_equipo, nombre_equipo, pokemon):
    """
    Recibe una lista de la forma: [{equipo: {pokemon: [movimientos]}}]
    Recibe el nombre/numero del equipo donde se debe borrar el pokemon.
    Recibe el nombre del pokemon a borrar.
    Devulve la lista de equipos sin el pokemon.
    """

    equipos[numero_equipo][nombre_equipo].pop(pokemon)
    return equipos
    
def agregar_movimientos(equipos, numero_equipo, nombre_equipo, pokemon, movimiento):
    """
    Recibe una lista de la forma: [{equipo: {pokemon: [movimientos]}}]
    Recibe el numero/nombre del equipo, el pokemon y el movimiento.
    Recibe el nombre del pokemon.
    Recibe el movimiento que se desea agregar.
    Devuelve el diccionario de equipos con el movimiento agregado.
    """

    equipo = equipos[numero_equipo]
    equipo[nombre_equipo][pokemon] += [movimiento]
    return equipos
