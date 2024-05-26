

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """ Cacluates the ottal cost of items in the supermarket basket
    
    """
    # Define the base price for each item
    price_table = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10,
        "I": 35, "J": 60, "K": 70, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50,
        "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40, "V": 50, "W": 20, "X": 17,
        "Y": 20, "Z": 21}
    
    # Define the basic offers for each item
    basic_offers_table = {
        "A": [(5, 200), (3, 130)], "B": [(2, 45)], "F": [(3, 20)], "H": [(10, 80), (5, 45)],
        "K": [(2, 120)], "P": [(5, 200)], "Q": [(3, 80)], "U": [(4, 120)], "V": [(3, 130), (2, 90)]
    }

    # Define the offers for each item that affect another item
    advanced_item_offers = {"E": ("B", 2), "N": ("M", 3), "R": ("Q", 3)} 

    # Define the group offer items, discount price and required count
    group_offers = {"S", "T", "X", "Y", "Z"}
    group_discount = 45
    group_count = 3

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
    
    # Check and apply the advanced item offers
    for offer_item, (free_item, required_count) in advanced_item_offers.items():
        # Check if the current item in the offer is in the basket and the required count is met
        if offer_item in sku_count and sku_count[offer_item] >= required_count:
            # Calculate number of free items to be given
            free_count = sku_count[offer_item] // required_count
            if free_item in sku_count:
                sku_count[free_item] -= free_count
                if sku_count[free_item] < 0:
                    sku_count[free_item] = 0
    
    # Calculate the total price by adding the value of each item
    for item, count in sku_count.items():
        # Checks if the item has a special offer
        if item in basic_offers_table:
            for offer_count, offer_price in sorted(basic_offers_table[item], reverse=True):
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



