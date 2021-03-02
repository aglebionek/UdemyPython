### Counter ###
from collections import Counter
mylist = [1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
print(Counter(mylist))
c = Counter(mylist)
print(c.most_common(2))
### Counter ###


### defaultdict ###
from collections import defaultdict
d = {'a': 10}
try:
    print(d['noSuchKeyyy'])
except Exception as e:
    print(e) # there will be an error

default = defaultdict(lambda: 0) # default value for each key is now set to 0
print(default['noSuchKey']) # there won't be an error here
### defaultdict ###

### namedtuple ###
t = (0, 1, 2)
print(t[2])
from collections import namedtuple
t_named = namedtuple('t_named', ['release', 'press', 'repeat'])
new_named = t_named(0, 1, 2)
print(new_named.release, new_named[0])
### namedtuple ###