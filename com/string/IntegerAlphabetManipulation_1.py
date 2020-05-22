print("Example ---> Input: D2A4C1F9, Output: ACDF1249")

input_string=input("Enter an alphanumeric String: ")
alphabets_string=numeric_string=sorted_alphanumeric_string=''

for str in input_string:
    if str.isalpha():
        alphabets_string+=str
    elif str.isdigit():
        numeric_string+=str

for i in sorted(alphabets_string):
    sorted_alphanumeric_string+=i

for i in sorted(numeric_string):
    sorted_alphanumeric_string+=i

print("sorted alphanumeric string: ", sorted_alphanumeric_string)
