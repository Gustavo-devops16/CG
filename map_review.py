import random

def generate_rating():
    return random.randint(3, 5)

def generate_name():
    names = ["pedro", "paulo", "joao", "maria", "luiz", "eduardo" ]
    surnames = ["silva", "souza", "pereira", "borges", "lima", "sales", "duarte", "johnson"  ]

    first_name = random.choice(names)
    last_name = random.choice(surnames)

    full_name = f"{first_name} {last_name}"
    return full_name



def generate_id():
    return str(random.randint(1000000, 9999999))

def map_review(review):
    mapped_review = {
        "id": generate_id(),  # Assuming generate_id() is defined elsewhere
        "productId": review["productId"],
        "rating": generate_rating(),  # Assuming generate_rating() is defined elsewhere
        "text": review["review"],  # Access the review text from the dictionary
        "reviewerName": generate_name(),  # Assuming generate_name() is defined elsewhere
        "approved": True,
        "title": review.get("title")  # Include title if it exists, else empty string
    }
    return mapped_review