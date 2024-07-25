# priority queue using linked list concept

class Node:
    def __init__(self ,item=None,priority=None,next=None) -> None:
        self.item=item
        self.priority=priority
        self.next=next

class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority :
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1                
    def pop(self):
        if self.is_empty():
            raise IndexError('priority queue is empty')
        delete_item=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return delete_item
    def size(self):
        return self.item_count
                
p=PriorityQueue()
p.push('bhavesh',9)
p.push('anupam',5)
p.push('abhishk',2)
p.push('dinesh',12)
p.push('arjun',6)
p.push('dharti',10)
p.push('aaradhya',1)
p.push('aryan',7)
p.push('abhay',3)
print(p.size())
while not p.is_empty():
    print(p.pop())
print(p.size())
                   
            




        

