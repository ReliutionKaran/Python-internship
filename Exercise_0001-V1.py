class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.NOP = no_of_products
        
class product(Category):
    def __init__(self, name, code, category, price):
        category.NOP += 1
        self.name = name
        self.code = code
        self.category = category.name
        self.price = price
        
C1 = Category("Electronics", "1", 0)
C2 = Category("Appliances", "2", 0)
C3 = Category("Sports", "3", 0)

P1 = product("Laptop", "P01", C1, 70.000)
P2 = product("Smart Phone", "P02", C1, 10.000)
P3 = product("Coffie Maker", "P03", C2, 5.500)
P4 = product("Digital Camera", "P04", C1, 50.000)
P5 = product("Television", "P05", C1, 12.000)
P6 = product("Running Shoes", "P06", C3, 1.200)
P7 = product("Season Bat", "P07", C3, 4.000)
P8 = product("Kitchen Stove", "P08", C2, 1.500)
P9 = product("Toaster", "P09", C2, 1.600)
P10 = product("Cricket Kit", "P10", C3, 17.000)

    
Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]


# Print category info with its no_of_products
categories = [C1, C2, C3]
for category in categories:
    print(f"Category: {category.name}\nCode: {category.code}\nNo. of Products: {category.NOP}\n")

   
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
    
    