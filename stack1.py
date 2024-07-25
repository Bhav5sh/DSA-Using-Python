# stack using list

class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return not bool(self.items) 
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
           return self.items.pop()
        else:
            raise IndexError('stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
           raise  IndexError('stack is empty')
    def size(self):
        return len(self.items)
    
    
sl=stack()
# sl.push(2)
# sl.push(3)
# sl.push(4)
print('Top element is',sl.peek())
print('removed element is ',sl.pop())
print('Top element is',sl.peek())



