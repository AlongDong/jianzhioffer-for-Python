
from  linkTableDelete import LinkNode

class Stack:
    def __init__(self):
        self.list=list()

    def push(self,element):
        self.list.append(element)

    def gettop(self):
            return self.list[-1] 

    def pop(self):
            self.list.pop()

def reversePrintLinkNode(head):
    stack=Stack()
    addnumber=0
    while head!=None:
        stack.push(head)
        addnumber+=1
        head=head.next
    while addnumber!=0:
        element=stack.gettop()
        print(element.value)
        addnumber-=1
        stack.pop()


a=LinkNode(1)
b=LinkNode(2)
c=LinkNode(3)
a.next=b
b.next=c
reversePrintLinkNode(a)