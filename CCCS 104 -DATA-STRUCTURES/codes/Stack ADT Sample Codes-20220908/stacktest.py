#stack using array
def create_stack():
    stack=[]
    return stack

def push(stack, item):
    stack.append(item)
    print('pushed item: '+ item)

def check_empty(stack):
    return len(stack) == 0

def pop(stack):
 if (check_empty(stack)):
    return 'stack is empty'
 return stack.pop()


stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))

print("stack after pushing an element: " + str(stack))

print("popped item:" + pop(stack))
print("stack after popping element: " + str(stack))
print("stack after popping an element: " + str(stack))

push(stack, str(5))
print("stack after pushing an element: " + str(stack))