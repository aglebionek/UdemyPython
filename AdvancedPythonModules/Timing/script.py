def func1(n: int) -> list: return [str(num) for num in range(n)]

print(func1(10))

def func2(n: int) -> list: return list(map(str, range(n)))

print(func2(10))

# we want to check which function is more efficient (faster)
import time
start_time1 = time.time()
func1(1000000)
end_time1 = time.time()
elapsed_time1 = end_time1 - start_time1
print(elapsed_time1)

start_time2 = time.time()
func2(1000000)
end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print(elapsed_time2)
# the time module will work badly for small arguments, and it's not really precise

# lets use timeit module instead
import timeit
stmt = '''
func1(100)
'''
setup = '''
def func1(n: int) -> list: return [str(num) for num in range(n)]
'''
print(timeit.timeit(stmt=stmt, setup=setup, number=100000))

stmt2 = '''
func2(100)
'''
setup2 = '''
def func2(n: int) -> list: return list(map(str, range(n)))
'''
print(timeit.timeit(stmt=stmt2, setup=setup2, number=100000))
