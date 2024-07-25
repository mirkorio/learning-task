import pyinputplus as pyip
def is_even(number):
    if int(number) % 2 == 0:
        return True
    else:
        raise ValueError("Input must be an even number.")

even_number = pyip.inputCustom(is_even, prompt="Enter an even number: ")
#####
import pyinputplus as pyip
confirm = pyip.inputBool(prompt="True or False?: ")
#####
import pyinputplus as pyip
drink = pyip.inputChoice(["Coffee", "Tea", "Water"], prompt="Choose your drink: ")
#####
import pyinputplus as pyip
import datetime
date = pyip.inputDate(prompt="Enter a date (YYYY-MM-DD): ", formats=["%Y-%m-%d"])
#####
import pyinputplus as pyip
datetime_input = pyip.inputDatetime(prompt="Enter a datetime (YYYY-MM-DD HH:MM): ", formats=["%Y-%m-%d %H:%M"])
#####
import pyinputplus as pyip
day_of_week = pyip.inputDayOfWeek(prompt="Enter a day of the week: ")
#####
import pyinputplus as pyip
day_of_month = pyip.inputDayOfMonth(prompt="Enter a day of the month: ",year=2001,month=2)  #try 29
#####
import pyinputplus as pyip
email = pyip.inputEmail(prompt="Enter your email address: ")
#####
import pyinputplus as pyip
filename = pyip.inputFilename(prompt="Enter a filename: ")
# #####
# import pyinputplus as pyip
# filepath = pyip.inputFilepath(prompt="Enter a filepath: ", mustExist=True)
# #####
import pyinputplus as pyip
price = pyip.inputFloat(prompt="Enter the price: ")
#####
import pyinputplus as pyip
age = pyip.inputInt(prompt="Enter your age: ")
#####
import pyinputplus as pyip
choice = pyip.inputMenu(["Option 1", "Option 2", "Option 3"], numbered=True, prompt="Select an option: ")
#####
import pyinputplus as pyip
ip_address = pyip.inputIP(prompt="Enter an IP address: ")
#####
import pyinputplus as pyip
month = pyip.inputMonth(prompt="Enter a month: ")
#####
import pyinputplus as pyip
name = pyip.inputStr(prompt="Enter your name: ")
#####
import pyinputplus as pyip
num = pyip.inputNum(prompt="Enter a number between 1 and 10: ", min=1, max=10)
#####
import pyinputplus as pyip
password = pyip.inputPassword("Enter your password: ")
print("Password set successfully!")
#####
import pyinputplus as pyip
phone_number = pyip.inputPhone("Enter your phone number: ")
print("Phone number:", phone_number)

### OR
import pyinputplus as pyip
# Define a custom validation function for a phone number pattern
def phone_number_pattern(value):
    import re
    pattern = r'^\d{3}-\d{3}-\d{4}$'  # Example pattern: ###-###-####
    if not re.match(pattern, value):
        raise ValueError("Invalid phone number format. Please use the format ###-###-####.")
    return value

# Use the custom validation function with inputPhone
phone_number = pyip.inputCustom(phone_number_pattern, prompt="Enter your phone number (###-###-####): ")
print("Phone number:", phone_number)
#####
# Function to validate an email address
import pyinputplus as pyip
def is_valid_email(email):
    import re
    email_regex = r'^[\w\.-]+@[\w\.-]+$'
    return re.match(email_regex, email) is not None

# Prompt the user for an email address and validate it using PyInputPlus
email = pyip.inputCustom(is_valid_email, prompt="Please enter your email address: ", blockRegexes=[r'.*\.edu$'], allowRegexes=[r'example\.com$'])

print(f"Thank you! You entered a valid email address: {email}")
#####
import pyinputplus as pyip
pattern = pyip.inputRegex("Enter a string matching 'abc': ", blockRegexes=r'a|b|e', allowRegexes=r'zxc')
print("Input:", pattern)
#####
import pyinputplus as pyip
text = pyip.inputStr("Enter some text: ")
print("You entered:", text)
#####
import pyinputplus as pyip
time = pyip.inputTime("Enter a time (HH:MM): ",formats=["%H:%M:%S"])
print("Time:", time)

#####
import pyinputplus as pyip
url = pyip.inputURL("Enter a URL: ")
print("URL:", url)
#####
import pyinputplus as pyip
state = pyip.inputUSState("Enter a U.S. state abbreviation: ")
print("State:", state)
#####
import pyinputplus as pyip
response = pyip.inputYesNo("Do you want to continue? (yes/no): ")
if response == 'yes':
    print("Continuing...")
else:
    print("Exiting.")
