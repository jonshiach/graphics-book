#!/usr/bin/env python
# coding: utf-8

# (drawing-circles-section)=
# # Drawing circles
# 
# Now that we have the ability to rasterise straight lines the next fundamental problem is the rasterisation of circles. This can be done by deriving a Bresenham-type algorithm that uses the [Cartesian equation of a circle](https://en.wikipedia.org/wiki/Circle#Equations) to determine which of two candidate pixels are plotted.
# 
# The circle line drawing algorithms can use the concept of **circle symmetry** to reduce the number of computations required to rasterise a circle. Consider {numref}`circle-symmetry-figure` where a circle is centred at the origin. If the coordinate of a point on the circle in the shaded octant where $x > y$ is known to be $(x,y)$ then the corresponding points on the circle in the other seven octants can be found via circle symmetry through combinations of $(\pm x,\pm y)$ and $(\pm y,\pm x)$.
# 
# ```{figure} /images/circle_symmetry.svg
# :name: circle-symmetry-figure
# :width: 400px
# 
# Circle symmetry can be used to calculate points on a circle.
# ```
# 
# For circles not centred at the original, which will be the case in the vast majority of applications, we calculate the co-ordinates of a point on the circle in the first octant $(x, y)$ and then add the co-ordinates of the circle centre $(c_x,c_y)$ giving the following eight pixel co-ordinates
# 
# \begin{align*}
#     (c_x + x, c_y + y), & 
#     &(c_x + x, c_y - y), \\
#     (c_x - x, c_y + y), &
#     &(c_x - x, c_y - y), \\
#     (c_x + y, c_y + x), &
#     &(c_x + y, c_y - x), \\
#     (c_x - y, c_y + x), &
#     &(c_x - y, c_y - x).
# \end{align*}

# ## The midpoint algorithm
# 
# The **midpoint algorithm** {cite}`pitteway:1967` is a form of Bresenham's algorithm that is used to draw circles. Consider the <a href="https://en.wikipedia.org/wiki/Circle#Equations" target="_blank">Cartesian equation of a circle</a> centred at $(0, 0)$ with radius $r$
# 
# $$x^2 + y^2 = r^2,$$
# 
# which an be rearranged to
# 
# $$0 = x^2 + y^2 - r^2.$$
# 
# Let $f(x,y) = x^2 + y^2 - r^2$ then like Bresenham's algorithm, the sign of $f(x,y)$ tells us whether the pixel at $(x,y)$ is inside or outside of the circle
# 
# \begin{align*}
#     f(x,y) 
#     \begin{cases}
#         \geq 0, & \text{$(x,y)$ is on or outside of the circle,} \\
#         <0, & \text{$(x,y)$ is inside the circle.}
#     \end{cases}
# \end{align*}
# 
# To derive an algorithm to rasterise a circle we assume that the circle is centred at $(0, 0)$ and we start at the pixel at the 3 o'clock position with pixel co-ordinates $(r,0)$. We then move clockwise around the circle calculating the pixels that lie closest to the idealised circle until $x=y$ which is the end of the first octant. For each pixel co-ordinates we calculate, the pixel co-ordinates of the corresponding pixels in the 7 other octants are calculated using circle symmetry. 
# 
# Once a pixel $(x,y)$ has been plotted we move down by one pixel so that $y=y+1$ and we have a choice between the two pixels at $(x-1,y+1)$ and $(x,y+1)$ to plot next. Similar to Bresenham's line drawing algorithm, we define a decision variable $d=f(x-\frac{1}{2}, y+1)$ which is the distance between the plotted pixel and the midpoint between the two candidate pixels ({numref}`midpoint-algorithm-figure`). 
# 
# ```{figure} /images/midpoint_algorithm.svg
# :width: 250px
# :name: midpoint-algorithm-figure
# 
# Determining the pixels on a circle using the midpoint algorithm.
# ```
# 
# The change in the value of $d$, denoted by $\Delta d$, depends upon which of the candidate pixels has been plotted. If $d \leq 0$ then the pixel at $(x,y+1)$ has been chosen and $\Delta d$ is the difference between $f(x-\tfrac{1}{2},y+1)$ and $f(x-\tfrac{1}{2},y+2)$
# 
# \begin{align*}
#     \Delta d &= f(x-\tfrac{1}{2},y+2) - f(x-\tfrac{1}{2},y+1) \\
#     &= (x - \tfrac{1}{2})^2 + (y+2)^2 - r^2 - (x + \tfrac{1}{2})^2 - (y+1)^2 + r^2 \\
#     &= y^2 + 4y + 4 - y^2 - 2y - 1 \\
#     &= 2y + 3.
# \end{align*}
# 
# Else if $d > 0$ then the pixel at $(x-1,y+1)$ has been chosen and $\Delta d$ is the difference between $f(x-\tfrac{1}{2},y+1)$ and $f(x - \tfrac{3}{2},y+2)$
# 
# \begin{align*}
#     \Delta d &= f(x - \tfrac{3}{2},y+2) - f(x-\tfrac{1}{2},y+1) \\
#     &= (x - \tfrac{3}{2})^2 + (y+2)^2 - r^2 - (x-\tfrac{1}{2})^2 - (y+1)^2 + r^2 \\
#     &= x^2 - 3x + \tfrac{9}{4} + y^2 + 4y + 4 - x^2 + x - \tfrac{1}{4} - y^2 - 2y - 1 \\
#     &= 2y - 2x + 5.
# \end{align*}
# 
# Since the first pixel to be plotted has the co-ordinates $(r,0)$, the initial value of $d$ is the difference between $f(r,0)$ and $f(r-\tfrac{1}{2},1)$
# 
# \begin{align*}
#     d &= f(r,0) - f(r-\tfrac{1}{2},1) \\
#     &= r^2 + 0^2 - r^2 - (r-\tfrac{1}{2})^2 - 1^2 + r^2 \\
#     &= -r^2 + r - \tfrac{1}{4} - 1 + r^2 \\
#     &= r - \tfrac{5}{4}.
# \end{align*}
# 
# Here we have a floating point number in $\frac{5}{4}=1.25$. To write down an algorithm that only uses integer numbers we simply round this number to $1$
# 
# \begin{align*}
#     d &= r - 1.
# \end{align*}
# 
# We do not need to adjust the expressions for $\Delta d$ since these used the values of the pixel co-ordinates. 
# 
# ```{prf:algorithm} Midpoint algorithm
# :label: midpoint-algorithm
# 
# **Inputs** A raster array $R$, pixel co-ordinates of the centre of a circle $(c_x, c_y)$ the radius of the circle $r$ and the colour of the circle line defined by the RBG triplet $colour$.
# 
# **Output** A raster array $R$.
# 
# - $x \gets r$
# - $y \gets 0$
# - $d \gets 1 - r$.
# - While $x \geq y$ do
#     - $R(c_x \pm x, c_y \pm y) \gets colour$ (use circle symmetry to plot the 8 pixels)
#     - $R(c_x \pm y, c_y \pm x) \gets colour$
#     - If $d \leq 0$ then
#         - $d \gets D + 2y + 3$
#     - Else
#         - $d \gets d + 2y - 2x + 5$
#         - $x \gets x - 1$
#     - $y \gets y + 1$   
# - Return $R$
# ```
# 
# `````{prf:example} 
# :class: seealso
# :label: midpoint-example
# 
# Use the midpoint algorithm to rasterise a circle centred at $(12, 12)$ with radius 10.
# 
# ````{dropdown} Solution
# 
# \begin{align*}
#     x &= 10, \\
#     y &= 0, \\
#     d &= 1 - 10 = -9.
# \end{align*}
# 
# Stepping through the algorithm:
# \begin{align*}
# 	x &= 10, & y &= 0, & d &\leq 0, & \therefore d &= -9 + 2(0) + 3 = -6, \\
# 	x &= 10, & y &= 1, & d &\leq 0, & \therefore d &= -6 + 2(1) + 3 = -1, \\
# 	x &= 10, & y &= 2, & d &\leq 0, & \therefore d &= -1 + 2(2) + 3 = 6,\\
# 	x &= 10, & y &= 3, & d &> 0, & \therefore d &= 6 + 2(3) - 2(10) + 5 = -3, \\
# 	x &=  9, & y &= 4, & d &\leq 0, & \therefore d &= -3 + 2(4) + 3 = 8, \\
# 	x &=  9, & y &= 5, & d &> 0, & \therefore d &= 8 + 2(5) - 2(9) + 5 = 5, \\
# 	x &=  8, & y &= 6, & d &> 0, & \therefore d &= 5 + 2(6) - 2(8) + 5 = 6, \\
# 	x &=  7, & y &= 7.
# \end{align*}
# 
# Adding the centre co-ordinates gives the following co-ordinates for the pixels on the first octant of the circle
# 
# \begin{align*}
# 	(22,12), && (22, 13), && (22, 14), && (22, 15), \\
#     (21, 16), && (21, 17), && (20, 18), && (19, 19).
# \end{align*}
# 
# Applying circle symmetry to determine the pixels in the other seven octants completes the circle.
# 
# ```{figure} /images/midpoint_example.png
# :figwidth: 400px
# ```
# 
# ````
# `````
