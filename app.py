import os
from flask import Flask, jsonify
import pocketbase
from flask_cors import CORS
# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)
# Conectar con PocketBase
pb = pocketbase.PocketBase('http://localhost:8090')  # Asegúrate de que la URL sea correcta
pb.admins.auth_with_password('vargascamachojoseedwin@gmail.com', '12345678')

@app.route('/api/products', methods=['GET'])
def get_products():
    # Obtener todos los registros de la colección 'Product'
    products = pb.collection('Product').get_full_list()

    # Convertir los productos a un formato JSON
    products_data = []
    for product in products:
        # Convertir cada registro a un diccionario (aseguramos que sea serializable a JSON)
        product_dict = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image": product.image,
            "stock": product.stock,
            "provider": product.provider,
            "state": product.state,
            "location": product.location,
            "created": product.created,
            "updated": product.updated,
        }
        products_data.append(product_dict)
    
    return jsonify(products_data)

@app.route('/api/wineries', methods=['GET'])
def get_wineries():
    # Obtener todos los registros de la colección 'Winery'
    wineries = pb.collection('Winery').get_full_list()

    # Convertir las bodegas a un formato JSON
    wineries_data = []
    for winery in wineries:
        # Usar 'name__winery' en lugar de 'name'
        winery_dict = {
            "id": winery.id,
            "name__winery": winery.name__winery,  # Usamos 'name__winery' correctamente
            "description": winery.description,
            "created": winery.created,
            "updated": winery.updated,
        }
        wineries_data.append(winery_dict)
    
    return jsonify(wineries_data)

    

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
