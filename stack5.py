# stack by exceding sll class

from SLL import SLL

class Stack(SLL):
    def __init__(self):
        super().__init__()
        self.items_count = 0

    # def is_empty(self):
    #     return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
        self.items_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.delete_first()
            self.items_count-=1
            return data
        else:
            raise IndexError('Stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('stack is empty')
    def size(self):
        return self.items_count
    


sl=Stack()
sl.push(2)
sl.push(23)
sl.push(24)
sl.push(25)
sl.push(66)
sl.push(77)
sl.push(88)
sl.push(99)
print('top element of stack ',sl.peek())
print(' removed element of stack ',sl.pop())
print('top element of stack ',sl.peek())
print(sl.is_empty())
