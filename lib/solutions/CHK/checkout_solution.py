

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """ Cacluates the ottal cost of items in the supermarket basket
    
    """
    # Define prices and offers
    price_table = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10,
        "I": 35, "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50,
        "Q": 30, "R": 50, "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
        "Y": 10, "Z": 50}
    offers_table = {"A": [(5, 200), (3, 130)], "B": [(2, 45)], "F": [(3, 20)]} 

    # Track total cost of basket
    total_cost = 0

    # Validate input and add all items to a counter
    if not isinstance(skus, str):
        return -1
    
    sku_count = {}
    for sku in skus:
        if sku not in price_table:
            return -1
        elif sku in sku_count:
            sku_count[sku] += 1
        else:
            sku_count[sku] = 1
    
    # Check and apply the special offer of E
    if "E" in sku_count and sku_count["E"] >= 2:
        free_b = sku_count["E"] // 2
        if "B" in sku_count:
            sku_count["B"] -= free_b
            if sku_count["B"] < 0:
                sku_count["B"] = 0
    
    # Calculate the total price by adding the value of each item
    for item, count in sku_count.items():
        # Checks if the item has a special offer
        if item in offers_table:
            for offer_count, offer_price in sorted(offers_table[item], reverse=True):
                if count >= offer_count:
                    # Calculate how many items this offer can be applied to 
                    num_offers = count // offer_count 
                    # Calculate number of remaining items after offer has been applied
                    remaining_items = count % offer_count
                    # Add it all up
                    total_cost += num_offers * offer_price
                    count = remaining_items
            total_cost += count * price_table[item]
        else:
            # If item does not have a promotion just add its price onto the total
            total_cost += count * price_table[item]
    
    return total_cost

