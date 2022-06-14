class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        self.parent=None


def getNextTreeNode(pNode):
    pNext=None
    if pNode.right!=None:
        pright=pNode.right
        while pright.left!=None:   #
            pright=pright.left
        pNext=pright
    elif pNode.parent!=None:
        pCurrent=pNode
        pParent=pNode.parent
        while pParent!=None and pCurrent==pParent.right:
            pCurrent=pParent
            pParent=pParent.parent
            if pParent==None:
                pNext=None
        pNext=pParent

    return pNext


a=BinaryTree("a")
b=BinaryTree("b")
c=BinaryTree("c")
d=BinaryTree("d")
e=BinaryTree("e")
f=BinaryTree("f")
g=BinaryTree("g")
h=BinaryTree("h")
i=BinaryTree("i")
a.left=b
a.right=c
b.left=d
b.right=e
b.parent=a
c.left=f
c.right=g
c.parent=a
e.parent=b
d.parent=b
e.left=h
e.right=i
e.parent=b
h.parent=e
i.parent=e
f.parent=c
g.parent=c

ans=getNextTreeNode(c)
print(ans.value)


