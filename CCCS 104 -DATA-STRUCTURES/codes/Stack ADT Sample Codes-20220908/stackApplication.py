def create_stack():
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

    
print('\n')
print('----------------------------------------------''\n')

stack = create_stack()
user_input = input("Enter elements of Stack 1: ")
myArr = user_input.split(" ")
push(stack, user_input)
myArr = [int(i) for i in myArr]


print(type(stack))


for i in range(list):
        sum=0
        sum = sum + list[i]

print('\n')
print('----------------------------------------------''\n')

 
print('Stack 1 total height:' +str(sum))     

   

