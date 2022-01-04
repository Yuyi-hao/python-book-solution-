import random
heads = 0
tails = 0
for i in range(1,1000001,1):
    n = random.randint(1,2)
    if n ==1:
        heads +=1
    else:
        tails +=1
print(f'Numbers of heads : {heads} \nNumbers of tails : {tails}')
