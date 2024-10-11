from bin import Bin
from avl import AVLTree
from node import Node
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.objects=AVLTree()
        self.bins_capac_leastid=AVLTree()
        self.bins_capac_maxid=AVLTree()
        self.bins_id=AVLTree()

    def add_bin(self, bin_id, capacity):
        bin=Bin(bin_id,capacity)
        node1=Node(bin_id,bin)
        node2=Node([capacity,bin_id],bin)
        node3=Node([capacity,-bin_id],bin)
        self.bins_capac_leastid.insert(node2)
        self.bins_capac_maxid.insert(node3)
        self.bins_id.insert(node1)

    def add_object(self, object_id, size, color):
        bin=None
        obj=Object(object_id,size,color)
        temp=None
        if(color==Color.BLUE):
            temp=self.bins_capac_leastid.root
            if temp!=None:
                while(temp!=None):
                    if (size>temp.value[0]):
                        temp=temp.right
                    else:
                        bin=temp.stored_data
                        temp=temp.left
        elif (color==Color.YELLOW):
            temp=self.bins_capac_maxid.root
            if temp!=None:
                while(temp!=None):
                    if (size>temp.value[0]):
                        temp=temp.right
                    else:
                        bin=temp.stored_data
                        temp=temp.left
        elif (color==Color.RED):
            temp=self.bins_capac_maxid.root
            if temp!=None:
                while (temp.right!=None):
                    temp=temp.right
                if (size<=temp.value[0]):
                    bin=temp.stored_data
        elif (color==Color.GREEN):
            temp=self.bins_capac_leastid.root
            if temp!=None:
                while (temp.right!=None):
                    temp=temp.right
                if (size<=temp.value[0]):
                    bin=temp.stored_data
            

        if (bin==None):
            raise NoBinFoundException
        node2=Node([bin.capacity,bin.id])
        node3=Node([bin.capacity,-bin.id])
        self.bins_capac_leastid.delete(node2)
        self.bins_capac_maxid.delete(node3)
        
        bin.add_object(obj)

        node4=Node([bin.capacity,bin.id],bin)
        node5=Node([bin.capacity,-bin.id],bin)
        self.objects.insert(Node(object_id,[size,bin]))
        self.bins_capac_leastid.insert(node4)
        self.bins_capac_maxid.insert(node5)

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin

        element=Node(object_id)
        to_be_deleted=self.objects.search(element)
        if (to_be_deleted==None or element.value!=to_be_deleted.value):
            return None

        bin=to_be_deleted.stored_data[1]
        object_size=to_be_deleted.stored_data[0]
        self.objects.delete(element)
        node2=Node([bin.capacity,bin.id])
        node3=Node([bin.capacity,-bin.id])
        self.bins_capac_leastid.delete(node2)
        self.bins_capac_maxid.delete(node3)

        bin.capacity += object_size
        bin.remove_object(object_id)
        node4=Node([bin.capacity,bin.id],bin)
        node5=Node([bin.capacity,-bin.id],bin)
        self.bins_capac_leastid.insert(node4)
        self.bins_capac_maxid.insert(node5)
        

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        element= Node(bin_id)
        bin = self.bins_id.search(element)
        return bin.stored_data.traverse()

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        element=Node(object_id)
        to_be_searched=self.objects.search(element)
        if (to_be_searched==None or element.value!=to_be_searched.value):
            return None
        bin=to_be_searched.stored_data[1]
        return bin.id
        
    
    