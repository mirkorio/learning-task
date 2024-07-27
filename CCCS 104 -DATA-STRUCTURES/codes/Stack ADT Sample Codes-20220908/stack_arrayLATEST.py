
def create_stack1():
    stack = []
    return stack

def create_stack2():
    stack = []
    return stack

def create_stack3():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
 if (check_empty(stack)):
    return 'stack is empty'
 return stack.pop()

def equalStacks(user_input1, user_input2, user_input3):
   
    user_input1 = user_input1[::-1]
    user_input2 = user_input2[::-1]
    user_input3 = user_input3[::-1]

    sum1 = sum(user_input1)
    sum2 = sum(user_input2)
    sum3 = sum(user_input3)
    
    while True:
        minheight = min(sum1,sum2, sum3)

        if minheight == 0:
            return 0

        if minheight<sum1:
            sum1-= user_input1.pop()  
        if minheight<sum2:
            sum1-= user_input2.pop()    
        if minheight<sum3:
            sum1-= user_input3.pop()     

        if sum1 == sum2 == sum3:
            return sum1       
  
print('\n')
print('----------------------------------------------''\n')

stack = create_stack1()
user_input1 = list(map(int, input("Enter elements of Stack 1: ").split()))
push(stack, user_input1)



stack = create_stack2()
user_input2 = list(map(int, input("Enter elements of Stack 2: ").split()))
push(stack, user_input2)



stack = create_stack3()
user_input3 = list(map(int, input("Enter elements of Stack 3: ").split()))
push(stack, user_input3)



print('\n')
print('----------------------------------------------''\n')

 
print('Stack 1 total height:', sum( user_input1))
print('Stack 2 total height:', sum( user_input2))
print('Stack 3 total height:', sum( user_input3))

print('\n')
print('----------------------------------------------''\n')

print('All stack are equal at Height: ')
print('Stack 1: ')
print('Stack 2: ')
print('Stack 3: ')

print('\n')
print('----------------------------------------------''\n')
 

while True:
   answer = input('Continue? Y or N?')
   if answer.upper().startswith("Y"):
      continue
   elif answer.upper().startswith("N"):
      print("Thank you!")
      exit() 