import time
start_time=time.time()
def Bubble_sort(e_list):
    for round in range(len(e_list)-1):
        for i in range(len(e_list)-1-round):
            count_swap=0
            if e_list[i] > e_list[i+1]:
                e_list[i],e_list[i+1] = e_list[i+1],e_list[i]
                count_swap+=1    
        if count_swap==0:
            break
                
    return e_list
element_list=[25,13,15,20,55,34,66,72,81]
sorted_list=Bubble_sort(element_list)
end_time=time.time()
execution_time=end_time-start_time

for i in sorted_list:
    print(i,end=' ')
print('Execution',execution_time)