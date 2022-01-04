import random
counter = 0
print("Throwing the dart....")
for i in range(0, 1000000):
    if random.randint(1, 4) % 2 != 0:
        counter += 1

prob = counter / 1000000
print("The probability that the dart fall in an odd numbered region is", prob)