# stck using linked list

class Node:
    def __init__(self,item=None,next=None):
       self.item=item
       self.next=next

class stack:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError('stack is Empty')
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('stck is Empty')
    def size(self):
        return self.item_count
    
s3=stack()
s3.push(10)
s3.push(20)
s3.push(30)
s3.push(40)
print('top element is ', s3.peek())
print('remove element is ', s3.pop())
print('top element is ', s3.peek())
        
       
       
        

