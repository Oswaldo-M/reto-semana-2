# Reto Semana 2 — Clasificador de Temperaturas

Programa en **Python** que procesa un archivo CSV con temperaturas de distintas ciudades del mundo, convierte las temperaturas a **Celsius** y las clasifica según su valor.

El programa:

* Lee datos desde **stdin**
* Escribe resultados en **stdout**
* Ignora automáticamente líneas inválidas


---

# Formato de Entrada

El programa recibe un **archivo CSV** con el siguiente formato:

```
ciudad,temperatura,unidad
```

Columnas:

| Columna     | Descripción         | Ejemplo |
| ----------- | ------------------- | ------- |
| ciudad      | Nombre de la ciudad | CDMX    |
| temperatura | Valor numérico      | 22      |
| unidad      | C o F               | C       |

Ejemplo de entrada:

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
Cancun,30,C
Chicago,14,F
Phoenix,104,F
Error,abc,C
Lima,25,C
Bangkok,36,C
```

---

# Procesamiento

## Conversión de Fahrenheit a Celsius

Si la temperatura está en Fahrenheit se usa la fórmula:

```
C = (F - 32) * 5 / 9
```

Ejemplo:

| Fahrenheit | Celsius |
| ---------- | ------- |
| 50°F       | 10°C    |
| 95°F       | 35°C    |
| 104°F      | 40°C    |

---

## Clasificación de temperatura

Las temperaturas en Celsius se clasifican de la siguiente forma:

| Temperatura (°C) | Clasificación |
| ---------------- | ------------- |
| < 0              | Congelante    |
| 0 – 15           | Frio          |
| 16 – 25          | Templado      |
| 26 – 35          | Calido        |
| > 35             | Extremo       |

---

## Manejo de líneas inválidas

El programa **ignora automáticamente** líneas que tengan:

* Temperatura no numérica
* Unidad diferente de `C` o `F`
* Menos de 3 columnas
* Datos mal formateados

---

# Formato de Salida

El programa genera un **CSV** con el siguiente formato:

```
ciudad,temperatura_celsius,clasificacion
```

Ejemplo de salida:

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
Cancun,30.0,Calido
Chicago,-10.0,Congelante
Phoenix,40.0,Extremo
Lima,25.0,Templado
Bangkok,36.0,Extremo
```

La temperatura se muestra con **1 decimal**.

---

# Cómo ejecutar el programa

1. Clona el repositorio

```
git clone https://github.com/Oswaldo-M/reto-semana-2.git
cd reto-semana-2
```

2. Ejecuta el programa pasando el archivo de entrada y llevalo a uno de salida

### Linux / Mac

```
python main.py < entrada.csv > salida.csv
```

### Windows (PowerShell)

```
Get-Content entrada.csv | python main.py > salida.csv
```

### Windows (CMD)

```
type entrada.csv | python main.py > salida.csv
```

---

# Ejemplo completo

Archivo `entrada.txt`:

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
Cancun,30,C
Chicago,14,F
Phoenix,104,F
Error,abc,C
Lima,25,C
Bangkok,36,C
```

Ejecución:

```
python main.py < entrada.csv > salida.csv
```

Salida:

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
Cancun,30.0,Calido
Chicago,-10.0,Congelante
Phoenix,40.0,Extremo
Lima,25.0,Templado
Bangkok,36.0,Extremo
```

---


# Autor

Oswaldo Jafet Morales Flores
