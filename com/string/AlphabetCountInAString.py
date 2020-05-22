input_string=input("Enter a String: ").lower()
occurrences_dict={}

for alphabet in input_string:
    occurrences_dict[alphabet]=occurrences_dict.get(alphabet,0)+1
#occurrences_dict.get(alphabet,0) will fetch the value for that alphabet(key), returns 0 if not present


for key,value in sorted(occurrences_dict.items()):
    print(key,"------->",value)