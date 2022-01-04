n = ''
positive = 0
negative = 0
sum = 0
average = 0
count = 0
while(n !=0 ):
    n = eval(input("Enter an integer, the input ends if it is 0 : "))
    if n<0:
        negative = negative+1
    elif n > 0:
        positive = positive+1
    if n!=0:
        sum +=n
    if positive+negative != 0 :
        average = sum/(positive+negative)
    count +=1

if( count > 1):
    print('The number of positives is {}'.format(positive))
    print('The number of negatives is {}'.format(negative))
    print('The total is {}'.format(sum))
    print('The average is {:.2f}'.format(average))
else:
    print("You didn't any number")  
