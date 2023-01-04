#!/usr/bin/env python
# coding: utf-8

# # Rasterisation
# 
# Computer displays use an array of small squares called pixels which are illuminated using different colours. When the array of pixels is viewed as a whole the brain interprets it as a single image. The pixel array is called a raster array and the process of determining the illumination of the pixels is called **rasterisation**. The image that is approximated as a raster array is known as the **idealised image**.
# 
# ```{glue:figure} smiley-raster-plot
# 
# The idealised image and the raster approximation.
# ```
# 
# ```{prf:definition} Pixel
# :class: note
# 
# A **pixel** is a small square that is illuminated using different colours.
# ```
# 
# ```{prf:definition} Raster
# :class: note
# 
# A **raster** is a rectangular array of pixels.
# ```
# 
# ```{prf:definition} Idealised image
# :class: note
# 
# An **idealised image** is an analogue image that we wish to represent in a raster.
# ```

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from myst_nb import glue
    
    
def circle(R, cx, cy, radius, colour):
    D, x, y = 5 - radius * radius, radius, 0
    while y <= x:
        for i in range(3):
            R[cx + x, cy + y, i] = colour[i]
            R[cx + x, cy - y, i] = colour[i]
            R[cx - x, cy + y, i] = colour[i]
            R[cx - x, cy - y, i] = colour[i] 
            R[cx + y, cy + x, i] = colour[i]
            R[cx + y, cy - x, i] = colour[i]
            R[cx - y, cy + x, i] = colour[i]
            R[cx - y, cy - x, i] = colour[i]
        
        if D > 0:
            D -= 8 * x - 8
            x -= 1
        
        D += 8 * y + 12
        y += 1
        
    return R


# Idealised image
face_cx, face_cy, face_r = 0.5, 0.5, 0.4
eye1_cx, eye1_cy, eye1_r = 0.33, 0.6, 0.06
eye2_cx, eye2_cy, eye2_r = 0.67, 0.6, 0.06

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

circle1 = plt.Circle((face_cx, face_cy), face_r, color="#FFFF00", ec="k", lw=12)
circle2 = plt.Circle((eye1_cx, eye1_cy), eye1_r, color="k")
circle3 = plt.Circle((eye2_cx, eye2_cy), eye2_r, color="k")
arc = patches.Arc((0.5, 0.5), 0.5, 0.5, angle=0, theta1=210, theta2=330, lw=12)

ax[0].add_patch(circle1)
ax[0].add_patch(circle2)
ax[0].add_patch(circle3)
ax[0].add_patch(arc)
ax[0].set_aspect("equal")
ax[0].axis("off")

# Raster
n = 20
R = 255 * np.ones((n, n, 3)).astype(int)

for i in range(n+1):
    for j in range(n+1):
        if (i - face_cx * n + 1) ** 2 + (j - face_cy * n) ** 2 <= (face_r * n) ** 2:
            R[i,j,:] = [255, 255, 0]
            
        ax[1].add_patch(plt.Rectangle((i-0.5,j-0.5), 1, 1, fill=False))

R = circle(R, int(face_cx*n)-1, int(face_cy*n), int(face_r*n), [0, 0, 0])

R[6:8, 13:15, :] = [0,0,0]
R[6:8, 6:8, :] = [0,0,0]
R[12,6,:] = [0,0,0]
R[13,7:8,:] = [0,0,0]
R[14,8:13,:] = [0,0,0]
R[13,13:14,:] = [0,0,0]
R[12,14,:] = [0,0,0]

ax[1].imshow(np.flipud(R))
ax[1].set_aspect("equal")
ax[1].axis([-1, 21, -1, 21])
ax[1].axis("off")

glue("smiley-raster-plot", fig, display=False)


# ## The RGB colour model
# 
# The **RGB** colour model uses the three primary colours <span style="color: red;">Red</span>, <span style="color: green;">Green</span> and <span style="color: blue;">Blue</span> (RGB) that are added to produce colours in the visible spectrum. Using a single bit for each primary colour (i.e., adding all of that colour or none of that colour) means that it is possible to produce eight colours: <span style="color: red;">red</span>, <span style="color: yellow;">yellow</span>, <span style="color: green;">green</span>, <span style="color: cyan;">cyan</span>, <span style="color: blue;">blue</span>, <span style="color: magenta;">magenta</span>, black and <span style="background-color:black;color:white">white</span> as shown in {ref}`rgb-table`. For example mixing full amounts of red and green results in pure yellow. 
# 
# ### 24-bit colour 
# 
# Adding proportions of each primary colours means that many more colours can be produced. Using 8 bits for each primary colour means that there are a possible $2^8 = 256$ different quantities of that colour. Combining the three primary colours means that the number of colours that can be produced is $3 \times 2^8 = 16,772,216$. It is estimated that the most number of colours that the human eye can distinguish is approximately 10 million so 24 bit colour (known as [true color](https://en.wikipedia.org/wiki/Color_depth#True_color_(24-bit))) is considered sufficient.
# 
# :::{figure} ../images/rgb_wheel.png
# :width: 300px
# 
# RGB color wheel
# :::
# 
# Since there are 256 levels of the three primary colours in the true color model we can use the integers 0 to 255 in an ordered triplet. For example, the colour <span style="color: cyan;">cyan</span> is made by mixing full amounts of green and blue which corresponds to the triplet `[0, 255, 255]`. Most software packages also accept [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal) (base-16) colour codes where the values in the triplet are represented using 2-digit hexadecimal numbers 00 to FF which follow a # symbol. For example, <span style="color: cyan;">cyan</span> is represented using `"#00FFFF"`. 
# 
# ```{list-table} 1-bit RGB codes
# :header-rows: 1
# :name: rgb-table
# 
# * - Colour
#   - RGB triplet
#   - Hexadecimal colour code
# * - <span style="color: black;">Black</span>
#   - `(0, 0, 0)`
#   - `"#FFFFFF"`
# * - <span style="color: red;">Red</span>
#   - `(255, 0, 0)`
#   - `"#FF0000"`
# * - <span style="color: yellow;">Yellow</span>
#   - `(255, 255, 0)`
#   - `"#FFFF00"`
# * - <span style="color: green;">Green</span>
#   - `(0, 255, 0)`
#   - `"#00FF00"`
# * - <span style="color: cyan;">Cyan</span>
#   - `(0, 255, 255)`
#   - `"#00FFFF"`
# * - <span style="color: blue;">Blue</span>
#   - `(0, 0, 255)`
#   - `"#0000FF"`
# * - <span style="color: magenta;">Magenta</span>
#   - `(255, 0, 255)`
#   - `"#FF00FF"`
# * - <span style=" background-color: black; color: white;">White</span>
#   - `(255, 255, 255)`
#   - `"#FFFFFF"`
# ```
# 
# ## Raster arrays
# 
# The information that defines a raster can be stored in a raster array. If a raster has a width of $N_x$ pixels and a height of $N_y$ pixels then it can be defined as an $N_y \times N_x \times 3$ array. The colour of each of the pixels in the raster is defined by the 3 levels for the red, green and blue components.
# 
# The matplotlib command for reading in an image file is `plt.imread(<filename>)`. For example, the following code reads in the image file `cavendish.png` which if a photograph of my cat Cavendish and prints the size of the raster array.

# In[2]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("../images/cavendish.jpg")
print(img.shape)


# So the raster array has a height of $N_y = 600$ pixels, a width of $N_x=800$ pixels with each pixel defined by a colour triplet.
# 
# The matplotlib command for displaying a raster array `X` is `plt.imshow(X)`

# In[3]:


imgplot = plt.imshow(img)


# Now we have the raster array for the image we can use Python commands to manipulate the image. For example, the following code sets the colour of each pixel to either black or white depending on whether the sum of the colour triplet is greater or less than 383 which is halfway between 0 and 767 .

# In[4]:


colour_sum = np.sum(img, axis=2)
imgbw = np.copy(img)
imgbw[colour_sum > 382,:] = [255,255,255]
imgbw[colour_sum <= 382,:] = [0,0,0]
imgbwplot = plt.imshow(imgbw)


# ## Pixel co-ordinates
# 
# You may have noticed that the vertical axes on the image plots have a scale that starts at 0 at the top and increases as we move down the rows of pixels. The reason for this is that digital displays are refreshed using horizontal lines of pixels starting at the top row and moving down to the bottom. 
# 
# If the raster represents a region defined by the $x$ and $y$ Euclidean space co-ordinates $x, y \in [0, 1]$ which is to be represented by an $N_y \times N_x$ raster then the corresponding pixel co-ordinates are
# 
# :::{math}
# 
# \begin{align}
#     x_{pixel} &= \lfloor x \cdot N_x \rfloor, \\
#     y_{pixel} &= \lfloor (1 - y) \cdot N_y \rfloor, 
# \end{align}
# :::
# 
# where $\lfloor \cdot \rfloor$ is rounds the contents to the integer below. Note that the $y$ co-ordinate is subtracted from 1 to ensure that the pixel co-ordinates $(0, 0)$ correspond to $(0, 1)$, i.e., the top-left hand pixel in the raster. 
# 
# The Python function defined below calculates the pixel co-ordinates from the $x$ and $y$ Euclidean space co-ordinates

# In[5]:


def pixelcoords(x, y, Nx, Ny):
    xpixel = int(x * Nx)
    ypixel = int((1 - y) * Ny)
    return xpixel, ypixel

