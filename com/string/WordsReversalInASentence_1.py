sentence="Durga Software Solutions"
temp=sentence.split()
sentence=''

for word in temp:
    for chr in word[::-1]:
        sentence+=chr

    if(temp.index(word)<len(temp)-1):
        sentence+=' '


print(sentence)