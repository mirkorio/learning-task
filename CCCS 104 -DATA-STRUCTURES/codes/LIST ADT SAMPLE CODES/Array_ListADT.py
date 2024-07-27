# Creation of Array
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
 
# printing original array
print ("The new created int array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array
print ("The new created float array is : ", end =" ")
for i in range (0, len(b)):
    print (b[i], end =" ")
    
print("\nThird element of array b: ", b[2])

#removing an element in an array
a.remove(2)

#adding an element at the end of an array
a.append(4)

# printing new array
print ("The updated in array is : ", end =" ")
#for i in a:
 #   print (i)
    
for i in range (0, len(a)):
    print (a[i], end =" ")