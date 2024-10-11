'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import *
from heap import *
from treasure import *
from custom import *
def comp_crew(crewmate1,crewmate2):
    return crewmate1.empty_time<crewmate2.empty_time

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.crewmate_heap=Heap(comp_crew,[])
        for i in range(m):
            new_mate = CrewMate()
            self.crewmate_heap.insert(new_mate)
        self.non_emp_crew=DoublyLinkedList()
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        insert_mate=self.crewmate_heap.extract()
        first_time=False
        if (insert_mate.empty_time==0):
            first_time=True
        if insert_mate.empty_time<treasure.arrival_time:
            insert_mate.empty_time=treasure.arrival_time + treasure.size
        else:
            insert_mate.empty_time+=treasure.size
        insert_mate.storage_list.append(treasure)
        self.crewmate_heap.insert(insert_mate)
        if (first_time and insert_mate.empty_time>0):
            self.non_emp_crew.append(insert_mate)
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        answer=[]
        self.non_emp_crew.start_iterate()
        process_mate=self.non_emp_crew.next()
        while(process_mate!=None):
            process_mate.processed(answer)
            process_mate=self.non_emp_crew.next()
        answer.sort(key=lambda x:x.id)
        return answer
    
    # You can add more methods if required