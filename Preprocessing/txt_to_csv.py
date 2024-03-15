import sys
import re
import csv

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

# Expresión regular para extraer la información deseada
pattern = r'\[(.*?)\]\s(.*?):\s(.*)'

# Abre el archivo de entrada y salida
with open(INPUT_FILE, 'r', encoding='UTF-8', errors='ignore') as infile, open(OUTPUT_FILE, 'w', encoding='UTF-8', newline='') as outfile:
    # Crea un objeto CSV para escribir en el archivo de salida
    csv_writer = csv.writer(outfile)

    # Escribe la primera fila del archivo CSV con los encabezados
    csv_writer.writerow(['Fecha', 'Usuario', 'Mensaje'])

    # Procesa cada línea del archivo de entrada
    for line in infile:
        # Busca el patrón en cada línea
        match = re.match(pattern, line)
        if match:
            # Extrae las partes coincidentes
            fecha = match.group(1)
            usuario = match.group(2)
            mensaje = match.group(3)

            # Escribe la información en el archivo CSV
            csv_writer.writerow([fecha, usuario, mensaje])
