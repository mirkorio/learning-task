# BSCS2A - Group 9
# Python program to get the maximum number of thieves that can be caught 

# Define function and set parameters
def policemen_thieves(K, list1):

    # Counter
    counter = 0

    # Search and count the maximum number of thieves that can be caught using for loop
    for i in range(len(list1)):
        if list1[i] == 'T' and 'P' in list1:
            if i-K >= 0:
                front = list1[i-K:i]
            else:
                front = list1[0:i]
            if i+K+1 <= len(list1):
                end = list1[i+1:i+K+1]
            else:
                end = list1[i+1:len(list1)]      
            if 'P' in front:
                counter = counter + 1
                if i-K >= 0:
                    front_index = (i-K)+front.index('P')
                else:
                    front_index = front.index('P')
                list1[front_index] = 0
            elif 'P' in end:
                counter = counter + 1
                end_index = i+1+end.index('P')
                list1[end_index] = 0
                
    return counter

# Get user input for the number of test cases
test_case = int(input("Enter the Number of Test Cases: \n"))
for _ in range(test_case):
    # Get the number of N lines and the K units away based from the user input
    N, K = map(int, input().split())
    total = 0
    for _ in range(N):
        list1 = [ x for x in input().split() ]
        total = total + policemen_thieves(K, list1)

    # Display the total of the maximum number of thieves that can be caught
    print("\nMaximum thieves that can be caught: ", total)
    print("")