import random
import time as time
import numpy as np
"""
x = [random.random() for i in range(10)]
print(x)

t = input("Enter to continue: ")

for i in x:
    if i <= 0.33:
        print("Continue")
        continue
    elif i > 0.33 and i <= 0.66:
        print("Pass")
        pass
    elif i > 0.66:
        break

print(f'Number: {i}')



x = [random.random() for i in range(1, 10)]
y = [random.random() for i in range(1, 10)]

start_time = time.time()
z = []
for counter, value in enumerate(x):
    z.append(value*y[counter])
end_time = time.time()
#print(z)
print(f'List Time: {end_time - start_time}')
print()
x = np.array(x)
y = np.array(y)
start_time = time.time()
z = x*y
end_time = time.time()
#print(z)
print(f'ArrayTime: {end_time - start_time}')

"""

## Define Arrays
# array
# linspace
# zeros
# ones
# matrix
#
## Matrix Operations
# inverse
# eig
# svd
