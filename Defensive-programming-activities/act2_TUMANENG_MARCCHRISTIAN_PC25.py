#ACTIVITY 2 -  DEFENSIVE PROGRAMMING || BUILDING A BASIC SHOPPING SYSTEM (OOP)
#MARC CHRISTIAN TUMANENG - BSCS 3A

# Product class 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#ShoppingCart class 
class ShoppingCart:
    def __init__(self, user_balance):
        self.user_balance = user_balance  
        self.products = []  

     # Adds a product to the shopping cart.
    def add_product(self, product):      
        self.products.append(product)
        print("Added product: {} (₱{})".format(product.name, product.price))

    # Lists of all products in the cart.
    def list_products(self):
        print("\nProducts in cart:")
        for idx, product in enumerate(self.products, start=1):
            print("{}. {} - ₱{}".format(idx, product.name, product.price))

     # Allows user to purchase product from the cart if they have enough balance
    def purchase_product(self, product):
        print("\nAvailable balance: ₱{}".format(self.user_balance))
        total_price = product.price

        if total_price > self.user_balance:
            print("Insufficient balance to purchase {}.".format(product.name))
        else:
            self.user_balance -= total_price
            self.products.remove(product)
            print("Purchased {} for ₱{}. \nRemaining balance: {}".format(product.name, product.price, self.user_balance))

if __name__ == "__main__":
    # Create an instance of the ShoppingCart
    my_cart = ShoppingCart(user_balance=1005352)

    # Create instances of the Product 
    laptop = Product("Laptop", 45000)
    phone = Product("Phone", 30000)
    keyboard = Product("Keyboard", 4000)
    mouse = Product("Mouse", 4000)
    pc = Product("Super ultra very rare high-end Computer", 950000)

    # Add products to the shopping cart.
    my_cart.add_product(laptop)
    my_cart.add_product(phone)
    my_cart.add_product(keyboard)
    my_cart.add_product(mouse)
    my_cart.add_product(pc)

    # List the products in the cart.
    my_cart.list_products()

    # Purchase products from the cart.
    my_cart.purchase_product(laptop)
    my_cart.purchase_product(phone)
    my_cart.purchase_product(keyboard)
    my_cart.purchase_product(mouse)
    my_cart.purchase_product(pc)
