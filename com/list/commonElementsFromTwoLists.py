list1=[1,3,6,2,5]
list2=[4,3,5,9,8,8]
common_element_list=[]

for i in list1:
    if i in list2 and i not in common_element_list:
        common_element_list.append(i)

for i in list2:
    if i in list1 and i not in common_element_list:
        common_element_list.append(i)

print(common_element_list)