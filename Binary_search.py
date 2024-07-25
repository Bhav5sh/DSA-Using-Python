def binary_search(list1,item,low=0,high=None):
    if high is None:
        high=len(list1)-1        
    mid=(low+high)//2    
    if low<=high:
        if list1[mid]==item:
            return mid
        if list1[mid]<item:
            return binary_search(list1,item,mid+1,high)
        else:
            return binary_search(list1,item,low,mid-1)
    return None
list1=[15,20,33,41,57,63,79,87,90,10]
list1.sort()
print(binary_search(list1,87))