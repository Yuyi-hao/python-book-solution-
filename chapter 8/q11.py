def reverse(s):
    s = str(s)
    s1 = ''
    for i in s:
        s1 = i + s1
    return s1 

def main():
    string = input("Enter the string : ")
    print("Reversed string : {}".format(reverse(string)))

main()