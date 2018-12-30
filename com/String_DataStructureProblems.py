#-----------Check whether given String is Palindrome-----------------------


print("Example ---> Check whether given String is Palindrome")

#Take input from user and convert the String in lower case
input_string=input("Enter the String: ").lower()


#Reverse the input_string using splicing and -1 as step size and compare that with original String
if input_string==input_string[::-1]:
    print("The String is palindrome")


#-----------Check whether given sub-string is present in String-----------------------

print("Example ---> Check whether given sub-string is present in String")

input_string=input("Enter a String: ")
input_substring=input("Enter a sub string: ")

if input_substring in input_string:
    print(input_substring,"is PRESENT in", input_string)
else:
    print(input_substring,"is NOT PRESENT in", input_string)

#-----------Check number of occurrences of a substring in a given String-----------------------

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

#-----------Input: D2A4C1F9, Output: ACDF1249---------------------------------------------------

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


#-----------Input: A2B4C3, Output: AABBBBCCC ---------------------------------------------------
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


#-----------Input: A2B4C3, Output: ACBFG ---------------------------------------------------
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

#-----------Input--> str1='Computer' str2='Science', Output: 'CSocmipeuntceer  ---------------------------------------------------
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

#-----------To check whether the two strings are Anagram ---------------------------------------------------

first_string=input("Enter 1st String: ").lower().replace(" ","")
second_string=input("Enter 2nd String: ").lower().replace(" ","")

isAnagram=True

if len(first_string)==len(second_string):
    for i in first_string:
        if(first_string.count(i)!=second_string.count(i)):
            isAnagram=False
            break
        else:
            pass
else:
    isAnagram=False

print(isAnagram)

#-----------Counting occurrences of alphabets in a String using dictionary -----------------------------------

input_string=input("Enter a String: ").lower()
occurrences_dict={}

for alphabet in input_string:
    occurrences_dict[alphabet]=occurrences_dict.get(alphabet,0)+1
#occurrences_dict.get(alphabet,0) will fetch the value for that alphabet(key), returns 0 if not present


for key,value in sorted(occurrences_dict.items()):
    print(key,"------->",value)

#-----------Counting occurrences of vowels in a String using dictionary -----------------------------------

input_string=input("Enter a String: ").lower()
vowel_occurrences_dict={'a':0,'e':0,'i':0,'o':0,'u':0}

for alphabet in input_string:
    if alphabet.lower() in vowel_occurrences_dict:# it will check the keys in vowel_occurrences_dict
        vowel_occurrences_dict[alphabet.lower()]=vowel_occurrences_dict.get(alphabet.lower())+1
#occurrences_dict.get(alphabet) will fetch the value for that alphabet(key)


for key,value in vowel_occurrences_dict.items():
    print(key,"------->",value)

#-----------Reversing words in a sentence -----------------------------------

sentence="Durga Software Solutions"
temp=sentence.split()
sentence=''

for word in temp:
    for chr in word[::-1]:
        sentence+=chr

    if(temp.index(word)<len(temp)-1):
        sentence+=' '


print(sentence)