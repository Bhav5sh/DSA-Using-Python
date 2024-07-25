from SLL import SLL


class Queue(SLL):
    def __init__(self,):
        super().__init__()
        self.item_count=0
    # def is_empty(self):
    #     return super().is_empty()
    def enqueue(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            self.item_count-=1
            self.delete_last()
            return temp.item
        else:
            raise IndexError('Queue is empty')
    def get_front(self):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            data=temp.item
            return data
        else:
            raise IndexError('Queue is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Queue is empty')
        
    def size(self):
        return self.item_count

q1=Queue()
q1.enqueue(200)
q1.enqueue(400)
q1.enqueue(600)
q1.enqueue(800)
q1.enqueue(1000)
print('first element of queue', q1.get_front())
print('last element of queue', q1.get_rear())
print('remove element is ', q1.dequeue())
print('remove element is ', q1.dequeue())
print('remove element is ', q1.dequeue())
q1.enqueue(1200)
q1.enqueue(1400)
print('first element of queue', q1.get_front())
print('last element of queue', q1.get_rear())
print('size of queue', q1.size())


         
        

    