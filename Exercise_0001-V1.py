class category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.NOP = no_of_products
        
class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        
C1 = category("Electronics", "P20", 20)
C2 = category("Appliances", "D30", 30)
C3 = category("Sports", "F50", 50)

P1 = product("Laptop", "P01", "Electronics", 70.000)
P2 = product("Smart Phone", "P05", "Electronics", 10.000)
P3 = product("Coffie Maker", "D04", "Appliances", 5.500)
P4 = product("Digital Camera", "P08", "Electronics", 50.000)
P5 = product("Television", "P26", "Electronics", 12.000)
P6 = product("Running Shoes", "F45", "Sports", 1.200)
P7 = product("Season Bat", "F38", "Sports", 4.000)
P8 = product("Kitchen Stove", "D28", "Apppliances", 1.500)
P9 = product("Toaster", "D21", "Appliances", 1.600)
P10 = product("Cricket Kit", "F39", "Sports", 17.000)

Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

# Print category info with its no_of_products
categories = [C1, C2, C3]
for category in categories:
    print(f"Category: {category.name}\nCode: {category.code}\nNo. of Products: {category.NOP}\n")
    
    
# Sort and print products based on price (High to Low)    
print("Products sorted by price (High to Low):")
sorted_products_high_to_low = sorted(Products, key=lambda x: x.price, reverse=True)
for product in sorted_products_high_to_low:
    print(f"{product.name} ({product.category}): {product.price:.3f}")

# Sort and print products based on price (Low to High)
print("\nProducts sorted by price (Low to High):")
sorted_products_low_to_high = sorted(Products, key=lambda x: x.price, reverse=False)
for product in sorted_products_low_to_high:
    print(f"{product.name} ({product.category}): {product.price:.3f}")
