import sys

print("ciudad,temperatura_celsius,clasificacion")

def procesar_linea(linea):
    partes = linea.strip().split(',')
    
    if len(partes)!=3:
        return None
    
    ciudad = partes[0]
    temp_str = partes[1]
    unidad= partes[2].strip().upper()

    if unidad not in ['C','F']:
        return None
    
    try:
        temperatura = float(temp_str)
    except ValueError:
        return None
    
    if unidad == "F":
        celsius = (temperatura-32)*5/9
    else:
        celsius = temperatura

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




for linea in sys.stdin:
    resultado = procesar_linea(linea)
    if resultado:
        ciudad, celsius, clasificacion = resultado
        print(f'{ciudad}, {celsius: .1f},{clasificacion}')
    else:
        print(f'[IGNORADA]{linea}')    

    