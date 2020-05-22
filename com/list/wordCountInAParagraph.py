paragraph="This is San Diego. It is an amazing place to live. San Diego is on west coast".lower().split(".")

paragraph_words_list=[]
unique_words_list=[]

for sentence in paragraph:
    for i in sentence.strip().split():
        paragraph_words_list.append(i)
        if i not in unique_words_list:
            unique_words_list.append(i)

for word in unique_words_list:
    print("'",word,"'", " is present in paragraph for ","'",paragraph_words_list.count(word),"'", "times")