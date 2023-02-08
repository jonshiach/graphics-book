#!/usr/bin/env python
# coding: utf-8

# # Points, lines, planes and spheres
# 
# Computer graphics uses points, line, planes and spheres to describe virtual environments. Euclid defined the first three of these in his works *The Elements* around 300 BCE which is considered the most important mathematical works ever written. It introduced mathematical concepts of Euclidean geometry, mathematical proofs, logic and number theory. 
# 
# (points-section)=
# ## Points
# 
# Euclid described a *point* as *"that which has no part"*. A point has position only, it has no length, width or thickness, and thus no area or volume. As we have [already seen](euclidean-space-section), a typical point in $\mathbb{R}^n$ is described by its co-ordinates $(a_1,a_2,\dots,a_n)$, where the $a_i \in \mathbb{R}$.
# 
# (lines-section)=
# ## Lines
# 
# Euclid defined a line as having *"breadthless length"* which is another way of saying a line is a one dimensional object that has a length but no breadth or volume. 
# 
# ````{prf:definition} Vector equation of a line
# :class: note
# 
# Let $\mathbf{p} = (p_1, \ldots ,p_n)$ be the position of a point in $\mathbb{R}^n$ and $\mathbf{d} = (d_1, \ldots, d_n)$ a non-zero vector in $\mathbb{R}^n$. The line $\ell$ [^1] which passes through $\mathbf{p}$ in the direction of $\mathbf{d}$ has equation
# 
# ```{math}
# :label: line-vector-equation
# 
# \mathbf{q} = \mathbf{p} + t\mathbf{d},
# ```
# where $\mathbf{q}$ is a general point on $\ell$ and $t\in \mathbb{R}$ is known as a **parameter**.
# ````
# 
# [^1]: $\ell$ is used here instead of $l$ to avoid confusing with a 1 or uppercase i.
# 
# In other words, every point on $\ell$ is obtained by adding some scalar multiple of $\mathbf{d}$ to $\mathbf{p}$ ({numref}`line-vector-equation-figure`). So $\ell$ is the line which passes through $\mathbf{p}$ in the direction of $\mathbf{d}$. We call the vector $\mathbf{d}$ a **direction vector** of the line.
# 
# ```{figure} ../images/line_vector_equation.svg
# :name: line-vector-equation-figure
# :width: 500px
# 
# The position of any point on the line $\ell$ can be obtained by adding a scalar multiple of $\mathbf{d}$ to $\mathbf{p}$.
# ```
# 
# In practice one can determine the direction vector $\mathbf{d}$ of a line by taking any two distinct points $\mathbf{p}_1$ and  $\mathbf{p}_2$ on $\ell$ and setting $\mathbf{d}=\mathbf{p}_2 - \mathbf{p}_1$ and $\mathbf{p}$ in the line equation to be any point on the line. In particular, $\mathbf{d}$ and $\mathbf{p}$ are not unique. 
# 
# `````{prf:example}
# :class: seealso
# 
# A line $\ell$ in $\mathbb{R}^3$ passes through the two points at $\mathbf{p}_1=(1,0,2)$ and $\mathbf{p}_2 = (2, 2, 2)$.
# 
# (i) &emsp; Find the equation of the line $\ell$.
# 
# ````{dropdown} Solution
# Calculating the direction vector
# 
# \begin{align*}
#     \mathbf{d} &= \mathbf{p}_2 - \mathbf{p}_1 =
#     \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}
#     = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# Therefore the equation that describes $\ell$ is
# 
# \begin{align*}
#     \mathbf{q} &= \mathbf{p}_1 + t \mathbf{d} 
#     = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}.
# \end{align*}
# ````
# 
# (ii) &emsp; Find the position of the point one quarter of the way along the chord $\mathbf{p}_1 \to \mathbf{p}_2$
# 
# ````{dropdown} Solution
# \begin{align*}
#     \mathbf{q} &= \mathbf{p}_1 + \frac{1}{4}\mathbf{d} = 
#     \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + \frac{1}{4}
#     \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}
#     = \begin{pmatrix} 5/4 \\ 1/2 \\ 2 \end{pmatrix}.
# \end{align*}
# ````
# 
# (iii) &emsp; Does the line $\ell$ pass through the point at $\mathbf{p}_3 = (2, 1, 2)$?
# 
# ````{dropdown} Solution
# If $\mathbf{p}_3$ lies on $\ell$ then the following system has a unique solution
# 
# \begin{align*}
#     \mathbf{p}_1 + t \mathbf{d} &= \mathbf{p}_3, \\
#     \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + t
#     \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}
#     &= \begin{pmatrix} 2 \\ 1 \\ 2 \end{pmatrix}
# \end{align*}
# 
# So we have the system
# 
# \begin{align*}
#     1 + t &= 2, \\
#     2t &= 1, \\
#     2 &= 2.
# \end{align*}
# 
# The second equation gives $t = 1/2$ so substituting into the first equation gives $t = 3/2$ which is a contradiction so the line $\ell$ does not pass through $\mathbf{p}_3$.
# ````
# 
# `````
# 
# (planes-section)=
# ## Planes
# 
# ```{prf:definition}{Plane}
# :class: note
# 
# A **plane** is an object of dimension 2 that has a length and width but no thickness.
# ```
# 
# A **plane** is a flat two-dimensional surface. The vector equation for a plane in $\mathbb{R}^n$ is very similar to that of a line. We just need two direction vectors instead of just the one we needed for a line.
# 
# ````{prf:definition} Vector equation of a plane
# :class: note
# 
# The position of a point $\mathbf{p}$ that lies on the plane $p$ which passes through the three point $\mathbf{p}_1$, $\mathbf{p}_2$ and $\mathbf{p}_3$ is
# 
# $$ \mathbf{q} = \mathbf{p}_1 + a (\mathbf{p}_2 - \mathbf{p}_1) + b (\mathbf{p}_3 - \mathbf{p}_2), $$
# 
# where $a, b \in \mathbb{R}$ are parameters ({numref}`plane-vector-equation-figure`). 
# ````
# 
# ```{figure} ../images/plane_vector_equation.svg
# :name: plane-vector-equation-figure
# :width: 500px
# 
# The vector equation of a plane.
# ```
# 
# In other words, every point on $p$ is obtained by adding some scalar multiples of the vectors $\mathbf{p}_2 - \mathbf{p}_1$ and $\mathbf{p}_3 - \mathbf{p}_2$. Note that we need $\mathbf{p}_2 - \mathbf{p}_1$ and $\mathbf{p}_3 - \mathbf{p}_2$ not to be parallel else we would have only described a line again.
# 
# (normal-vector-section)=
# ## The normal vector
# 
# A more convenient way of describing a plane uses the normal vector.
# 
# ````{prf:definition} The normal vector
# :class: note
# :label: normal-vector-definition
# 
# The **normal vector** to a plane is a vector that is perpendicular to that plane. If $\mathbf{a}$ and $\mathbf{b}$ are two vectors that lie on a plane then the normal vector is calculated using $\mathbf{n} = \mathbf{a} \times \mathbf{b}$. 
# ````
# 
# ```{figure} ../images/normal_vector.svg
# :name: normal-vector-figure
# :width: 400px
# 
# The normal vector $\mathbf{n}$ is perpendicular to the plane $p$.
# ```
# 
# Recall the [geometric definition of a dot product](geometric-dot-product-definition) which states
# 
# $$ \mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta),$$
# 
# where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$. If the two vectors are perpendicular then $\theta = \pi / 2$ and $\cos(\theta) = 0$. Therefore if $\mathbf{a} \cdot \mathbf{b}=0$ then $\mathbf{a}$ and $\mathbf{b}$ are perpendicular. If $\mathbf{p}$ lies on a plane with normal vector $\mathbf{n}$ then if $\mathbf{q}$ is another point that lies on the plane then the vector $\mathbf{p} - \mathbf{q}$ must be perpendicular to $\mathbf{n}$, i.e.,
# 
# $$ \mathbf{n} \cdot (\mathbf{p} - \mathbf{q}) = 0,$$
# 
# which can be written as
# 
# $$ \mathbf{n} \cdot \mathbf{p} = \mathbf{n} \cdot \mathbf{q},$$
# 
# which gives the point-normal equation of a plane. 
# 
# ````{prf:definition} Point-normal equation of a plane
# :label: point-normal-definition
# 
# The **point normal equation of a plane** is 
# 
# ```{math}
# :label: point-normal-equation
# 
# \mathbf{n} \cdot \mathbf{p} = s
# ```
# 
# where $\mathbf{n}$ is the normal vector, $\mathbf{p}$ is a point on the plane and $s$ is a scalar.
# 
# ````
# 
# ````{prf:example}
# :class: seealso
# 
# A plane passes through the three points $\mathbf{p}_1 = (1, 0, 3)$, $\mathbf{p}_2 = (2, 1, 1)$ and $\mathbf{p}_3 = (0, 1, 3)$.
# 
# (i) &emsp; Determine the point-normal equation of the plane.
# 
# ```{dropdown} Solution
# Calculate the normal vector
# 
# \begin{align*}
#     \mathbf{n} &= (\mathbf{p}_2 - \mathbf{p}_1) \times (\mathbf{p}_3 - \mathbf{p}_1)
#     = \begin{vmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         1 & 1 & -2 \\
#         -1 & 1 & 0 
#     \end{vmatrix}
#     = \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix}.
# \end{align*}
# 
# Calculate the scalar $s$
# 
# \begin{align*}
#     s &= \mathbf{n} \cdot \mathbf{p}_1 = 
#     \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix}
#     = 2 + 0 + 6 = 8,
# \end{align*}
# 
# therefore the point-normal equation of the plane is
# 
# \begin{align*}
#     \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} \cdot \mathbf{r} = 8.
# \end{align*}
# ```
# 
# (ii) &emsp; Does the point with position vector $\mathbf{p}_4 = (1, 2, 5)$ lies on this plane?
# 
# ```{dropdown} Solution
# Calculate $\mathbf{n} \cdot \mathbf{p}_4$
# \begin{align*}
#     \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} \cdot 
#     \begin{pmatrix} 1 \\ 2 \\ 5 \end{pmatrix}
#     = 2 + 4 + 10 = 16 \neq 8,
# \end{align*}
# 
# therefore $\mathbf{p}_4$ does not lie on the plane.
# ```
# 
# ````

# (spheres-section)=
# ## Spheres 
# 
# A sphere is a three-dimensional geometric object where all points on the surface of the sphere are the same distance from its centre. 
# 
# ````{prf:definition} Equation of a sphere
# 
# The **Cartesian equation of a sphere** centred at $(x_0, y_0, z_0)$ with radius $r$ is
# 
# ```{math}
# :label: sphere-equation
# 
# (x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2 = r^2
# ```
# 
# ```{figure} /images/sphere.svg
# ```
# 
# ````
