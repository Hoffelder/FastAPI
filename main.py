from fastapi import FastAPI
from json_db import JsonDB
from product import Product
from indb import generate_products  

app = FastAPI() 

productDB = JsonDB(path='./data/products.json')

@app.get("/products")
def get_products():
    products = productDB.read()
    return { "products" : products }

@app.post("/products")
def create_products(product: Product):
    productDB.insert(product)
    print("new product", product)

    return { "status" : "inserted" }

