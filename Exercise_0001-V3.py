class Category:
    def __init__(self, name, code, no_of_products, parent=None, display_name=None):
        self.name = name
        self.code = code
        self.NOP = no_of_products
        self.parent = parent
        self.display_name = display_name
        self.Products = []
     
    # Generate Display Name.(Used Recursion Method) 
    def generate_display_name(self):
        if self.parent:
            self.display_name = f"{self.parent.generate_display_name()} > {self.name}"
        else:
            self.display_name = self.name
        return self.display_name
    
    # This function append a product for its specific Category, from List of products. 
    def add_product(self, product):
        self.Products.append(product)  
        
    # Sorting Categories from Bubble Sorting Method by name (Alphabetical Manner)     
    def sorting_categories(categories):
        n = len(categories)
        for i in range(n):
            for j in range(0, n-i-1):
                if categories[j].name > categories[j + 1].name:
                    categories[j], categories[j + 1] = categories[j + 1], categories[j]
    
    # Print All Info of category class    
    def Category_info(categories):
        Category.sorting_categories(categories)
        for category in categories:
            print(f"Category: {category.name}\nCode: {category.code}\nNo. of Products: {category.NOP}\n")
            for product in category.Products:
                print(f"Product: {product.name} (Code: {product.code}, Price: {product.price:.3f})")
            print("\n")
            
class Product(Category):
    def __init__(self, name, code, category, price):
        category.add_product(self)
        category.NOP += 1
        self.name = name
        self.code = code
        self.category = category.name
        self.price = price
        self.stock_at_locations = {}
        
    def add_stock_at_location(self, location, quantity):
        if location in self.stock_at_locations:
            self.stock_at_locations[location] += quantity
        else:
            self.stock_at_locations[location] = quantity
            
    def update_stock_for_multiple_products(products, location, stock_quantity):
        for product in products:
            product.add_stock_at_location(location, stock_quantity)
            
        for product in [P26, P27, P28, P29, P30]:
            print(f"{product.name} Stock at {C1.name}: {product.stock_at_locations.get(C1, 0)}")
            print(f"{product.name} Stock at {C2.name}: {product.stock_at_locations.get(C2, 0)}")
            print(f"{product.name} Stock at {C3.name}: {product.stock_at_locations.get(C3, 0)}")
        
        #print(f"\nStock information for {P1.name} (Code: {P1.code}):")
        #for location, stock in P1.stock_at_locations.items():
        #    print(f"At {location.name}: {stock} units")
                       
# Sort and print products based on price (High to Low) 
    @staticmethod
    def sorted_products_high_to_low(Products):   
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price <= Products[j].price:
                    Products[i], Products[j] = Products[j], Products[i]
                    
# Sort and print products based on price (Low to High)
    @staticmethod
    def sorted_products_low_to_high(Products):
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price >= Products[j].price:
                    Products[i], Products[j] = Products[j], Products[i]
       
# Search Products from code
    @staticmethod                
    def find_products(Products, target_code):           
        find_products = next((product for product in Products if product.code == target_code))
        return find_products
    
    def Product_info(Products):
    #High to low Sorting
        print("Products sorted by price (High to Low):")        
        Product.sorted_products_high_to_low(Products)
        for product in Products:
            print(f"{product.name} ({product.category}): {product.price:.3f}")

    #Low to High Sorting
        Product.sorted_products_low_to_high( Products)                
        print("\nProducts sorted by price (Low to High):")
        for product in Products:
            print(f"{product.name} ({product.category}): {product.price:.3f}")
            
    #Searching of Product
        target_code = input("Enter the code: ")
        found_products = Product.find_products(Products, target_code)
 
        if found_products:
            print(f"Product found: {found_products.name} (Code: {found_products.code}, Category: {found_products.category}, Price: {found_products.price:.3f})")
        else:
            print(f"Product with code '{target_code}' not found.")
            
class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.FL = from_location
        self.TL = to_location
        self.product = product
        self.quantity = quantity

    @staticmethod
    def movements_by_product(product):
        return [movement for movement in Movement.movements if movement.product == product]
    
    #def move_product(movements):
        
C1 = Category("Electronics", "1", 0)
C2 = Category("Appliances", "2", 0)
C3 = Category("Sports", "3", 0)

Vehicle = Category("Vehicle", "4", 0)
Car = Category("Car", "5", 0, Vehicle)
Petrol = Category("Petrol", "6", 0, Car)
Electric = Category("Electric", "7", 0, Car)
Gas = Category("Gas", "8", 0, Car)

categories = [C1, C2, C3, Vehicle, Car, Petrol, Electric, Gas]

P1 = Product("Laptop", "P001", C1, 50.000)
P2 = Product("Smart Phone", "P002", C1, 10.000)
P3 = Product("Coffie Maker", "P003", C2, 5.500)
P4 = Product("Digital Camera", "P004", C1, 50.000)
P5 = Product("Television", "P005", C1, 12.000)
P6 = Product("Running Shoes", "P006", C3, 1.200)
P7 = Product("Season Bat", "P007", C3, 4.000)
P8 = Product("Kitchen Stove", "P008", C2, 1.500)
P9 = Product("Toaster", "P009", C2, 1.600)
P10 = Product("Cricket Kit", "P010", C3, 17.000)

P11 = Product("TATA Harier", "P011", Car, 150.000)
P12 = Product("TATA Safari", "P012", Car, 250.000)
P13 = Product("TATA Altroz", "P013", Car, 100.000)

P14 = Product("Platina", "P014", Vehicle, 75.000)
P15 = Product("Pulser", "P015", Vehicle, 90.000)
P16 = Product("Honda Shine", "P016", Vehicle, 80.000)

P17 = Product("Toyota Supra", "P017", Petrol, 990.000)
P18 = Product("Fortuner", "P018", Petrol, 500.000)
P19 = Product("Thar", "P019", Petrol, 250.000)

P20 = Product("Nexon EV", "P020", Electric, 900.000)
P21 = Product("Hundai EV", "P021", Electric, 120.000)
P22 = Product("Maruti EV", "P022", Electric, 100.000)

P23 = Product("Swift", "P023", Gas, 700.000)
P24 = Product("Alto", "P024", Gas, 450.000)
P25 = Product("Ecco", "P025", Gas, 400.000)

P26 = Product("Knife", "P026", C2, 1.000)
P27 = Product("Spoon", "P027", C2, 1.200)
P28 = Product("Tennis Balls", "P028", C3, 6.000)
P29 = Product("Season Balls", "P029", C3, 12.000)
P30 = Product("Air Cooler", "P030", C1, 15.000)

Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25, P26, P27, P28, P29, P30]

L1 = Location("Stock Hall A", "A0001")
L2 = Location("Stock Hall B", "B0002")
L3 = Location("Stock Hall C", "C0003")
L4 = Location("Stock Hall D", "D0004")

locations = (L1, L2, L3, L4)

movement1 = Movement(L1, L2, P1, 100)
movement2 = Movement(L2, L3, P2, 500)
movement3 = Movement(L3, L4, P3, 300)

movements = [movement1, movement2, movement3]

a = Category.Category_info(categories)
print(a)
b = Product.Product_info(Products)
b
c = Category.generate_display_name(Petrol)
print(c)

A = Product.update_stock_for_multiple_products(Products, C1, 20)
print(A)