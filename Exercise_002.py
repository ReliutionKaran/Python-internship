import re
from datetime import datetime

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
            if isinstance(company, dict):
                self.company = Customer(**company)
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
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(email_regex, email))

    def _valid_phone(self, phone):
        phone_regex = re.compile(r"^\d{3}-\d{3}-\d{4}$")
        return bool(re.match(phone_regex, phone))

    def _contains_numbers(self, value):
        return any(char.isdigit() for char in value)
    
    def __repr__(self):
        return f"Name:({self.name})\nEmail:({self.email})\nPhone no.:({self.phone})\nAddress:({self.street})\nCity:({self.city})\nState:({self.state})\nCountry:({self.country})\nType:({self.type})\nCompany's Info:({self.company})"

class Order:
    def __init__(self, number, date, company, billing, shipping, total_amount, order_lines):
        self.number = number
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.TM = total_amount
        self.OL = order_lines
        self._validate_date(date)
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
        
        # Calculate the 'total_amount' based on order lines
        self.total_amount = sum(line["quantity"] * line["unit_price"] for line in order_lines)
        
    def _validate_date(self, date_str):
        today = datetime.now().date()
        order_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        if order_date < today:
            raise ValueError("Invalid order date. Must be today or in the future.")
        
    def __repr__(self):
        return f"Order Number: {self.number}\nDate: {self.date}\nCompany: {self.company}\nBilling: {self.billing}\nShipping: {self.shipping}\nTotal Amount: {self.total_amount}\nOrder Lines: {self.OL}"
       
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

order_lines = [{"product": "Samsung Galaxy S22", "quantity": 2, "unit_price": 10000},
               {"product": "One Plus Ultra", "quantity": 1, "unit_price": 20000}]

company = Customer(**Company_info)
billing = Customer(**Billing_info)
shipping = Customer(**Company_info)

order1 = Order(
    number="12345",
    date="2024-01-09",
    company=company,
    billing=billing,
    shipping=shipping,
    total_amount=50,
    order_lines=order_lines)

print(order1)