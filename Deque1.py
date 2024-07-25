# deque using list

class deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.append(data)

    def insert_rear(self,data):
        self.items.insert(0,data)
    def delete_front(self):
        if not self.is_empty():
            self.items.pop()
        else:
            raise IndexError('Deque is empty')

    def delete_rear(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError('Deque is empty')

    def get_front(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Deque is empty')
    def get_rear(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Deque is empty')
    def size(self):
        return len(self.items)


d1=deque()

d1.insert_front(2)
d1.insert_front(4)
d1.insert_front(6)
d1.insert_front(8)
d1.insert_front(10)
d1.insert_rear(12)
d1.insert_rear(14)
d1.insert_rear(16)
d1.insert_rear(18)
d1.insert_rear(20)
print('front=',d1.get_front())
print('rear=',d1.get_rear())
d1.delete_front()
d1.delete_front()
d1.delete_rear()
d1.delete_rear()
print('front=',d1.get_front())
print('rear=',d1.get_rear())
