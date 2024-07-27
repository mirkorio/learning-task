# Queue implementation using Array in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item) #add element at the end

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0) #removes the first element (index 0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

# A queue implemented using a array
q = Queue()
#enqueue #s 1-5
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
#display current queue
print("Current Queue: ", end =" ")
q.display()
#remove first element
q.dequeue()
#display current queue
print("After removing an element: ", end =" ")
q.display()