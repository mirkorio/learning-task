
class Queue1:

    def create_queue1():
        q1 = []
        return q1
    
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

    print('\n----------------------------------------------''\n')    

    user_input1 = list(map(int, input("\nQueue 1: ").split()))


    print('\n----------------------------------------------''\n')

    q1 = create_queue1()
    for i in (user_input1):
        enqueue(q1, (i))
    
    q = Queue1()
    q.display()
  
    
    

    

    