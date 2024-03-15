import csv
import re

def filtrar_mensaje(mensaje):
    # Filtrar mensajes que contengan 'added', 'message was deleted', 'left', emojis y enlaces
    palabras_prohibidas = ['added', 'message was deleted', 'left']
    
    for palabra in palabras_prohibidas:
        if palabra in mensaje.lower():
            return False
    
    # Filtrar emojis
    emoji_pattern = re.compile("["
                              u"\U0001F600-\U0001F64F"  # emoticons
                              u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas
                              u"\U0001F680-\U0001F6FF"  # transporte y mapa de bits
                              u"\U0001F700-\U0001F77F"  # alquimia
                              u"\U0001F780-\U0001F7FF"  # alquimia suplementaria
                              u"\U0001F800-\U0001F8FF"  # símbolos de compatibilidad ideográfica suplementaria
                              u"\U0001F900-\U0001F9FF"  # emoji suplementario
                              u"\U0001FA00-\U0001FA6F"  # emoji suplementario para juegos de cartas
                              u"\U0001FA70-\U0001FAFF"  # símbolos de compatibilidad ideográfica suplementaria
                              u"\U00002702-\U000027B0"  # Dingbats
                              u"\U000024C2-\U0001F251" 
                              "]+", flags=re.UNICODE)
    
    if emoji_pattern.search(mensaje):
        return False
    
    # Filtrar enlaces
    if 'http' in mensaje.lower() or 'www' in mensaje.lower():
        return False
    
    return True

def filtrar_archivo_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as infile, open(archivo_salida, 'w', newline='', encoding='utf-8') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)
        
        # Escribir la primera fila (encabezados) en el nuevo archivo CSV
        headers = next(csv_reader)
        csv_writer.writerow(headers)
        
        # Obtener el índice de la columna 'Mensaje'
        mensaje_index = headers.index('Mensaje')
        
        # Procesar cada fila del archivo de entrada
        for row in csv_reader:
            mensaje = row[mensaje_index]
            
            # Filtrar el mensaje y escribir la fila en el nuevo archivo CSV si pasa el filtro
            if filtrar_mensaje(mensaje):
                csv_writer.writerow(row)

if __name__ == "__main__":
    # Reemplaza 'archivo_entrada.csv' y 'archivo_salida_filtrado.csv' con los nombres reales de tus archivos
    archivo_entrada = 'out.csv'
    archivo_salida = 'filtered.csv'
    
    filtrar_archivo_csv(archivo_entrada, archivo_salida)
