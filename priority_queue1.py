# priority queue using list


class PriorityQueue:
    def __init__(self) -> None:
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))

    def pop(self):
        if self.is_empty():
            raise IndexError('Priority Queue is empty')
        return self.items.pop(0)
    def size(self):
        if self.is_empty():
            raise IndexError('Priority Queue is empty')
        return len(self.items)
    

p=PriorityQueue()
p.push('bhavesh',9)
p.push('anupam',5)
p.push('abhishk',2)
p.push('dinesh',12)
p.push('arjun',6)
p.push('dharti',10)
p.push('aaradhya',1)
p.push('aryan',7)
p.push('abhay',2)

while not p.is_empty():
    print(p.pop()[0])