from node import Node

def comp_1(node_1, node_2):
    return node_1.value<node_2.value
def inorder(node,inorder_list):
    
    if node==None:
        return
    inorder(node.left,inorder_list)
    inorder_list.append(node.value)
    inorder(node.right,inorder_list)
    return

class AVLTree:

    def __init__(self, compare_function=comp_1):
        self.root= None
        self.comparator = compare_function

    def get_height(self,node):
        if node==None:
            return 0
        else:
            return node.height
    
    def search(self, node):
        
        if (self.root==None):
            return None
        temp=self.root
        while(temp.isNotLeaf):
            if (temp.value==node.value):
                return temp
            elif (self.comparator(temp,node)):
                if (temp.right!=None):
                    temp=temp.right
                else:
                    return temp
            else:
                if (temp.left!=None):
                    temp=temp.left
                else:
                    return temp
        return temp
    
    def insert(self,node):
        if self.root==None:
            self.root=node
            return
        parent=self.search(node)
        if (parent.value==node.value):
            return
        if (self.comparator(parent,node)):
            parent.right=node
            node.parent=parent     
        else:
            node.parent=parent
            parent.left=node
        parent.height= 1+max(self.get_height(parent.left),self.get_height(parent.right))
        curr_node = parent.parent
        child  =  parent
        grandchild = node
        while (curr_node!=None):
            if (-2>=self.get_height(curr_node.left) - self.get_height(curr_node.right) or self.get_height(curr_node.left) - self.get_height(curr_node.right)>=2) :
                if(curr_node.left==child and child.left==grandchild):
                    self.restructure_left_left(curr_node)
                elif(curr_node.left==child and child.right==grandchild):
                    self.restructure_left_right(curr_node)
                elif(curr_node.right==child and child.right==grandchild):
                    self.restructure_right_right(curr_node)
                else:
                    self.restructure_right_left(curr_node)
            curr_node.height=1+max(self.get_height(curr_node.left) , self.get_height(curr_node.right))
            grandchild=child
            child=curr_node
            curr_node=curr_node.parent
        return
            
    def delete(self,node):
        if (self.root==None):
            return
        deleted_node=self.search(node)
        if (deleted_node.value!=node.value):
            return
        if (deleted_node==self.root):
            if (deleted_node.left==None and deleted_node.right==None):
                self.root=None
                del deleted_node
                return
            elif(deleted_node.left==None):
                deleted_node.right.parent=None
                self.root=deleted_node.right
                del deleted_node
                return
            elif(deleted_node.right==None):
                deleted_node.left.parent=None
                self.root=deleted_node.left
                del deleted_node
                return
        curr_node=None
        if (deleted_node.left==None and deleted_node.right==None):
            curr_node=deleted_node.parent
            if curr_node.right==deleted_node:
                curr_node.right=None
            else:
                curr_node.left=None
            del deleted_node
        elif(deleted_node.left==None):
            curr_node=deleted_node.parent
            T1= deleted_node.right
            T1.parent=curr_node
            if curr_node.right==deleted_node:
                curr_node.right=T1
            else:
                curr_node.left=T1
            del deleted_node
        elif(deleted_node.right==None):
            curr_node=deleted_node.parent
            T1= deleted_node.left
            T1.parent=curr_node
            if curr_node.right==deleted_node:
                curr_node.right=T1
            else:
                curr_node.left=T1
            del deleted_node
        else:
            temp=deleted_node.left
            while(temp.right!=None):
                temp=temp.right
            if (temp==deleted_node.left):
                temp.parent=deleted_node.parent
                temp.right=deleted_node.right
                temp.right.parent=temp
                if (deleted_node.parent==None):
                    self.root=temp
                    temp.parent=None
                else:
                    if deleted_node.parent.left==deleted_node:
                        deleted_node.parent.left=temp
                    else:
                        deleted_node.parent.right=temp
                curr_node=temp
                del deleted_node
            else:
                curr_node=temp.parent
                T1=temp.left
                if curr_node.left==temp:
                    curr_node.left=T1
                    if (T1!=None):
                        T1.parent=curr_node
                else:
                    curr_node.right=T1
                    if(T1!=None):
                        T1.parent=curr_node
                    
                if deleted_node==self.root:
                    self.root=temp
                    temp.parent=None
                else:
                    temp.parent=deleted_node.parent
                    if deleted_node.parent.left== deleted_node:
                        deleted_node.parent.left=temp
                    else:
                        deleted_node.parent.right=temp
                temp.left=deleted_node.left
                temp.right=deleted_node.right
                temp.left.parent=temp
                temp.right.parent=temp
                del deleted_node
        while (curr_node!=None):
            if (-2>=self.get_height(curr_node.left) - self.get_height(curr_node.right) or self.get_height(curr_node.left) - self.get_height(curr_node.right)>=2) :
                if (self.get_height(curr_node.left) > self.get_height(curr_node.right)):
                    if self.get_height(curr_node.left.left) >= self.get_height(curr_node.left.right):
                        self.restructure_left_left(curr_node)
                    else:
                        self.restructure_left_right(curr_node)
                else:
                    if self.get_height(curr_node.right.left) <= self.get_height(curr_node.right.right):
                        self.restructure_right_right(curr_node)
                    else:
                        self.restructure_right_left(curr_node)
            curr_node.height=1+max(self.get_height(curr_node.left) , self.get_height(curr_node.right))
            curr_node=curr_node.parent
        return
        
    def restructure_left_left(self,node):
        child = node.left
        T2=child.right
        if (node==self.root):
            self.root=child
            child.parent=None
            child.right=node
            node.parent=child
            if T2!=None:
                T2.parent=node
            node.left=T2
            child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
            node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
            return
        if node.parent.left==node:
            node.parent.left=child
        else:
            node.parent.right=child
        child.parent=node.parent
        child.right=node
        node.parent=child
        if T2!=None:
                T2.parent=node
        node.left=T2
        child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
        node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
        return
    
    def restructure_right_right(self,node):
        child = node.right
        T2=child.left
        if (node==self.root):
            self.root=child
            child.parent=None
            child.left=node
            node.parent=child
            if T2!=None:
                T2.parent=node
            node.right=T2
            child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
            node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
            return
        if node.parent.left==node:
            node.parent.left=child
        else:
            node.parent.right=child
        child.parent=node.parent
        child.left=node
        node.parent=child
        if T2!=None:
                T2.parent=node
        node.right=T2
        child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
        node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
        return
    
    def restructure_left_right(self,node):
        child=node.left
        grandchild=child.right
        T2=grandchild.left
        T3=grandchild.right
        if (node==self.root):
            self.root=grandchild
            grandchild.parent=None
            child.parent=node.parent= grandchild
            grandchild.left=child
            grandchild.right=node
            if T2!=None:
                T2.parent=child
            child.right=T2
            if T3!=None:
                T3.parent=node
            node.left=T3
            child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
            node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
            grandchild.height= 1 + max(self.get_height(grandchild.left),self.get_height(grandchild.right))
            return
       
        if node.parent.left==node:
            node.parent.left=grandchild
        else:
            node.parent.right=grandchild
        grandchild.parent=node.parent
        child.parent=node.parent= grandchild
        grandchild.left=child
        grandchild.right=node
        if T2!=None:
                T2.parent=child
        child.right=T2
        if T3!=None:
                T3.parent=node
        node.left=T3
        child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
        node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
        grandchild.height= 1 + max(self.get_height(grandchild.left),self.get_height(grandchild.right))
        return

    def restructure_right_left(self,node):
        child=node.right
        grandchild=child.left
        T2=grandchild.left
        T3=grandchild.right
        if (node==self.root):
            self.root=grandchild
            grandchild.parent=None
            child.parent=node.parent= grandchild
            grandchild.left=node
            grandchild.right=child
            if T2!=None:
                T2.parent=node
            node.right=T2
            if T3!=None:
                T3.parent=child
            child.left=T3
            child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
            node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
            grandchild.height= 1 + max(self.get_height(grandchild.left),self.get_height(grandchild.right))
            return
        if node.parent.left==node:
            node.parent.left=grandchild
        else:
            node.parent.right=grandchild
        grandchild.parent=node.parent
        child.parent=node.parent= grandchild
        grandchild.right=child
        grandchild.left=node
        if T2!=None:
                T2.parent=node
        node.right=T2
        if T3!=None:
                T3.parent=child
        child.left=T3
        child.height= 1 + max(self.get_height(child.left),self.get_height(child.right))
        node.height= 1 + max(self.get_height(node.left),self.get_height(node.right))
        grandchild.height= 1 + max(self.get_height(grandchild.left),self.get_height(grandchild.right))
        return
    
    def in_order(self):
        inorder_list=[]
        inorder(self.root,inorder_list)
        return inorder_list
# tree=AVLTree()

# l=[6,9,8,3,2,1,8,7]
# k=[-1,12,4,-5,15,5]
# for i in l[:6]:
#     n=Node(i)
#     tree.insert(n)
#     tree.in_order()
# for i in l[1:4]:
#     n=Node(i)
#     tree.delete(n)
#     tree.in_order()
# for i in k:
#     n=Node(i)
#     tree.insert(n)
#     tree.in_order()
# for i in k[1:]:
#     n=Node(i)
#     tree.delete(n)
#     tree.in_order()