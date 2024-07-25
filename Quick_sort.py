# def Quick_processor(data_list,left,right,loc):
#     while data_list[loc]<data_list[right]:
#         right-=1
#     data_list[loc],data_list[right]=data_list[right],data_list[loc]
#     loc=right
#     while data_list[loc] > data_list[left]:
#         left+=1
#     data_list[loc],data_list[left]=data_list[left],data_list[loc]
#     loc=left
#     if left==right==loc:
#         return loc
#     Quick_processor(data_list,left,right,loc)

# def Quick_sort(l1):
#     left=0
#     right=len(l1)-1
#     loc=0
#     while  left!=right :
#         if  len(l1)<=1:
#             return l1
#         Quick_processor(l1[left:loc],left,loc-1,left)
    
        