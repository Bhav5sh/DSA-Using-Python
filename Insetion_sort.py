# my logic

def Insertion_sort(e_list):
    k=1
    for i in range(1,len(e_list)):
        for j in range(k):
            if e_list[i-1-j] > e_list[i-j]:
                e_list[i-1-j],e_list[i-j] = e_list[i-j],e_list[i-1-j]
            else:
                break
        k+=1 
                
l1=[45,67,89,99,12,24,52]
Insertion_sort(l1)
# print(l1)
for i in l1:
    print(i,end=' ')        