class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item 
        self.next = next

class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            n.prev=n
            n.next=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            n.prev=n
            n.next=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.start
        if temp.item==data:
            return temp
        else:
            temp=temp.next
        while temp!=self.start:
            if temp.item==data:
                return temp
            temp=temp.next
        return None   
    def insert_after(self,temp,data):
        if temp!=None:
            n=Node(None,data,None)
            n.next=temp.next
            n.prev=temp
            temp.next.prev=n
            temp.next=n

    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev=self.start.prev
                self.start=self.start.next
    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.prev.prev.next=self.start
                self.start.prev=self.start.prev.prev

    def delete_item(self,data):
        if self.start is not None:
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp is not self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next    
                    temp=temp.next

    def print_list(self):
        temp=self.start
        if temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
            while temp!=self.start:
                print(temp.item ,end=' ')
                temp=temp.next
    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data


mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)
mylist.insert_after(mylist.search(40),60)
mylist.insert_after(mylist.search(20),70)
mylist.delete_item(35)
# mylist.delete_item(50)
# mylist.delete_first()
# mylist.delete_last()
# mylist.print_list() 
# mylist.delete_item(30)     
mylist.delete_first()   
mylist.delete_last()
# mylist.delete_item(30)
# mylist.delete_item(40)
for x in mylist:
    print(x,end=' ')