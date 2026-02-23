from json import load, dump
archivo_datos = "invemtario.json"

def cargar_datos():
    try:
        with open(archivo_datos, "r") as archivo:
            return load(archivo)
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
        return []
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

def guardar_datos(coleccion):
    try:
        with open(archivo_datos, "w") as archivo:
            dump(coleccion, archivo, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def separador():  
    print("==========================================")
   
def mostrar_coleccion(coleccion):
    if not coleccion:
        print("La colección está vacía.")
    else:
        for i, item in enumerate(coleccion, start=1):
            print(f"{i}. {item['tipo']}: {item['titulo']} - {item['autor']} - {item['genero']} - {item['valoracion']}")

while True:
    try:
        separador()
        print("        Administrador de colecciones    ")
        separador()
        print("1. Añadir elemento a la colección")
        print("2. ver todos los elementos")
        print("3. Buscar elementos")
        print("4. Editar elementos")
        print("5. Eliminar elementos")
        print("6. Ver elementos por categoria")
        print("7. Salir")
        separador()

        op = int(input("Ingrese una opción: "))
        separador()

        if op == 1:
            while True:
                try:
                    separador()
                    print("    añadir un nuevo elemento")
                    separador()
                    print("1.libro")
                    print("2.película")
                    print("3.música")
                    print("4.regresar al menu principal")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op in [1, 2, 3]:
                        tipo = "Libro" if sub_op == 1 else "Película" if sub_op == 2 else "Música"
                        titulo = input("Ingrese el título: ")
                        autor = input("Ingrese el autor/director/artista: ")
                        genero = input("Ingrese el género: ")
                        valoracion = input("Ingrese la valoración: ")
                        coleccion = cargar_datos()
                        coleccion.append({
                            "tipo": tipo,
                            "titulo": titulo,
                            "autor": autor,
                            "genero": genero,
                            "valoracion": valoracion
                        })
                        guardar_datos(coleccion)  
                        print(f"{tipo} añadido exitosamente.")
                    elif sub_op == 4:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 2:
            while True:
                try:
                    separador()
                    print("    Ver todos los elementos   ")
                    separador()
                    print("1. ver todos los libros")
                    print("2. ver todas las peliculas")
                    print("3. ver toda la musica")
                    print("4. regresar al munu principal")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        coleccion = cargar_datos()
                        separador()
                        libros = [item for item in coleccion if item['tipo'] == "Libro"]
                        
                        
                        mostrar_coleccion(libros)
                        separador()
                    elif sub_op == 2:
                        coleccion = cargar_datos()
                        separador()
                        peliculas = [item for item in coleccion if item['tipo'] == "Película"]
                        
                        
                        mostrar_coleccion(peliculas)
                    elif sub_op == 3:
                        coleccion = cargar_datos()
                        musica = [item for item in coleccion if item['tipo'] == "Música"]
                
                        mostrar_coleccion(musica)
                    elif sub_op == 4:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    
        elif op == 3:
            while True:
                try:
                    separador()
                    print("")
                    separador()
                    print("1. buscar por titulo")
                    print("2. buscar por autor/director/artista")
                    print("3. buscar por genero")
                    print("4.regresar al menu")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        criterio = input("Ingrese el título a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['titulo'].lower()]
                        mostrar_coleccion(resultados)
                    elif sub_op == 2:
                        criterio = input("Ingrese el autor a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['autor'].lower() ]
                        mostrar_coleccion(resultados)
                    elif sub_op == 3:
                        criterio = input("Ingrese el genero a buscar: ").lower()
                        coleccion = cargar_datos()
                        resultados = [item for item in coleccion if criterio in item['genero'].lower()]
                        mostrar_coleccion(resultados)
                    elif sub_op ==4:    
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        elif op == 4: 
            while True:
                try:
                    separador()
                    print("     editar un elemento    ")
                    separador()
                    coleccion = cargar_datos()
                    mostrar_coleccion(coleccion)
                    separador()
                    print("1. editar titulo")
                    print("2. editar autor/director/artista")
                    print("3. editar genero")
                    print("4. editar valoracion")
                    print("5. regresar al menu principal")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        if not coleccion:
                            print("La colección está vacía.")
                        else:
                            indice = int(input("Ingrese el número del elemento a editar: ")) - 1
                            if 0 <= indice < len(coleccion):
                                item = coleccion[indice]
                                print(f"Editando: {item['titulo']} (deja en blanco para no cambiar)")
                                titulo = input(f"Nuevo título [{item['titulo']}]: ")
                                autor = input(f"Nuevo autor [{item['autor']}]: ")
                                genero = input(f"Nuevo género [{item['genero']}]: ")
                                valoracion = input(f"Nueva valoración [{item['valoracion']}]: ")
                                if titulo: item['titulo'] = titulo
                                if autor: item['autor'] = autor
                                if genero: item['genero'] = genero
                                if valoracion: item['valoracion'] = valoracion
                                guardar_datos(coleccion)
                                print("Elemento editado exitosamente.")
                            else:
                                print("Número inválido.")
                    elif sub_op == 2:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
         
        elif op == 5:  
            while True:
                try:
                    separador()
                    print("*** ELIMINAR ELEMENTO ***")
                    separador()
                    coleccion = cargar_datos()
                    mostrar_coleccion(coleccion)
                    separador()
                    print("1. Eliminar un elemento")
                    print("2. Volver")
                    separador()
                    sub_op = int(input("Elija una opción: "))
                    if sub_op == 1:
                        if not coleccion:
                            print("La colección está vacía.")
                        else:
                            indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
                            if 0 <= indice < len(coleccion):
                                eliminado = coleccion.pop(indice)
                                guardar_datos(coleccion)
                                print(f"'{eliminado['titulo']}' eliminado exitosamente.")
                            else:
                                print("Número inválido.")
                    elif sub_op == 2:
                        print("Regresando...")
                        break
                    else:
                        print("Opción inválida")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    
        elif op == 6:
            while True:
                try:
                    
                    separador()
                    print("        ver elementos por categoria      ")
                    print("¿que categoria deseas ver?")
                    print("1. ver libros")
                    print("2. ver peliculas")
                    print("3. ver musicas")
                    print("4. regresar al menu principal")
                    separador()
                    sub_op = int(input("ingrese una opcion (1-4)"))
                    if sub_op == 1:
                        coleccion = cargar_datos()
                        libros = [item for item in coleccion if 'libro' in item.get('genero', ''). lower()]
                        separador()
                        print("1. ver por genero")
                        print("2. ver por autor")
                        print("3. regresar")
                        separador()
                        opc = int(input("ingrese una opcion(1-2)"))
                        
                        if opc ==1:
                            criterio = input("ingrese el genero a buscar: ").lower()
                            resultados = [ libro for libro in libros if criterio in libro['genero'].lower()]
                            if resultados:
                                print(f"libros de  '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print(" no se encuentran libros de este genero.")
                        elif opc ==2:
                            criterio = input("ingrese el nombre del autor a buscar").lower()
                            resulrados = [libro for libro in libros if criterio in libro['autor'].lower]
                            separador()
                            if resultados:
                                print("libros de '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print("no se encontraron libros con este autor")
                        elif opc == 3:
                            print("regresando...")
                            break
                            
                        else:
                            print("opcion invalida")
                              
                    elif sub_op == 2:
                        coleccion = cargar_datos()
                        peliculas = [item for item in coleccion if 'pelicula' in item.get('genero', '').lower()]
                        separador()
                        print("1. ver por genero")
                        print("2. ver por autor")
                        print("3. volver")
                        separador()
                        opc = int(input("ingrese una opcion(1-2)"))
                        
                        if opc ==1:
                            criterio = input("ingrese el genero a buscar: ").lower()
                            resultados = [ libro for libro in peliculas if criterio in peliculas['genero'].lower()]
                            if resultados:
                                print(f"peliculas de  '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print(" no se encuentran peliculas de este genero.")
                        elif opc ==2:
                            criterio = input("ingrese el nombre del autor a buscar").lower()
                            resulrados = [pelicula for pelicula in peliculas if criterio in pelicula['autor'].lower]
                            separador()
                            if resultados:
                                print("peliculas de '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print("no se encontraron peliculas con este autor")
                        elif opc == 3:
                            print("regresando...")
                            break
                        else:
                            print("opcion invalida")
                    elif sub_op == 3:
                        coleccion = cargar_datos()
                        musica = [item for item in coleccion if 'musica' in item.get('genero', '').lower()]
                        separador()
                        print("1. ver por genero")
                        print("2. ver por autor")
                        print("3: volver")
                        separador()
                        opc = int(input("ingrese una opcion(1-2)"))
                        
                        if opc ==1:
                            criterio = input("ingrese el genero a buscar: ").lower()
                            resultados = [ musica for musica in musica if criterio in musica['genero'].lower()]
                            if resultados:
                                print(f"musicas de  '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print(" no se encuentran musicas de este genero.")
                        elif opc ==2:
                            criterio = input("ingrese el nombre del autor a buscar").lower()
                            resultados = [musica for musica in musica if criterio in musica['autor'].lower]
                            separador()
                            if resultados:
                                print("musicas de '{criterio}':")
                                mostrar_coleccion(resultados)
                            else:
                                print("no se encontraron musicas con este autor")
                        elif opc == 3:
                            print("regresando...")
                            break
                        else:
                            print("opcion invalida")
                    elif sub_op == 4:
                        print("regresando")
                    else:
                        print("opcion invalida.")
                except ValueError:
                    print("por favor, ingrese un numero valido.")        
                
        elif op == 7:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")
    except ValueError:
        print("Por favor, ingrese un número válido.")
