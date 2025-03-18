import json 

def get_seller():
    with open("sellers.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    ids = [item["id"] for item in data.get("items", []) if "id" in item]

    seller_list = {"ids": ids}

    with open("seller.json", "w", encoding="utf-8") as file:
        json.dump(seller_list, file, indent=4)

    print("seller ids saved: ", len(ids)) 

get_seller()
    

