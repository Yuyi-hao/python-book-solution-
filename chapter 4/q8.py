a,b,c = eval(input("Enter three intigers (e.g. 2,3,8) : "))
sum = a+b+c


if a>b:
    if a>c:
        max = a
    else:
        max = c
elif b>c:
    max = b
else:
    max = c 

if a<b:
    if a<c:
        min = a
    else:
        min = c
elif b<c:
    min = b
else:
    min = c 

# # using built in function 
# min = min(a,b,c)
# max = max(a,b,c)
print(min,(sum-min-max),max)


