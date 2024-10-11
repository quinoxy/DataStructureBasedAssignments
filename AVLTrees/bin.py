from avl import AVLTree
from object import Object
from node import Node
class Bin:
    def __init__(self, bin_id, capacity):
        self.id=bin_id
        self.capacity=capacity
        self.storage=AVLTree()

    def add_object(self, object):
        # Implement logic to add an object to this bin
        object_node=Node(object.id,object.size)
        self.storage.insert(object_node)
        self.capacity-=object.size

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        object_node=Node(object_id)
        self.storage.delete(object_node)
    def traverse(self):
        return(self.capacity,self.storage.in_order())
