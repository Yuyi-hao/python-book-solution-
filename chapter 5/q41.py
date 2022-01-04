num = -1
highest  = 0
count = 1
while num!=0:
    num  = int(input("Enter a number (0: for end of input) : "))
    if num > highest:
        highest = num
        count = 1
    elif num == highest:
        count +=1

print(f'The largest number is {highest}')
print(f'The occurrence count of largest number is {count}')
