from curses.ascii import isalpha

def countWordInLine(line):
    vowels = ('a','e','i','o','u')
    vowel,consonant = 0,0
    line = line.lower()
    for  ch in line:
        if isalpha(ch) and (ch in vowels):
            vowel +=1
        elif isalpha(ch) and (ch not in vowels):
            consonant +=1
    return vowel,consonant

def findNonDuplicateWord(filename):
    vowel,consonant = 0,0
    fileobj = open(filename,'r')
    for line in fileobj:
        x,y = countWordInLine(line)
        vowel +=x
        consonant +=y

    return vowel,consonant

def main():
    filename = input("Enter filename : ").strip()
    consonants,vowels = findNonDuplicateWord(filename)
    print(f'No. of vowels in file : {vowels}')
    print(f'No. of consonants in file : {consonants}')

main()



