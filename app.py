"""
    Product Registration Application.
    This application aims to be part of a personal portfolio.
    author: Victor Salustrino Bezerra
    e-mail: salustrino@gmail.com
    linkedin: https://www.linkedin.com/in/victorvsb/
    github: https://github.com/victorvsb
"""
import sqlite3 as sql

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

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

    conn = sql.connect('database.db')
    conn.row_factory = sql.Row
    cursor = conn.cursor()

    query = "SELECT * FROM products ORDER BY name;"

    cursor.execute(query)

    products = cursor.fetchall()

    conn.close()

    return render_template('products_list.html', products=products)

@app.route("/products_add", methods=['POST', 'GET'])
def products_add():
    """
        Route to product insert.
    """

    if request.method == 'POST':

        product_id = int(request.form['product_id'])
        product_name = request.form['product_name']
        product_brand = request.form['product_brand']
        product_price = float(request.form['product_price'])

        insert_product_query = f"INSERT INTO products (id, name, brand, price ) "\
            f"VALUES ({product_id}, '{product_name}', "\
            f"'{product_brand}', {product_price} );"
        conn = sql.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(insert_product_query)
        conn.commit()
        conn.close()

        return redirect(url_for('products_list'))

    return render_template('products_add.html')

@app.route("/products_details/<int:product_id>")
def products_detail(product_id):
    """
        Route to product details.
    """

    select_product_query = f" SELECT * FROM products WHERE id={product_id};"
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    cursor.execute(select_product_query)

    product = cursor.fetchone()

    conn.close()

    return render_template('products_details.html', product=product)

if __name__ == "__main__":
    app.run(debug=True)
