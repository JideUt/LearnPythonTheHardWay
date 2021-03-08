# Import random module
import random

# Create 2 random lists

a = random.sample(range(10,100),10)
b = random.sample(range(10,200), 5)
c = []

# compare items in a to b
for i in a:
    if i not in b:
        c.append(i)

# repeat comparison from b and c perspective
for i in b:
    if i not in b and c:
        c.append(i)

# print all lists to confirm working correctly
print(a)
print(b)
print(c)
