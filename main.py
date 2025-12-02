
## varialbe booleana que maneja el clclo del programa
activo = True

## Lista que almacena todos los suplementos
catalogo = [("0025","Whey","Prote","Rica",250.00),("0028","Whey","Testo","Mala",1000.00),("0012","Inlabs","Prote","Mee",500.00)]


while(activo):
    print("""

    1. Agregar una nueva suplemento
    2. Dar de baja un suplemento del catálogo
    3. Actualizar los datos de un suplemento
    4. Mostrar el listado de suplementos en el catálogo
    5. Terminar operación

    """)

    opcion = int(input("Teclee su opcion: ")) 
    


    if opcion == 1:
        volver_a_registrar = True
        
        while(volver_a_registrar):

            nSerie = ""
            invalido = True
        
            while(invalido):
                nSerie = input("Ingrese el N° Serie del suplemento:")
                encontrado = False
                for s in catalogo:
                    if s[0] == nSerie:
                        encontrado = True
                if encontrado == False:
                    invalido = False
                    break

            marca = input("Ingrese la marca del suplemento:")

            nombre = input("Ingrese el Nombre del suplemento:")

            descripcion = input("Ingrese la descripcion del suplemento:")
        
            precio = float(input("Ingrese el precio del suplemento: "))

            suplemento = (nSerie, marca,nombre, descripcion, precio)

            print("\n\n")
            print("------------- Datos adicionales -------------")
            print(f"N° Serie: ", nSerie)
            print(f"Marca: ", marca)
            print(f"Nombre: ", nombre)
            print(f"Descripción: ", descripcion)
            print(f"Precio: $", precio)
            print("")


        
            while(True):
                confirmar = input("¿Desea confirmar registro? (S/N)")
                catalogo.append(suplemento)
                if confirmar == "S" or confirmar == "s":

                    print("-----------------------------------------------------------------------------")
                    print("N°Serie          Marca           Nombre          Descripcion         Precio") 
                    print("-----------------------------------------------------------------------------")
                
                    for objeto in catalogo:
                        print(f"{objeto[0]}           {objeto[1]}             {objeto[2]}            {objeto[3]}        ${objeto[4]}")

                    print("-----------------------------------------------------------------------------")
                    print("Total de suplementos: ", len(catalogo))
                    break
                if confirmar == "n" or confirmar == "N":
                    print("\nRegistro cancelado")
                    break


        
            while(True):
                confirmar = input("¿Desea continuar con otro autobús (s/n)?")
                if confirmar == "S" or confirmar == "s":
                    volver_a_registrar = True
                    break
                if confirmar == "n" or confirmar == "N":
                    print("\nRegistro cancelado")
                    volver_a_registrar = False
                    break




    if opcion == 2:
        volver_a_eliminar = True
        
        while(volver_a_eliminar):
            print("-----------------------------------------------------------------------------")
            print("N°Serie          Marca           Nombre          Descripcion         Precio") 
            print("-----------------------------------------------------------------------------")
                
            for s in catalogo:
                print(f"{s[0]}          {s[1]}           {s[2]}          {s[3]}        ${s[4]}")

            print("-----------------------------------------------------------------------------")
            print("Total de suplementos: ", len(catalogo))
            
        

            numeroSuplemento = input("Ingrese el número de serie del suplemento: ")
            encontrado = ()
            existe = False
            for s in catalogo:
                if s[0] == numeroSuplemento:
                    encontrado = s
                    existe = True

            if existe == False:
                print("No se enonctró ningun suplemento con ese número de serie")
                break

            print("---------------------- Informacion del suplemento ---------------------------")
            print("N°Serie          Marca           Nombre          Descripcion         Precio") 
            print(f"{encontrado[0]}          {encontrado[1]}           {encontrado[2]}          {encontrado[3]}        ${encontrado[4]}")
            print("")
            print("")

            while(True):
                confirmar = input("¿Realmente desea eliminar el suplemento y todos sus datos? (S/N)")
                print("")
                if confirmar == "s" or confirmar == "S":
                    catalogo.remove(encontrado)
                    break
                elif confirmar == "n" or confirmar == "N":
                    break
            
            while(True):
                confirmar = input("¿Continuar con otro suplemento (s/n)?")
                print("")
                if confirmar == "s" or confirmar == "S":
                    volver_a_eliminar = True 
                    break
                elif confirmar == "n" or confirmar == "N":
                    volver_a_eliminar = False
                    break

            


    if opcion == 3:
        
        print("-----------------------------------------------------------------------------")
        print("N°Serie          Marca           Nombre          Descripcion         Precio") 
        print("-----------------------------------------------------------------------------")
        for s in catalogo:
            print(f"{s[0]}          {s[1]}           {s[2]}          {s[3]}        ${s[4]}")
        print("-----------------------------------------------------------------------------")
        print("Total de suplementos: ", len(catalogo))
        print("")

        volver_a_editar = True
        while(volver_a_editar):

            numeroSuplemento = input("Ingrese el número de serie del suplemento: ")
            encontrado = ()
            existe = False
            indice = 0
            for s in catalogo:
                if s[0] == numeroSuplemento:
                    encontrado = s
                    existe = True
                    break
                indice+= 1
            if existe == False:
                print("No se enonctró ningun suplemento con ese número de serie")
                break
                
            
            print("---------------------- Informacion del suplemento ---------------------------")
            print("N°Serie          Marca           Nombre          Descripcion         Precio") 
            print(f"{encontrado[0]}          {encontrado[1]}           {encontrado[2]}          {encontrado[3]}        ${encontrado[4]}")
            print("")
            print("")

            print("---------------------- Actualizacion de datos ---------------------------")

            newMarca =  input(f"    Marca: {encontrado[1]}     ---> ")
            newNombre =  input(f"    Nombre: {encontrado[2]}     ---> ")
            newDescripcion =  input(f"    Descripcion: {encontrado[3]}     ---> ")
            newPrecio =  input(f"    Precio: {encontrado[4]}     ---> ")

            print("")

            while(True):
                confirmar = input("¿Desea confirmar registro? (S/N)")
                print("")

                if confirmar == "S" or confirmar == "s":
                    sustituto = list(encontrado)
                    
                    if newMarca != "":
                        sustituto[1] = newMarca
                    if newNombre != "":
                        sustituto[2] = newNombre
                    if newDescripcion != "":
                        sustituto[3] = newDescripcion
                    if newPrecio != "":
                        sustituto[4] = newPrecio
                    
                    catalogo.remove(encontrado)
                    tuplaSustiuto = tuple(sustituto)
                    catalogo.insert(indice, tuplaSustiuto)

                    print("-----------------------------------------------------------------------------")
                    print("N°Serie          Marca           Nombre          Descripcion         Precio") 
                    print("-----------------------------------------------------------------------------")
                
                    for s in catalogo:
                        print(f"{s[0]}          {s[1]}           {s[2]}          {s[3]}        ${s[4]}")
                    print("-----------------------------------------------------------------------------")
                    print("Total de suplementos: ", len(catalogo))
                    print("")
                    break
                if confirmar == "n" or confirmar == "N":
                    print("\nRegistro cancelado")
                    break

            while(True):
                confirmar = input("¿Continuar con otro suplemento (s/n)?")
                print("")
                if confirmar == "s" or confirmar == "S":
                    volver_a_editar = True 
                    break
                elif confirmar == "n" or confirmar == "N":
                    volver_a_editar = False
                    break





    if opcion == 4:
        print("-----------------------------------------------------------------------------")
        print("N°Serie          Marca           Nombre          Descripcion         Precio") 
        print("-----------------------------------------------------------------------------")
                
        for s in catalogo:
            print(f"{s[0]}          {s[1]}           {s[2]}          {s[3]}        ${s[4]}")
        print("-----------------------------------------------------------------------------")
        print("Total de suplementos: ", len(catalogo))




    if opcion == 5:
        activo = False        
        break
