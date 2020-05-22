list1=[1,3,6,2,5]
list2=[4,3,5,9,8,8]
unique_element_list=[]

for i in list1:
    if i not in list2 and i not in unique_element_list:
        unique_element_list.append(i)

for i in list2:
    if i not in list1 and i not in unique_element_list:
        unique_element_list.append(i)

print(unique_element_list)
