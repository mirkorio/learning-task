#Program for LinkedList Creation
#defined class Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#define Linked List
class SampLinkedList:
    def __init__(self):
        self.head = None

    #Function to add node at the beginning
    def Atbegining(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode
        
    # Function to add node in the middle
    def Inbetween(self,mid,newdata):
        if mid is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.next = mid.next
        mid.next = NewNode
        
    # Function to add newnode at the end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next=NewNode

    # Function to remove node
    def RemoveNode(self, removeNode):
        ptr = self.head
         
        if (ptr is not None):
            #remove at the head
            if (ptr.data == removeNode):
                self.head = ptr.next
                ptr = None
                return
        #remove until val is found
        while (ptr is not None):
            if ptr.data == removeNode:
                break
            prev = ptr
            ptr = ptr.next
        
        #remove element not found
        if (ptr == None):
            return

        prev.next = ptr.next
        ptr = None

    # Print the linked list
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data)
            printval = printval.next

llist = SampLinkedList()
llist.head = Node("Thu")
llist.Atbegining("Wed")
llist.Atbegining("Mon")
llist.Atbegining("Sun")
llist.AtEnd("Fri")
llist.AtEnd("Sat")
llist.Inbetween(llist.head.next,"Tue")
llist.RemoveNode("Tue")
llist.LListprint()