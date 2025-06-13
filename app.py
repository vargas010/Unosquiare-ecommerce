import os
from flask import Flask, jsonify
import pocketbase
from flask_cors import CORS
from flask import Flask, request, jsonify

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

# Ruta para añadir productos
@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json  # Obtener datos JSON enviados desde el frontend

    # Verificar que todos los campos necesarios están presentes
    if not data.get('name') or not data.get('provider_id') or not data.get('price') or not data.get('stock'):
        return jsonify({"error": "Faltan campos requeridos"}), 400

    # Obtener el proveedor de la base de datos usando el ID proporcionado
    provider_id = data.get('provider_id')
    try:
        provider = pb.collection('Provider').get_one(provider_id)
    except Exception as e:
        return jsonify({"error": f"Proveedor no encontrado: {str(e)}"}), 404

    # Crear un nuevo producto
    new_product = {
        "name": data.get('name'),
        "description": data.get('description'),
        "price": data.get('price'),
        "stock": data.get('stock'),
        "provider": provider_id,  # Relacionar con el proveedor
        "created": "2025-06-12T00:00:00Z",  # Solo para ejemplo
        "updated": "2025-06-12T00:00:00Z",  # Solo para ejemplo
    }

    # Añadir el producto a la base de datos de PocketBase
    try:
        pb.collection('Product').create(new_product)
        return jsonify({"message": "Producto añadido correctamente", "product": new_product}), 201
    except Exception as e:
        return jsonify({"error": f"Error al guardar el producto: {str(e)}"}), 500

# Ruta para obtener proveedores
@app.route('/api/providers', methods=['GET'])
def get_providers():
    # Obtener todos los proveedores desde la colección 'Provider'
    providers = pb.collection('Provider').get_full_list()

    # Devolver la lista de proveedores
    providers_data = []
    for provider in providers:
        provider_data = {
            "id": provider.id,  # Asegúrate de que incluimos el ID
            "name": provider.name,  # Asegúrate de que el campo 'name' esté disponible
            "email": provider.email,
            "description": provider.description,
            "phone": provider.phone,
            "address": provider.address,
            "created": provider.created,
            "updated": provider.updated
        }
        providers_data.append(provider_data)

    return jsonify(providers_data)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
