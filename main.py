import requests
import json
import funciones as mr

# URL de la API de aves
url = 'https://aves.ninjas.cl/api/birds'

# Obtener información de la API de aves
lista_aves = mr.obtener_informacion(url)

# Generar HTML con la información de las aves
generar_html = mr.generar_html(lista_aves)

# Generar el HTML completo con el contenido HTML generado
html_completo = mr.generar_html_completo(generar_html)

# Guardar el HTML completo en un archivo HTML
mr.guardar_html(html_completo, 'index.html')