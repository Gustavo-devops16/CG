import json
from map_review import map_review
from generate_review import generate_review
from send_review import send_review
from get_product import collect_products
from verify_products import verify_products


def load_products():
    with open("verified_products_hirata.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_reviews(seller_id):
    print("Carregando produtos...")
    raw_products = collect_products(seller_id)
    print("Verificando produtos...")
    products = verify_products(raw_products)
    print("Gerando reviews...")

    all_mapped_reviews = []
    x =1
    for product in products:
        product_name = product["productName"]
        product_id = product["productId"]

        
        
        try:
            
            review = generate_review(product_name)

            
            review["productId"] = product_id

            mapped_review = map_review(review)

            print(f"Review generated for: {mapped_review} | number {x}")
            x+=1

            sent_review = send_review(mapped_review)

        except Exception as e:
            print(f"Error generating review for {product_name}: {e}")  # Detailed error message

    return all_mapped_reviews




get_reviews("odelli001") 

