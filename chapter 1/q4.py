# question :: (Print a table) Write a program that displays the following table:
# a      a^2    a^3
# 1      1      1
# 2      4      8
# 3      9      27
# 4      16     64

# first way 
print('a','a**2','a**3')
for i in range(1,5,1):
    print(i,i**2,i**3)

#without loop 
print('a','a**2','a**3')
print(1,1**2,1**3)
print(2,2**2,2**3)
print(3,3**2,3**3)
print(4,4**2,4**3)
