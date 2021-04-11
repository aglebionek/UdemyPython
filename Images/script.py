#%%
from PIL import Image

mac = Image.open(fp='example.jpg')

#mac.crop((0,0,100,100))

pencils = Image.open(fp='pencils.jpg')

x = 0
y = 0

w = pencils.size[0] / 3
h = pencils.size[1] / 10

#pencils.crop((x, y, w, h))

y = 1100
h = pencils.size[1]

#pencils.crop((x, y, w, h))

x = mac.size[0] / 2 - 200
w = mac.size[0] / 2 + 200
y = 800
h = mac.size[1]

computer = mac.crop((x, y, w, h))
mac.paste(im=computer, box=(0,0))

mac.resize((3000, 700))
mac.rotate(90)
# %%
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png').convert('RGB')
red.putalpha(100)
blue.putalpha(100)
blue.paste(im=red, box=(0,0), mask=red)
blue.save('purple.png')
# %%
