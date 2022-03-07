from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost:8001/shopping_website_db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(10, 2))

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f'{self.name}'


@app.route('/products', methods=['GET'])
def get_products_list():
    products = Product.query.all()
    results = [
        {
            'name': product.name,
            'description': product.description,
            'price': product.price
        } for product in products
    ]
    return {'count': len(results), 'products': results}


@app.route('/product', methods=['POST'])
def post_product():
    data = request.get_json()
    new_product = Product(name=data['name'], description=data['description'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return {"message": f"product {new_product.name} has been created successfully."}


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.filter_by(id=product_id).one()
    result = {'id': product.id}
    return {'product': result}


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(product_id):
    product = Product.querry.get_or_404(product_id)
    data = request.get_jason()
    product.name = data['name']
    product.description = data['description']
    product.price = data['price']
    db.session.add(product)
    db.session.commit()
    return {"message": f"product {product.name} successfully updated"}


@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.querry.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return {"message": f"product {product.name} successfully deleted"}


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8002)
