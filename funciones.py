import requests
def obtener_informacion(url):
    """
    Función para obtener información sobre aves desde una API REST.
    Retorna la lista de aves con sus nombres en español e inglés y su imagen principal.
    """
    response = requests.get(url)
    if response.status_code == 200:
        lista_aves = response.json()
        return lista_aves
    else:
        print("Error al obtener los datos de la API:", response.status_code)
        return None

def generar_html(lista_aves):
    """
    Genera el HTML con la información de las aves en forma de tarjetas Bootstrap.
    
    Args:
    - lista_aves (list): Lista de diccionarios con la información de las aves.
    
    Returns:
    - str: Cadena de texto con el HTML generado.
    """
    if lista_aves:
            estructura_html = "<div class='row container'>\n"  # Apertura de la clase row
            
            for ave in lista_aves:
                estructura_html += "<div class='col-md-4'>\n"  # Apertura de la clase column
                estructura_html += "<div class='card h-100' style='width: 18rem;'>\n"  # Añadir la clase h-100
                estructura_html += f"<img src='{ave['images']['main']}' class='card-img-top' alt='foto de la aves'>\n"
                estructura_html += "<div class='card-body'>\n"
                estructura_html += f"<h5 class='card-title'>Nombre en Español: {ave['name']['spanish']}</h5>\n"
                estructura_html += f"<p class='card-text'>Nombre en Inglés: {ave['name']['english']}</p>\n"
                estructura_html += "</div></div></div>\n"  # Cierre de la tarjeta (card) y la columna (column)
            
            estructura_html += "</div>\n"  # Cierre de la clase row

            return estructura_html
    else:
            return None
def generar_html_completo(html_aves):
    """
    Genera el HTML completo cargando una plantilla HTML y reemplazando una etiqueta de marcador de posición.

    Args:
    - html_aves (str): HTML generado con la información de las aves.

    Returns:
    - str: HTML completo listo para ser guardado en un archivo.
    """
    with open('template.html', 'r', encoding='utf-8') as file:
        template = file.read()

    html_completo = template.replace('{{content}}', html_aves)
    return html_completo
    

def guardar_html(html_completo, file_path):
    """
    Función para crear un archivo HTML con el contenido especificado.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_completo)

    print(f"Se ha creado el archivo '{file_path}' con los nombres en español e inglés y las imágenes.")
