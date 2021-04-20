#%%
#note - this only works in jupyter notebook
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x): return x**2

interact(func, x=10) # fucntion, default value

# we can use a decorator instead
@interact(x=2) # default value
def func2(x): return x**3

@interact(x=2, y=fixed(3)) # you can fix one argument in place
def func3(x, y): return x*y

# powers of 3 of even numbers from -10 to 10
@interact(x=widgets.IntSlider(value=2, min=-10, max=10, step=2))
def func4(x): return x**3

# dropdown menu, can do it with dict, key is an option, value is the argument
@interact(x=['option1', 'option2', 'option3'])
def func5(x): return x


from IPython.display import display

def f(a, b):
    display(a+b)
    return a+b

w = interactive(f, a=10, b=20)
display(w)

# %%
import ipywidgets as widgets
from IPython.display import display

w1 = widgets.IntText()
w2 = widgets.IntSlider()

display(w1, w2) # we can dipslay multiple widgets at once
link = widgets.jslink((w1, 'value'), (w2, 'value')) # we can also link them together via a key. to check keys, type widget.keys

# you can change widgets style and layout with css-like properties
