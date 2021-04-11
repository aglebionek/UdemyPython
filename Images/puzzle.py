#%%
from PIL import Image

words = Image.open('word_matrix.png').convert('RGB')
mask = Image.open('mask.png').convert('RGB')

mask = mask.resize((words.size[0], words.size[1]))
mask.putalpha(150)
words.paste(im=mask, box=(0,0), mask=mask)
# answer - great job with images you are the best
# %%
