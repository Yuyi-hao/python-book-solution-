n = int(input('Enter the number of students : '))
count = 1
highest = 0
secondHighest = -1
while(count< n+1):
    score = float(input("Enter the score of student {} : ".format(count))) 
    if score > highest and score > secondHighest:
        secondHighest = highest
        highest = score
    count +=1

print('Highest score is {}'.format(highest)) 
print(secondHighest)