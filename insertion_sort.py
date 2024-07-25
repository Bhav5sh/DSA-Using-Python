def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]

        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp

mylist=[78,12,34,1,56,89,56,45,67]
insertion_sort(mylist)
for i in mylist:
    print(i,end=' ')
