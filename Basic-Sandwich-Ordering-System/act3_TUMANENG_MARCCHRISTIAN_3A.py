#Marc Christian D. Tumaneng BSCS 3A || Defensive Programming
#Activity #3:
#Task: Building a basic Sandwich Ordering System with Discounts
#Using Object-Oriented Programming (OOP) principles and the pyinputplus library.

# Import the pyinputplus library as pyip
import pyinputplus as pyip

# Define a class called SandwichOrderSystem to manage sandwich orders
class SandwichOrderSystem:
    def __init__(self):
        # Initialize the prices_dict with sandwich component prices
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
        # List of discount codes
        self.discountcode_list = [43312, 67433, 67886, 55534, 89074]
        # Initialize the total_price variable
        self.total_price = 0

    # Method to order sandwiches
    def order_sandwiches(self):
        print("\n============================")
        print("Sandwich Ordering System")
        print("----------------------------\n")
        while True:
            # Prompt the user to choose bread type
            bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True, prompt="Please choose bread type:\n")
            print("----------------------------\n")
            # Prompt the user to choose protein type
            protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True, prompt="Please choose protein type:\n")
            print("-------------------------------")
            # Prompt the user to choose whether they want cheese
            cheese_choice = pyip.inputYesNo("Do you want cheese? (yes/no):")
            print("-------------------------------\n")

            if cheese_choice == 'yes':
                # If yes, prompt the user to choose a cheese type
                cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True, prompt="Please choose a cheese type:\n")
                print("-----------------------------------")
            else:
                cheese_type = None

            print("Add-on\n")
            addons = []
            addons_choices = ['mayo', 'mustard', 'lettuce', 'tomato']
            for addon in addons_choices:
                # Prompt the user for each addon choice
                addon_choice = pyip.inputYesNo(f"Do you want {addon}? (yes/no): ")
                if addon_choice == 'yes':
                    addons.append(addon)

            print("----------------------------------------------------------")
            # Prompt the user for the quantity of sandwiches
            quantity = pyip.inputInt("How many sandwiches do you want?: ", min=1)

            # Calculate the price of the selected sandwich
            sandwich_price = self.calculate_sandwich_price(bread_type, protein_type, cheese_type, addons)
            total_price = sandwich_price * quantity
            self.total_price += total_price

            print(f"You have ordered {quantity} sandwich(s), The price will be ₱{total_price:.2f}.")
            print("----------------------------------------------------------")

            continue_ordering = pyip.inputYesNo("\nAdd another sandwich? (yes/no): ")
            if continue_ordering == 'no':
                break

    # Method to calculate the price of a sandwich
    def calculate_sandwich_price(self, bread_type, protein_type, cheese_type, addons):
        # Calculate the base price based on the selected options
        base_price = self.prices_dict['breads'][bread_type] + self.prices_dict['proteins'][protein_type]

        if cheese_type:
            base_price += self.prices_dict['cheeses'][cheese_type]

        # Add the price for each selected addon
        for addon in addons:
            base_price += self.prices_dict['addons'][addon]

        return base_price

    # Method to apply a discount code
    def apply_discount_code(self):
        has_discount_code = pyip.inputYesNo("Do you have a discount code? (yes/no): ")

        if has_discount_code == 'yes':
            while True:
                discount_code = pyip.inputInt("Enter discount code: ")
                if discount_code in self.discountcode_list and '1' not in str(discount_code):
                    # Apply a 25% discount
                    self.total_price *= 0.75
                    print("-----------------------------------------------------------")
                    print("Discount applied!")
                    break
                else:
                    print("Invalid discount code. Please try again.")
        else:
            print("-----------------------------------------------------------")
            print("No discount code applied.")

    # Method to print the total price
    def print_total_price(self):
        print("Total Price: ₱{:.2f}".format(self.total_price))
        print("===========================================================\n")

# The __main__ block to create an instance and run the ordering system
if __name__ == "__main__":
    order_system = SandwichOrderSystem()
    order_system.order_sandwiches()  # Start ordering sandwiches
    order_system.apply_discount_code()  # Apply discount code if available
    order_system.print_total_price()  # Print the total price
