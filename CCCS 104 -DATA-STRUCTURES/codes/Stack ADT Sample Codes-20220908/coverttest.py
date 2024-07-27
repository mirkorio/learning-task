def fibonacci(x):
 a = 0 #first number
 b = 1 #second number

 if x <= 1:
  return x
 
 else:
  for x in range(1,x):
    c = a + b
    a = b
    b = c
    return b

print(fibonacci(4))