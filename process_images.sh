#!/bin/bash

# Directorio de las imágenes originales
input_directory="images"

# Directorio donde se guardarán las imágenes convertidas
output_directory="black"

# Crear el directorio de salida si no existe
mkdir -p "$output_directory"

# Procesar cada archivo .png en el directorio de entrada
for image in "$input_directory"/*.png; do
    # Extraer el nombre base del archivo
    base_name=$(basename "$image")
    
    # Ejecutar el comando 'convert' en cada imagen
    convert "$image" -fill white -fuzz 10% +opaque '#4b2f84' -level-colors '#c8c8c8' "$output_directory/$base_name"
done

echo "Conversión completada."

