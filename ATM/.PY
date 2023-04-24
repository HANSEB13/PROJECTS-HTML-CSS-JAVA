""" 
Crearemos un algoritmo que responda esa pregunta.
la cantidad total disponible es de $1.650, repartidos en billetes de:
4 billetes de $100 
9 billetes de $50  
20 billetes de $20  
30 billetes de $10  
100 billetes de $1  
"""

# billetes disponibles (billete : cantidad)
disponible = 
{
    100: 4,
    50: 9,
    20: 20,
    10: 30,
    1: 100,
}

# consultar el total disponible en el cajero
def total_disponible():
    total = 0
    for billete, cantidad in disponible.items():
         total += billete * cantidad
    return total
        
# Obtener el monto a retirar
def retirar(monto):
    if monto > total_disponible():
        print("Error, no hay suficiente efectivo")
    
    saldo_retirar = monto
    while saldo_retirar > 0:
        for denominacion, valor in disponible.items():
            cantidad = get_denominacion(denominacion, saldo_retirar)
            if cantidad != 0:
                print(f'{cantidad} billetes de:  ${denominacion}')

            saldo_retirar -= cantidad * denominacion
        

# obtener la denominación (tipo billete) de cada billete a entregar (¿cuantos billetes de?)
def get_denominacion(denominacion, saldo_retirar):
    cantidad = saldo_retirar//denominacion
    if (cantidad > disponible[denominacion]):
        cantidad = disponible[denominacion]
    
    disponible[denominacion] -= cantidad
    return cantidad


total_usuario = int(input('Escriba el valor entero a retirar: '))
retirar(total_usuario)
print(disponible)
