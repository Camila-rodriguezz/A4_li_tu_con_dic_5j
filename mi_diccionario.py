print("Ejemplos diccionarios")
productos = {
  "tipo": "Pan",
  "marca": "Bimbo",
  "precio": 40
}
print(productos)
print("Lista de los elementos del diccionario productos con for")
for rodriguez, ruiz in productos.items():
    print(rodriguez,ruiz)