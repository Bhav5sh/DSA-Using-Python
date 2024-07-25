# presize code

def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x<=pivot]
        grater=[x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(grater)
    
mylist=[26,38,12,20,2,56,89,67,88,4,42,21]
mylist=quick_sort(mylist)
for i in mylist:
    print(i,end=' ')
