# n = int(input("Enter a integer between (1-15) : "))
#  for this problem we have taken n as 8 you can take user input if you want 
n = 8
k = 0
# if n>=1 and n<=15:
for i in range(1,n+1,1):
    for j in range(n,i,-1):
        print(end = '  ')
    while k != i:
        for l in range(0,i,1):
            print(2**(l), end = ' ')
        k +=1
    for m in range(i+1,2,-1):
        print(2**(m-3), end = ' ')
    print()
# else:
#     print("You've entered a digit which is greater than 15 or lesser than 1 ") 