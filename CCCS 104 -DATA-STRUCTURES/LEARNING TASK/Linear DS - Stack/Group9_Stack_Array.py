# BSCS 2A-GROUP 9
# Python program to demonstrate stack implementation using an array.

# Creating the array for the 1st stack 
def create_stack():
    stack = []
    return stack

# Creating the array for the 2nd stack
def create_stack2():  
    stack2 = []
    return stack2

# Creating the array for the 3rd stack
def create_stack3():
    stack3 = []
    return stack3

# Add items into the stacks
def push(stack, item):
    stack.append(item)

# Checkthe length of the stack is not empty
def check_empty(stack):
    return len(stack) == 0

# Remove an element from the stack
def pop(stack):
 if (check_empty(stack)):
    return 'stack is empty'
 return stack.pop()

# Balancing the stacks & determine which height they are all equal at
def equalStacks(user_input1, user_input2, user_input3):

    stack = sum(user_input1)
    stack2 = sum(user_input2)
    stack3 = sum(user_input3)

    while True:
        minheight = min(stack,stack2,stack3)

        # Determine if balancing of the stacks is possible
        if minheight == 0:
             print('Stack heights will never be equal.')
             print('\n----------------------------------------------''\n')

        # Pop an element from the stack 
        if minheight<stack:
            stack-= user_input1.pop()  
        if minheight<stack2:
            stack2-= user_input2.pop()    
        if minheight<stack3:
            stack3-= user_input3.pop()     

        # Return the height of the stacks they are all equal at
        if stack == stack2 == stack3:
            return stack


# While loop for starting the program again
while True:
    # Ask for user inputs separated by space for the elements of stacks
    user_input1 = list(map(int, input("Enter elements of Stack 1: ").split()))


    user_input2 = list(map(int, input("Enter elements of Stack 2: ").split()))


    user_input3 = list(map(int, input("Enter elements of Stack 3: ").split()))

    # For loop to push each of the input element into the stacks
    stack = create_stack()
    for i in (user_input1):
        push(stack, (i))

    stack2 = create_stack2()
    for i in (user_input2):
        push(stack2, (i))

    stack3 = create_stack3()
    for i in (user_input3):
        push(stack3, (i))


    
    print('\n----------------------------------------------''\n')

    # Print the sums or the heights of the stacks
    print('Stack 1 total height:', sum(stack))
    print('Stack 2 total height:', sum(stack2))
    print('Stack 3 total height:', sum(stack3))


    print('\n----------------------------------------------''\n')
    # Print the stacks after balancing and the height they are all equal at
    print('All stacks are equal at Height: ',equalStacks(user_input1,user_input2,user_input3))
    print('Stack 1: ',user_input1)
    print('Stack 2: ',user_input2)
    print('Stack 3: ',user_input3)

    print('\n----------------------------------------------''\n')

    # Start again or terminate the program
    check = input("Continue? Y or N? ")
    print('\n----------------------------------------------''\n')
    if check.upper() == 'Y':
        continue
    print("Thank You!")
    break
