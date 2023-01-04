#!/usr/bin/env python
# coding: utf-8

# # Screen space
# 
# ```{figure} /images/viewing_pipeline_screen_space.svg
# :figclass: margin
# ```
# 
# After aligning the world space to the viewer we need to transform the three-dimensional camera space to a two-dimensional space that we can represent on a computer display. This is achieved by defining a **projection plane** that is parallel to the $x$ and $y$ axes of the camera space (we have dropped the $'$ suffix from the camera space co-ordinates) and positioned so that intersects with a negative value on the $z$ axes ({numref}`screen-space-figure`).
# 
# ```{figure} /images/screen_space.svg
# :name: screen-space-figure
# :width: 500px
# 
# The camera space is projected onto a projection plane.
# ```
# 
# ## Orthographic projection
# 
# The simplest kind of projection is the <a href="https://en.wikipedia.org/wiki/Orthographic_projection" target="_blank">**orthographic projection**</a>. This is where we simply ignore the $z$ co-ordinate of each point in the camera space, and consider the positions of the points in the plane to be given by their $x$ and $y$ coordinates.
# 
# An orthographic projection can often be carried out directly without the need for any real processing by simply neglecting the $z$ co-ordinate of all the points. However to retain consistency with our previous matrix representations we could carry out this projection with the use of the transformation matrix (again using homogeneous coordinates) $P$ given by
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		1 & 0 & 0 & 0 \\ 
# 		0 & 1 & 0 & 0 \\
# 		0 & 0 & 0 & 0 \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}.
# \end{align*}
# 
# A point with a position given by the homogeneous camera space co-ordinates $(x, y, z, 1)$ the orthographic screen space co-ordinates are calculated using
# 
# \begin{align*}
# 	P \cdot 
#     \begin{pmatrix} x \\ y \\ z \\ 1  \end{pmatrix}
#     = \begin{pmatrix}
# 		1 & 0 & 0 & 0 \\ 
# 		0 & 1 & 0 & 0 \\
# 		0 & 0 & 0 & 0 \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}
# 	\begin{pmatrix} x \\ y \\ z \\ 1  \end{pmatrix} =
# 	\begin{pmatrix} x \\ y \\ 0 \\ 1  \end{pmatrix}
# \end{align*}
# 
# ## Perspective projection
# 
# The problem with using orthographic projection is that we lose all the depth information and will not be able to tell which object are closer than others. <a href="https://en.wikipedia.org/wiki/3D_projection#Perspective_projection" target="_blank">**Perspective projection**</a> retains this depth information by making objects further away from the viewpoint appear smaller in the projection than similar objects closer to the viewpoint. Perspective projection emulates the way the human eye, or a camera, perceives objects. Rays of light are reflected off objects and travel in straight lines, converging on the eye, or lens, which for these purposes can be thought of as a single point, the viewpoint.
# 
# In perspective projection the viewpoint is often called the centre of projection, it is the point where all the projectors meet. The projected image is formed on a projection plane, a plane parallel to the $xy$-plane and positioned at a distance $f$ from the centre of projection (which after alignment is of course positioned at the origin). The projection plane can be thought of as a glass pane held up between the eye and the scene being viewed ({numref}`perspective-projection-figure`). A projector line from a point in the world space intersects the projection plane in the projected point, and then goes through the centre of projection.
# 
# ```{figure} /images/perspective_projection.svg
# :width: 400px
# :name: perspective-projection-figure
# 
# Perspective projection
# ```
# 
# Consider the diagram shown in {numref}`perspective-projection-calculation-figure` where the point with co-ordinates $(x, y, z)$ is projected onto the projection plane located at $z=-f$ to give to the point with co-ordinates $(x', y', z')$. 
# 
# ```{figure} /images/perspective_projection_calculation.svg
# :width: 500px
# :name: perspective-projection-calculation-figure
# 
# Perspective projection of the point $(x, y, z)$ onto the projection plane located at $z=-f$.
# ```
# 
# The triangle with sides $x$, $y$ and $h$ is similar to the triangle $x'$, $y'$ and $h'$ so
# 
# \begin{align*}
# 	\frac{x'}{f} &= \frac{x}{z}, &
# 	\frac{y'}{f} &= \frac{y}{z}, 
# \end{align*}
# 
# which gives the projected co-ordinates
# 
# \begin{align*}
# 	x' &= \frac{fx}{z}, &
# 	y' &= \frac{fy}{z}.
# \end{align*}
# 
# Both $x'$ and $y'$ are divided by $z / f$ so the homogeneous co-ordinates of the projected point is $(x, y, z, z/f)$ (remember that we divide by the fourth co-ordinates to convert to Cartesian co-ordinates). Therefore the transformation matrix for perspective projection is
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		1 & 0 & 0 & 0 \\
# 		0 & 1 & 0 & 0 \\
# 		0 & 0 & 1 & 0 \\
# 		0 & 0 & 1/f & 0
# 	\end{pmatrix}.
# \end{align*}
# 
# The screen space co-ordinates of a point with the homogeneous camera space co-ordinates $(x, y, z, 1)$ are calculated using
# 
# \begin{align*}
# 	P \cdot \mathbf{x} =
# 	\begin{pmatrix}
# 		1 & 0 & 0 & 0 \\
# 		0 & 1 & 0 & 0 \\
# 		0 & 0 & 1 & 0 \\
# 		0 & 0 & 1/f & 0
# 	\end{pmatrix}
# 	\begin{pmatrix} x \\ y \\ z \\ 1  \end{pmatrix} =
# 	\begin{pmatrix} x \\ y \\ z \\ z/f  \end{pmatrix}
# \end{align*}
# 
# and dividing by the fourth co-ordinates gives $(fx/z, fy/z, f, 1)$ which are the projected co-ordinates derived above.
# 
# ## The viewing frustum
# 
# When we view a virtual world we will only be able to see objects that are located within a finite region known as the **viewing frustum**. Consider the diagram shown in {numref}`viewing-frustum-figure`. The camera space is projected onto the near viewing plane and we view the virtual environment through the display screen which lies on the near projection plane. If we place another plane parallel to the projection plane further away from the origin then we have a volume which will contain the region of the camera space that should be visible to us. The location of the far viewing plane depends upon the computing power available, the further away it is the more of the camera space we will be able to see but this will of course require more computational resources.
# 
# ```{figure} /images/viewing_frustum.svg
# :width: 600px
# :name: viewing-frustum-figure
# 
# The viewing frustum
# ```
# 
# The viewing frustum is an awkward shape to deal with when it comes to clipping objects that lie partially outside so we transform it so that the viewing frustum is a cube with sides of lengths 2 parallel to the co-ordinate axes whilst still maintaining the perspective projection. Consider the diagram shown in {numref}`viewing-frustum-details-figure`. The camera space co-ordinates of the vertices of the screen on the near projection plane are $(l,b,-near)$, $(r,b,-near)$, $(r, t, -near)$ and $(l, t, -near)$ where $l$, $r$, $t$ and $b$ denote left, right, top and bottom edges respectively. The values of these co-ordinates are determined by the width-to-height ratio of the screen and the position of the near viewing plane, the **field of view** angle, $fov$, which controls the horizontal peripheral vision of the viewer.
# 
# ```{figure} /images/viewing_frustum_details.svg
# :width: 500px
# :name: viewing-frustum-details-figure
# 
# The viewing frustum
# ```
# 
# We want to transform the viewing frustum so that its sides are parallel to the co-ordinate axes and each have side lengths of 2 as shown in {numref}`transformed-viewing-frustum-figure`. The co-ordinates of the left, right, top and bottom corners of the screen are transformed so they are either $-1$ or $+1$. 
# 
# ```{figure} /images/clipping_cube.svg
# :width: 400px
# :name: transformed-viewing-frustum-figure
# 
# The transformed viewing frustum
# ```
# 
# The co-ordinate of the right edge, $r$, is calculated using
# 
# \begin{align*}
# 	r &= near \cdot \tan \left( \frac{fov}{2} \right),
# \end{align*}
# 
# and since the centre of the screen is on the $z$ axis then $l = -r$. The co-ordinate of the top edge, $t$, is determined by the aspect ratio of the screen
# 
# \begin{align*}
# 	aspect = \frac{width}{height},
# \end{align*}
# 
# so
# 
# \begin{align*}
# 	aspect &= \frac{r - l}{t - b} = \frac{r}{t} \\
# 	\therefore t &= \frac{r}{aspect} = \frac{r \cdot height}{width},
# \end{align*}
# 
# Common aspect ratios are 4/3 (for old televisions and computer monitors), 16/9 (modern televisions) and 2.35/1 (cinema screens).
# 
# To transform the viewing frustum we need to transform the camera space so that the points within the viewing frustum have $x'$, $y'$ and $z'$ co-ordinates in the range $x',y',z' \in [-1,1]$ and projected using perspective projection. The $x$ camera space co-ordinate for a point that is on the near projection plane and within our screen will be in the range $l \leq x \leq r$. Since $l = -r$ and dividing throughout by $r$ we have
# 
# \begin{align*}
# 	-1 \leq \frac{x}{r} \leq 1,
# \end{align*}
# 
# and using perspective projection $x' = x / near$ then
# 
# \begin{align*}
# 	-1 \leq \frac{near \cdot x}{rz} \leq 1,
# \end{align*}
# 
# so 
# 
# \begin{align*}
# 	x' = \frac{near \cdot x}{rz}.
# \end{align*}
# 
# Doing similar for $y'$ gives
# 
# \begin{align*}
# 	y' = \frac{near \cdot y}{tz}.
# \end{align*}
# 
# Now $x'$ and $y'$ are perspective screen space co-ordinates that are in the range $-1 \leq x', y' \leq 1$. The matrix that performs this transformation is
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & \dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \alpha & \beta \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix},
# \end{align*}
# 
# where $\alpha$ and $\beta$ are some scalars. A point with the homogeneous camera space co-ordinates $(x, y, z, 1)$ the screen space co-ordinates are calculated using
# 
# \begin{align*}
# 	P \cdot \mathbf{x} = \begin{pmatrix}
# 		\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & \dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \alpha & \beta \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix}
# 	\begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix} =
# 	\begin{pmatrix} near \cdot x / r \\ near \cdot y / t \\ \alpha z + \beta \\ z  \end{pmatrix},
# \end{align*}
# 
# and dividing by the fourth co-ordinate to convert to Cartesian co-ordinates we have
# 
# \begin{align*}
# 	\begin{pmatrix}
# 		near \cdot x / (r z) \\ near \cdot y / (t z) \\ (\alpha z + \beta)/z \\ 1
# 	\end{pmatrix}.
# \end{align*}
# 
# The $z$ camera space co-ordinate for a point within the viewing frustum is in the range $near \leq z \leq far$ so we need to transform $near \mapsto 1$ and $far \mapsto -1$. So the minimum and maximum $z'$ co-ordinates are
# 
# \begin{align*}
# 	1 &= \frac{\alpha \cdot near + \beta}{near}, \\
# 	-1 &= \frac{\alpha \cdot far + \beta}{far}.
# \end{align*}
# 
# Solving for $\alpha$ and $\beta$ gives $\alpha = (near + far)/(near - far)$ and $\beta = - 2 \cdot near \cdot far / (near - far)$ so the transformation matrix becomes
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & \dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \dfrac{near + far}{near - far} & - \dfrac{2 \cdot near \cdot far}{near - far} \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix}.
# \end{align*}
# 
# The transformation matrix $P$ combines perspective projection and transformation of the viewing frustum to a cube. The screen space co-ordinates are calculated using
# 
# \begin{align*}
# 	V_{\text{screen}} = P \cdot V_{\text{camera}}.
# \end{align*}
# 
# Each column in $V_{\text{screen}}$ is a homogeneous screen space co-ordinate where the fourth row contains the scaling factor. The Cartesian co-ordinates are calculated by dividing $V_{\text{screen}}$ by the fourth row.
# 
# `````{prf:example}
# :class: seealso
# 
# The camera space from {prf:ref}`camera-space-example` is projected onto the screen space defined by near and far projection plans located at $z = -2$ and $z = -10$, a field of view angle of $fov = 1$ and a width-to-height screen aspect ratio of $aspect = 4/3$. Calculate the screen space co-ordinates of the virtual world.
# 
# ````{dropdown} Solution
# Calculate the $r$ and $t$ co-ordinates
# 
# \begin{align*}
#     r &= |near| \cdot \tan \left( \frac{fov}{2} \right) = 2 \tan(0.5) = 1.0926, \\
#     t &= \frac{r \cdot height}{width} = \frac{1.0926(3)}{4} = 0.8195,
# \end{align*}
# 
# so the projection matrix is
# 
# \begin{align*}
#     P &= \begin{pmatrix}
#         near / r & 0 & 0 & 0 \\
#         0 & near / t & 0 & 0 \\
#         0 & 0 & (near + far)/(near - far) & -2 \cdot near \cdot far / (near - far) \\
#         0 & 0 & 1 & 0 
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -2 / 1.0926 & 0 & 0 & 0 \\
#         0 & -2 / 0.8195 & 0 & 0 \\
#         0 & 0 & (-2 - 10) / (-2 + 10) & -2(-2)(-10) / (-2 + 10) \\
#         0 & 0 & 1 & 0
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -1.8305 & 0 & 0 & 0 \\
#         0 & -2.4407 & 0 & 0 \\
#         0 & 0 & -1.5 & 5 \\
#         0 & 0 & 1 & 0
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the perspective transformation matrix to the camera space co-ordinates from 
# \cref{exm:camera space example}
# 
# \begin{align*}
#     V_{\text{screen}} &= P \cdot V_{\text{view}} \\
#     &= \begin{pmatrix}
#         -1.8305 & 0 & 0 & 0 \\
#         0 & -2.4407 & 0 & 0 \\
#         0 & 0 & -1.5 & 5 \\
#         0 & 0 & 1 & 0
#     \end{pmatrix} 
#     \begin{pmatrix}
#         1.6000 & 0.8000 & -0.4000 & 0.4000 & \cdots \\
#         -0.8745 & -0.9353 & -0.7761 & -0.7164 & \cdots \\
#         -3.7314 & -4.3284 & -2.7364 & -2.1393 & \cdots \\
#         1 & 1 & 1 & 1 & \cdots
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         -2.9288 &  -1.4644 &   0.7322 &  -0.7322 & \cdots \\
#         2.1371 &   2.2828 &   1.8943 &   1.7485 & \cdots \\
#         0.5971 &   1.4926 &  -0.8955 &  -1.7910 & \cdots \\
#        -3.7314 &  -4.3284 &  -2.7364 &  -2.1393 & \cdots
#     \end{pmatrix}.
# \end{align*}
# 
# Dividing $V_{\text{screen}}$ by the fourth row to give the Cartesian screen space co-ordinates
# 
# \begin{align*}
#     V_{screen} &=
#     \begin{pmatrix}
#         0.7849 &   0.3383 &  -0.2676 &   0.3423 & \cdots \\
#         -0.5727 &  -0.5274 &  -0.6923 &  -0.8173 & \cdots \\
#         -0.1600 &  -0.3448 &   0.3273 &   0.8372 & \cdots \\
#          1 &   1 &   1 &   1 & \cdots
#     \end{pmatrix}
# \end{align*}
# ````
# 
# `````
