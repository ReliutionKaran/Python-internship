class Category:
    def __init__(self, name, code, no_of_products, parent=None):
        self.name = name
        self.code = code
        self.NOP = no_of_products
        self.parent = parent
        self.display_name = None
        self.Products = []
      
    def generate_display_name(self):
        if self.parent:
            self.display_name = f"{self.parent.generate_display_name()} > {self.name}"
        else:
            self.display_name = self.name
        return self.display_name
    
    def display_products_by_category(categories):
        category_dict = {}

        # Organize products by category name
        for category in categories:
            category_name = category.name
            if category_name not in category_dict:
                category_dict[category_name] = []

            category_dict[category_name].extend(category.Products)
        
    def Category_info(categories):
        for Category in categories:
            print(f"Category: {Category.name}\nCode: {Category.code}\nNo. of Products: {Category.NOP}\n")
            Category.generate_display_name()

   
class Product(Category):
    
    def __init__(self, name, code, category, price):
        category.NOP += 1
        self.name = name
        self.code = code
        self.category = category.name
        self.price = price
                
# Sort and print products based on price (High to Low) 
    @staticmethod
    def sorted_products_high_to_low(Products):   
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price <= Products[j].price:
                    Products[i].price, Products[j].price = Products[j].price, Products[i].price
                    
# Sort and print products based on price (Low to High)
    @staticmethod
    def sorted_products_low_to_high(Products):
        for i in range(0, len(Products)):
            for j in range(i+1, len(Products)):
                if Products[i].price >= Products[j].price:
                    Products[i].price, Products[j].price = Products[j].price, Products[i].price
    
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
            print(f"Product found: {found_products.name} (Code: {found_products.code}, Category: {found_products.category}, Price: {found_products.price:.5f})")
        else:
            print(f"Product with code '{target_code}' not found.")
        
C1 = Category("Electronics", "1", 0)
C2 = Category("Appliances", "2", 0)
C3 = Category("Sports", "3", 0)

Vehicle = Category("Vehicle", "4", 0)
Car = Category("Car", "5", 0, Vehicle)
Petrol = Category("Petrol", "6", 0, Car)
Electric = Category("Electric", "7", 0, Car)
Gas = Category("Gas", "8", 0, Car)

categories = [C1, C2, C3, Vehicle, Car, Petrol, Electric, Gas]


P1 = Product("Laptop", "P001", C1, 70.000)
P2 = Product("Smart Phone", "P002", C1, 10.000)
P3 = Product("Coffie Maker", "P003", C2, 5.500)
P4 = Product("Digital Camera", "P004", C1, 50.000)
P5 = Product("Television", "P005", C1, 12.000)
P6 = Product("Running Shoes", "P006", C3, 1.200)
P7 = Product("Season Bat", "P007", C3, 4.000)
P8 = Product("Kitchen Stove", "P008", C2, 1.500)
P9 = Product("Toaster", "P009", C2, 1.600)
P10 = Product("Cricket Kit", "P010", C3, 17.000)

P11 = Product("TATA Harier", "P011", Car, 15.00000)
P12 = Product("TATA Safari", "P012", Car, 25.00000)
P13 = Product("TATA Altroz", "P013", Car, 10.00000)

P14 = Product("Platina", "P014", Vehicle, 75.000)
P15 = Product("Pulser", "P015", Vehicle, 90.000)
P16 = Product("Honda Shine", "P016", Vehicle, 80.000)

P17 = Product("Toyota Supra", "P017", Petrol, 99.00000)
P18 = Product("Fortuner", "P018", Petrol, 50.00000)
P19 = Product("Thar", "P019", Petrol, 25.00000)

P20 = Product("Nexon EV", "P020", Electric, 9.00000)
P21 = Product("Hundai EV", "P021", Electric, 12.00000)
P22 = Product("Maruti EV", "P022", Electric, 10.00000)

P23 = Product("Swift", "P023", Gas, 7.00000)
P24 = Product("Alto", "P024", Gas, 4.50000)
P25 = Product("Ecco", "P025", Gas, 4.00000)

Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23, P24, P25]

C = Category.Category_info(categories)
print(C)

P = Product.Product_info(Products)
P

D = Category.generate_display_name(Petrol)
print(D)

E = Category.display_products_by_category(categories)
print(E)