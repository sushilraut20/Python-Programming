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