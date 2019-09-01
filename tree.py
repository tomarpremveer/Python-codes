class Node:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.value=v

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
def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)
def mirror(root):
    if root==None:
        return
    else:
        node=root
        mirror(root.left)
        mirror(root.right)
        temp=node.left
        node.left=node.right
        node.right=temp
def lca(root,n1,n2):
    if root==None:
        return
    if root.value< n1 and root.value < n2:
        return lca(root.right ,n1,n2)
    if root.value > n1 and root.value > n2:
        return lca(root.left,n1,n2)
    return root
def inorderit(root):
    stack=[]
    curr=root
    while True:
        if curr is not None:
            stack.append(curr)
            curr=curr.left
        elif stack:
            curr=stack.pop()
            print(curr.value ,end =" ")
            curr=curr.right
        else:
            break
def preOrderRec(root):
    if root:
        print(root.value,end =" ")
        preOrderRec(root.left)
        preOrderRec(root.right)
def preOrder(root):
    curr=root
    stack=[]
    while True:
        if curr is not None:
            print(curr.value ,end =" ")
            stack.append(curr)
            curr=curr.left
        elif stack :
            curr=stack.pop()
            curr=curr.right
        else:
            break


if __name__=="__main__":
    root=None
    root=insert(root,8)
    insert(root,3)
    insert(root, 4)
    insert(root,5)
    insert(root,7)
    insert(root,1)
    insert(root,6)
    insert(root,9)
    preOrderRec(root)
    print("iterative preorder traversal")
    preOrder(root)


