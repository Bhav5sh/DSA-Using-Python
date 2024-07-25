class Heap:
    def __init__(self):
        self.heap=[]
    def create_heap(self,list1):
        for e in list1:
            self.insert(e)

    def insert(self,e):
        index=len(self.heap)
        parentIndex=(index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e

    def Top(self):
        if len(self.heap)==0:
            raise EmptyHeapExceptione()
        return self.heap[0]
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapExceptione()
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        leftChildIndex= 2*index+1
        rightChildIndex=2*index+2

        while leftChildIndex<len(self.heap):
            if rightChildIndex<len(self.heap):
                if self.heap[leftChildIndex]>self.heap[rightChildIndex]:
                    if self.heap[leftChildIndex]>temp:
                        self.heap[index] = self.heap[leftChildIndex]
                        index=leftChildIndex
                    else:
                        break
                else:
                    if self.heap[rightChildIndex]>temp:
                        self.heap[index] = self.heap[rightChildIndex]
                        index=rightChildIndex
                    else:
                        break
            else: #no right child
                if self.heap[leftChildIndex]>temp:
                    self.heap[index] = self.heap[leftChildIndex]
                    index=leftChildIndex
                else:
                    break         
            leftChildIndex=2*index+1
            rightChildIndex=2*index+2
        self.heap[index]=temp
        return max_value
    def heapSort(self,list1):
        self.create_heap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapExceptione:
            pass            
        return list2
    
class EmptyHeapExceptione(Exception):
    def __init__(self, msg='Empty Heap' ):
        self.msg=msg
    def ___str__(self):
        return self.msg
        
mylist=[13,45,23,20,56,78,39,9,66,51,42,99]
h=Heap()
mylist=h.heapSort(mylist)

for i in mylist:
    print(i,end=' ')


        