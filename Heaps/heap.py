'''
Python Code to implement a heap with general comparison function
'''
def comp1(a,b):
    return a<b

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        # Write your code here
        self.comparator=comparison_function
        if init_array==None:
            self.stored=[]
        else:
            self.stored=init_array
        self.len=len(self.stored)
        for i in range(self.len-1,-1,-1):
            j=i
            self.downheap(j)
            
    def print_list(self):
        return self.stored
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        # Write your code here
        self.stored.append(value)
        self.len+=1
        k=self.len-1
        while(k!=0):
            if(self.comparator(self.stored[k],self.stored[(k-1)//2])):
                self.stored[k],self.stored[(k-1)//2]=self.stored[(k-1)//2],self.stored[k]
                k=(k-1)//2
            else:
                break
        
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.len==0:
            return None
        if self.len==1:
            self.len=0
            return self.stored.pop()
        el=self.stored.pop()
        answer=self.stored[0]
        self.len-=1
        self.stored[0] = el
        self.downheap(0)
        return answer
        
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if (self.len>0):
            return self.stored[0]
        return None
    
    # You can add more functions if you want to
    def downheap(self,j):
        while(j<self.len):
            left=True
            right=True
            if(j*2 +1 <self.len):
                left=self.comparator(self.stored[j], self.stored[2*j+1])
            if(j*2 +2 <self.len):
                right=self.comparator(self.stored[j], self.stored[2*j+2])
            if ((not(left) or not(right))):
                if(2*j+2<self.len):
                    if self.comparator(self.stored[2*j+1],self.stored[2*j+2]):
                        self.stored[j], self.stored[2*j+1]= self.stored[2*j+1], self.stored[j]
                        j=2*j+1
                    else:
                        self.stored[j], self.stored[2*j+2]= self.stored[2*j+2], self.stored[j]
                        j=2*j+2
                elif(2*j+1<self.len):
                    self.stored[j], self.stored[2*j+1]= self.stored[2*j+1], self.stored[j]
                    j=2*j+1
                else:
                    break
            else:
                break
        return
        
    
# h=Heap(comp1,[1,15,6,23,12,34,15,4,22])
# print(h.print_list())
# h.insert(5)
# h.insert(15)
# print(h.print_list())
# while(h.top()!=None):
#     print(h.extract())

# print(h.print_list())
