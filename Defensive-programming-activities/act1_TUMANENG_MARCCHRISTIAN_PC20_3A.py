#TUMANENG,MARC CHRISTIAN D. - BSCS3A | DEFENSIVE PROGRAMMING
#Fibonacci sequence

#recursive approach
def func1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func1(n - 1) + func1(n - 2)

#Dynamic Programming
def func2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

#Using While Loop
def func3(n):
    f = [0, 1]
    i = 2
    while i <= n:
        next_fib = f[i - 1] + f[i - 2]
        f.append(next_fib)
        i += 1
    return f[n]

#main function
if __name__ == "__main__":
    print("+----------------------------------------------------------------------------------------+")
    print("| Fibonacci numbers:", end=' ')
    print(', '.join(str(func1(n)) for n in range(1, 18)), end=" |")
    print("\n| The nth position:", end=' ')
    print(', '.join(str(i) for i in range(1, 18)) + "            |")
    print("+----------------------------------------------------------------------------------------+")
    print(" ")

    #accept and validate input
    while True:
        try:
            n = int(input("Error: Nth position must be a positive integer: "))
            if n <= 0 or n > 17:
                print("Error: Please enter a positive number between 1 and 17.")
                continue
            break
        except ValueError:
            print("Error: Invalid input. Please enter a valid positive number.")

    #display output
    print("Using 1st Approach:", func1(n))
    print("Using 2nd Approach:", func2(n))
    print("Using 3rd Approach:", func3(n))
    print(" ")

#outfile
file1=open(r'd:\CSPC_BSCS3A_1ST-SEM\DEFENSIVE PROGRAMMING\\act1_out.out','w')
file1.write('1\n')
for i in range(2,n+1):
    file1.write(str(func1(i))+'\n')
file1.close()
