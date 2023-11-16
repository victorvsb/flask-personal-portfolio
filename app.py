"""
    Product Registration Application.
    This application aims to be part of a personal portfolio.
    author: Victor Salustrino Bezerra
    e-mail: salustrino@gmail.com
    linkedin: https://www.linkedin.com/in/victorvsb/
    github: https://github.com/victorvsb
"""

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

from dao.product_dao import ProductDAO
from models.product import Product

app = Flask(__name__)


@app.route("/")
def home():
    """
        Route to homepage.
    """
    return render_template('index.html')

@app.route("/products")
def products_list():
    """
        Route to products list.
    """
    products = ProductDAO().select_all()

    return render_template('products_list.html', products=products)

@app.route("/products/add", methods=['POST', 'GET'])
def products_add():
    """
        Route to product insert.
    """

    if request.method == 'POST':

        product = Product()
        product.id = int(request.form['product_id'])
        product.name = request.form['product_name']
        product.brand = request.form['product_brand']
        product.price = float(request.form['product_price'])

        product_dao = ProductDAO()
        product_dao.product = product
        product_dao.insert()

        return redirect(url_for('products_list'))

    return render_template('products_add.html')

@app.route("/products/<int:product_id>")
def products_detail(product_id):
    """
        Route to product details.
    """

    product = Product()
    product.id = product_id

    product_dao = ProductDAO()
    product_dao.product = product
    product = product_dao.select()

    return render_template('products_details.html', product=product)

@app.route("/products/edit/<int:product_id>", methods=['GET', 'POST'])
def products_edit(product_id):
    """
        Route to product edit.
    """

    if request.method == "GET":

        product = Product()
        product.id = product_id

        product_dao = ProductDAO()
        product_dao.product = product
        product = product_dao.select()

        return render_template("products_add.html", product=product)

    product = Product()
    product.id = int(request.form['product_id'])
    product.name = request.form['product_name']
    product.brand = request.form['product_brand']
    product.price = float(request.form['product_price'])

    product_dao = ProductDAO()
    product_dao.product = product
    product_dao.update()

    return redirect(url_for('products_detail', product_id=product_id))


@app.route("/products/delete/<int:product_id>", methods=['GET', 'POST'])
def products_delete(product_id):
    """
        Route to product delete.
    """

    if request.method == "GET":

        product = Product()
        product.id = product_id

        product_dao = ProductDAO()
        product_dao.product = product
        product_dao.delete()

    return redirect(url_for('products_list'))


if __name__ == "__main__":
    app.run(debug=True)
