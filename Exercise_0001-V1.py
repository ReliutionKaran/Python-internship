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
            
C1 = category("Electronics", "1", 20)
C2 = category("Appliances", "2", 30)
C3 = category("Sports", "3", 50)

P1 = product("Laptop", "P01", "Electronics", 70.000)
P2 = product("Smart Phone", "P02", "Electronics", 10.000)
P3 = product("Coffie Maker", "P03", "Appliances", 5.500)
P4 = product("Digital Camera", "P04", "Electronics", 50.000)
P5 = product("Television", "P05", "Electronics", 12.000)
P6 = product("Running Shoes", "P06", "Sports", 1.200)
P7 = product("Season Bat", "P07", "Sports", 4.000)
P8 = product("Kitchen Stove", "P08", "Apppliances", 1.500)
P9 = product("Toaster", "P09", "Appliances", 1.600)
P10 = product("Cricket Kit", "P10", "Sports", 17.000)

# Print category info with its no_of_products
categories = [C1, C2, C3]
for category in categories:
    print(f"Category: {category.name}\nCode: {category.code}\nNo. of Products: {category.NOP}\n")
    
Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
   
# Sort and print products based on price (High to Low) 
def sorted_products_high_to_low(Products):   
    for i in range(0, len(Products)):
        for j in range(i+1, len(Products)):
            if Products[i].price <= Products[j].price:
                Products[i].price, Products[j].price = Products[j].price, Products[i].price
                
sorted_products_high_to_low(Products)
print("Products sorted by price (High to Low):")
for product in Products:
    print(f"{product.name} ({product.category}): {product.price:.3f}")

# Sort and print products based on price (Low to High)
def sorted_products_low_to_high(Products):
    for i in range(0, len(Products)):
        for j in range(i+1, len(Products)):
            if Products[i].price >= Products[j].price:
                Products[i].price, Products[j].price = Products[j].price, Products[i].price

sorted_products_low_to_high(Products)                
print("\nProducts sorted by price (Low to High):")
for product in Products:
    print(f"{product.name} ({product.category}): {product.price:.3f}")

def find_products(Products, target_code):           
    find_products = next((product for product in Products if product.code == target_code), None)
    return find_products

target_code = input("Enter the code: ")
found_products = find_products(Products, target_code)
 
if found_products:
    print(f"Product found: {found_products.name} (Code: {found_products.code}, Category: {found_products.category}, Price: {found_products.price:.3f})")
else:
    print(f"Product with code '{target_code}' not found.")