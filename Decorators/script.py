# I can pass functions as arguments and assign them to variables
# I can also declare function inside functions
# Thus I can do this

def my_decorator(func_to_decorate):
    def wrapper():
        print('Some code to do before the function to decorate is executed')
        func_to_decorate()
        print('Some code to be executed after the function to decorate is executed')
    return wrapper

# Normally you would need to do this
def func_to_decorate():
    print('Please decorate me senpai')

decorated_func = my_decorator(func_to_decorate)
decorated_func()

# the code above and the code below do the same
print()
# But there is a speciall syntax to do that
@my_decorator
def decorated_func2():
    print('pwease decorate meh')

decorated_func2()