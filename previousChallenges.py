#out = []
#    for i in range(len(string)):
#        if i%2==0:
#            out.append(string[i].lower())
#        else:
#            out.append(string[i].upper())
#    return ''.join(out)

def myfunc(string):
    output = str()
    for i in range(len(string)):
        if i%2==0:
            output += string[i].lower()
        else:
            output += string[i].upper()
    return output

print(myfunc("hello"))

#%%
def lesser_of_two_evens(a,b):
    if(a%2==0 and b%2==0):
        if a<b:
            return a
        else:
            return b
    else:
        if a<b:
            return b
        else:
            return a
        
print(lesser_of_two_evens(2, 5))

#%%
def animal_crackers(text):
    words = text.split()
    if len(words)==2:
        if words[0][0] == words[1][0]:
            return True
    return False

animal_crackers("lol mano")
    
#%%
def makes_twenty(n1,n2):
    return (n1+n2==20 or n1==20 or n2==20)

makes_twenty(10,10)
#%%
def old_macdonald(name):
    output = name[:3].capitalize()
    toJoin = name[3:].capitalize()
    return output + toJoin
    
old_macdonald("macdonald")
#%%
def master_yoda(text):
    output = text.split()
    output.reverse()
    return " ".join(output)

master_yoda("I am home")
# %%
def almost_there(n):
    return (n>=90 and n <=110) or (n>=190 and n<=210) 

almost_there(150)
# %%
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1]==3:
            return True
    return False
            
has_33([1,3,3])
        

# %%
def paper_doll(text):
    tab = [letter * 3 for letter in text]
    return "".join(tab)

paper_doll("Hello")
# %%
def blackjack(a,b,c):
    s = a+b+c
    if s>21 and (a==11 or b ==11 or c==11):
        s=s-10
    if s<=21:
        return s
    else:
        return 'BUST'
        
blackjack(9,9,11)
# %%
def summer_69(arr):
    sum = 0
    ignore = False
    for num in arr:
        if ignore:
            if num == 9:
                ignore = False
            continue
        if num == 6:
            ignore = True
            continue
        sum += num
    return sum

summer_69([2, 1, 6, 9, 11])
# %%
def spy_game(nums):
    zerosAndSevens = str()
    for num in nums:
        if num == 0 or num == 7:
            zerosAndSevens += str(num)
    return "007" in zerosAndSevens

spy_game([1,7,2,0,4,5,0])
# %%
from math import sqrt
def count_primes(n):
    nums = [num for num in range(2,n+1)]
    root = int(sqrt(n)) + 1
    counter = 3
    for i in range(2, root):
        multiplied = i * 2
        while multiplied<=n:
            if multiplied in nums:
                nums.remove(multiplied)
            multiplied = i * counter
            counter+=1
        counter = 3
    print(nums)
    return len(nums)

count_primes(100)
# %%
from math import pi
def vol(rad):
    return (4/3)*pi*rad**3

vol(2)
# %%
def ran_bool(num,low,high):
    return num >= low and num <=high

ran_bool(3,1,10)
# %%
def up_low(s):
    d = {"upperCase": 0, "lowerCase": 0}
    for letter in s:
        if letter.isupper():
            d["upperCase"] += 1
        elif letter.islower():
            d["lowerCase"] += 1
            
    print(f"Original string: {s}")
    print(f"Upper case letters: {d['upperCase']}")
    print(f"Lowercase letters: {d['lowerCase']}")
    
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
# %%
def unique_list(lst):
    return list(set(lst))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
# %%
def multiply(numbers):
    out = 1
    for number in numbers:
        out *= number
    return out

multiply([1,2,3,-4])
# %%
def palindrome(s):
    return s.replace(' ', '') == s[::-1]

palindrome('helleh')
# %%
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    return set(str1.replace(" ", "").lower()) == set(alphabet)

ispangram("The quick brown fox jumps over the lazy dog")
# %%
def test(a): return a**3

list(map(lambda num: num**3, [1, 2, 3, 4]))
# %%
