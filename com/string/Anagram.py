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