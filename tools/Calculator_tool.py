def calculate_total(products):
    if isinstance(products, list):
        return sum([p['price'] for p in products])
    return 0
