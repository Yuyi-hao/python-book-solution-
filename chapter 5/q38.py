import time 
n = int(input("Enter the number of seconds : "))
time.sleep(1)
for i in range(n-1,0,-1):
    time.sleep(1)
    if i > 1:
        print(f'{i} seconds remaining')
    else:
        print('1 second remaining ')
print('Stopped')