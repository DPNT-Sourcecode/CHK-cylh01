

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """ Cacluates the ottal cost of items in the supermarket basket
    
    """
    # Define prices
    price_table = {"A": 50, "B": 30, "C": 20, "D": 15}
    offers_table = {"A": (3, 130), "B": (2, 45)}

    total_cost = 0

    # Validate input and add items to a counter
    if not isinstance(skus, str) or skus == "":
        return -1
    
    sku_count = {}
    for sku in skus:
        if sku not in price_table:
            return -1
        elif sku in sku_count:
            sku_count[sku] += 1
        else:
            sku_count[sku] = 1
    
    # Calculate the total price by adding the value of each item
    for item, count in sku_count.items():
        # Checks if the item has a special offer
        if item in offers_table:
            offer_count, offer_price = offers_table[item]
            # Calculate how many items this offer can be applied to 
            num_offers = count // offer_count 
            # Calculate number of remaining items after offer has been applied
            remaining_items = count % offer_count
            # Add it all up
            total_cost += (num_offers * offer_price) + (remaining_items * price_table[item])
        else:
            # If item does not have a promotion just add its price onto the total
            total_cost += count * price_table[item]
    
    return total_cost



