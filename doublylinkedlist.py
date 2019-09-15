class Node:
	def __init__(self, value):
		self.next = None
		self.prev = None
		self.val = value


class dblLinkedList:
	def __init__(self):
		self.head = None

	def insertHead(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def printlist(self):
		temp = self.head

		while temp is not None:
			print(temp.val)
			temp = temp.next


if __name__ == "__main__":
	dbl = dblLinkedList()

	dbl.insertHead(3)
	dbl.insertHead(4)
	dbl.insertHead(5)
	dbl.printlist()
