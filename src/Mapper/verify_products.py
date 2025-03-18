import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()
app_key = os.getenv("X_VTEX_API_AppKey")
app_token = os.getenv("X_VTEX_API_AppToken")

def verify_products(collected_products):

    verified_products = []

    for product in collected_products:
        product_id = product["productId"]
        url = f"https://compresuapeca.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitByProductId/{product_id}"
        headers = { 
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-VTEX-API-AppKey": app_key,
        "X-VTEX-API-AppToken": app_token
        }

        try:
            time.sleep(0.2)
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
            
                data = response.json()
                data = data[0]
                if data.get("IsActive"):
                
                    print(f"Producto {product_id} está ativo.")
                    print(f"Ativo: {data.get('IsActive')}")

                    if 'description' in product:
                        del product['description']
        
                    verified_products.append(product)
                else:
                    print(f"Producto {product_id} está inativo.")
            else:
                print(f"Erro ao verificar produto {product_id}: {response.status_code}")

        except Exception as e:
            print(f"Erro ao verificar produto {product_id}: {e}")
        
    return verified_products

