# 1. Creamos los productos disponibles (frutitas).
productos = [
    {"id": 1, "nombre": "Manzana Roja", "precio": 2.50, "stock": 20},
    {"id": 2, "nombre": "Banano", "precio": 1.80, "stock": 30},
    {"id": 3, "nombre": "Naranja Jugosa", "precio": 2.20, "stock": 25},
    {"id": 4, "nombre": "Fresa Fresca", "precio": 3.00, "stock": 15},
    {"id": 5, "nombre": "Mango Dulce", "precio": 3.50, "stock": 10}
]

# 2. Función para mostrar el catálogo de frutas
def mostrar_catalogo():
    print("\n Frutitas Disponibles:")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - S/{p['precio']} (Stock: {p['stock']})")

# 3. Función principal
def main(): 
    print("""
  *******************************
  *   TIENDA DE FRUTITAS   *
  *******************************
  """)

    carrito = []
    total = 0

    while True:
        mostrar_catalogo()
        opcion = input("\nElige una fruta (número) o 'p' para pagar: ")

        if opcion.lower() == 'p':
            break

        try:
            id_producto = int(opcion)
            producto = next((p for p in productos if p["id"] == id_producto), None)

            if producto:
                if producto["stock"] > 0:
                    carrito.append(producto)
                    producto["stock"] -= 1
                    total += producto["precio"]
                    print(f" Añadido: {producto['nombre']}")
                else:
                    print(" ¡Fruta agotada!")
            else:
                print(" Fruta no válida")
        except ValueError:
            print(" Ingresa un número válido o 'p' para pagar")

    # Resumen de la compra
    print("\n----- TU COMPRA -----")
    for p in carrito:
        print(f"- {p['nombre']}: S/{p['precio']}")
    print(f"TOTAL: S/{total:.2f}")
    print("\n ¡Gracias por comprar frutitas! ")

if __name__ == "__main__":
    main()
