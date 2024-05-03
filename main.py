import hashlib
from itertools import permutations

def find_hash(original_hash):
    wordFile=open("words.txt")
    wordFile=list(wordFile)
    anagram="who outlay thieves"
    words=anagram.count(" ")
    words+=1
    charList=list(set(anagram))
    if " " in charList:
        charList.remove(" ")
    finalWords=[]
    for i in wordFile:
        flag=False
        tempWord=i.replace("\n","")
        tempChar=list(set(tempWord))
        for i in tempChar:
            if i not in charList:
                flag=True
                break
        if flag==False:
            finalWords.append(tempWord)
    for element in permutations(finalWords,words):
        hashElem=" ".join(element)
        if  len(hashElem) != len(anagram):
            continue
        m=hashlib.md5()
        m.update(hashElem.encode("utf-8"))
        wordHash=m.hexdigest()
        if wordHash == original_hash:
            return hashElem

hash = '13b382e1a2f8e22535b4730d78bc8591'
answer = find_hash(hash)
print(f"Collision!  The word corresponding to the given hash is '{answer}'")