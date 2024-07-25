import pyinputplus as pyip

class SandwichOrderSystem:
    def __init__(self):
        #prices as is, don't change it
        self.prices_dict = {
            'breads': {
                'wheat': 10.00,
                'white': 10.25,
                'sourdough': 20.00,
            },
            'proteins': {
                'chicken': 10.50,
                'turkey': 10.25,
                'ham': 10.75,
                'tofu': 20.00,
            },
            'cheeses': {
                'cheddar': 10.75,
                'Swiss': 10.25,
                'mozzarella': 11.25,
            },
            'addons': {
                'mayo': 5.5,
                'mustard': 5.25,
                'lettuce': 5.50,
                'tomato': 5.50,
            }
        }
        self.discountcode_list = [43312, 67433, 67886, 55534, 89074]  # you can add more
        self.total_price = 0

    # you can add more functions if you wish
    def order_sandwiches(self):
        # your code here

   # def apply_discount_code(self):
        # your code here

   # def print_total_price(self):
        # your code here

        if __name__ == "__main__":
            order_system = SandwichOrderSystem()
            order_system.order_sandwiches()
            order_system.apply_discount_code()
            order_system.print_total_price()

