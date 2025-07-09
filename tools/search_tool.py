import json

def search_products(query, max_price=1000):
    with open("tools/Product_db.json") as f:
        products = json.load(f)

    filtered = []
    for p in products:
        if any(tag in p["tags"] for tag in query.lower().split()) and p["price"] <= max_price:
            filtered.append(p)
    return filtered[:5]  # Return top 5 matching products
