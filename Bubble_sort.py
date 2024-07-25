import time
start_time=time.time()
def Bubble_sort(e_list):
    for round in range(len(e_list)-1):
        for i in range(len(e_list)-1-round):
            if e_list[i] > e_list[i+1]:
                e_list[i],e_list[i+1] = e_list[i+1],e_list[i]           
    return e_list
element_list=[25,13,15,20,55,34,66,72,81]
sorted_list=Bubble_sort(element_list)
end_time=time.time()
execution_time=end_time-start_time
for i in sorted_list:
    print(i,end=' ')
# print('Execution',execution_time)


def modified_Bubble_sort(data_list):
    flag=False
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
l=[34,67,89,12,25,50]
modified_Bubble_sort(l)
print()
for i in l:
    print(i,end=' ')