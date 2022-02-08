def count(string,character):
    count = 0
    ch = str(character).lower()
    s = str(string).lower()
    if len(s) == 1:
        for i in s:
            if i == ch:
                count +=1
        return count
    else:
        return None

def main():
    string = input("Enter your string : ").strip()
    character = input("Input character : ").strip()
    result = count(string,character)
    print(f"Occurrence of letter {character} in string {string} is {result}")

main()