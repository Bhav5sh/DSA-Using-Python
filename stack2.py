# stack extending list


class stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError('stack is Empty')  
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('stack is Empty')
    def size(self):
        return len(self)
    def insert(self, index,data):
        raise AttributeError("NO attribute 'insert' in stack")
        
sl=stack()
# sl.insert(0,10)
sl.push(10)
sl.push(20)
sl.push(30)
print('top value is ',sl.peek())
print('remove value is '  ,sl.pop())
print('top value is ',sl.peek())
