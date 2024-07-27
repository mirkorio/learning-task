#BSCS 2A - GROUP 9

#define function
def recursion(n):
  #if else statement
  if(n >= 0): 
    result = n+ recursion(n - 1)
    print(result)
  else:
    result = 0
  return result
#prints the output
print("OUTPUT")
recursion(5)