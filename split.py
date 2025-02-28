def count_word(sentence):
    words=sentence.split()
    count=0
    for word in words:
        count+=1
    return count
#test the function
sentence="I like Apples"
print("word count=",count_word(sentence))