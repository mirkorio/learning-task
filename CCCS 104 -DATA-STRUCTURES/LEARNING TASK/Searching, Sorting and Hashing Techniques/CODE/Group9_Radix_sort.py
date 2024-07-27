# Python program that implements Radix Sort algorithm
# Using counting sort to sort the elements in the basis of significant places
import time #import time for getting the execution time

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
 
    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
 
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
 
    for i in range(0, size):
        array[i] = output[i]
 
 
# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)
 
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
 

# Get the Exam Scores
exam_scores = list(map(int, input("Enter the Exam Scores: \n").split()))

# get the start time
st = time.time()

radixSort(exam_scores)
#Display the sorted exam scores in an ascending order
print('\nSorted Exam Scores in Ascending Order:')
print(exam_scores)

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
