sentence="Durga Software Solutions"
temp=sentence.split()
sentence_list=[]

for word in temp:
    sentence_list.append(word[::-1])

sentence=" ".join(sentence_list)

print(sentence)