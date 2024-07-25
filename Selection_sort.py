# using built in function

def Selection_sort(e_list):
    for i in range(len(e_list)):
        next_small=min(e_list[i:])
        index=e_list.index(next_small)
        e_list[i],e_list[index] = e_list[index],e_list[i]

    return e_list

element_list=[25,1,5,20,55,34,66,72,81]
sorted_list=Selection_sort(element_list)
for i in sorted_list:
    print(i,end=' ')

# using logic

def selection_sort(list1):
    n=len(list1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if list1[j] < list1[min_index]:
                min_index=j
        list1[i],list1[min_index] = list1[min_index],list1[i]

l1=[64,35,89,21,72,13]
selection_sort(l1)
print()
for i in l1:
    print(i,end=' ')