class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, v):
        new_node = Node(v)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        return self.head

    def reverse(self):
        temp = self.head
        p = None
        n = None
        while temp is not None:
            n = temp.next
            temp.next = p
            p = temp
            temp = n
        self.head=p
    def printlist(self):
        t = self.head
        while t is not None:
            print(t.value, end=" ")
            t = t.next


if __name__ == "__main__":
    arr=[9,9,9,9]
    #arr = list(map(int, input().split(' ')))
    l = Linkedlist()
    for i in arr:
        l.insert(i)
    l.add()
    l.printlist()

