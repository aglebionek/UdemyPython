#%%
#Problem 1
for i in ['a','b','c']:
    try:
        print(i**2)
    except TypeError:
        print("Can't square a string.")

#%%
#Problem 2
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't devide by zero.")
finally:
    print("All done.")

# %%
#Problem 3
def ask():
    try:
        inp = int(input("Input an integer: "))
    except:
        print("An error occured! Please, try again.")
        ask()
    else:
        print(f"Thank you, your number squared is {inp**2}")

ask()
# %%
