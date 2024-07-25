# Queue using list 


class Queue:
    def __init__(self):
        self.item=[]
    
    def is_empty(self):
        return len(self.item)==0
    
    def enqueue(self,data):
        self.item.insert(0,data)
    

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError('Queue is Empty')
    

    def get_front(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError('Queue is Empty')

    def get_rear(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError('Queue is Empty')
        

    def size(self):
        return len(self.item)
    

q1 = Queue()
q1.enqueue(10)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
print('first element of Queue ', q1.get_front())
print('Last element of Queue ', q1.get_rear())
print('remove element of queue', q1.dequeue())
q1.enqueue(100)
q1.enqueue(120)
print('first element of Queue ', q1.get_front())
print('Last element of Queue ', q1.get_rear())