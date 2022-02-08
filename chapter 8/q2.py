def search(string,find):
    length = len(string)
    for i in range(length):
        if string[i] == find[0]:
            for j in find:
                if j == string[i]:
                    i =+1
                else:
                    break
                return True

def main():
    string = input("Enter you r string : ")
    find = input("Enter substring : ")
    r = search(string,find)
    if r:
        print("True")
    else:
        print('False')
main()
            