# stack using class sll 


from SLL import SLL

class Stack:
    def __init__(self):
        self.items = SLL()
        self.items_count = 0
    def is_empty(self):
        return self.items.is_empty()    
    def push(self,data):
        self.items.insert_at_start(data)
        self.items_count += 1
    def pop(self):
        if not self.items.is_empty():
            data = self.items.start.item
            self.items.delete_first()
            self.items_count -= 1
            return data
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.items.is_empty():
            return self.items.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.items_count
    


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
print("top element is ", s1.peek())
print("size of stack is ", s1.size())
print("removed element is ", s1.pop())
print("top element is ", s1.peek())
print("size of stack is ", s1.size())
        
            
        

