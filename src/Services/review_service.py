from Mapper.map_review import map_review
from Dal.c3po import generate_review
from Controllers.send_review import send_review
from Dal.vtex import collect_products
from Mapper.verify_products import verify_products


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






