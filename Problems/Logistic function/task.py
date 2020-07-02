import math
x = int(input())
#sigmoid = (math.e ** x) / ((math.e ** x) + 1)
sigmoid = 1 / (1 + (pow(math.e, -x)))
print(round(sigmoid, 2))