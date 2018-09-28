#Take input from user and convert the String in lower case
input_string=input("Enter the String: ").lower()


#Reverse the input_string using splicing and -1 as step size and compare that with original String
if input_string==input_string[::-1]:
    print("The String is palindrome")

