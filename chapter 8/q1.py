from operator import truediv


def isvalid(ssn):
    ssn = str(ssn)
    s1 = ssn[0:3]
    s2 = ssn[4:6]
    s3 = ssn[7:11]
    if len(ssn) == 11:
        if s1.isdigit() and s2.isdigit() and s3.isdigit():
            return True
        else:
            return False
    else:
        return False

def main():
    ssn = input("Enter the ssn (ddd-dd-dddd) : ")
    if isvalid(ssn):
        print("Valid SSN")
    else:
        print('Invalid SSN')

main()