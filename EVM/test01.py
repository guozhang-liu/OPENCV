import numpy as np

l = 2
h = 4
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
a[:l] = 0
print(a)
a[h:-h] = 0
print(a)
a[-l:] = 0
print(a)
