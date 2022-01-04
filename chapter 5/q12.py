NUMBER_OF_NUMBERS_PER_LINE = 10 
target = 10 
count = 0
for i in range(100,1000):
  if i%5 == 0 or i%6 == 0:
    print(i ,end = ' ')
    count += 1
  if count == target:
    print()
    target +=10