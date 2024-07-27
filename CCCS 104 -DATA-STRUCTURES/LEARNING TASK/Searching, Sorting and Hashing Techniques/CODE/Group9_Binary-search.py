# BSCS2A - Group 9
# Python program to get the total number of qualified teams for the playoffs
 
import math
 
# Define playoffs as function
def playoffs():
    # Get the number of test cases from the user
    test_case = int(input("Enter the Number of Test Cases: \n"))
 
    # While loop to run how many test cases were given
    while test_case > 0:
        test_case -= 1
 
        # Take the inputs for the N, M, K, B separated by space
        N, M, K, B = map(int, input().split())
        list1 = list(map(int, input().split()))
 
        # Sort the list for it to be in order which is a must in Binary search
        list1.sort(reverse = True)
 
        LB = B-1
        UB = N
        while UB - LB > 1:
            mid = (UB + LB) // 2
            a = M * (K - (B-1) - (N-1))
            for i in range(B-1, mid):
                if list1[i] > list1[mid] + M:
                    a = math.inf
                else:
                    a -= list1[mid] + M - list1[i]      
                if a > 0:
                    UB = mid
                else:
                    LB = mid
       
        # Display the number of qualified teams for the playoffs
        print("\nTeams that can make it into the playoffs: ", LB + 1)
        print("")
 
 
# function call
playoffs()
