#program that will implement a list data structures using linked list
#defined class Node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
#define Linked List
class SampLinkedList:
    def __init__(self):
        self.head = None        
