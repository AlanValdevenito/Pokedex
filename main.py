import gamelib
import pokedex

ANCHO_VENTANA = 950
ALTO_VENTANA = 650

MAX_POKEMONS = 6
MAX_MOVIMIENTOS = 4

def pokedex_crear():
    """
    Inicializa el estado de la pokedex.

    Devuelve una lista de la forma: [(pokemon1, {informacion1}), (pokemon2, {informacion2}), ...]
    Devuelve un dicionario con todos los pokemons de la forma: {pokemon: numero_pokemon}
    Devuelve un diccionario de la forma: {pokemon: [movimiento1,movimiento1...], ...}
    Devuelve un diccionario de la forma: {equipo: {pokemon: [movimiento1,movimiento2...], ...}, ...}
    """
    
    pokemons, indices_pokemons = pokedex.datos_pokemon("data/pokemons.csv")
    movimientos = pokedex.movimientos_pokemon('data/movimientos.csv')
    equipos = pokedex.cargar_partida("data/partida.csv")

    return pokemons, indices_pokemons, movimientos, equipos

def mostrar_pokedex(vista_pokemon, nombre_actual, informacion, equipos, equipo_actual):
    """
    Actualiza la ventana.
    """
    
    gamelib.draw_rectangle(0,0,1000,700, fill='red')
    gamelib.draw_oval(80, 70, 130, 120, outline='black', fill='#15E8E8')
    gamelib.draw_oval(150, 70, 170, 90, outline='black', fill='red')
    gamelib.draw_oval(180, 70, 200, 90, outline='black', fill='green')
    gamelib.draw_oval(210, 70, 230, 90, outline='black', fill='yellow')
    gamelib.draw_rectangle(80,150,870,550, fill='grey')
    gamelib.draw_rectangle(90,160,860,540, fill='white')
    gamelib.draw_rectangle(700, 560, 730, 590, fill = 'green') 
    gamelib.draw_rectangle(700, 600, 730, 630, fill = 'green') 
    gamelib.draw_rectangle(660, 600, 690, 630, fill = 'green') 
    gamelib.draw_rectangle(740, 600, 770, 630, fill = 'green') 
    gamelib.draw_text('⇧', 715, 575, fill = 'white', size = 30)
    gamelib.draw_text('⇩', 715, 615, fill = 'white', size = 30)
    gamelib.draw_text('⇦', 675, 615, fill = 'white', size = 30)
    gamelib.draw_text('⇨', 755, 615, fill = 'white', size = 30)
    
    if vista_pokemon:
        mostrar_vista_pokemon(nombre_actual, informacion)
        
    else:
        mostrar_vista_equipos(equipos, equipo_actual)

def mostrar_vista_pokemon(nombre_actual, informacion):
    """
    Actualiza la vista pokemon.
    """

    gamelib.draw_oval(150, 560, 180, 590, fill='green', outline = 'green')  
    gamelib.draw_rectangle(165, 560, 235, 590, fill='green', outline = 'green')
    gamelib.draw_oval(220, 560, 250, 590, fill='green', outline = 'green')  
    gamelib.draw_text('Pokemons', 475, 120, fill = 'white', size = 20)
    gamelib.draw_text(nombre_actual, 175, 185, fill = 'black', size = 20)
    gamelib.draw_text(informacion['numero'], 825, 185, fill = 'black', size = 20)
    gamelib.draw_image(informacion['imagen'], 125, 225)
    gamelib.draw_text(f"HP: {informacion['hp']}", 700, 250, fill = 'black', size = 20)
    gamelib.draw_text(f"Ataque: {informacion['atk']}", 700, 300, fill = 'black', size = 20)
    gamelib.draw_text(f"Defensa: {informacion['defe']}", 700, 350, fill = 'black', size = 20)
    gamelib.draw_text(f"Ataque Especial: {informacion['spa']}", 700, 400, fill = 'black', size = 20)
    gamelib.draw_text(f"Defensa Especial: {informacion['spd']}", 700, 450, fill = 'black', size = 20)
    gamelib.draw_text(f"Velocidad: {informacion['spe']}", 700, 500, fill = 'black', size = 20)
    gamelib.draw_text('Buscar Pokemon', 201, 611, fill = 'black', size = 15)
    gamelib.draw_text('ESPACIO', 200, 575, fill = 'black', size = 12)
    gamelib.draw_text('Buscar Pokemon', 201, 611, fill = 'white', size = 15)
    gamelib.draw_text('ESPACIO', 200, 575, fill = 'white', size = 12)

def mostrar_vista_equipos(equipos, equipo_actual):
    """
    Actualiza la vista de equipos.
    """

    gamelib.draw_text("Equipos", 475, 120, fill = 'white', size = 20)
    gamelib.draw_oval(80, 560, 120, 600, fill='#800000')
    gamelib.draw_oval(160, 560, 200, 600, fill = '#008080')
    gamelib.draw_oval(240, 560, 280, 600, fill = 'yellow')
    gamelib.draw_oval(320, 560, 360, 600, fill = 'green')
    gamelib.draw_text('A', 101, 581, fill = 'black', size = 15)
    gamelib.draw_text('B', 181, 581, fill = 'black', size = 15)
    gamelib.draw_text('C', 261, 581, fill = 'black', size = 15)
    gamelib.draw_text('E', 341, 581, fill = 'black', size = 15)
    gamelib.draw_text('A', 100, 580, fill = 'white', size = 15)
    gamelib.draw_text('B', 180, 580, fill = 'white', size = 15)
    gamelib.draw_text('C', 260, 580, fill = 'white', size = 15)
    gamelib.draw_text('E', 340, 580, fill = 'white', size = 15)
    gamelib.draw_text('Agregar', 101, 621, fill = 'black', size = 15)
    gamelib.draw_text('Borrar', 181, 621, fill = 'black', size = 15)
    gamelib.draw_text('Crear', 261, 621, fill = 'black', size = 15)
    gamelib.draw_text('Agregar', 100, 620, fill = 'white', size = 15)
    gamelib.draw_text('Borrar', 180, 620, fill = 'white', size = 15)
    gamelib.draw_text('Crear', 260, 620, fill = 'white', size = 15)
    gamelib.draw_text('Eliminar', 341, 621, fill = 'black', size = 15)
    gamelib.draw_text('Eliminar', 340, 620, fill = 'white', size = 15)

    if len(equipos) == 0:
        gamelib.draw_text("Aún no hay equipos. Pulsa 'C' para crear uno. ", 475, 185, fill = 'black', size = 20)
        
    elif len(equipos) > 0:
        nombre_equipo = list(equipos[equipo_actual].keys())[0]
        
        gamelib.draw_text(f"Equipo {nombre_equipo}", 110, 185, fill = 'black', size = 20, anchor = 'w')

        separador = 50
        numero = 1

        try:
            if len(equipos[equipo_actual][nombre_equipo]) == 0:
                for i in range(MAX_POKEMONS):
                    gamelib.draw_text("<Agrega un Pokemon pulsando la tecla 'A'>", 325, 185 + separador, fill = 'grey', size = 15)
                    separador += 50
        except KeyError:
            pass

        if len(equipos[equipo_actual][nombre_equipo]) > 0:
            for pokemon, movimientos in (equipos[equipo_actual][nombre_equipo].items()):
                gamelib.draw_text(f"{numero}. {pokemon}", 135, 185 + separador, fill = 'black', size = 15, anchor = 'w')
                gamelib.draw_text(", ".join(movimientos), 400, 185 + separador, fill = 'black', size = 15, anchor = 'w')
                separador += 50
                numero += 1
                
            for i in range(MAX_POKEMONS - len(equipos[equipo_actual][nombre_equipo])):
                gamelib.draw_text("<Agrega un Pokemon pulsando la tecla 'A'>", 325, 185 + separador, fill = 'grey', size = 15)
                separador += 50

def pokemon_correcto(indices_pokemons, pokemons, nombre_actual, numero_actual, vista_pokemon):
    """
    Recibe un diccionario de la forma: {pokemon: numero_pokemon}
    Recibe una lista de la forma: [(pokemon1, {informacion1}), (pokemon2, {informacion2}), ...]
    Recibe el nombre actual y el numero actual del pokemon.
    Recibe la vista actual.
    Devuelve el nombre actual, el numero actual y la informacion actual del pokemon que se quiere buscar.

    Se encarga de revisar si lo que ingreso el usuario (numero o nombre) es correcto. Sera correcto si el
    nombre ingresado se encuentra en la lista o si el numero ingresado esta en el rango de la cantidad de los
    pokemons. Si es incorrecto se seguira pidiendo al usuario ingresar un pokemon correcto.
    
    Si el pokemon ingresado es correcto, entonces devuelve el nombre del pokemon, el numero del pokemon y la
    informacion del pokemon para poder mostrarlo por pantalla.
    """

    pokemon_pedido = gamelib.input("Ingrese el Pokemon deseado. Puede buscar por numero y nombre.")

    while pokemon_pedido != None:

        if pokemon_pedido != None and pokemon_pedido.isalpha() and pokedex.esta_pokemon(indices_pokemons, pokemon_pedido):
            nombre_actual = pokemon_pedido
            numero_actual = int(indices_pokemons[nombre_actual])
            numero_actual -= 1
            informacion_actual = pokedex.informacion_nombre(pokemons, indices_pokemons, nombre_actual)
            return nombre_actual, numero_actual, informacion_actual
        
        if pokemon_pedido != None and pokemon_pedido.isdigit() and 1 <= int(pokemon_pedido) <= len(pokemons): 
            numero_actual = int(pokemon_pedido) - 1
            informacion = pokedex.informacion_numero(pokemons, numero_actual)
            nombre_actual, informacion_actual = informacion
            return nombre_actual, numero_actual, informacion_actual

        pokemon_pedido = gamelib.input("Ingrese el Pokemon deseado. Puede buscar por numero y nombre.")

    if vista_pokemon:
        informacion = pokedex.informacion_nombre(pokemons, indices_pokemons, nombre_actual)
        return nombre_actual, numero_actual, informacion

    else:
        pokemon = None
        return pokemon, None, None

def agregar_pokemon(pokemon, equipos, equipo_actual, nombre_equipo, movimientos):
    """
    Recibe un pokemon, la lista de equipos, el indice del equipo actual, el nombre del equipo actual y
    el diccionario de movimientos.
    Devuelve el equipo con el pokemon agregado.
    """
    
    info_equipo = equipos[equipo_actual][nombre_equipo]
    
    if pokemon is None:
        return equipos
    else:
        cantidad_movimientos = pedir_cantidad_movimientos(pokemon, movimientos)
        
        if cantidad_movimientos is None:
            return equipos
        else:
            lista_movimientos = seleccionar_movimientos(equipos, equipo_actual, pokemon, movimientos, cantidad_movimientos)
            
            if lista_movimientos is None:
                return equipos
            else:
                equipos = pokedex.agregar_pokemon(equipos, equipo_actual, nombre_equipo, pokemon)
                info_equipo[pokemon] = lista_movimientos
                return equipos

def pedir_cantidad_movimientos(pokemon, movimientos):
    """
    Recibe el nombre del pokemon que se esta agregando y el diccionario con los movimientos.
    Devuelve la cantidad de movimientos que el usuario desea ponerle a dicho pokemon.
    """

    cantidad_movimientos = 0
    movimientos_totales = len(movimientos[pokemon])
    
    if movimientos_totales >= MAX_MOVIMIENTOS:
        cantidad_maxima = MAX_MOVIMIENTOS
    elif movimientos_totales < MAX_MOVIMIENTOS:
        cantidad_maxima = movimientos_totales
    
    while cantidad_movimientos != None:
        cantidad_movimientos = gamelib.input(f"¿Cuantos movimientos desea agregarle a {pokemon}?")
        
        if cantidad_movimientos is not None:
            if cantidad_movimientos.isdigit() and 0 < int(cantidad_movimientos) <= cantidad_maxima:
                return int(cantidad_movimientos)

def seleccionar_movimientos(equipos, equipo_actual, pokemon, movimientos, cantidad_movimientos):
    """
    Recibe la lista de equipos, el equipo que se esta editando, el pokemon al cual se le esta agregando
    movimientos, el diccionario con los movimientos y la cantidad de movimientos que el usuario ingreso.
    Devuelve una lista con los movimientos que se seleccionaron, y en caso de que no se haya seleccionado
    ninguno, devuelve None.
    """
    
    lista_movimientos = []
    
    for movimiento in movimientos[pokemon]:
        respuesta = ''
        
        while respuesta not in ('S', 's', 'N', 'n', None):
            respuesta =  gamelib.input(f"¿Desea añadir '{movimiento}' a {pokemon}? │ [S/N]")
            
        if respuesta == "S" or respuesta == "s":
            lista_movimientos.append(movimiento)
        if respuesta == "N" or respuesta == "n":
            pass
        if respuesta == None:
            return None
        if len(lista_movimientos) == int(cantidad_movimientos):
            return lista_movimientos

def adelantar_equipo(equipos, equipo_actual):
    """
    Recibe la lista de equipos y la posicion del equipo actual.
    Cambia la posicion del equipo actual al siguiente en la lista de equipos.
    """
    
    if equipo_actual == len(equipos) - 1:
        return equipo_actual
    
    equipo_actual += 1
        
    return equipo_actual

def retroceder_equipo(equipos, equipo_actual):
    """
    Recibe la lista de equipos y la posicion del equipo actual.
    Cambia la posicion del equipo actual al anterior en la lista de equipos.
    """
    
    if equipo_actual == 0:
        return equipo_actual
    
    equipo_actual -= 1
        
    return equipo_actual

def pedir_nombre_equipo(equipos):
    """
    Recibe la lista de equipos.
    Verifica que el nombre que ingresó el usuario no esté en la lista de equipos.
    Devuelve el nombre del equipo que ingresó el usuario.
    """
    
    lista_equipos = []
    for equipo in equipos:
        lista_equipos.append(list(equipo.keys())[0])

    nombre_equipo = ''
    while nombre_equipo == '' or nombre_equipo in lista_equipos:
        nombre_equipo = gamelib.input("¿Qué nombre desea ponerle a su equipo?")

    return nombre_equipo

def crear_equipo(equipos):
    """
    Recibe la lista de equipos y le pide al usuario que ingrese un nombre para
    el equipo a crear.
    Agrega el equipo con el nombre que eligió el usuario a la lista de equipos.
    """
    
    nombre_equipo = pedir_nombre_equipo(equipos)
    
    if nombre_equipo is None:
        return equipos

    equipos.append({nombre_equipo:{}})
    return equipos

def pedir_pokemon_a_borrar(equipos, equipo_actual, nombre_equipo):
    """
    Recibe la lista de equipos, el índice del equipo actual y el nombre del equipo actual.
    Le pide al usuario que ingrese el nombre del pokemon que desea borrar y verifica que
    el mismo esté en el equipo actual.
    Devuelve el nombre del pokemon que se desea borrar.
    """
    
    info_equipo = equipos[equipo_actual][nombre_equipo]
    pokemon_a_borrar = ''
    
    while pokemon_a_borrar not in info_equipo:
        pokemon_a_borrar = gamelib.input("Ingrese el nombre del Pokemon que desea borrar: ")
        if pokemon_a_borrar is not None:
            pokemon_a_borrar = pokemon_a_borrar.lower().title()
        else:
            return pokemon_a_borrar
    
    return pokemon_a_borrar

def borrar_pokemon(equipos, equipo_actual, nombre_equipo, pokemon):
    """
    Recibe la lista de equipos, el indice del equipo actual, el nombre del equipo
    y el nombre del pokemon que se desea borrar.
    Devuelve el equipo sin el pokemon.
    """
    
    if pokemon is None:
        return equipos
    
    equipos = pokedex.borrar_pokemon(equipos, equipo_actual, nombre_equipo, pokemon)
    return equipos

def eliminar_equipo(equipos, equipo_actual):
    """
    Recibe la lista de equipos y el índice del equipo actual.
    Pregunta al usuario si desea eliminar el equipo en el cual esta parado.
    Elimina el equipo o no en función de lo que responda el usuario.
    """
    
    respuesta = ''
    while respuesta not in ['S', 's', 'N', 'n', None]:
        respuesta = gamelib.input("¿Esta seguro de que desea eliminar este equipo? │ [S/N]")

    if respuesta in ['N', 'n', None]:
        return equipos, equipo_actual

    if respuesta in ['S', 's']:
        equipo_a_eliminar = equipo_actual
        
        if equipo_actual > 0:
            equipo_actual = retroceder_equipo(equipos, equipo_actual)

        equipos = pokedex.eliminar_equipo(equipos, equipo_a_eliminar)
        return equipos, equipo_actual

def main():

    gamelib.title("Pokedex")
    pokemons, indices_pokemons, movimientos, equipos = pokedex_crear()

    vista_pokemon = True
    numero_actual = 0
    equipo_actual = 0
    
    informacion = pokedex.informacion_numero(pokemons, numero_actual)
    nombre_actual, informacion_actual = informacion

    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    while gamelib.is_alive():
        gamelib.draw_begin()
        mostrar_pokedex(vista_pokemon, nombre_actual, informacion_actual, equipos, equipo_actual)
        gamelib.draw_end()
  
        ev = gamelib.wait()

        if not ev:
            pokedex.guardar_partida(equipos)
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            pokedex.guardar_partida(equipos)
            break

        if ev.type == gamelib.EventType.KeyPress:

            if ev.key in ["Up", "Down"]:
                vista_pokemon = not vista_pokemon

            if vista_pokemon:
                
                if ev.key in ["Right", "Left"]:
                    
                    if ev.key == "Right":       
                        if numero_actual == (len(pokemons) - 1):
                            numero_actual = numero_actual
                        else:
                            numero_actual += 1
                        
                    if ev.key == "Left":
                        if numero_actual == 0:
                            numero_actual = numero_actual  
                        else:
                            numero_actual -= 1
                        
                    informacion = pokedex.informacion_numero(pokemons, numero_actual)
                    nombre_actual, informacion_actual = informacion
                
                if ev.key == "space":
                    nombre_actual, numero_actual, informacion_actual = pokemon_correcto(indices_pokemons, pokemons, nombre_actual, numero_actual, vista_pokemon)
               
            else:
                
                if len(equipos) > 0:
                    nombre_equipo = list(equipos[equipo_actual].keys())[0]

                if ev.key in ["C", "c"]:                    
                    equipos = crear_equipo(equipos)
                    equipo_actual = len(equipos) - 1                    
                
                if ev.key == "Left" and len(equipos) > 0:
                    equipo_actual = retroceder_equipo(equipos, equipo_actual)

                if ev.key == "Right" and len(equipos) > 0:
                    equipo_actual = adelantar_equipo(equipos, equipo_actual)
                    
                if ev.key in ["A", "a"] and  0 < len(equipos) and len(equipos[equipo_actual][nombre_equipo]) < MAX_POKEMONS:
                    pokemon, __, __ = pokemon_correcto(indices_pokemons, pokemons, nombre_actual, numero_actual, vista_pokemon)
                    equipos = agregar_pokemon(pokemon, equipos, equipo_actual, nombre_equipo, movimientos)

                if ev.key in ["B", "b"] and len(equipos[equipo_actual][nombre_equipo]) > 0:
                    pokemon_a_borrar = pedir_pokemon_a_borrar(equipos, equipo_actual, nombre_equipo)
                    equipos = borrar_pokemon(equipos, equipo_actual, nombre_equipo, pokemon_a_borrar) 
                
                if ev.key in ["E", "e"] and len(equipos) > 0:
                    equipos, equipo_actual = eliminar_equipo(equipos, equipo_actual)
                        
gamelib.init(main)
