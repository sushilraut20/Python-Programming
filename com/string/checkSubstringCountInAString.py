print("Example ---> Check number of occurrences of a substring in a given String")

input_string=input("Enter a String: ")
input_substring=input("Enter a sub string: ")

position=-1
occurence_list=[]
occurence_count=input_string.count(input_substring)

while True:
    position=input_string.find(input_substring,position+1,len(input_string))
    # string.find(substring, start_index, end_index)
    # 'find' will return the position of occurrence of a substring in given String, will return -1 if the substring is not found
    # the start_index is updated for every iteration
    if position==-1:
        break
    occurence_list.append(position)

if position==-1 and len(occurence_list)==0:
    print("The substring is not present in given string")
else:
    print('Given Substring "', input_substring,'" is present in given String "', input_string, '" for ',occurence_count,'no of times and it is present at locations',
                            occurence_list)
