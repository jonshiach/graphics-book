#!/usr/bin/env python
# coding: utf-8

# (screen-space-section)=
# # Screen space
# 
# ```{figure} /images/viewing_pipeline_screen_space.svg
# :figclass: margin
# ```
# 
# After aligning the world space to the viewer we need to transform the three-dimensional camera space to a two-dimensional space that we can represent on a computer display. This is achieved by defining a **projection plane** that is parallel to the $x$ and $y$ axes of the camera space (we have dropped the $^\ast$ suffix from the camera space co-ordinates) and positioned so that intersects with a negative value on the $z$ axes ({numref}`screen-space-figure`).
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
# The orthographic projection of the camera space from {prf:ref}`camera-space-example` is shown in {numref}`orthographic-projection-figure`. Note that the two house objects appear the same size even though the house object on the right is closer to the viewer.
# 
# ```{figure} /images/camera_space_example_2.png
# :width: 400px
# :name: orthographic-projection-figure
# 
# The camera space from {prf:ref}`camera-space-example` projected using orthographic projection.
# ```
# 
# ## Perspective projection
# 
# We have seen in {numref}`orthographic-projection-figure` that the problem with using orthographic projection is that we lose all the depth information and will not be able to tell which object are closer than others. <a href="https://en.wikipedia.org/wiki/3D_projection#Perspective_projection" target="_blank">**Perspective projection**</a> retains this depth information by making objects further away from the viewpoint appear smaller in the projection than similar objects closer to the viewpoint. Perspective projection emulates the way the human eye, or a camera, perceives objects. Rays of light are reflected off objects and travel in straight lines, converging on the eye, or lens, which for these purposes can be thought of as a single point, the viewpoint.
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
# :width: 600px
# :name: perspective-projection-calculation-figure
# 
# Perspective projection of the point $(x, y, z)$ onto the projection plane located at $z=-f$.
# ```
# 
# The triangle with sides $x$, $y$ and $h$ is similar to the triangle $x'$, $y'$ and $h'$ so
# 
# \begin{align*}
# 	\frac{x'}{-f} &= \frac{x}{z}, &
# 	\frac{y'}{-f} &= \frac{y}{z}, 
# \end{align*}
# 
# which gives the projected co-ordinates
# 
# \begin{align*}
# 	x' &= -\frac{fx}{z}, &
# 	y' &= -\frac{fy}{z}.
# \end{align*}
# 
# Both $x'$ and $y'$ are divided by $-z / f$ so the homogeneous co-ordinates of the projected point is $(x, y, z, -z/f)$ (remember that we divide by the fourth co-ordinates to convert to Cartesian co-ordinates). Therefore the transformation matrix for perspective projection is
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		1 & 0 & 0 & 0 \\
# 		0 & 1 & 0 & 0 \\
# 		0 & 0 & 1 & 0 \\
# 		0 & 0 & -1/f & 0
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
# 		0 & 0 & -1/f & 0
# 	\end{pmatrix}
# 	\begin{pmatrix} x \\ y \\ z \\ 1  \end{pmatrix} =
# 	\begin{pmatrix} x \\ y \\ z \\ -z/f  \end{pmatrix}
# \end{align*}
# 
# and dividing by the fourth co-ordinates gives $(-fx/z, -fy/z, -f, 1)$ which are the projected co-ordinates derived above.
# 
# (viewing-frustum-section)=
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
# The viewing frustum is an awkward shape to deal with when it comes to clipping objects that lie partially outside so we transform it so that the viewing frustum is a cube with sides of lengths 2 parallel to the co-ordinate axes whilst still maintaining the perspective projection. Consider the diagram shown in {numref}`viewing-frustum-details-figure` where a near viewing plane is positioned at distance $near$ from the origin of the camera space. The camera space co-ordinates of the vertices of the screen on the near projection plane are $(l,b,-near)$, $(r,b,-near)$, $(r, t, -near)$ and $(l, t, -near)$ where $l$, $r$, $t$ and $b$ denote left, right, top and bottom edges respectively. The values of these co-ordinates are determined by the width-to-height ratio of the screen and the position of the near viewing plane, the **field of view** angle, $fov$, which controls the horizontal peripheral vision of the viewer.
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
# 	aspect &= \frac{r - l}{t - b} = \frac{r - (-r)}{t - (-t)} = \frac{r}{t} \\
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
# and using perspective projection $x' = -near \cdot x / z$ then
# 
# \begin{align*}
# 	-1 \leq -\frac{near \cdot x}{rz} \leq 1,
# \end{align*}
# 
# so 
# 
# \begin{align*}
# 	x' = -\frac{near \cdot x}{rz}.
# \end{align*}
# 
# Doing similar for $y'$ gives
# 
# \begin{align*}
# 	y' = -\frac{near \cdot y}{tz}.
# \end{align*}
# 
# Now $x'$ and $y'$ are perspective screen space co-ordinates that are in the range $-1 \leq x', y' \leq 1$. The matrix that performs this transformation is
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		-\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & -\dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \alpha & \beta \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix},
# \end{align*}
# 
# where $\alpha$ and $\beta$ are some scalars. A point with the homogeneous camera space co-ordinates $(x, y, z, 1)$ the screen space co-ordinates are calculated using
# 
# \begin{align*}
# 	P \cdot \mathbf{x} = \begin{pmatrix}
# 		-\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & -\dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \alpha & \beta \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix}
# 	\begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix} =
# 	\begin{pmatrix} -near \cdot x / r \\ -near \cdot y / t \\ \alpha z + \beta \\ z  \end{pmatrix},
# \end{align*}
# 
# and dividing by the fourth co-ordinate to convert to Cartesian co-ordinates we have
# 
# \begin{align*}
# 	\begin{pmatrix}
# 		-near \cdot x / (r z) \\ -near \cdot y / (t z) \\ (\alpha z + \beta)/z \\ 1
# 	\end{pmatrix}.
# \end{align*}
# 
# The $z$ camera space co-ordinate for a point within the viewing frustum is in the range $-near \leq z \leq -far$ so we need to transform $-near \mapsto 1$ and $-far \mapsto -1$. So the minimum and maximum $z'$ co-ordinates are
# 
# \begin{align*}
# 	1 &= \frac{-near \cdot \alpha + \beta}{-near}, \\
# 	-1 &= \frac{-far \cdot \alpha + \beta}{-far}.
# \end{align*}
# 
# Solving for $\alpha$ and $\beta$ gives $\alpha = (near + far)/(near - far)$ and $\beta = 2 \cdot near \cdot far / (near - far)$ so the transformation matrix becomes
# 
# \begin{align*}
# 	P = \begin{pmatrix}
# 		-\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & -\dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \dfrac{near + far}{near - far} & \dfrac{2 \cdot near \cdot far}{near - far} \\
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
# :label: screen-space-example
# 
# The camera space from {prf:ref}`camera-space-example` is projected onto the screen space defined by near and far projection plans located at distances $near = 1$ and $far = 9$ from the origin, a field of view angle of $fov = \pi/3$ and a width-to-height screen aspect ratio of $4/3$. Calculate the screen space co-ordinates of the virtual world.
# 
# ````{dropdown} Solution
# First we calculate the $r$ and $t$ co-ordinates
# 
# \begin{align*}
#     r &= near \cdot \tan \left( \frac{fov}{2} \right) = 2 \tan\left(\frac{\pi}{6}\right) \approx 1.1547, \\
#     t &= \frac{r \cdot height}{width} = \frac{1.1547(3)}{4} \approx 0.8660,
# \end{align*}
# 
# so the projection matrix is
# 
# \begin{align*}
#     P &= 
#     \begin{pmatrix}
# 		-\dfrac{near}{r} & 0 & 0 & 0 \\
# 		0 & -\dfrac{near}{t} & 0 & 0 \\
# 		0 & 0 & \dfrac{near + far}{near - far} & \dfrac{2 \cdot near \cdot far}{near - far} \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix} \\
#     &=
#     \begin{pmatrix}
# 		-\dfrac{2}{1.1547} & 0 & 0 & 0 \\
# 		0 & -\dfrac{2}{0.8660} & 0 & 0 \\
# 		0 & 0 & \dfrac{1 + 9}{1 - 9} & \dfrac{2 \cdot 1 \cdot 9}{1 - 9} \\
# 		0 & 0 & 1 & 0 
# 	\end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -1.8660 & 0 & 0 & 0 \\
#         0 & -1.1547 & 0 & 0 \\
#         0 & 0 & -1.2222 & -2.2222 \\
#         0 & 0 & 1 & 0
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the perspective transformation matrix to the camera space co-ordinates from 
# {prf:ref}`camera-space-example`
# 
# \begin{align*}
#     V_{\text{screen}} &= P \cdot V_{\text{view}} \\
#     &= 
#     \begin{pmatrix}
#         -1.8660 & 0 & 0 & 0 \\
#         0 & -1.1547 & 0 & 0 \\
#         0 & 0 & -1.2222 & -2.2222 \\
#         0 & 0 & 1 & 0
#     \end{pmatrix} 
#     \begin{pmatrix}
#         1.4142 &   0.7071 &  -0.7071 &        0 & \cdots \\
#         -1.2309 &  -1.1078 &  -1.3540 &  -1.4771 & \cdots \\
#         -3.0899 &  -3.7862 &  -2.3936 &  -1.6973 & \cdots \\
#         1&   1&   1&   1& \cdots 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         -1.2247 &  -0.6124 &   0.6124 &        0  & \cdots \\
#         1.4213 &   1.2792 &   1.5635 &   1.7056 & \cdots \\
#         1.5543 &   2.4053 &   0.7032  & -0.1478 & \cdots \\
#         -3.0899 &  -3.7862 &  -2.3936  & -1.6973 & \cdots 
#     \end{pmatrix}.
# \end{align*}
# 
# Since these are homogeneous co-ordinates we need to divide by the fourth row to give the Cartesian co-ordinates
# 
# \begin{align*}
#     V_{screen} &=
#     \begin{pmatrix}
#         0.3964 &   0.1617 &  -0.2558 &        0  & \cdots \\
#        -0.4600 &  -0.3379 &  -0.6532 &  -1.0049 & \cdots \\
#        -0.5030 &  -0.6353 &  -0.2938 &   0.0871 & \cdots \\
#         1 &   1 &   1 &   1 & \cdots 
#     \end{pmatrix}
# \end{align*}
# ````
# 
# `````
# 
# ## MATLAB code
# 
# The MATLAB code below calculates the screen space co-ordinates for the virtual world from {prf:ref}`world-space-example` with the viewing parameters from {prf:ref}`camera-space-example` and projected using perspective projection with the screen parameters from {prf:ref}`screen-space-example`.
# 
# ```matlab
# % Define projection parameters
# near = 1;
# far = 5;
<<<<<<< Updated upstream
# fov = pi/2;
=======
# fov = pi/3;
>>>>>>> Stashed changes
# aspect = 4/3;
# 
# % Calculate projection matrix
# r = near * tan(fov / 2);
# t = r / aspect;
# P = [-near / r, 0, 0, 0 ;
#      0, -near / t, 0, 0 ;
#      0, 0, (near + far) / (near - far), 2 * near * far / (near - far) ;
#      0, 0, 1, 0 ];
# 
# % Calculate screen space co-ordinates
# Vscreen = P * Vcamera;
# Vscreen = Vscreen ./ Vscreen(4,:);
# 
# % Plot camera space (from viewing position)
# figure()
# h1 = axes;
# patch('Vertices', Vscreen([1,3,2],:)', 'Faces', F, FaceColor='w', FaceAlpha=0.75, LineWidth=2)
# xlabel('$x$', 'Interpreter', 'latex', 'FontSize', 18)
# ylabel('$z$', 'Interpreter', 'latex', 'FontSize', 18)
# zlabel('$y$', 'Interpreter', 'latex', 'FontSize', 18)
# set(h1, 'Ydir', 'reverse')
# view(0,0)
# axis([-1, 1, -1, 1, -1, 1])
# grid on
# ```
# 
<<<<<<< Updated upstream
# A plot of the camera space with the viewing frustum defined using the viewing parameter from {prf:ref}`screen-space-example` is shown in {numref}`screen-space-example-figure-1`. 
=======
# A plot of the camera space with the viewing frustum defined using the viewing parameter from {prf:ref}`screen-space-example` is shownin {numref}`screen_space_example_1`. 
>>>>>>> Stashed changes
# 
# ```{figure} /images/screen_space_example_1.png
# :width: 400px
# :name: screen-space-example-figure-1
# 
# The camera space and viewing frustum from {prf:ref}`screen-space-example`.
# ```
# 
<<<<<<< Updated upstream
# The affect of applying the perspective projection to the camera space is shown in {numref}`screen-space-example-figure-2`. Note that the viewing frustum is now a unit cube and the camera space objects have been skewed so that the polygons of the object closest to the viewer are larger than similar polygons further away. The plot of the screen space viewed looking down the $z$-axis is shown in in {numref}`screen-space-example-figure-3` which gives a realistic representation of the world space. 
# 
# ```{figure} /images/screen_space_example_2.png
# :width: 400px
# :name: screen-space-example-figure-2
=======
# The affect of applying the persective projection to the camera space is shown in {numref}`screen-space-example-figure-1`. Note that the viewing frustum is now a unit cube and the camera space objects have been skewed so that the polygons of the object closest to the viewer are larger than similar polygons further away. The plot of the screen space viewed looking down the $z$-axis is showin in {numref}`screen-space-example-figure-2` which gives a realistic representation of the world space. 
# 
# ```{figure} /images/screen_space_example_3.png
# :width: 400px
# :name: screen-space-example-figure-1
>>>>>>> Stashed changes
# 
# The screen space from {prf:ref}`screen-space-example` viewed from an arbitrary point.
# ```
# 
<<<<<<< Updated upstream
# ```{figure} /images/screen_space_example_3.png
# :width: 400px
# :name: screen-space-example-figure-3
=======
# ```{figure} /images/screen_space_example_2.png
# :width: 400px
# :name: screen-space-example-figure-2
>>>>>>> Stashed changes
# 
# The screen space from {prf:ref}`screen-space-example` viewed looking down the $z$-axis.
# ```
