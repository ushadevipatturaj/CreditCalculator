import math
x = int(input())
sigmoid = 1 / (1 + (pow(math.e, -x)))
print(round(sigmoid, 2))
