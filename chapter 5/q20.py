# part a
# we have hard coded n here you can take from user input 
n = 6 
k = 0
print("Pattern first ")
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(j,end=' ')
        
    print()
# we can use same variable here coz they are defined inside the loop and their scope is limited only there 

print("pattern second ")
for i in range(n+1,1,-1):
    for j in range(1,i,1):
        print(j,end=' ')
    print()

print("Third pattern ")
for i in range(1,n+1,1):
    for j in range(n,i,-1):
        print(end='  ')
    while k<i:
        for l in range(i,0,-1):
            print(l,end=' ')
        k+=1
    print()

print("Fourth pattern")
for i in range(n+1,1,-1):
    for j in range(1,i,1):
        print(j,end= ' ')
    print()