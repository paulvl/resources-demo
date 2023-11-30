import os
import requests
from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk

# Variables globales
global pil_image
global image_label
global entry

def get_image():
    global pil_image  # Declarar la variable como global
    global image_label

    # URL de donde se obtendrá la imagen
    url = 'https://www.apeseg.org.pe/php/web/captcha.php'
    
    # Realizar la petición HTTP para descargar la imagen
    response = requests.get(url, stream=True)
    
    # Verificar que la petición fue exitosa
    if response.status_code == 200:
        # Leer la imagen desde la respuesta HTTP y abrirla con PIL
        pil_image = Image.open(response.raw)
        
        # Convertir la imagen para Tkinter
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # Mostrar la imagen en la interfaz
        image_label.config(image=tk_image)
        image_label.image = tk_image  # Guardar una referencia de la imagen de Tkinter
    else:
        print("Error al descargar la imagen")

def clear_entry():
    entry.delete(0, 'end')  # Borra el contenido actual del Entry

def save_image(event=None):
    global entry
    global pil_image

    # Obtener el nombre del archivo del Entry
    filename = entry.get()
    
    # Crear la carpeta 'images' si no existe
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Guardar la imagen en la carpeta 'images' con el nombre y extensión .jpg
    image_path = os.path.join('images', f"{filename}.png")
    pil_image.save(image_path, 'PNG', quality=100)  # Usar pil_image para guardar la imagen
    
    clear_entry()
    get_image()

# Crear la ventana principal
root = Tk()
root.title('Image Downloader')

# Etiqueta para mostrar la imagen
image_label = Label(root)
image_label.pack()

# Entrada de texto para el nombre del archivo
entry = Entry(root)
entry.pack()
entry.bind('<Return>', save_image)  # Vincula la tecla Enter a la función save_image


# Botón para guardar la imagen
save_button = Button(root, text="Save", command=save_image)
save_button.pack()

get_image()

# Ejecutar el bucle principal de Tkinter
root.mainloop()
