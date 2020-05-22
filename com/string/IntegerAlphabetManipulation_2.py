#Note: The integers must be less than 10 and greater than 0

print("Example ---> Input: A2B4C3, Output: AABBBBCCC")

input_string=input("Enter an alphanumeric String: ")
alphabets_list=[]
numeric_list=[]
output_string=''

for str in input_string:
    if str.isalpha():
        alphabets_list.append(str)
    elif str.isdigit():
        numeric_list.append(int(str))

for i in range(len(alphabets_list)):
    output_string+=alphabets_list[i]*numeric_list[i]

print("Output string: ", output_string)