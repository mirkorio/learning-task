
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Stack:

	
	def __init__(self):
		self.head = Node("head")
		self.size = 0

	def __str__(self):
		cur = self.head.next
		out = ""
		while cur:
			out += str(cur.value) + "->"
			cur = cur.next
		return out[:-3]

	
	def isEmpty(self):
		return self.size == 0

	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Popping from an empty stack")
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value


print('\n')
print('----------------------------------------------''\n')

int(input('Enter elements of Stack: '))