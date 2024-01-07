from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

api_key = "AIzaSyBlojaJZvCAQYL4hI20XGVDgXYLv5jWs1Q"
cx = "34901dc6a24504262"

def google_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    results = response.json()
    links = []

    if "items" in results:
        for item in results["items"]:
            link = item.get("link")
            if link:
                links.append(link)

    return links

@app.route('/buscar', methods=['POST'])
def buscar_paginas_tema_libre():
    try:
        data = request.get_json()
        pregunta = data.get('pregunta')

        busqueda_query = f"{pregunta}"
        resultados_api = google_search(busqueda_query)

        if resultados_api:
            return jsonify(resultados=resultados_api)
        else:
            return jsonify(error='Error en la solicitud de búsqueda'), 500
    
    except requests.RequestException as e:
        print('Error en la búsqueda:', str(e))
        return jsonify(error='Error en la búsqueda'), 500
    except Exception as e:
        print('Error desconocido:', str(e))
        return jsonify(error='Error desconocido'), 500

if __name__ == '__main__':
    app.run(port=3001)
