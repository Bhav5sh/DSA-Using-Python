class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class Dll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty:
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if  not self.is_empty():
            while temp.next is not None:
                temp=temp.next
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            # n.next=temp.next
            if temp.next is not None:
                temp.next.prev=n
            # n.prev=temp
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
    def delete_last(self):
        if self.start is None:
            pass    
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next.perv=None
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item == data:       
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break     




    
# driver code 
mylist=Dll()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
print(mylist.is_empty())
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(10),50)
mylist.insert_after(mylist.search(40),80)
mylist.print_list()