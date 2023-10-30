import requests

# URL de la API a la que deseas acceder
url = 'http://localhost:5000/api/data'

# Realizar una solicitud GET

while True:
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Decodificar el contenido JSON de la respuesta
        data = response.json()
        print("Datos recibidos:")
        print(data)
    else:
        print("La solicitud no fue exitosa. Código de respuesta:", response.status_code)
