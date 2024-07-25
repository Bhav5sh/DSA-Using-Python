# deque using doubly linked list concepts

class Node:
    def  __init__(self,prev=None,item=None,next=None):
        self.perv=prev
        self.item=item
        self.next=next
    

class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.rear==None
    def insert_front(self,data):
        n=Node(None,data,self.front)
        if not self.is_empty():
            self.front.perv=n            
        else:
            self.rear=n
        self.front=n
        self.item_count+=1
    def insert_rear(self,data):
        n=Node(self.rear,data)
        if not self.is_empty():
            self.rear.next=n
        else:
            self.front=n
        self.rear=n
        self.item_count+=1
    def delete_front(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front.next.perv=None
                self.front=self.front.next
            self.item_count-=1
        else:
            raise IndexError('Deque is empty')
    def delete_rear(self):
        if not self.is_empty():
            if self.front==self.rear:
                self.rear=None
                self.front=None
            else:
                self.rear.perv.next=None
                self.rear=self.rear.perv
            self.item_count-=1
        else:
            raise IndexError('Deque is empty')
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        raise IndexError('Deque is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        raise IndexError('Deque is empty')
        
    def size(self):
        return self.item_count
    

d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(),d1.get_rear())
d1.delete_front()
d1.delete_rear()
print(d1.get_front(),d1.get_rear())
print(d1.size())

