def count(string,word):
    s = str(string).lower().replace(',',' ')+' '
    counter = 0
    s1 = ''
    s2 = str(word).lower()
    while len(s)>0:
        s1 = s[0:s.index(' ')]
        if s1 == s2:
            counter +=1
        s = s[s.index(' ')+1:len(s)]
    return counter


def main():
    string = input("Enter your string : ").strip()
    word = input("Input character : ").strip()
    result = count(string,word)
    print(f"Occurrence of word '{word}' in string '{string}' is : {result}")

main()