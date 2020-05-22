print("Example ---> Check whether given sub-string is present in String")

input_string=input("Enter a String: ")
input_substring=input("Enter a sub string: ")

if input_substring in input_string:
    print(input_substring,"is PRESENT in", input_string)
else:
    print(input_substring,"is NOT PRESENT in", input_string)
