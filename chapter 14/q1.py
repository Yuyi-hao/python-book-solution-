import os
import sys

def countWords(line,count,keywords):
    line = replacePunctuation(line)
    words = line.split()
    for word in words:
        if word in count and keywords:
            count[word]+=1
        elif word in keywords:
            count[word] = 1
    
    return count

def replacePunctuation(line):
    for i in line:
        if i in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(i,' ')
    return line

def main():
    keywords = ("and", "as", "assert", "break", "class",
"continue", "def", "del", "elif", "else",
"except", "False", "finally", "for", "from",
"global", "if", "import", "in", "is", "lambda",
"None", "nonlocal", "not", "or", "pass", "raise",
"return", "True", "try", "while", "with", "yield")
    fileName = input("Enter file name(should be in same directory) : ").strip()
    if not os.path.isfile(fileName):
        print(f"File ({fileName}) does not exit in current directory")
        sys.exit()
    
    fileObj = open(fileName,'r')
    countWord = {}

    for line in fileObj:
        countWords(line,countWord,keywords)
    
    for key in countWord:
        print(f'{key} : {countWord[key]}')

main()


    



