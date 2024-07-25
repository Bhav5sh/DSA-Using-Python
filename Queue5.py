# Queue using singly linklist concept
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def  __init__(self):
        self.Front=None
        self.Rear=None
        self.item_count=0

    def is_empty(self):
        return self.Front==None
    def enqueue(self, data):
        n=Node(data)
        if self.Rear is None:
            self.Front=n
        else:
            self.Rear.next=n
        self.Rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Empty Queue')
        elif self.Front==self.Rear:
            self.Front=None
            self.Rear=None
        else:
            self.Front=self.Front.next
        self.item_count-=1
        
    def get_front(self):
        if self.is_empty():
            raise IndexError('Data not in Queue')
        else:
            return self.Front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError('Data not in Queue')
        else:
            return self.Rear.item
    def size(self):
        return self.item_count
    
q1=Queue()
q1.enqueue(10)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
print('front=',q1.get_front(), 'rear=',q1.get_rear())
q1.dequeue()
q1.dequeue()
q1.enqueue(100)
print('front=',q1.get_front(),'rear=',q1.get_rear())

            
        