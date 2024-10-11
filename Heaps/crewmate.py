'''
    Python file to implement the class CrewMate
'''
from custom import *
from heap import *
def treasure_comp(info1,info2):
    if (info1[0].arrival_time+info1[1]<info2[0].arrival_time+info2[1]):
        return True
    elif (info1[0].arrival_time+info1[1]==info2[0].arrival_time+info2[1]):
        return info1[0].id<info2[0].id
    return False

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.storage_list=DoublyLinkedList()
        self.empty_time=0
    
    # Add more methods if required
    def processed(self,answer):
        work_heap=Heap(treasure_comp,[])
        last_disturbed=0
        self.storage_list.start_iterate()
        curr=self.storage_list.next()

        while(curr!=None):
            while(work_heap.top()!=None and work_heap.top()[1]+last_disturbed<=curr.arrival_time):
                treasure,remaining_time=work_heap.extract()
                treasure.completion_time=remaining_time+last_disturbed
                answer.append(treasure)
                last_disturbed+=remaining_time

            if (work_heap.top()==None):
                work_heap.insert((curr,curr.size))
                last_disturbed=curr.arrival_time
            else:
                treasure, remaining_time=work_heap.extract()
                remaining_time-=curr.arrival_time-last_disturbed
                work_heap.insert((treasure,remaining_time))
                last_disturbed=curr.arrival_time
                work_heap.insert((curr,curr.size))
            curr=self.storage_list.next()
        while(work_heap.top()!=None):
            treasure,remaining_time=work_heap.extract()
            treasure.completion_time=remaining_time+last_disturbed
            last_disturbed+=remaining_time
            answer.append(treasure)
                

              