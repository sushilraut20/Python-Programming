#-----------Check whether given String is Palindrome-----------------------

#Take input from user and convert the String in lower case
input_string=input("Enter the String: ").lower()


#Reverse the input_string using splicing and -1 as step size and compare that with original String
if input_string==input_string[::-1]:
    print("The String is palindrome")


#-----------Check whether given sub-string is present in String-----------------------

input_string=input("Enter a String: ")
input_substring=input("Enter a sub string: ")

if input_substring in input_string:
    print(input_substring,"is PRESENT in", input_string)
else:
    print(input_substring,"is NOT PRESENT in", input_string)

#-----------Check number of occurrences of a substring in a given String-----------------------

input_string=input("Enter a String: ")
input_substring=input("Enter a sub string: ")

position=-1
occurence_list=[]
occurence_count=0

while True:
    position=input_string.find(input_substring,position+1,len(input_string))
    # string.find(substring, start_index, end_index)
    # 'find' will return the position of occurrence of a substring in given String, will return -1 if the substring is not found
    if position==-1:
        break
    occurence_list.append(position)
    occurence_count+=1

if position==-1 and len(occurence_list)==0:
    print("The substring is not present in given string")
else:
    print('Given Substring "', input_substring,'" is present in given String "', input_string, '" for ',occurence_count,'no of times and it is present at locations',
                            occurence_list)

