import ctypes
class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.storage=GrowableArray()
    def pop(self):
        if (len(self.storage)!=0):
            self.storage.pop()
    def top(self):
        if(len(self.storage)!=0):
            return self.storage[len(self.storage)-1]
        return -1
    def push(self,x):
        self.storage.append(x)
    # You can implement this class however you like
class GrowableArray:
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds !')
        return self.A[k]
    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = ele
        self.n += 1
    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    def pop(self):
        if (self.n!=0):
            self.n-=1
            self.A[self.n]=None