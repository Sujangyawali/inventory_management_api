from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data
products_list = [
    {
        'id': 0,
        "name": "Laptop",
        "category": "Electronics",
        "price": 1200.00
    },
    {
        'id': 1,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 800.00
    },
    {
        'id': 2,
        "name": "Desk Chair",
        "category": "Furniture",
        "price": 150.00
    },
    {
        'id': 3,
        "name": "Blender",
        "category": "Kitchen Appliances",
        "price": 70.00
    },
]

@app.route('/products', methods=['GET', 'POST'])
def products():
    # Retrieve all products
    if request.method == 'GET':
        if len(products_list) > 0:
            return jsonify(products_list)
        else:
            return jsonify({"message": "No products found"}), 404

    # Add a new product
    if request.method == 'POST':
        new_name = request.form['name']
        new_category = request.form['category']
        new_price = float(request.form['price'])  # convert price to float
        new_id = len(products_list)  # generate a new ID

        new_product = {
            "id": new_id,
            "name": new_name,
            "category": new_category,
            "price": new_price,
        }

        products_list.append(new_product)
        return jsonify(products_list), 201

@app.route('/product/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_product(id):
    # Retrieve a product by ID
    if request.method == 'GET':
        for product in products_list:
            if product['id'] == id:
                return jsonify(product)
        return jsonify({"message": "Product not found"}), 404

    # Update a product by ID
    if request.method == 'PUT':
        for product in products_list:
            if product['id'] == id:
                product['name'] = request.form['name']
                product['category'] = request.form['category']
                product['price'] = float(request.form['price'])  # convert price to float
                updated_product = {
                    "id": product['id'],
                    "name": product['name'],
                    "category": product['category'],
                    "price": product['price']
                }
                return jsonify(updated_product)
        return jsonify({"message": "Product not found"}), 404

    # Delete a product by ID
    if request.method == 'DELETE':
        for product in products_list:
            if product['id'] == id:
                products_list.remove(product)
                return jsonify(products_list)
        return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
