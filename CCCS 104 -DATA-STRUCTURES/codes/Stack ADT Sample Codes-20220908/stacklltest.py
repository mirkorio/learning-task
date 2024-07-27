# stack using singly link list
from multiprocessing import Value
from os import remove
from platform import node


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:

    def _init_(self):
        self.value = Node('head')
        self.next = 0



    def push( self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size +=1

    def pop(self):
        if self.isEmpty():
            raise Exception('Popping from an empty stack')
            
        remove.head.next = self.head.next.next
        self.size -=1
        return remove.value