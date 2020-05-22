list1=[1,3,6,2,5]
list2=[4,3,5,9,8,8]
common_elements_list=[]

for i in list1:
    if i in list2 and i not in common_elements_list:
        common_elements_list.append(i)

print(common_elements_list)

"""
BRUTE FORCE APPROACH:

list1=[1,3,6,2,5]
list2=[4,3,5,3,8,8]
common_elements_list=[]


for i in list1:
    found=False
    for j in list2:
        if(i==j):
            found=True
            if len(common_elements_list)==0:
                common_elements_list.append(i)
            else:
                for k in common_elements_list:
                    if(k==i):
                        break
                else:
                    common_elements_list.append(i)
            if found==True:
                    break

print("Common Elements: ",common_elements_list)

"""