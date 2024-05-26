

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """ Cacluates the ottal cost of items in the supermarket basket
    
    """
    # Define prices
    price_table = {"A": 50, "B": 30, "C": 20, "D": 15}
    offers_table = {"A": (3, 130), "B": (2, 45)}

    total_cost = 0

    # Validate input
    sku_count = {}
    for sku in skus:
        if sku not in price_table:
            return -1
        elif sku in sku_count:
            sku_count[sku] += 1
        else:
            sku_count[sku] = 1
    
    for item, count in sku_count.items():
        if item in offers_table:
            offer_count, offer_price = offers_table[item]
            num_offers = count // offer_count 
            remaining_items = count % offer_count
            total_cost += (num_offers * offer_price) + (remaining_items * price_table[item])
        else:
            total_cost += count * price_table[item]
    
    return total_cost

