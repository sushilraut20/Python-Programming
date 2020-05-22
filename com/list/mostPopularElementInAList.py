input_list=[1,1,2,3,4,5,5,5]
unique_elements_list=[]
occurence_count_list=[]

for i in input_list:
    if i not in unique_elements_list:
        unique_elements_list.append(i)

for i in unique_elements_list:
    unique_elements_list.append(input_list.count(i))

print("The most popular element in given list is: ",unique_elements_list[occurence_count_list.index(max(occurence_count_list))])