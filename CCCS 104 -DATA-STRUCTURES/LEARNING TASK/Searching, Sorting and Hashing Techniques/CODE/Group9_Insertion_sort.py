# BSCS2A - Group 9
# Python program that implements Insertion Sort algorithm
 
# Define the function for insertion sort with the parameters needed
import time #import time for getting the execution time

def insertion_sort(array):
 
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
       
        """ Compare key with each element on the left of it 
            until an element smaller than it is found"""
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
       
        # Place key at after the element just smaller than it.
        array[j + 1] = key
 

# Get the Exam Scores
exam_scores = list(map(int, input("Enter the Exam Scores: \n").split()))

#get the start time
st = time.time()

insertion_sort(exam_scores)

#Display the sorted exam scores in an ascending order
print('\nSorted Exam Scores in Ascending Order:')
print(exam_scores)

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
