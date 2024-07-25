# Queue by extending list class

class Queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,data):
        self.insert(0,data)
    def dequeue(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise IndexError('Queue is Empty')
    def get_front(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError('Queue is Empty')
    def get_rear(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError('Queue is Empty')
    def size(self):
        return len(self)



q1=Queue()
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
print('firt element of queue', q1.get_front())
print('last element of queue', q1.get_rear())
print('remove element of queue', q1.dequeue())
print('remove element of queue', q1.dequeue())
print('remove element of queue', q1.dequeue())
print('remove element of queue', q1.dequeue())
q1.enqueue(100)
q1.enqueue(120)
q1.enqueue(140)
q1.enqueue(160)
print('firt element of queue', q1.get_front())
print('last element of queue', q1.get_rear())

