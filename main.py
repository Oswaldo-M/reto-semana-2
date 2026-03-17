import sys

#funcion para procesar cada linea
def procesar_linea(linea):
    partes = linea.strip().split(',')
    
    #Separar campos
    if len(partes)!=3:
        return None
    ciudad = partes[0]
    temp_str = partes[1]
    unidad= partes[2].strip().upper()

    #Validar unidad
    if unidad not in ['C','F']:
        return None
    
    #Convertir temperatura
    try:
        temperatura = float(temp_str)
    except ValueError:
        return None
    
    #Convierte Fahrenheit a celsius 
    if unidad == "F":
        celsius = (temperatura-32)*5/9
    else:
        celsius = temperatura

    #Clasifica la temperatura
    if celsius <0:
        clasificacion = "Congelante"
    elif celsius <= 15:
        clasificacion = "Frio"
    elif celsius <= 25:
        clasificacion = "Templado"
    elif celsius <= 35:
        clasificacion = "Calido"
    else:
        clasificacion= "Extremo"
    
    return(ciudad,celsius,clasificacion)


def main():
    #Leer y descartar encabezado de entrada 
    primera_linea = True
    #Imprimir encabezado de salida
    print("ciudad,temperatura_celsius,clasificacion")

    for linea in sys.stdin:
        #Saltar encabezado
        if primera_linea == False:
            continue
        #Saltando las lineas vacias
        if not linea:
            continue
        #Evaluando la linea con la funcion procesar_linea
        resultado = procesar_linea(linea)
        if resultado:
            ciudad,celsius,clasificacion = resultado
            print(f'{ciudad},{celsius: .1f},{clasificacion}')
    
if __name__=="__main__":
    main()
    