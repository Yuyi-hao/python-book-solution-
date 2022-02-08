def isValid(password):
    test = str(password)
    countDigit = 0
    if len(test) >=8:
        if test.isalnum():
            for i in test:
                if i.isdigit():
                    countDigit +=1
            if countDigit >=2:
                print("It is a valid password ")
            else:
                print("Invalid password ")
                print("No. of digit is lesser than two ")
        else:
            print("Invalid password ")
            print("Password contain special charaters")
    else:
        print("Invalid password ")
        print("Password has less than eight charaters")


def main():
    password = input("Enter password : ")
    isValid(password)

main()
