import re
from datetime import datetime

class Category:
    def __init__(self, name, code, no_of_products):
        self.name = name
        self.code = code
        self.NOP = no_of_products
        
    def Category_info(categories):
        for category in categories:
            print(f"Category: {category.name}\nCode: {category.code}\nNo. of Products: {category.NOP}\n")
   
   
class Product(Category):
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category.name
        self.price = price
        category.NOP += 1
        
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, type=None, company=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.company = self 
        self.type = type
    
        valid_types = ["company", "contact", "billing", "shipping"]
        if type is not None and type not in valid_types:
            raise ValueError(f"Invalid Coustomer type. Valid types are: {valid_types}")
        
        if company is not None:
            if isinstance(Company_info, dict):
                self.company = Customer(**Company_info)
            else:
                print("Invalid company information. Expected a dictionary.")
        else:
            self.company = None
    
        # Validate email
        if not self._valid_email(email):
            print("Please enter a valid email...")

        # Validate phone number
        if not self._valid_phone(phone):
            print("Please Enter a valid phone number...")

        # Validate city, state, and country
        if self._contains_numbers(city):
            print("City can't contain numbers...")
            

        if self._contains_numbers(state):
            print("State can't contain numbers...")

        if self._contains_numbers(country):
            print("Country can't contain numbers...")
            
    def _valid_email(self, email):
        email_reg = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(email_reg, email))

    def _valid_phone(self, phone):
        phone_reg = re.compile(r"^\d{3}-\d{3}-\d{4}$")
        return bool(re.match(phone_reg, phone))

    def _contains_numbers(self, value):
        return any(char.isdigit() for char in value)
    
    def __repr__(self):
        return f"Name:({self.name})\nEmail:({self.email})\nPhone no.:({self.phone})\nAddress:({self.street})\nCity:({self.city})\nState:({self.state})\nCountry:({self.country})\nType:({self.type})\nCompany's Info:({self.company})"
    print("\n")

class Order:
    def __init__(self, number, date, company, billing, shipping, order_lines):
        self.number = number
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines
        self.validate_date(date)
        self.date = date
        
        # Validate and set the 'company' attribute
        if not isinstance(company, Customer):
           raise ValueError("Invalid company information. Expected an instance of Customer.")
        
        # Validate and set the 'billing' attribute
        if not isinstance(billing, Customer):
           raise ValueError("Invalid billing information. Expected an instance of Customer.")
        
        # Validate and set the 'shipping' attribute
        if not isinstance(shipping, Customer):
            raise ValueError("Invalid shipping information. Expected an instance of Customer")
        
    def calculate_total_amount(self):
        total_amount = 0
        for order in self.order_lines:
            total_amount += order.calculate_subtotal()
        print("Total Amount :", total_amount)    
        
    def validate_date(self, date_str):
        today = datetime.now().date()
        order_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        if order_date < today:
            raise ValueError("Invalid order date. Must be today or in the future.")
        
    # Sorting orders based on date
    @staticmethod
    def sort_by_date(Orders):   
        for i in range(0, len(Orders)):
            for j in range(i+1, len(Orders)):
                if Orders[i].date <= Orders[j].date:
                    Orders[i], Orders[j] = Orders[j], Orders[i]
                    
    @staticmethod                
    def find_orders(Orders, target_number):           
        find_orders = next((order for order in Orders if order.number == target_number))
        return find_orders
        
    def __repr__(self):
        return f"Order Number: {self.number}\nDate: {self.date}\nCompany: {self.company}\nBilling: {self.billing}\nShipping: {self.shipping}\nOrder Lines: {self.order_lines}"
    print("\n")
    
    def order_info(Orders, month=None):
        for order in Orders:
            order_month = datetime.strptime(order.date, "%Y-%m-%d").month
            if month is None or order_month == month:
                print(f"Order Number: {order.number}\nDate: {order.date}\nCompany: {order.company}")
        print("\n")
                
        Order.sort_by_date(Orders)
        for order in Orders:
            print(f"\nDate: {order.date}\nOrder Number: {order.number}")
        print("\n")    
            
            
        #Searching of Order
        target_number = input("Enter the Order Number: ")
        found_orders = Order.find_orders(Orders, target_number)
 
        if found_orders:
            print(f"Product found: {found_orders.number} (Order Date: {found_orders.date})")
        else:
            print(f"Product with code '{target_number}' not found.")
        print("\n")
        
class OrderLine:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.calculate_subtotal()
        
        if not isinstance(order, Order):
            raise ValueError("Invalid company information. Expected an instance of Order.")
        
    def calculate_subtotal(self):
        return self.quantity * self.price
        
    def __repr__(self):
        return f"\nOrder:({self.order}), Product:({self.product}), Quantity:({self.quantity}), Price:({self.price}), Subtotal:({self.subtotal})"
    print("\n")

        
C1 = Category("Electronics", "1", 0)
C2 = Category("Appliances", "2", 0)
C3 = Category("Sports", "3", 0)
categories = [C1, C2, C3]

P1 = Product("Laptop", "P01", C1, 70.0)
P2 = Product("Smart Phone", "P02", C1, 10.0)
P3 = Product("Coffie Maker", "P03", C2, 5.5)
P4 = Product("Digital Camera", "P04", C1, 50.0)
P5 = Product("Television", "P05", C1, 12.0)
P6 = Product("Running Shoes", "P06", C3, 1.2)
P7 = Product("Season Bat", "P07", C3, 4.0)
P8 = Product("Kitchen Stove", "P08", C2, 1.5)
P9 = Product("Toaster", "P09", C2, 1.6)
P10 = Product("Cricket Kit", "P10", C3, 17.0)
Products = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

Company_info = {"name":"Aspect Technologies",
                "email":"aspect.6369@gmial.com",
                "phone":"123-456-7893",
                "street":"Trikon Baug main street",
                "city":"Rajkot",
                "state":"Gujrat",
                "country":"India"} 

Billing_info = {"name":"GK Software Solutions",
                "email":"gk2254@gmail.com",
                "phone":"223-563-6789",
                "street":"150 fit ring road",
                "city":"new Rajkot",
                "state":"Gujrat",
                "country":"India"}

CO1 = Customer("Gopal Ajani", 
               "gopalajani09@gmail.com", 
               "955-859-4761", 
               "Gauridad main street", 
               "Rajkot", 
               "Gujrat", 
               "India",
               "billing", 
               Company_info)

company = Customer(**Company_info)
billing = Customer(**Billing_info)
shipping = Customer(**Company_info)

order1 = Order("22054", "2024-03-17", company, billing, shipping, order_lines = [])
order2 = Order("23089", "2024-01-12", company, billing, shipping, order_lines = [])
order3 = Order("24078", "2024-05-11", company, billing, shipping, order_lines = [])
order4 = Order("24034", "2024-06-12", company, billing, shipping, order_lines = [])

Orders = [order1, order2, order3, order4] 

Orderline1 = OrderLine(order1, P1.name, 50, P1.price)
Orderline2 = OrderLine(order1, P2.name, 100, P2.price)
Orderline3 = OrderLine(order1, P3.name, 20, P3.price)
Orderline4 = OrderLine(order1, P4.name, 30, P4.price)

order1.order_lines = [Orderline2, Orderline4]

current_month = datetime.now().month
print(Order.order_info(Orders, month=current_month))
print(order1)
order1.calculate_total_amount()