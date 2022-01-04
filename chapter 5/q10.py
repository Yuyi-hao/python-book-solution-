n = int(input('Enter the number of students : \n'))
count = 1
highest = 0
while(count< n+1):
    score = eval(input("Enter the score of student {} : \n ".format(count))) 
    if highest < score:
        highest = score
    count +=1

print('Highest score is {}'.format(highest)) 