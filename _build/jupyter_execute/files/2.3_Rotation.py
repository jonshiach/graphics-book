#!/usr/bin/env python
# coding: utf-8

# (rotation-section)=
# # Rotation
# 
# **Rotation** in $\mathbb{R}^3$ is a linear transformation that rotates a set of points by some angle about one of the $x$, $y$ or $z$-axes. The direction of rotation is assumed to be *anti-clockwise* when viewed looking down the axis towards the origin ({numref}`3D-rotation-figure`).
# 
# ```{figure} /images/3D_rotation.svg
# :name: 3D-rotation-figure
# :width: 250px
# 
# The direction of rotation is assumed as anti-clockwise when viewed looking towards the origin.
# ```
# 
# ```{figure} /images/rotation.svg
# :name: rotation-figure
# :width: 300px
# 
# Rotation of the vector $\mathbf{u}$ anti-clockwise about the origin.
# ```
# 
# Consider the diagram in {numref}`rotation-figure` that shows the axes from {numref}`3D-rotation-figure` when viewed looking down the $x$-axis. The point with position vector $\mathbf{u}=(u_x, u_y, u_z)$ is rotated anti-clockwise about the $x$-axis by the angle $\theta$ to $\mathbf{v}=(v_x, v_y, v_z)$. To determine the linear transformation we first consider the rotation of a vector pointing along the $x$-axis which has the same magnitude of $\mathbf{u}$, i.e., $|\mathbf{u}| \mathbf{e}_1$, rotated by the angle $\phi$. Forming a right-angled triangle with the angle $\phi$ and hypotenuse of length $|\mathbf{u}|$ then
# 
# ```{math}
# :label: rotation-equation-1
# 
# \begin{align*}
#     \cos(\phi) &= \frac{u_x}{|\mathbf{u}|} & \therefore u_x &= |\mathbf{u}| \cos(\phi), \\
#     \sin(\phi) &= \frac{u_y}{|\mathbf{u}|} & \therefore u_y &= |\mathbf{u}| \sin(\phi).
# \end{align*}
# ```
# 
# Doing similar for rotating $\mathbf{u}$ by the angle $\theta$ to $\mathbf{v}$ we have
# 
# \begin{align*}
#     v_x &= |\mathbf{u}| \cos(\phi + \theta), \\
#     v_y &= |\mathbf{u}| \sin(\phi + \theta), \\
#     v_z &= u_x
# \end{align*}
# 
# using the [angle sum indentities](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Angle_sum_and_difference_identities)
# 
# \begin{align*}
#     \cos(\phi + \theta) &= \cos(\phi) \cos(\theta) - \sin(\phi) \sin(\theta), \\
#     \sin(\phi + \theta) &= \sin(\phi) \cos(\theta) + \cos(\phi) \sin(\theta),
# \end{align*}
# 
# then we have
# 
# ```{math}
# :label: rotation-equation-2
# 
# \begin{align*}
#     v_x &= |\mathbf{u}| \cos(\phi) \cos(\theta) - |\mathbf{u}|\sin(\phi) \sin(\theta) \\
#     v_y &= |\mathbf{u}| \sin(\phi) \cos(\theta) + |\mathbf{u}|\cos(\phi) \sin(\theta).
# \end{align*}
# ```
# 
# Substituting equation {eq}`rotation-equation-1` into equation {eq}`rotation-equation-2` 
# 
# \begin{align*}
#     v_x &= u_x \cos(\theta) - u_y \sin(\theta), \\
#     v_y &= u_y \cos(\theta) + u_x \sin(\theta), \\
#     v_z &= u_z
# \end{align*}
# 
# which can be written as the matrix equation.
# 
# \begin{align*}
#     \begin{pmatrix} v_x \\ v_y \\ v_z \end{pmatrix} &= 
#     \begin{pmatrix} 
#         \cos(\theta) & -\sin(\theta) & 0 \\
#         \sin(\theta) & \cos(\theta) & 0 \\
#         0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix}.
# \end{align*}
# 
# The square matrix is the transformation matrix for rotation by the angle $\theta$ anti-clockwise about the $z$-axis, i.e., in {numref}`rotation-figure` we are looking down the $z$-axis. Doing similar we can determine the equivalent matrices for rotating about the $x$ and $y$-axes.
# 
# ````{prf:theorem} Rotation in $\mathbb{R}^3$
# :label: rotation-in-R3-theorem
# 
# The rotation of a vector in $\mathbb{R}^3$ expressed using homogeneous co-ordinates *anti-clockwise* by an angle $\theta$ about the $x$, $y$ and $z$ axes is the linear transformation given by the following rotation matrices.
# 
# ```{math}
# :label: rotation-matrix-equation
# 
# \begin{align*}
#     R_x(\theta) &= 
#     \begin{pmatrix} 
#         1 & 0 & 0 & 0 \\
#         0 & \cos(\theta) & -\sin(\theta) & 0 \\
#         0 & \sin(\theta) & \cos(\theta) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_y(\theta) &= 
#     \begin{pmatrix} 
#         \cos(\theta) & 0 & \sin(\theta) & 0 \\
#         0 & 1 & 0 & 0 \\
#         -\sin(\theta) & 0 & \cos(\theta) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_z(\theta) &= 
#     \begin{pmatrix} 
#         \cos(\theta) & -\sin(\theta) & 0 & 0 \\
#         \sin(\theta) & \cos(\theta) & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# ```
# 
# Since $\cos(-\theta) = \cos(\theta)$ and $\sin(-\theta) = -\sin(\theta)$, the transformation matrices for inverse rotation, rotation in the *clockwise* direction, are
# 
# ```{math}
# :label: inverse-rotation-matrix-equation
# 
# \begin{align*}
#     R_x^{-1}(\theta) &= 
#     \begin{pmatrix} 
#         1 & 0 & 0 & 0 \\
#         0 & \cos(\theta) & \sin(\theta) & 0 \\
#         0 & -\sin(\theta) & \cos(\theta) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_y^{-1}(\theta) &= 
#     \begin{pmatrix} 
#         \cos(\theta) & 0 & -\sin(\theta) & 0 \\
#         0 & 1 & 0 & 0 \\
#         \sin(\theta) & 0 & \cos(\theta) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_z^{-1}(\theta) &= 
#     \begin{pmatrix} 
#         \cos(\theta) & \sin(\theta) & 0 & 0 \\
#         -\sin(\theta) & \cos(\theta) & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# ```
# ````
# 
# `````{prf:example} 
# :class: seealso
# :label: rotation-example-1
# 
# A triangular polygon has vertices located at $\mathbf{p}_1 = (4, 1, 2)$, $\mathbf{p}_2 = (6, 1, 2)$ and $\mathbf{p}_3 = (5, 3, 2)$. The triangle is rotated by angle $\theta = \pi/4$ anti-clockwise about the $z$-axis. Calculate the positions of the vertices of the rotated triangle.
# 
# ````{dropdown} Solution
# 
# The homogeneous co-ordinate matrix is 
# 
# \begin{align*}
#     P &= \begin{pmatrix}
#         4 & 6 & 5 \\
#         1 & 1 & 3 \\
#         2 & 2 & 2 \\
#         1 & 1 & 1 
#     \end{pmatrix},
# \end{align*}
# 
# and the rotation matrix is
# 
# \begin{align*}
#     R_z &= \begin{pmatrix}
#         \cos(\pi/4) & -\sin(\pi/4) & 0 & 0 \\
#         \sin(\pi/4) &  \cos(\pi/4) & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1 
#     \end{pmatrix} \\
#     &= 
#     \begin{pmatrix}
#         \sqrt{2}/2 & -\sqrt{2}/2 & 0 & 0 \\
#         \sqrt{2}/2 & \sqrt{2}/2 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1 
#     \end{pmatrix}
# \end{align*}
# 
# Applying the transformation
# 
# \begin{align*}
#     R_y \cdot P &= 
#     \begin{pmatrix}
#         \sqrt{2}/2 & -\sqrt{2}/2 & 0 & 0 \\
#         \sqrt{2}/2 & \sqrt{2}/2 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1 
#     \end{pmatrix}
#     \begin{pmatrix}
#         4 & 6 & 5 \\
#         1 & 1 & 3 \\
#         2 & 2 & 2 \\
#         1 & 1 & 1 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         3\sqrt{2}/2 & 5\sqrt{2}/2 & \sqrt{2} \\
#         5\sqrt{2}/2 & 7\sqrt{2}/2 & 4\sqrt{2} \\
#         2 & 2 & 2 \\
#         1 & 1 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# So the vertex co-ordinates fo the translated triangle are $(3\sqrt{2}, 5\sqrt{2}/2, 2) \approx (2.12, 3.54, 2)$, $(5\sqrt{2}/2, 7\sqrt{2}{2}, 2) \approx (3.54, 4.95, 2.00)$ and $(\sqrt{2}, 4\sqrt{2}, 2) \approx (1.41, 5.66, 2.00)$. The original triangle and the translated triangle are plotted below looking along the $z$ axis.
# 
# ```{figure} /images/rotation_example.png
# :width: 400px
# ```
# 
# ````
# 
# `````
# 
# ## Rotation about polygon centre
# 
# We saw in {prf:ref}`rotation-example-1` that the polygon has shifted position because we rotate about the origin. If we wanted to rotate the polygon about its centre we first need to translate it so that its centre is at the origin, apply the rotation transformation and then translate the centre to the original position ({numref}`rotate-about-centre-figure`).
# 
# ```{figure} /images/rotate_about_centre.svg
# :name: rotate-about-centre-figure
# 
# Steps required to rotate a polygon by its centre.
# ```
# 
# If the centre of the polygon is at point $\mathbf{c}=(c_x, c_y, c_z)$ then the first transformation is translation by $-\mathbf{c}$ and the {prf:ref}` transformation matrix<translation-matrix-definition>` is 
# 
# \begin{align*}
#     T(-\mathbf{c}) = \begin{pmatrix}
#         1 & 0 & 0 & -c_x \\
#         0 & 1 & 0 & -c_y \\
#         0 & 0 & 1 & -c_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# The second transformation is rotation around the origin using equation {ref}`rotation-matrix-equation` and the third transformation is translation by $\mathbf{c}$, so that the centre is back to the original position, using
# 
# \begin{align*}
#     T(\mathbf{c}) = \begin{pmatrix}
#         1 & 0 & 0 & c_x \\
#         0 & 1 & 0 & c_y \\
#         0 & 0 & 1 & c_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# The transformation matrix for the composite transformation that achieves rotation of a polygon about its centre is
# 
# \begin{align*}
#     A = T(\mathbf{c}) \cdot R (\theta) \cdot T(-\mathbf{c}),
# \end{align*}
# 
# where $R(\theta)$ is either $R_x(\theta)$, $R_y(\theta)$ or $R_z(\theta)$.
# 
# `````{prf:example} 
# :class: seealso
# :label: rotation-example-2
# 
# Rotate the polygon from {prf:ref}`rotation-example-1` by $\theta = \pi/4$ around the $z$-axis about its centre.
# 
# ````{dropdown} Solution
# The homogeneous co-ordinate matrix is 
# 
# \begin{align*}
#     P &= \begin{pmatrix}
#         4 & 6 & 5 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1 
#     \end{pmatrix},
# \end{align*}
# 
# and since the polygon is a triangle the co-ordinates of the centre are the average of the vertices
# 
# \begin{align*}
#     \mathbf{c} &= \frac{(4, 0, 1) + (6, 0, 1) + (5, 0, 3)}{3} = 
#     \begin{pmatrix} 5 \\ 5/3 \\ 2 \end{pmatrix}.
# \end{align*}
# 
# The individual transformation matrices are
# 
# \begin{align*}
#     T(-\mathbf{c}) &= \begin{pmatrix}
#         1 & 0 & 0 & -5 \\
#         0 & 1 & 0 & -5/3 \\
#         0 & 0 & 1 & -2 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_y\left(\frac{\pi}{4}\right) &=
#     \begin{pmatrix}
#         \sqrt{2}/2 & -\sqrt{2}/2 & 0 & 0 \\
#         \sqrt{2}/2 & \sqrt{2}/2 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     T(\mathbf{c}) &= 
#     \begin{pmatrix}
#         1 & 0 & 0 & 5 \\
#         0 & 1 & 0 & 5/3 \\
#         0 & 0 & 1 & 2 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix},
# \end{align*}
# 
# which are multiplied to give the composite transformation matrix
# 
# \begin{align*}
#     A &= T(\mathbf{c}) \cdot R_y\left(\frac{\pi}{4}\right) \cdot T(-\mathbf{c}) \\
#     &= 
#     \begin{pmatrix} 
#         \sqrt{2}/2 & -\sqrt{2}/2 &  0 & 5 - 5\sqrt{2}/3 \\
#         \sqrt{2}/2 & \sqrt{2}/2 & 0 & 5/3 - 10\sqrt{2}/3 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# 
# Applying the composite transformation
# 
# \begin{align*}
#     A \cdot P &= 
#     \begin{pmatrix} 
#         \sqrt{2}/2 & -\sqrt{2}/2 &  0 & 5 - 5\sqrt{2}/3 \\
#         \sqrt{2}/2 & \sqrt{2}/2 & 0 & 5/3 - 10\sqrt{2}/3 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         4 & 6 & 5 \\
#         1 & 1 & 3 \\
#         2 & 2 & 2 \\
#         1 & 1 & 1 
#     \end{pmatrix} \\
#     &= 
#     \begin{pmatrix}
#         5 - \sqrt{2}/6 & 5 + 5\sqrt{2}/6 & 5 - 2\sqrt{2}/3 \\
#         5/3 - 5\sqrt{2}/6 & 5/3 + \sqrt{2}/6 & 5/3 + 2 \sqrt{2}/3 \\
#         2 & 2 & 2 \\
#         1 & 1 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# So the vertices of the rotated polygon are $(5 - \sqrt{2}/6, 5/3 - 5\sqrt{2}/6, 2) \approx (4.76, 0.49, 2.00)$, $(5 + 5\sqrt{2}/6, 5/3 + \sqrt{2}/6, 2) \approx (6.18, 1.90, 2.00)$ and $(5 - 2\sqrt{2}/3, 5/3 + 2\sqrt{2}/3, 2) \approx (4.06, 2.61, 2.00)$. The original polygon and the translated polygon are plotted below looking along the $z$ axis.
# 
# ```{figure} /images/rotation_about_centre_example.png
# :width: 400px
# ````
# 
# `````
# 
# ## Rotation about a line
# 
# Suppose we wish to rotate $\mathbb{R}^3$ by an angle $\theta$ about a general line that passes through the point $\mathbf{p}=(p_x,p_y,p_z)$ with direction $\mathbf{d}$ that does not pass through the origin and $\mathbf{d}=(d_x,d_y,d_z)$ is not parallel to any of the three co-ordinate axes ({numref}`rotation-about-line-figure-1`). To achieve this we first need to apply translation and rotation so that the line lies along one of the co-ordinate axes, preform the rotation about this axis before reversing the rotation and translation operations. Each of the individual transformations can be represented by a matrix so the composite transformation that achieves the rotation about the line is a product of the individual matrices.
# 
# ```{figure} ../images/rotate_about_line_1.svg
# :width: 400px
# :name: rotation-about-line-figure-1
# 
# Rotation about a line.
# ```
# 
# The first transformation is to translate by $-\mathbf{p}$ so that the line passes through the origin so the transformation matrix is
# 
# \begin{align*}
#     T(-\mathbf{p}) = 
#     \begin{pmatrix}
#         1 & 0 & 0 & -p_x \\
#         0 & 1 & 0 & -p_y \\
#         0 & 0 & 1 & -p_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# ```{figure} ../images/rotate_about_line_2.svg
# :width: 400px
# :name: rotation-about-line-figure-2
# 
# The line is translated so that $\mathbf{p}$ is at the origin.
# ```
# 
# {numref}`rotation-about-line-figure-2` shows that affect of translating by $-\mathbf{p}$. Now we need to rotate the line so that it lies in a plane the contains two of the three co-ordinate axes. If we rotate about the $z$ axis then the line will be in the $yz$ plane. The values of $\cos(\phi)$ and $\sin(\phi)$ in $R_z(\phi)$ are
# 
# \begin{align*}
#     \cos(\phi) &= \frac{|d_y|}{d_1}, &
#     \sin(\phi) &= \frac{|d_x|}{d_1},
# \end{align*}
# 
# where $d_1 = \sqrt{d_x^2 + d_y^2}$ is the hypotenuse of the right-angled triangle formed by projecting $\mathbf{d}$ onto the $xy$ plane. So the rotation matrix is
# 
# \begin{align*}
#     R_z(\phi) &=
#     \begin{pmatrix} 
#         |d_y|/d_1 & -|d_x|/d_1 & 0 & 0 \\
#         |d_x|/d_1 & |d_y|/d_1 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# ```{figure} ../images/rotate_about_line_3.svg
# :width: 250px
# :name: rotation-about-line-figure-3
# 
# The line is rotated about the $z$-axis so that $\mathbf{d}$ is in the $yz$ plane.
# ```
# 
# {numref}`rotation-about-line-figure-3` shows that affect of rotating about the $z$-axis. Now we need to rotate **clockwise** about the $x$ axis so that $\mathbf{d}$ points along the $z$ axis. The values of $\cos(\psi)$ and $\sin(\psi)$ are
# 
# \begin{align*}
#     \cos(\psi) &= \frac{|d_z|}{|\mathbf{d}|}, &
#     \sin(\psi) &= \frac{d_1}{|\mathbf{d}|},
# \end{align*}
# 
# so the transformation matrix is
# 
# \begin{align*}
#     R_x &=
#     \begin{pmatrix}
#         1 & 0 & 0 & 0 \\
#         0 & |d_z|/|\mathbf{d}| & -d_1/|\mathbf{d}| & 0 \\
#         0 & d_1/|\mathbf{d}| & |d_z|/|\mathbf{d}| & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# ```{figure} ../images/rotate_about_line_4.svg
# :width: 150px
# :name: rotation-about-line-figure-4
# 
# The line is rotated about the $x$-axis so that $\mathbf{d}$ points along the $z$ axis.
# ```
# 
# {numref}`rotation-about-line-figure-4` shows that affect of rotating about the $x$-axis. Now that the line is pointing along the $z$-axis we can perform the rotation about the line using $R_z(\theta)$ and reverse the two rotation and translation transformations. The composite transformation matrix is
# 
# $$A = T(\mathbf{p}) \cdot R_z(-\phi) \cdot R_x(-\psi) \cdot R_z(\theta) \cdot R_x(\psi) \cdot R_z(\phi) \cdot T(-\mathbf{p}).$$
# 
# `````{prf:example}
# :class: seealso
# 
# A flight simulation program is simulating the flight of an aeroplane positioned with its centre of mass at $\mathbf{c} = (10, 5, 50)$ travelling in the direction given by the vector $\mathbf{d} = (2, -1, -3)$. The user performs a roll of the plane by rotating about $\mathbf{d}$ by angle $\theta = \pi/6$ in the anti-clockwise direction. Calculate the composite transformation matrix that performs this action.
# 
# ````{dropdown} Solution
# 
# 
# ```{figure} ../images/rotate_about_line_example_1.svg
# :width: 180px
# ```
# 
# First we translate by $-\mathbf{c}$ so that the centre of the plane is at the origin.
# 
# \begin{align*}
#     T(-\mathbf{c}) = 
#     \begin{pmatrix}
#         1 & 0 & 0 & -c_x \\
#         0 & 1 & 0 & -c_y \\
#         0 & 0 & 1 & -c_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix} =
#     \begin{pmatrix}
#         1 & 0 & 0 & -10 \\
#         0 & 1 & 0 & -5 \\
#         0 & 0 & 1 & -50 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# ```{figure} ../images/rotate_about_line_example_2.svg
# :name: rotate-about-line-example-2
# :width: 180px
# 
# Rotate $\mathbf{d}$ about the $z$-axis.
# ```
# 
# Now we need to consider which rotations we apply so that $\mathbf{d}$ points along one of the axes. This decision is arbitrary but in this case since $d_x$ is positive then rotating so that $\mathbf{d}$ points along the $x$ axis would require the fewest rotations. Looking at {numref}`rotate-about-line-example-2` this means can first rotate **anti-clockwise** about the $z$ axis by angle $\phi$ so that $\mathbf{d}$ is in the $xz$ plane. The values of $\cos(\phi)$ and $\sin(\phi)$ are
# 
# \begin{align*}
#     \cos(\phi) &= \frac{|d_x|}{d_1} = \frac{2\sqrt{5}}{5}, &
#     \sin(\phi) &= \frac{|d_y|}{d_1} = \frac{\sqrt{5}}{5},
# \end{align*}
# 
# and the transformation matrix is
# 
# \begin{align*}
#     R_z(\phi) &= \begin{pmatrix}
#         \cos(\phi) & -\sin(\phi) & 0 & 0 \\
#         \sin(\phi) & \cos(\phi) & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         2\sqrt{5}/5 & -\sqrt{5}/5 & 0 & 0 \\
#         \sqrt{5}/5 & 2\sqrt{5}/5 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# 
# We can check whether this rotation is correct by multiplying it by the homogeneous form of $\mathbf{d}$
# 
# \begin{align*}
#     R_z(\phi) \cdot \mathbf{d} &= 
#     \begin{pmatrix}
#         2\sqrt{5}/5 & -\sqrt{5}/5 & 0 & 0 \\
#         \sqrt{5}/5 & 2\sqrt{5}/5 & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ -1 \\ -3 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} \sqrt{5} \\ 0 \\ -3 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# Since $d_y = 0$ then the rotated $\mathbf{d}$ vector is now in the $xz$ plane. 
# 
# ```{figure} ../images/rotate_about_line_example_3.svg
# :width: 180px
# 
# Rotate $\mathbf{d}$ about the $y$ axis.
# ```
# 
# Looking at {numref}`rotate-about-line-example-2` we need to rotate **clockwise** around the $y$ axis by angle $\psi$ so that $\mathbf{d}$ points along the $x$ axis (remember that the direction of rotation is based on the view looking down the axis towards the origin). The values of $\cos(\psi)$ and $\sin(\psi)$ are
# 
# \begin{align*}
#     \cos(\psi) &= \frac{d_1}{|\mathbf{d}|} = \frac{\sqrt{5}}{\sqrt{14}}, &
#     \sin(\psi) &= \frac{|d_z|}{|\mathbf{d}|} = \frac{3}{\sqrt{14}},
# \end{align*}
# 
# so the transformation matrix is 
# 
# \begin{align*}
#     R_y(\psi) &= 
#     \begin{pmatrix}
#         \cos(\psi) & 0 & -\sin(\psi) & 0 \\
#         0 & 1 & 0 & 0 \\
#         \sin(\psi) & 0 & \cos(\psi) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix} \\
#     &= 
#     \begin{pmatrix}
#         \sqrt{5}\sqrt{14}/14 & 0 & -3\sqrt{14}/14 & 0 \\
#         0 & 1 & 0 & 0 \\
#         3\sqrt{14}/14 & 0 & \sqrt{5}\sqrt{14}/14 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Again, we can check whether this rotation is correct by multiplying it by $R_y(\psi) \cdot R_z(\phi) \cdot \mathbf{d}$
# 
# \begin{align*}
#     R_y(\psi) \cdot R_z(\phi) \cdot \mathbf{d} &= 
#     \begin{pmatrix}
#         \sqrt{5}\sqrt{14}/14 & 0 & -3\sqrt{14}/14 & 0 \\
#         0 & 1 & 0 & 0 \\
#         3\sqrt{14}/14 & 0 & \sqrt{5}\sqrt{14}/14 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         \sqrt{5} \\ 0 \\ -3 \\ 1
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix} \sqrt{14} \\ 0 \\ 0 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# Since $d_y=0$, $d_z=0$ and $d_x > 0$ then $\mathbf{d}$ is now pointing along the $x$ axis. 
# 
# ```{figure} /images/rotate_about_line_example_4.svg
# :width: 200px
# 
# Rotate $\mathbf{d}$ about the $x$ axis.
# ```
# 
# Now we perform the rotation anti-clockwise around the $x$ axis by angle $\theta = \pi / 6$ and the matrix for achieving this rotation is
# 
# \begin{align*}
#     R_x(\theta) &= \begin{pmatrix}
#         1 & 0 & 0 & 0 \\
#         0 & \cos(\theta) & -\sin(\theta) & 0 \\
#         0 & \sin(\theta) & \cos(\theta) & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix} \\
#     &= 
#     \begin{pmatrix}
#         1 & 0 & 0 & 0 \\
#         0 & \sqrt{3}/2 & -1/2 & 0 \\
#         0 & 1/2 & \sqrt{3}/2 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# The rotations about the $y$ and $z$ axis and the translation are reversed so the complete composite matrix is
# 
# \begin{align*}
#     A &= T(\mathbf{c}) \cdot R_z(-\phi) \cdot R_y(-\psi) \cdot R_x(\theta) \cdot R_y(\psi) \cdot R_z(\phi) \cdot T(-\mathbf{c}),
# \end{align*}
# 
# where
# 
# \begin{align*}
#     R_{z}(-\phi) &= 
#     \begin{pmatrix}
#         2 / \sqrt{5} & 1 / \sqrt{5} & 0 & 0 \\
#         -1 / \sqrt{5} & 2 / \sqrt{5} & 0 & 0 \\
#         0 & 0 & 1 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     R_y(-\psi) &= 
#     \begin{pmatrix}
#         \sqrt{5} / \sqrt{14} & 0 & -3 / \sqrt{14} & 0 \\
#         0 & 1 & 0 & 0 \\
#         3 / \sqrt{14} & 0 & \sqrt{5} / \sqrt{14} & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     T(\mathbf{c}) &= 
#     \begin{pmatrix}
#         1 & 0 & 0 & 10 \\
#         0 & 1 & 0 & 5 \\
#         0 & 0 & 1 & 50 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*} 
# ````
# `````
