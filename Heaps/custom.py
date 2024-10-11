# You can add any additional function and class you want to implement in this file
class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class DoublyLinkedList:
    def __init__(self):
        self.header=Node()
        self.trailer=Node(left=self.header)
        self.header.right=self.trailer
        self.pointer=None
    def append(self,val):
        node= Node(val,self.trailer.left,self.trailer)
        node.left.right=node
        self.trailer.left=node
    def start_iterate(self):
        self.pointer=self.header.right
    def next(self):
        if (self.pointer!=self.trailer):
            send = self.pointer.val
            self.pointer=self.pointer.right
            return send
        return None

