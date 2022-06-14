from collections import deque

#创建节点
class Bitree:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parents=None

#插入
class BST:
    def __init__(self,li=None):
        self.root=None
        if li:
            for val in li:
                self.insert_no_src(val)
                

    def query(self,node,val):
        if not node:
            return None
        if node.data<val:
            return self.query(node.rchild,val)
        elif node.data>val:
            return self.query(node.lchild,val)
        else:
            return node

    def query_no_rec(self,val):
        p=self.root
        while p:
            if p.data<val:
                p=p.rchild
            elif p.data>val:
                p=p.lchild
            else:
                return p
        raise IndexError("没有该值")




    def insert_no_src(self,val):
        p=self.root
        if  not p:
            self.root=Bitree(val)
            return
        while p:
            if val < p.data:
                if  p.lchild:
                    p=p.lchild
                else:
                    p.lchild=Bitree(val)
                    p.lchild.parents=p
                    return
            elif val >p.data:
                if  p.rchild:
                    p=p.rchild
                else:
                    p.rchild=Bitree(val)
                    p.rchild.parents=p
                    return
            else:
                return

    def insert(self,node,val):
        if not node:
            node=Bitree(val)
        elif val<node.data:
            node.lchild=self.insert(node.lchild,val)
            node.lchild.parents=node
        elif val>node.data:
            node.rchild=self.insert(node.rchild,val)
            node.rchild.parents = node
        return node

    def pre_order(self,root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

    def level_order(self,root):
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            print(node.data, end=",")
            if node.lchild:
                q.append(node.lchild)
            if node.rchild:
                q.append(node.rchild)




tree=BST([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print(" ")
tree.in_order(tree.root)
print(" ")
tree.post_order(tree.root)
print(" ")
print(tree.query_no_rec(3).data)