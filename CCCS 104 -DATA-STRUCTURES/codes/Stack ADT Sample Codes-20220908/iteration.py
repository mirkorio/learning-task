#BSCS 2A - GROUP 9

#define function
def iteration(n):
  sum=0
  #while loop statement
  while n:
    sum+=n
    n-=1
  return sum
#prints the output 
print("OUTPUT")
for i in range(0,6):
   print(iteration(i))