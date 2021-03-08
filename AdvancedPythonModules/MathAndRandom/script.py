import math
#help(math)

### rounding
value = 4.35
print(math.floor(value))
print(math.ceil(value))
print(round(value, 1))

# python will round a number to the closest even number to even the roundings
v = 4.5
v2 = 5.5
print(round(v), round(v2)) # v is rounded to 4, v2 to 6
###

### stuff
print(math.log(math.e))
print(math.degrees(math.pi/2))



import random
random.seed(42)
print(random.randint(0,100))

mylist = list(range(20))
print(random.choice(mylist))
print(random.choices(mylist, k=10)) # with repeating elements
print(random.sample(mylist, k=10)) # without repeating elements

#You can also use statistical distributions, like gaussian or uniform
#random.uniform(a=0,b=100)
#random.gauss(mu=0, sigma=1)
#However if you find yourself in need of using these, you probably want to use the numpy module