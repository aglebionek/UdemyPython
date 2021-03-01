### Create a generator that generates the squares of numbers up to some number N.
def gensquares(N):
    for number in range(N+1):
        yield number**2

for x in gensquares(10):
    print(x)

### Create a generator that yields "n" random numbers between a low and high number (that are inputs).
from random import randint

def rand_num(low,high,n):
    for _ in range(n):
        yield randint(low, high)

low = int(input('lower: '))
high = int(input('higher: '))

for num in rand_num(low, high, 12):
    print(num)

### Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)
for letter in s_iter:
    print(letter)

### Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
# ans: if you're operating on big numbers and don't want to needlessly store them in the memory but you need to iterate over them for something?

### Can you explain what gencomp is in the code below?
my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

#gencomp is a generator (the expression inside the parenthesses is a generator comprehension - like list comprehension)
#more memory efficient