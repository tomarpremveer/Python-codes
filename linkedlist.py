class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, n):
        new_node = Node(n)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printNode(self):
        temp=self.head
        while temp is not None:
            print(temp.value,end="->")
            temp = temp.next
        print(None)

    def add(self):
        self.reverse()
        t = self.head
        carry = 1
        while t is not None:
            t.value += carry
            if t.value >= 10:
                t.value = 0
                carry = 1
            else:
                carry = 0
            t = t.next
        self.reverse()
        if carry:
            n = Node(carry)
            n.next = self.head
            self.head = n
    def printMiddle(self):
        n1=self.head
        n2=self.head
        while n2 is not None and n2.next is not None:
            n1= n1.next
            n2=n2.next.next
        print(n1.value)
    def countNodes(self):
        count=0
        t=self.head
        while t is not None:
            count+=1
            t=t.next
        return count
    def reverse(self,h):
        temp = h
        p = None
        n = None
        while temp is not None:
            n = temp.next
            temp.next = p
            p = temp
            temp = n
        h=p
        return h
    def printlist(self):
        t = self.head
        while t is not None:
            print(t.value, end=" ")
            t = t.next
    def sortedMerge(self,a,b):
        result=None
        if a is None:
            return b
        if b is None:
            return a
        if a.value <= b.value:
            result=Node(a.value)
            result.next=self.sortedMerge(a.next,b)
        else:
            result=Node(b.value)
            result.next=self.sortedMerge(a,b.next)
        return result
    def getmiddle(self,h):
        if h is None:
            return h
        slow=h
        fast=h
        while fast.next.next is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSort(self,h):
        if h is None or h.next is None:
            return h
        mid=self.getmiddle(h)
        nextofmid=mid.next
        mid.next=None
        left=self.mergeSort(h)
        right=self.mergeSort(nextofmid)
        sortedlist=self.sortedMerge(left,right)
        return sortedlist
    def arrange(self,h):
        slow = h
        fast = h
        while fast.next.next is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        node2=slow.next
        node1=h
        slow.next=None
        node2=self.reverse(node2)
        node=Node(0)
        curr=node
        while node1 is not None or node2 is not None:
            if node1 is not None:
                curr.next=node1
                curr=curr.next
                node1=node1.next
            if node2 is not None:
                curr.next=node2
                curr=curr.next
                node2=node2.next
        h=node.next
        return h
#code for transforming linked list to BST

def sortedBst(head):
    n=head.countNodes()
    return  sortedBstRecur(head,n)
def sortedBstRecur(head,n):
    if n<=0:
        return None
    left=sortedBstRecur(head,n//2)

    root=Node(head.value)
    root.left=left
    head=head.next
    root.right=sortedBstRecur(head,n-n//2-1)
    return root
#code ends here

if __name__ == "__main__":
    l = LinkedList()
    #l.addHead(5)
    l.addHead(4)
    l.addHead(3)
    l.addHead(7)
    l.addHead(1)
    l.printlist()
    print()
    l.head=l.arrange(l.head)
    l.printlist()
