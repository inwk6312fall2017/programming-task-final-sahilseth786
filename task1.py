import string

def longestword(text):
    dict1 = dict()
    dict2 = dict()
    lenword = 0
    
    for line in open(text):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.punctuation + string.whitespace)
            dict1[word] = dict1.get(word, 0) + 1
    for i in dict1:
        dict2[i]=len(i)
    for key,value in dict2.items():
        if value>lenword:
            lenword=value
            print("longest wird for",text)
            print(key,value)

longestword("Book1.txt")
longestword("Book2.txt")
longestword("Book3.txt")



