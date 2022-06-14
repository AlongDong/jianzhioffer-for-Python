class LinkNode:
    def __init__(self,value):
        self.value=value
        self.next=None

def AddtoTail(head,value):
    head=a
    if not head:
        head=LinkNode(value)
    else:
        while head.next!=None:
            head=head.next

        head.next=LinkNode(value)
def deleteNode(linkhead,value):
    if not linkhead:
        return False
    if linkhead.value==value and linkhead.next==None:
        linkhead.value=None

    elif linkhead.value==value and linkhead.next!=None:
        linkhead=linkhead.next

    while linkhead.next!=None and linkhead.next.value!=value:
            linkhead=linkhead.next
    if linkhead.next==None:
        return False
    elif linkhead.next!=None and linkhead.next.value==value:
        linkhead.next=linkhead.next.next


if __name__=='__main__':

    a=LinkNode(1)
    b=LinkNode(2)
    c=LinkNode(3)
    a.next=b
    b.next=c
    deleteNode(a,2)
    print(a.next.value)






