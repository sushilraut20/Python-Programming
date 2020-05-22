#Note: The integers must be less than 10 and greater than 0

print("Example ---> Input--> str1='Computer' str2='Science', Output: 'CSocmipeuntceer")

input_string1=input("Enter first String: ")
input_string2=input("Enter second String: ")

output=''
i=j=0

while i<len(input_string1) or j<len(input_string2):
    if(i>=len(input_string1)):
        output+=input_string2[j]
    elif(j>=len(input_string2)):
        output+=input_string1[i]
    else:
        output+=input_string1[i]+input_string2[j]
    i=i+1
    j=j+1

print(output)
