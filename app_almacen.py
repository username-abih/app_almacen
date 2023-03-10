def ingresar_producto():

    sku = (input("ingresa el identificador de prod (sku): "))
    nombre_producto = input("ingresa el nombre del producto: ")
    unidades = int(input("ingresa la cantidad de unidades en existencia del producto: "))
    precio = float(input("ingresa el precio del producto: "))

    return(sku, nombre_producto, unidades, precio)


#variables y codigos
diccionario_productos = {}
loop = 0
actividad = 0

#variables para diccionario
sku = ""
nombre_producto = ""
unidades = 0
precio = 0.0

#variables para compra prod.
n_ingreso_prod = 0
n_productos_comprar = 0
lock_errores_unidades = 0
total_compra = 0.0
codigo_compra = 0
unidades_compra = 0

#loop
while loop == 0:
    print("""que deseas hacer?
    1 = ingresar producto
    2 = mostrar productos disponibles
    3 = comprar producto
    4 = salir""")

    actividad = int(input("ingresa la opcion numerica a elegir: "))

#ingreso de productos
    if actividad == 1:
        n_ingreso_prod = int(input("cuantos productos vas a agregar: "))
        for i in range(n_ingreso_prod):
            sku, nombre_producto, unidades, precio = ingresar_producto()
            diccionario_productos[sku] = {"nombre producto" : nombre_producto, "unidades" : unidades, "precio" : precio}

#mostrar productos disponibles
    elif actividad == 2:
        for codigo, datos in diccionario_productos.items():
            print("sku:", codigo, "producto:", datos["nombre producto"], "precio:", datos["precio"], "unidades existentes:", datos["unidades"])

#compra de productos
    elif actividad == 3:
        print("esta es la lista de productos en existencia actualmente:")
        for codigo, datos in diccionario_productos.items():
            print("sku:", codigo, "producto:", datos["nombre producto"])

        #ingreso de datos y cantidades de productos a comprar
        n_productos_comprar = int(input("cuantos productos compraras? "))
        for x in range(n_productos_comprar):
            #corroboramos que tengamos unidades suficientes
            while lock_errores_unidades == 0:
                codigo_compra = input("sku de producto: ")
                unidades_compra = int(input("unidades a comprar: "))
                if diccionario_productos[codigo_compra]["unidades"] >= unidades_compra:
                    lock_errores_unidades = 1
                else:
                    print("no hay unidades suficientes para su compra, intentelo de nuevo")
            lock_errores_unidades = 0

            #modificamos diccionario
            diccionario_productos[codigo_compra]["unidades"] -= unidades_compra
            # explicamos ticket producto por producto
            print("por ",unidades_compra , " unidades de ",diccionario_productos[codigo_compra]["nombre producto"],
                " el total a pagar es: ",float(unidades_compra * diccionario_productos[codigo_compra]["precio"]), "$ pesos mexicanos")

            #total de ventas
            total_compra += unidades_compra * diccionario_productos[codigo_compra]["precio"]
        print("el total a pagar por todos sus productos es: ", total_compra)

#exit
    elif actividad == 4:
        loop = 1
        print("gracias por venir, vuelva pronto")

#error
    else:
        print("no seleccionaste una actividad correctamente, vuelve a intentarlo")