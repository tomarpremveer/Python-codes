class Node:
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
def isValidBST(root,res):
    if  not root:
        return res
    isValidBST(root.left,res)
    res.append(root.val)
    isValidBST(root.right,res)
    return res

def search(root,val):
    if root is None:
        return
    if root.val==val:
        return root
    elif val < root.val:
        return search(root.left,val)
    else:
        return search(root.right,val)
    return None

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

def inor(root):
    if root:
        inor(root.left)
        print(root.val,end=" ")
        inor(root.right)
first=prev=last=midlle=None
def correctBstUtil(root):
    global first,prev,last,middle
    if root is not None:
        correctBstUtil(root.left)

        if (prev is not None and prev.val> root.val):
            if first is None:
                first=prev
                middle=root
            else:
                last=root
        prev=root
        correctBstUtil(root.right)
def correctBst(root):
    global first,prev,last,middle
    correctBstUtil(root)

    if first is not None and last is not None:
        temp=first.val
        first.val=last.val
        last.val=temp
    elif first is not None and middle is not None:
        temp=first.val
        first.val=middle.val
        middle.val=temp
def isOp(c):
    if c=="+" or c=="-" or c=="*" or c=="/" or c=="^":
        return True
    return False
def constructTree(postfix):
    stack=[]

    for char in postfix:

        if not isOp(char):
            t=Node(char)
            stack.append(t)
        else:
            t=Node(char)
            t1=stack.pop()
            t2=stack.pop()

            t.right=t1
            t.left=t2
            stack.append(t)
    t=stack.pop()
    return t




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
    root=Node(4)
    root.left=Node(2)
    root.left.left=Node(1)
    root.left.right=Node(3)
    root.right=Node(7)
    #root.right.left=Node(7)
    #root.right.right=Node(12)
    #print(countrtree(root,5,0))
    #postfix = "ab+ef*g*-"
    #root=constructTree(postfix)
    #inor(root)
    print(search(root,2).val)


