X = [1,2,3,4]
Z = list()

try:
    Z.extend([X.pop() for _ in range(5)])
except IndexError as error:
    print(traceback.)