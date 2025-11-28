#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random
import os
import webbrowser
from IPython.display import Image, display
import ascii_magic
import imageio
import time



# In[13]:


from IPython.display import Image, display
import random

celebration_gifs = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
    "https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"
]

sad_gifs = [
    "https://media.giphy.com/media/9J7tdYltWyXIY/giphy.gif",
    "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
    "https://media.giphy.com/media/10dU7AN7xsi1I4/giphy.gif"
]

def show_happy():
    gif = random.choice(celebration_gifs)
    display(Image(url=gif))

def show_sad():
    gif = random.choice(sad_gifs)
    display(Image(url=gif))


# In[1]:


get_ipython().system('jupyter nbconvert --to python gifs.ipynb')
#to convert into gif to py


# In[2]:


get_ipython().system('pip install ascii_magic pillow #for showing gifs in terminal')



# In[ ]:


#just a trial 
for fr in celebration_gif:
    outro = a


# In[ ]:





# In[ ]:




