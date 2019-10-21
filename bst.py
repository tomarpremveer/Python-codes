class Node:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.value=v

def countrtree(root,k,s):
    if root is None:
        return 0
    s+=root.value
    if root.left is not None:
        s+=root.left.value
    if root.right is not None:
        s+=root.right.value
    if s==k:
        return 1
    elif s > k:
        s=0
        return countrtree(root.left,k,s)+countrtree(root.right,k,s)
    else:
        return countrtree(root.left,k,0)+countrtree(root.right,k,0)



def insert(root,v):
    new_node=Node(v)
    if root == None:
        root=new_node
        return root
    else:
        curr=root
        parent=None
        while curr != None:
            parent=curr
            if curr.value <v:
                curr=curr.right
            else:
                curr=curr.left
        if parent==None:
            parent=new_node
        elif parent.value<v:
            parent.right=new_node
        else:
            parent.left=new_node


def levelordertraversal(root):
    if root is None:
        return
    queue=[]
    queue.append(root)
    while len(queue)> 0:
        print(queue[0].value,end=" ")
        node=queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


if __name__ == "__main__":
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right=Node(3)
    #root.right.left=Node(-4)
    #root.right.right=Node(7)
    #print(countrtree(root,5,0))
    print(levelordertraversal(root))

