import re

text = "The general's phone number is: 555-555-1223"
print("phone" in text)
pattern = "phone"
print(re.search(pattern, text))
match = re.search(pattern, text)
print(match.start(), match.end()) # returns indexes at which the match starts and ends (match.span())

text += " and admirals phone number is"
match = re.search(pattern, text)
print(match.start(), match.end()) # it returns only the first match it finds

matches = re.findall(pattern, text) # this just returns a list of strings
print(matches)
for ma in re.finditer(pattern, text): # this returns the actual match objects
    print(ma.span())

text += ": 901-805-1233"
pattern = r'\d\d\d-\d\d\d-\d\d\d\d' # regular expression (indicated by the r before the string), \d stands for digit
match = re.search(pattern, text) # this again returns only the first match
print(match)
print(match.group()) # this returns the matched text, in this case our phonenumber

for ma in re.finditer(pattern, text): # this way I can iterate over all phonenumbers found
    print(ma.group())


pattern = r'\d{3}-\d{3}-\d{4}' # The {number} means the number of occurences we want to get. It's calles a quantifier
match = re.search(pattern, text)
print(match)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # here I group the regular expression into 3 parts (each one in the bracket). This way I can call each group individually
result = re.search(phone_pattern, text)
print(result.group(2)) # indexing starts at 1 for some reason   


print(re.search(r'cat|dog', 'I like dogs')) # | - or, like in C#
print(re.findall(r'.at', 'The cat in the hat sat there.')) # the period is a wildcard, meaning it will match any character
print(re.findall(r'...at', 'The cat in the hat sat there, then it went splat.')) # the period will match any character, includings spaces
print(re.findall(r'^\d', '2 to the 1. One to the three.')) # checks if the text starts with (^) a number
print(re.findall(r'[^\d]', '2 to the 1.')) # exclude everything that's a digit
# and many many more, google if you ever need everything
# if you ever need to manipulate a string somehow, check if you can do it with regular expressions
