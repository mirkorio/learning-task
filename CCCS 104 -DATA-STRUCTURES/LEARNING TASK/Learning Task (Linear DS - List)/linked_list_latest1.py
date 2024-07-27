#Python program that will implement a List Data Structure using Linked List and menu
#define class node
class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

  def print(self):
    pass

    
#define class
class LinkedList:
  def __init__(self):
    self.head=None

  # Insert At Start
  def push_front(self,data):
    self.head=Node(data,self.head)

  # Insert At End
  def push_back(self,data):
    i=self.head
    if i:
      while i.next:
        i=i.next
      i.next=Node(data,i.next)
    else:
      self.head=Node(data,self.head)     

  #Insert At Position
  def push_at(self,index,data):
    i=self.head
    if i and index>0:
      j=0
      while i.next and j<index-1:
        j+=1
        i=i.next
      i.next=Node(data,i.next)
    else:
      self.head=Node(data,self.head)     

  #Delete At End
  def pop_back(self):
    i=self.head
    if i:
      while i.next:
        j=i
        i=i.next
      j.next=i.next
    return i    

  #Delete At Position
  def pop_at(self,index):
    i=self.head
    if i:
      if index>0:
        k=0
        while i.next and k<index:
          k+=1
          j=i
          i=i.next
        j.next=i.next
      elif index==0:
        self.head=self.head.next
    return i
  
  #Delete At Start
  def pop_front(self):
    node=self.head
    self.head=self.head.next
    return node
    
  #Display Number At Position
  def peek_at(self,index):
    i=self.head
    if i and index>0:
        j=0
        while i.next and j<index:
          j+=1
          i=i.next
    return i
    
  #Search Number  
  def search(self,data):
    i=self.head
    j=-1
    k=0
    while i:
      if i.data==data:
        j=k
        break
      k+=1
      i=i.next
    return j

  # Display items of the List
  def print(self):
    i=self.head
    print('head',end='->')
    while i:
      print(i.data,end='->')
      i=i.next
    print('None')


#define class
class LinkedListSystem:
  def __init__(self):
    self.linked_list=LinkedList()

  #define menu
  def main_menu(self):
    quit=False
    while not quit:

     # display all the choices in the menu
      print(
        '\nLinkedList Main Menu:\n'+
        '[1] Insert at Start\n'+      
        '[2] Insert at End\n'+      
        '[3] Insert at Position\n'+      
        '[4] Delete at Start\n'+      
        '[5] Delete at End\n'+      
        '[6] Delete at Position\n'+      
        '[7] Delete Number\n'+      
        '[8] Search Number\n'+        
        '[9] Display Number At Position\n'+      
        '[10] Display Linked List\n'+      
        '[0] Exit\n\n'
      )

     # ask for the user input
      choice=int(input('Enter choice: '))

      #if else statement that assigns function to the menu choices
      if choice==0:
        quit=True
        continue
      elif choice==1:
        self.insert_at_start()
      elif choice==2:
        self.insert_at_end()
      elif choice==3:
        self.insert_at_position()
      elif choice==4:
        self.delete_at_start()
      elif choice==5:
        self.delete_at_end()
      elif choice==6:
        self.delete_at_position()
      elif choice==7:
        self.delete_number()
      elif choice==8:
        self.search_number()
      elif choice==9:
        self.display_number_at_position()
      elif choice==10:
        self.print_linked_list()
      
    print('Thank you!')

  #function of choice 1
  def insert_at_start(self):
    data=int(input('Enter integer to insert: '))
    self.linked_list.push_front(data)
    print('Data is inserted at beginning')

  #function of choice 2
  def insert_at_end(self):
    data=int(input('Enter integer to insert: '))
    self.linked_list.push_back(data)
    print('Data Inserted at end')
    
  #function of choice 3
  def insert_at_position(self):
    data=int(input('Enter integer to insert: '))
    index=int(input('Insert at position: '))

    self.linked_list.push_at(index,data)

    print('Data Inserted at position',index)

  #function of choice 4
  def delete_at_start(self):
    print('Removed value from beginning: ',self.linked_list.pop_front().data)
    
  #function of choice 5
  def delete_at_end(self):
    print('Removed value at end: ',self.linked_list.pop_back().data)

  #function of choice 6  
  def delete_at_position(self):
    index=int(input('Remove value at position: '))
    self.linked_list.pop_at(index)
    print('Data removed  at',index)

  #function of choice 7
  def delete_number(self):
    data=int(input(' Enters the value of the number to be deleted: '))
    index=self.linked_list.pop_at(data)
    if index==-1: 
      print('Value',data,'“is not on the list and cannot be deleted.”')
    else:
      print('Value',data,'has been successfully deleted.')
      
  #function of choice 8
  def search_number(self):
    data=int(input('Enter value to search: '))
    index=self.linked_list.search(data)
    if index==-1: 
      print('Value',data,'not found.')
    else:
      print('Value',data,'is at position',index)

  #function of choice 9
  def display_number_at_position(self):
    index=int(input('Get value at position: '))
    print('Value at position',index,'is',self.linked_list.peek_at(index).data)

  #function of choice 10
  def print_linked_list(self):
    self.linked_list.print()


sys=LinkedListSystem()

sys.main_menu()