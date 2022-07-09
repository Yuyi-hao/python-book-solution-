def countWordInLine(line,count):
    line = line.lower().split()
    for word in line:
        if word not in count:
            count.append(word)

def findNonDuplicateWord(filename):
    count = []
    fileobj = open(filename,'r')
    for line in fileobj:
        countWordInLine(line,count)
    return count

def main():
    filename = input("Enter filename : ").strip()
    words = findNonDuplicateWord(filename)
    words.sort()
    print(words,sep=' ')

main()



