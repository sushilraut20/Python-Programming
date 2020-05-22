input_string=input("Enter a String: ").lower()
vowel_occurrences_dict={'a':0,'e':0,'i':0,'o':0,'u':0}

for alphabet in input_string:
    if alphabet.lower() in vowel_occurrences_dict:# it will check the keys in vowel_occurrences_dict
        vowel_occurrences_dict[alphabet.lower()]=vowel_occurrences_dict.get(alphabet.lower())+1
#occurrences_dict.get(alphabet) will fetch the value for that alphabet(key)


for key,value in vowel_occurrences_dict.items():
    print(key,"------->",value)
