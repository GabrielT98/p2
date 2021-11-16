from flask import render_template
from application import app

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/list')
def listarProdutos():
    return render_template("product_list.html")