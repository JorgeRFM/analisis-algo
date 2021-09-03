# recopilado de https://www.geeksforgeeks.org/python-program-for-binary-search/

import random

values = []
for i in range(1,1000):
    values.append(random.randint(1, 1000))
values.sort()
print ( values )

def binary_search(values, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if values[mid] == x:
            return mid

        elif values[mid] > x:
            return binary_search(values, low, mid - 1, x)
 
        else:
            return binary_search(values, mid + 1, high, x)
 
    else:
        return -1
 
k = 10
 
result = binary_search(values, 0, len(values)-1, k)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
