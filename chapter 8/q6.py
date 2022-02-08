def countLetters(s):
    s = str(s)
    count = 0
    for i in s:
        if i.isalpha():
            count +=1
    return count

def main():
    string = input("Enter the string : ").strip()
    result = countLetters(string)
    print(f"Number of letters in '{string}' is '{result}'")
    
main()