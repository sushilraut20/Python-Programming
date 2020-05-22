#Note: The integers must be less than 10 and greater than 0

print("Example ---> Input: A2B4C3, Output: ACBFG")

input_string=input("Enter an alphanumeric String: ")
output_string=''
previous=''

#ord('A')= 65
#chr(65)= 'A'

for str in input_string:
    if str.isalpha():
        output_string+=str
        previous=str
    elif str.isdigit():
        output_string+=chr(ord(previous)+int(str))

print("Output string: ", output_string)
