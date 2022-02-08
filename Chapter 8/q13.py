def prefix(s1,s2):
    s1,s2 = str(s1),str(s2)
    i = 0
    result = ''

    while i < min(len(s1),len(s2)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            break 
        i +=1
    return result

def main():
    s1 = input("Enter first string : ").strip()
    s2 = input("Enter second string : ").strip()
    r = prefix(s1,s2)
    print(r)

main()