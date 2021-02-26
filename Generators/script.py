# this method creates the list - meaning it calculates every element and stores all of them in the memory
def list_of_cubes(upper_bound):
    return [x**3 for x in range(upper_bound)]

print(list_of_cubes(10))

# this method is a generator - meaning it calculates the elements as they are called for (I think it also returns them one by one)
# without the need to store them in memory at any point

def gen_of_cubes(upper_bound): 
    for x in range(upper_bound): yield x**3

# if I print the generator, I will just get info about the object itself, I need to iterate over it
for x in gen_of_cubes(10): # I guess the range() method is also a generator
    print(x)

# this happens in the back when you iterate over a generator
gen = gen_of_cubes(10)
while True:
    try:
        print(next(gen)) # It doesn't print it here, it returns (yields) (?) it here, but you get the logic
    except StopIteration: # this exception signals that the end of the generator object was reached
        break

# you can also turn any object you can iterate over (like a string) into an iterator (what's the difference between an iterator and a generator?)
# (I know I can use the next keyword on them both)

string = 'hewwo'
string_iterator = iter(string)
while True:
    try:
        print(next(string_iterator))
    except StopIteration:
        break
'''
def yield_letters():
    for letter in string_iterator: yield letter

for letter in yield_letters():
    print(letter)
'''
