from flask import Flask, request
from products import products

app = Flask(__name__)


@app.route('/products', methods=['GET'])
def get_products():
    return products


@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product_found = list(filter(lambda x: x['id'] == product_id, products))
    if product_found:
        return product_found[0]
    return {'message': 'Producto no encontrado'}


@app.route('/add_product', methods=['POST'])
def add_product():
    products.append(request.json)
    return {'products': products, 'message': 'Product added successfully'}


@app.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product_found = [product for product in products if product['id'] == product_id]
    if product_found:
        product_found[0].update({
            'price': request.json['price'],
            'quantity': request.json['quantity']
        })
        return {'message': 'Product updated successfully', 'product': product_found}
    return {'message': 'Product not found'}


@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product_index = [index for index, product in enumerate(products) if product['id'] == product_id]
    if product_index:
        product_deleted = products.pop(product_index[0])
        return {'message': 'Product removed successfully', 'product': product_deleted}
    return {'message': 'Product not found'}


if __name__ == '__main__':
    app.run(port=4000, debug=True)
