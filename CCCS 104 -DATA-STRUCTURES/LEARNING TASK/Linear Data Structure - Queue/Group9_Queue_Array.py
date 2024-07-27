# GROUP 9
# Queue implementation using Array in Python


class Queue:

    def __init__(self):
        self.queue = []
        self.sum = 0

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)
        self.sum += item

     # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        self.sum -= self.queue[0]
        return self.queue.pop(0)

    # Display an element
    def display(self):
        print(self.queue)

    # Get the size of the queue
    def size(self):
        return len(self.queue)
    
    # Head pointer
    def head(self):
        return self.queue[0]
    
# Display all the queues and their elements
def printQueue(queue, queue2, queue3):
    print("Queue 1: ", end='')
    queue.display() if queue.size() != 0 else print("Empty")
    print("Queue 2: ", end='')
    queue2.display() if queue2.size() != 0 else print("Empty")
    print("Queue 3: ", end='')
    queue3.display() if queue3.size() != 0 else print("Empty")    

    print('\n----------------------------------------------''\n')



print('\n----------------------------------------------''\n')

# 3 queues implemented using an array
queue = Queue()
queue2 = Queue()
queue3 = Queue()
printQueue(queue, queue2, queue3)

# loop for starting the program again
while True:
    # menu
    print('[0] Exit')
    print('[1] Enqueue Workload')
    print('[2] Dequeue Workload')
    choice = int(input("Choice: "))

    # if the user selects 0, the program will end
    if choice == 0:
        print("Thank you!")
        print('\n----------------------------------------------''\n')
        break
    
    # if the user selects 1, the enqueue operation will be done to the queue with the least total work load
    elif choice == 1:
        print('\n----------------------------------------------''\n')
        workVal = int(input("Enter Value of Workload: "))
        if queue.sum <= queue2.sum and queue.sum <= queue3.sum:
            queue.enqueue(workVal)
        elif queue2.sum <= queue.sum and queue2.sum <= queue3.sum:
            queue2.enqueue(workVal)
        elif queue3.sum <= queue.sum and queue3.sum <= queue2.sum:
            queue3.enqueue(workVal)
        else:
            queue.enqueue(workVal)
        
    # if the user selects 2, the dequeue operation will be done to the queue with the lowest first element
    elif choice == 2:
        # Error message when trying to dequeue from an empty queue
        if queue.size() == 0 and queue2.size() == 0 and queue3.size() == 0:
            print("\nQueue Underflow!")
            input("Press any key to continue using the program...")
            print('\n----------------------------------------------''\n')
        
        # conditional statements to determine the queue which dequeue operation will be done
        elif queue.size() == 0:
            if queue3.size() == 0:
                queue2.dequeue()
                print('\n----------------------------------------------''\n')
                printQueue(queue, queue2, queue3)
                continue
            if queue2.size() == 0:
                queue3.dequeue()
                print('\n----------------------------------------------''\n')
                printQueue(queue, queue2, queue3)
                continue   
            if queue2.head() <= queue3.head():
                queue2.dequeue()
            else:
                queue3.dequeue()  
        elif queue.size() == 0:
            if queue2.size() == 0:
                queue3.dequeue        
        elif queue2.size() == 0:
            if queue3.size() == 0:
                queue.dequeue()
                print('\n----------------------------------------------''\n')
                printQueue(queue, queue2, queue3)
                continue 
            if queue.head() <= queue3.head():
                queue.dequeue()
            else:
                queue3.dequeue()  
        elif queue3.size() == 0:
            if queue.head() <= queue2.head():
                queue.dequeue()
            else:
                queue2.dequeue()       
        elif queue.head() <= queue2.head() and queue.head() <= queue3.head():
            queue.dequeue()
        elif queue2.head() <= queue.head() and queue2.head() <= queue3.head():
            queue2.dequeue()
        elif queue3.head() <= queue2.head() and queue3.head() <= queue.head():
            queue3.dequeue()
        else:
            queue.dequeue()

    print('\n----------------------------------------------''\n')
    # function call to print all the queues and their elements
    printQueue(queue, queue2, queue3)