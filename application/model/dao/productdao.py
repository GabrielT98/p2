from application.model.entily.product import  Product
import json
class ProductDao():

    def listar_produtos(self):
        result = []
        with open('products.json', 'r') as file:
            product_list = json.load(file)
            result = self.converter_dict_to_list(product_list)
        return result


    def converter_dict_to_list(self,produtos):
        resultado=[]

        for produto in produtos:
            product = Product()
            product.setId(produto['id'])
            product.setName(produto['name'])
            product.setImage(produto['image'])
            product.setOldPrice(produto['oldPrice'])
            product.setPrice(produto['price'])
            product.setDescription(produto['description'])
            product.setCount(produto['installments']['count'])
            product.setValue(produto['installments']['value'])
            resultado.append(product)

        return resultado
