# Queue implementation using Linked List in Python

class Node:
  # constructor
    def __init__(self, data): 
        self.data = data
        self.next = None
    
# A Linked List class with a single head node
class QueueLL:
    def __init__(self):  
        self.head = None
    # insert at the tail of the linked list
    def enqueue(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else: #for the first element/head
            self.head = newNode
    # delete an element from the head of the linked list
    def dequeue(self):
        temp = self.head 
        if (temp is not None):
            element = temp.data
            self.head = temp.next
            temp = None
            return element
    # display an element from the tail of the linked list
    def peek(self):
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            return current.data
    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data, end =" ")
            current = current.next

# A queue implemented using a linked list
Queue = QueueLL()
# Enqueue 2
Queue.enqueue(2)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 3
Queue.enqueue(3)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 4
Queue.enqueue(4)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 5
Queue.enqueue(5)
# Display element at the tail
print("Element at the tail:", Queue.peek())


#display queue
print("Current Queue:", end =" ")
Queue.printLL()

# Dequeue elements
print("\nElement dequeued:", Queue.dequeue())
print("Element dequeued:", Queue.dequeue())

#display queue
print("Current Queue:", end =" ")
Queue.printLL()