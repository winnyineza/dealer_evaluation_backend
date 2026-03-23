from flask import Flask
from flask_cors import CORS
import json
import os

app = Flask("List of products")
CORS(app)

@app.route("/products")
def getProductsList():
  products = []
  with open("products.json", "r") as prodfile:
    data = json.load(prodfile)
    for product in data["products"]:
      products.append(product["product"])
    return {"products":products}

@app.route("/getdealers/<product>")
def getDealers(product):
  products = []
  ret = False
  with open("products.json", "r") as prodfile:
    data = json.load(prodfile)
    for productMeta in data["products"]:
      if productMeta["product"] == product:
        ret = True
        return {"dealers":productMeta["Dealers"]}
  if ret == False:
    return {"message":"Could not find dealers for this product"}

if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
