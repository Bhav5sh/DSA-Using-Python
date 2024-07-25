# queue using singly list class
class Node:
    def __init__(self,item=None, next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0

    def is_empty(self):
        return self.start==None
    def enqueue(self,data):
        n=Node(data, self.start)
        self.start=n
        self.item_count+=1

    def dequeue(self):
        if not self.is_empty():
            if self.start.next is None:
                self.start=None
            else:
                temp=self.start
                while temp.next.next is not None:
                    temp=temp.next
                data=temp.next.item
                temp.next=None
                self.item_count-=1
            return data
        else:
            raise IndexError('Queue is Empty')
        
    def get_front(self):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                    temp=temp.next
            data=temp.item
            return data
        else:
            raise IndexError('Queue is Empty')
        
    def get_rear(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError('Queue is Empty')


    def size(self):
        raise self.item_count
    
q1=Queue()
# q1.enqueue(20)
# q1.enqueue(30)
# q1.enqueue(40)
# q1.enqueue(50)
# q1.enqueue(60)
# q1.enqueue(70)
print('first element of queue', q1.get_front())
print('last element of queue', q1.get_rear())
print('remove element is ', q1.dequeue())
print('remove element is ', q1.dequeue())
print('remove element is ', q1.dequeue())
# q1.enqueue(80)
# q1.enqueue(90)
# q1.enqueue(100)
print('first element of queue', q1.get_front())
print('last element of queue', q1.get_rear())


