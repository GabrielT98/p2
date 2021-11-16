from application.model.entily.product import Product
from application.model.dao.productdao import ProductDao
from flask import render_template
from application import app


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/list')
def listarProdutos():
    lista_produtos = ProductDao().listar_produtos()
    return render_template("product_list.html",lista_produtos = lista_produtos)