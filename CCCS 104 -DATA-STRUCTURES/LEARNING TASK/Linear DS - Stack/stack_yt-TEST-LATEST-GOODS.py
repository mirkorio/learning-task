def create_stack():
    stack = []
    return stack

def create_stack2():  
    stack2 = []
    return stack2

def create_stack3():
    stack3 = []
    return stack3

def push(stack, item):
    stack.append(item)

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
 if (check_empty(stack)):
    return 'stack is empty'
 return stack.pop()

def equalStacks(user_input1, user_input2, user_input3):

    stack = sum(user_input1)
    stack2 = sum(user_input2)
    stack3 = sum(user_input3)

    while True:
        minheight = min(stack,stack2,stack3)

        if minheight == 0:
             print('Stack heights will never be equal.')
             print('\n----------------------------------------------''\n')

        if minheight<stack:
            stack-= user_input1.pop()  
        if minheight<stack2:
            stack2-= user_input2.pop()    
        if minheight<stack3:
            stack3-= user_input3.pop()     

        if stack == stack2 == stack3:
            return stack

while True:
    user_input1 = list(map(int, input("\nEnter elements of Stack 1: ").split()))


    user_input2 = list(map(int, input("Enter elements of Stack 2: ").split()))


    user_input3 = list(map(int, input("Enter elements of Stack 3: ").split()))

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

 
    print('Stack 1 total height:', sum(stack))
    print('Stack 2 total height:', sum(stack2))
    print('Stack 3 total height:', sum(stack3))


    print('\n----------------------------------------------''\n')

    print('All stack are equal at Height: ',equalStacks(user_input1,user_input2,user_input3))
    user_input1 = list(map, print('Stack 1: ',user_input1).split())
    user_input2 = list(map,print('Stack 2: ',user_input2).split())
    user_input3 = list(map,print('Stack 3: ',user_input3).split())

    print('\n')
    print('----------------------------------------------''\n')


    check = input("Continue? Y or N? ")
    if check.upper() == 'Y':
        continue
    print("Thank You!")
    break

    