import json
import requests


def generate_review(product_name):
    url = "http://127.0.0.1:5000/review/generate"  # Placeholder URL
    body = {
        "name": product_name
    }
    try:
        response = requests.post(url, json=body)
        if response.status_code == 200:
            # Assuming the review text is in the response
            review_text = response.json()
            review_json = json.loads(review_text)
            return review_json
        else:
            print(f"Error generating review for {product_name}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error generating review for {product_name}: {e}")
        return None