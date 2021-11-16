from application.model.entily.product import  Product
class ProductDao():
    def __init__(self):
        self.__products_list = []

    def adicionar_produto(self,produto: Product):
        self.__products_list.append(produto)

    def listar_produtos(self):
        return self.__products_list