class Node:
    def __init__(self, value,stored_data=None, left=None, right= None, parent=None):
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent
        self.height=1
        self.stored_data=stored_data
    def isNotLeaf(self):
        if (self.left==None and self.right == None):
            return False
        return True