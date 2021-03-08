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