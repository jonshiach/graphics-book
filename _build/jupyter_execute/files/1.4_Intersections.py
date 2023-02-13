#!/usr/bin/env python
# coding: utf-8

# (intersections-section)=
# # Intersections between objects
# 
# In computer graphics it is useful to be able to determine where objects intersect or collide. Examples of where this is used in practice is finding out where polygons intersect with planes in [binary space partitioning](bsp-section) and the calculations of collisions of moving elements in a computer game. Here we will look some of the most common object-on-object intersections.
# 
# (intersecting-lines-section)=
# ## Intersection of two lines
# 
# Consider the intersection of two lines defined by the vector equations  $\mathbf{p}_1 + t_1\mathbf{d}_1$ and $\mathbf{p}_2 + t_2\mathbf{d}_2$.
# 
# ```{figure} ../Images/line_line_intersection.svg
# :name: line-line-intersection-figure
# :width: 400px
# 
# The intersection between the two lines $\ell_1$ and $\ell_2$.
# ```
# 
# Depending on the values of $\mathbf{p}_1$, $\mathbf{p}_2$, $\mathbf{d}_1$ and $\mathbf{d}_2$ we may have one of the following scenarios
# 
# - the two lines intersect;
# - the two lines are parallel and do not intersect;
# - the two lines neither intersect or are parallel and so are skew. 
# 
# (line-line-intersection-section)=
# ### Intersecting lines
# 
# If the two lines intersect between then the point of intersection is the point that passes through both of the lines. We can find this point by equating the vector equations of the lines and attempt to solve for $t_1$ and $t_2$. If no values exists for $t_1$ and $t_2$ that satisfies all co-ordinates then the lines do not intersect.
# 
# ````{prf:example}
# :class: seealso
# :label: line-line-intersection-example
# 
# Three lines in $\mathbb{R}^3$ are defined as $(1,-3,0) + t_1(1,2,1)$, $(6,-5,-1) + t_2(-1,2,1)$ and $(6,-11,-2)+t_3(2,2,-1)$. Determine the points of intersection between the three lines (if possible).
# 
# ```{dropdown} Solution
# 
# Let $\mathbf{p}_1 = (1, -3, 0)$, $\mathbf{p}_2 = (6, -5, -1)$, $\mathbf{p}_3 = (6, -11, -2)$, $\mathbf{d}_1 = (1, 2, 1)$, $\mathbf{d}_2 = (-1, 2, 1)$ and $\mathbf{d}_3 = (2, 2, -1)$. Equating the first two lines gives
# 
# \begin{align*}
#     1 + t_1 &= 6 - t_2, \\
#     -3 + 2t_1 &= -5 + 2t_2, \\
#     t_1 &= -1 + t_2.
# \end{align*}
# 
# The third equation is $t_1 = t_2 - 1$ and substituting into the first equation gives $t_2 = 3$ so $t_1 = 2$. Substituting these into the second equation gives $-3 + 2(2) = -5 + 2(3)$ which is $1 = 1$ so $\ell_1$ and $\ell_2$ intersect. To find the point of intersection we substitute $t_1$ or $t_2$ into the vector equations gives
# 
# \begin{align*}
#     \mathbf{p}_1 + t_1 \mathbf{d}_1 &= \begin{pmatrix} 1 \\ -3 \\ 0 \end{pmatrix} + 2\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}, \\
#     \mathbf{p}_2 + t_2 \mathbf{d}_2 &= \begin{pmatrix} 6 \\ -5 \\ -1 \end{pmatrix} + 3\begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}.
# \end{align*}
# 
# So the first two lines intersect at $(3, 1, 2)$. 
# 
# Equating the first and third lines gives
# 
# \begin{align*}
#     1 + t_1 &= 6 + 2t_3, \\
#     -3 + 2t_1 &= -11 + 2t_3, \\
#     t_1 &= -2 - t_3.
# \end{align*}
# 
# Substituting the third equation into the first equation gives $t_3 = -\frac{7}{3}$ which substituted into the third equation gives $t_1 = -\frac{14}{3}$. Substituting these into the second equation gives $-24 = -18$ which is a contradiction so no values of $t_1$ or $t_3$ satisfy all co-ordinates so these lines do not intersect.
# 
# Equating the second and third lines gives the system
# 
# \begin{align*}
#     6 - t_2 &= 6 + t_3, \\
#     -5 + 2t_2 &= -11 + 2t_3, \\
#     -1 + t_2 &= -2 - t_3.
# \end{align*}
# 
# The third equations give $t_2 = -1 - t_3$ which substituted into the first equation gives $7+t_3 = 6 + t_3$ which is a contradiction so these lines do not intersect.
# 
# ```
# ````
# 
# ### Parallel lines
# 
# If two lines with vector equations $\mathbf{p}_1 + t_1\mathbf{d}_1$ and $\mathbf{p}_2 + t_2\mathbf{d}_2$ are parallel then the direction vectors are also parallel, i.e., $\mathbf{d}_1 = k\mathbf{d}_2$ where $k \neq 0$ ({numref}`parallel-lines-figure`). 
# 
# ```{figure} ../Images/parallel_lines.svg
# :name: parallel-lines-figure
# 
# The lines $\ell_1$ and $\ell_2$ are parallel in $\mathbb{R}^3$.
# ```
# 
# ````{prf:example}
# :class: seealso
# :label: parallel-lines-example
# 
# Two lines are defined by the vector equations $(1, 0, 2) + t_1(1, 0, 1)$ and $(1, 3, -2) + t_2(1, 0, -1)$. Show that these lines are not parallel.
# 
# ```{dropdown} Solution
# 
# Two lines are parallel  $\mathbf{d}_1 = k\mathbf{d}_2$
# 
# \begin{align*}
#     \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} &= k
#     \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}
#     \qquad \implies \qquad 
#     \begin{matrix}
#         k = 1, \\
#         k = -1
#     \end{matrix}
# \end{align*}
# 
# Here we have a contradiction so no value of $k$ exists to satisfy $\mathbf{d}_1 = k\mathbf{d}_2$ so $\ell_1$ and $\ell_2$ are not parallel.
# 
# ```
# ````
# 
# ### Skew lines
# 
# If two lines do not intersect and they are not parallel then they are skew lines ({numref}`skew-lines-figure`)
# 
# ```{figure} ../Images/skew_lines.svg
# :name: skew-lines-figure
# :width: 300px
# 
# The lines $\ell_1$ and $\ell_2$ are skew lines.
# ```
# 
# ````{prf:example}
# :class: seealso
# :label: skew-lines-example
# 
# Show that the lines $\ell_1$ and $\ell_2$ from {prf:ref}`parallel-lines-example` are skew lines.
# 
# ```{dropdown} Solution
# 
# We have shown in [example 4.3](parallel-lines-example) that $\ell_1$ and $\ell_2$ are not parallel. Therefore to we need to show that they do not intersect. Equating $\ell_1$ and $\ell_2$ gives
# 
# \begin{align*}
#     t_1 &= t_2, \\
#     0 &= 3, \\
#     -1 &= -1 - t_2.
# \end{align*}
# 
# Here the second equation is a contradiction so this system is inconsistent and the lines $\ell_1$ and $\ell_2$ do not intersect. Since $\ell_1$ and $\ell_2$ are not parallel and do not intersect then they must be skew.
# ```
# ````
# 
# (line-sphere-intersection-section)=
# ### Intersection between a line and a sphere
# 
# Consider the possible intersection with a line defined by $\mathbf{p} + t\mathbf{d}$ and a sphere centred at $\mathbf{c}$ with radius $r$ where $\mathbf{r}$ is the point of intersection. Depending on the values of these we have the following three scenarios
# 
# - the line intersects with the sphere twice;
# ```{figure} /images/line_sphere_intersection_1.svg
# :name: line-sphere-intersection-1-figure
# :width: 400px
# 
# The line intersects with the sphere twice.
# ```
# 
# - the line intersects with the sphere once;
# ```{figure} /images/line_sphere_intersection_2.svg
# :name: line-sphere-intersection-2-figure
# :width: 400px
# 
# The line intersects with the sphere once.
# ```
# 
# - the line does not intersect with the sphere.
# ```{figure} /images/line_sphere_intersection_3.svg
# :name: line-sphere-intersection-3-figure
# :width: 400px
# 
# The line does not intersect with the sphere.
# ```
# 
# An intersection will occur when the distance between the centre of the sphere and point on the line is equal to the radius of the sphere
# 
# \begin{align*}
#     r = | \mathbf{r} - \mathbf{c} |.
# \end{align*}
# 
# Substituting in the equation of the line $\mathbf{r} = \mathbf{p} + t\mathbf{d}$ and rearranging gives
# 
# \begin{align*}
#     r &= | \mathbf{p} + t \mathbf{d} - \mathbf{c} | \\
#     r^2 &= | t \mathbf{d} + (\mathbf{p} - \mathbf{c}) |^2 \\
#     0 &= t^2 \mathbf{d}^2 + 2 t (\mathbf{p} - \mathbf{c}) + (\mathbf{p} - \mathbf{c})^2 - r^2. 
# \end{align*}
# 
# This is a quadratic equation where the roots give the value of the parameter $t$ where the intersection(s) occur (note that $\mathbf{d}^2 = \mathbf{d} \cdot \mathbf{d}$). Let
# 
# \begin{align*}
#     a &= \mathbf{d}^2, \\
#     b &= 2 \mathbf{d} \cdot (\mathbf{p} - \mathbf{c}), \\
#     c &= (\mathbf{p} - \mathbf{c})^2 - r^2,
# \end{align*}
# 
# then the solution is given by the <a href="https://en.wikipedia.org/wiki/Quadratic_formula" target="_blank">quadratic formula</a>
# 
# \begin{align*}
#     t &= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
# \end{align*}
# 
# A quadratic equation can have two, one or no real roots depending on the value of the discriminant $b^2 - 4ac$ which correspond to the three scenarios presented above
# 
# \begin{align*}
#     b^2 - 4ac 
#     \begin{cases}
#         > 0, & \text{line intersects sphere twice,} \\
#         = 0, & \text{line intersects the sphere once,} \\
#         < 0, & \text{line does not intersect the sphere.}
#     \end{cases}
# \end{align*}
# 
# ````{prf:example} 
# :class: seealso
# :label: line-sphere-intersection-example
# 
# A line is defined by the vector equation $(1, 0, 2) + t(2, 1, 1)$ and a sphere positioned so that its center is at $(5, 3, 1)$ and has radius $r=2$. Does the line intersect with the sphere and if so, where?
# 
# ```{dropdown} Solution
# 
# Let $\mathbf{p} = (1,0,2)$, $\mathbf{d} = (2,1,0)$ and $\mathbf{c}=(5,3,1)$ then at the point of intersection the value of $t$ satisfies $0 = t^2 \mathbf{d}^2 + 2 t (\mathbf{p} - \mathbf{c}) + (\mathbf{p} - \mathbf{c})^2 - r^2$. Let
# 
# \begin{align*}
#     a &= \mathbf{d}^2 = 
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}
#     = 5, \\
#     b &= 2 \mathbf{d} \cdot (\mathbf{p} - \mathbf{c}) = 2 
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} \cdot \left(
#         \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} -
#         \begin{pmatrix} 5 \\ 3 \\ 1 \end{pmatrix}
#     \right) = -22, \\
#     c &= (\mathbf{p} - \mathbf{c})^2 - r^2 = \left(
#         \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} -
#         \begin{pmatrix} 5 \\ 3 \\ 1 \end{pmatrix}
#     \right) \cdot \left(
#         \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} -
#         \begin{pmatrix} 5 \\ 3 \\ 1 \end{pmatrix}
#     \right) - 2^2 = 22,
# \end{align*}
# 
# then $b^2 - 4ac = 22^2 - 4(5)(22) = 44$ which is greater than zero so there are two intersection points. The values of $t$ are
# 
# \begin{align*}
#     t &= \frac{22 \pm \sqrt{44}}{10}, \\
#     \therefore t &\approx 1.5367, 2.8633,
# \end{align*}    
# 
# so the intersection points are at
# 
# \begin{align*}
#     \mathbf{r}_1 &= 
#     \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + 1.5367
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 4.0734 \\ 1.5367 \\ 2 \end{pmatrix}, \\
#     \mathbf{r}_2 &= 
#     \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} + 2.8633
#     \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 6.7266 \\ 2.8633 \\ 2 \end{pmatrix}.
# \end{align*}
# ```
# 
# ````

# (intersecting-planes-section)=
# ## Intersections with planes
# 
# Recall that a plane can be defined using the {prf:ref}`point-normal equation of a plane <point-normal-definition>` 
# 
# $$ \mathbf{n} \cdot \mathbf{p} = s, $$
# 
# where $\mathbf{n}$ is a normal vector for the plane, $\mathbf{p}$ is a point on the plane and $s$ is a scalar.
# 
# (line-plane-intersection-section)=
# ### Intersection of a line and a plane
# 
# Consider the intersection of a line defined by $\mathbf{q} + t\mathbf{d}$ and the plane which passes through the point $\mathbf{p}$ and has a normal vector $\mathbf{n}$. Here we have two scenarios to consider
# 
# - the line intersects with the plane at a single point $\mathbf{r}$;
# - the line is parallel to the plane and does not intersect with it.
# 
# ```{figure} /images/line_plane_intersection.svg
# :width: 300px
# :name: line-plane-intersection-figure
# 
# Intersection between a line and a plane.
# ```
# 
# If the line is parallel to the plane then $\mathbf{d}$ is perpendicular to $\mathbf{n}$ which occurs when
# 
# $$ \mathbf{d} \cdot \mathbf{n} = 0. $$
# 
# If the line is not perpendicular then we can determine the point of intersection $\mathbf{r}$ by using the fact that the normal vector $\mathbf{n}$ is perpendicular to the vector $\mathbf{r} - \mathbf{p}$, i.e., 
# 
# \begin{align*}
#     (\mathbf{r} - \mathbf{p}) \cdot \mathbf{n} = 0.
# \end{align*}
# 
# Substituting $\mathbf{r} = \mathbf{q} + t\mathbf{d}$ and rearranging gives
# 
# \begin{align*}
#     (\mathbf{q} + t\mathbf{d} - \mathbf{p}) \cdot \mathbf{n} &= 0 \\
#     (\mathbf{q} - \mathbf{p}) \cdot \mathbf{n} + t \mathbf{d} \cdot \mathbf{n} &= 0, \\
#     \therefore t &= \frac{(\mathbf{p} - \mathbf{q}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}}.
# \end{align*}
# 
# ````{prf:theorem} Intersection between a line and a plane
# :label: line-plane-intersection
# 
# The point of intersection between a line that passes through point $\mathbf{q}$ in the direction $\mathbf{d}$ and the plane which passes through the point $\mathbf{p}$ with a normal vector $\mathbf{n}$ is $\mathbf{r} = \mathbf{p} + t\mathbf{d}$ where
# 
# ```{math}
# :label: line-plane-intersection-equation
# 
# t = \frac{(\mathbf{p} - \mathbf{q}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}}.
# ```
# 
# ````
# 
# ````{prf:example}
# :class: seealso
# 
# A line defined by the equation $(0, 1, 1) + t(3, 1, -2)$ intersects a plane with the normal vector $(-3, -1, 1)$ and which passes through the point $(8, 2, 3)$. Calculate the co-ordinates of the point of intersection between the line and the plane.
# 
# ```{dropdown} Solution
# Here $\mathbf{q} = (0, 1, 1)$, $\mathbf{d} = (3, 1, -2)$, $\mathbf{n} = (-3, -1, 1)$ and $\mathbf{p} = (8, 2, 3)$. Calculating $t$
# 
# \begin{align*}
#     t &= \frac{(\mathbf{p} - \mathbf{q}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}}
#     = \frac{\left( 
#         \begin{pmatrix} 8 \\ 2 \\ 3 \end{pmatrix} -
#         \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}
#       \right) \cdot
#       \begin{pmatrix} -3 \\ -1 \\ 1 \end{pmatrix}}{
#         \begin{pmatrix} 3 \\ 1 \\ -2 \end{pmatrix} \cdot
#         \begin{pmatrix} -3 \\ -1 \\ 1 \end{pmatrix}
#       } 
#     = \frac{23}{12}.
# \end{align*}
# 
# Calculating the intersection point
# 
# \begin{align*}
#     \mathbf{r} &= \mathbf{q} + t \mathbf{d} = 
#     \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} + \frac{23}{12} 
#     \begin{pmatrix} 3 \\ 1 \\ -2 \end{pmatrix} = 
#     \begin{pmatrix} 23/4 \\ 35/12 \\ -17/6 \end{pmatrix}.
# \end{align*}
# ```
# ````
# 
# (plane-plane-intersection-section)=
# ### Intersecting planes
# 
# With the intersection between two planes we have three scenarios to consider:
# 
# - the two planes intersect at an infinite number of points along a straight line;
# 
# ```{figure} /images/intersecting_planes_1.svg
# 
# Two intersecting planes.
# ```
# 
# - the two planes are parallel and do not intersect;
#   
# ```{figure} /images/intersecting_planes_2.svg
# 
# Two parallel planes.
# ```
# - the two planes are coincident and intersect at an infinite number of points along a straight line.
# 
# ```{figure} /images/intersecting_planes_3.svg
# 
# Two coincident planes.
# ```
# 
# Two planes defined by the point-normal equations $\mathbf{n}_1 \cdot \mathbf{p}_1 = s_1$ and $\mathbf{n}_2 \cdot \mathbf{p}_2 = s_2$ are parallel if $\mathbf{n}_1 = k \mathbf{n}_2$ for $k \neq 0$. Two parallel planes are coincident if $s_1 = s_2$
# 
# If two planes are not parallel or coincident then they intersect along a line that is perpendicular to both of the normal vectors for the planes, therefore the direction vector is 
# 
# $$\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2.$$ 
# 
# To describe the line we also need the co-ordinates of a single point, $\mathbf{r}$ along the line, i.e., a point that satisfies both
# 
# \begin{align*}
#     \mathbf{n}_1 \cdot \mathbf{r} &= s_1, \\
#     \mathbf{n}_2 \cdot \mathbf{r} &= s_2.
# \end{align*}
# 
# Subtracting one from the other and rearranging gives
# 
# \begin{align*}
#     \mathbf{n}_1 \cdot \mathbf{r} - \mathbf{n}_2 \cdot \mathbf{r} &= s_1 - s_2 \\
#     (\mathbf{n}_1 - \mathbf{n}_2) \cdot \mathbf{r} &= s_1 - s_2.
# \end{align*}
# 
# Let $\mathbf{r} = (x,y,z)$ then
# 
# \begin{align*}
#     (\mathbf{n}_1 - \mathbf{n}_2) \cdot \begin{pmatrix} x \\ y \\ z \end{pmatrix} &= s_1 - s_2.
# \end{align*}
# 
# So we have an expression with three unknowns, $x$, $y$ and $z$. For simplicity let $y=z=0$ then 
# 
# \begin{align*}
#     (n_{1x} - n_{2x}) x &= s_1 - s_2 \\
#     \therefore x &= \frac{s_1 - s_2}{n_{1x} - n_{2x}},
# \end{align*}
# 
# so $\mathbf{r} = ((s_1 - s_2) / (n_{1x} - n_{2x}), 0, 0)$.
# 
# ````{prf:example}
# :class: seealso
# :label: intersecting-planes-example
# 
# Two non-parallel planes are defined by the equations $(3,-4,1)\cdot \mathbf{p} = 5$ and $(1,1,-1)\cdot \mathbf{q} = 2$ respectively. Find the intersection of these two planes
# 
# ```{dropdown} Solution
# 
# The normal vectors for these planes are $\mathbf{n}_1 = (3, -4, 1)$ and $\mathbf{n}_2 = (1, 1, -1)$ respectively. Calculate the direction vector for the line of intersection
# 
# \begin{align*}
#     \mathbf{d} = 
#     \begin{pmatrix} 3 \\ -4 \\ 1 \end{pmatrix} \times
#     \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} =
#     \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & -4 & 1 \\ 1 & 1 & -1 \end{vmatrix} =
#     \begin{pmatrix} 3 \\ 4 \\ 7 \end{pmatrix}.
# \end{align*}
# 
# Calculate a point which is on the line of intersection
# 
# \begin{align*}
#     x &= \frac{s_1 - s_2}{n_{1x} - n_{2x}} = \frac{5 - 2}{3 - 1} = \frac{3}{2},
# \end{align*}
# 
# therefore $\mathbf{r} = (3/2, 0, 0)$ so the intersection of the two planes is along the line $(3/2, 0, 0) + t(3, 4, 7)$.
# 
# ````
# 
# (sphere-plane-intersection-section)=
# ### Intersection between a sphere and a plane
# 
# Consider the possible intersection with a sphere centred at position $\mathbf{c}$ with radius $r$ traveling in a straight line in the direction of $\mathbf{d}$ with plane that passes through the point $\mathbf{p}$ with normal vector $\mathbf{n}$ ({numref}`sphere-plane-intersection-1-figure`).
# 
# ```{figure} /images/sphere_plane_intersection_1.svg
# :name: sphere-plane-intersection-1-figure
# :width: 400px
# 
# The intersection between a sphere with a plane.
# ```
# 
# A collision occurs when the distance between the centre at $\mathbf{c} + t\mathbf{d}$ and the plane is equal to the radius of the sphere. This distance is given by equation {eq}`point-plane-distance-equation` which is written below
# 
# \begin{align*}
#     d = (\mathbf{q} - \mathbf{p}) \cdot \frac{\mathbf{n}}{|\mathbf{n}|}.
# \end{align*}
# 
# where $\mathbf{q}$ is a point not on the plane. In our case $\mathbf{q} = \mathbf{c} + t \mathbf{d}$
# 
# so
# 
# \begin{align*}
#     r &= (\mathbf{c} + t \mathbf{d} - \mathbf{p}) \cdot \frac{\mathbf{n}}{|\mathbf{n}|} \\
#     |\mathbf{n}| r &= (\mathbf{c} - \mathbf{p}) \cdot \mathbf{n} + t \mathbf{d} \cdot \mathbf{n} \\
#     |\mathbf{n}| r + (\mathbf{p} - \mathbf{c}) \cdot \mathbf{n} &= t \mathbf{d} \cdot \mathbf{n} \\
#     \therefore t &= \frac{|\mathbf{n}|r + (\mathbf{p} - \mathbf{c}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}}.
# \end{align*}
# 
# This formula gives that value of $t$ where a collision occurs. However, this assumes that a collision will occur, there are two other scenarios we need to consider:
# 
# - the sphere is moving parallel to the plane;
# 
# ```{figure} /images/sphere_plane_intersection_2.svg
# :name: sphere-plane-intersection-2-figure
# :width: 400px
# 
# The sphere is moving parallel to the plane.
# ```
# 
# - the sphere is moving away from the plane.
# 
# ```{figure} /images/sphere_plane_intersection_3.svg
# :name: sphere-plane-intersection-3-figure
# :width: 400px
# 
# The sphere is moving away from the plane.
# ```
# 
# When the sphere is moving parallel to the plane this angle is $\pi/2$, using the {prf:ref}`geometric definition of the dot product <geometric-dot-product-definition>`
# 
# \begin{align*}
# 	\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta),
# \end{align*}
# 
# and since $\cos(\pi/2) = 0$ then if $\mathbf{d} \cdot \mathbf{n} = 0$ then we know that the sphere is moving parallel to the plane. For the scenario where the sphere is moving away from the plane we need to consider whether the sphere is in relation to the normal vector. If the sphere is in the space that the normal vector is pointing towards, known as being **in front** of the plane, then the distance between $\mathbf{c}$ and the plane will be positive, i.e.,
# 
# $$ (\mathbf{c} - \mathbf{p}) \cdot \mathbf{n} 
# \begin{cases}
#     > 0, & \text{sphere is in front of the plane}, \\
#     < 0, & \text{sphere is behind the plane}.
# \end{cases}$$
# 
# We can adapt the formula derived above for calculating $t$ to take this into account 
# 
# ```{math}
# :label: sphere-plane-intersection-equation
# 
# t = \frac{\operatorname{sign}((\mathbf{c} - \mathbf{p}) \cdot \mathbf{n} )|\mathbf{n}|r + (\mathbf{p} - \mathbf{c}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}}
# ```
# 
# where $\operatorname{sign}(x)$ returns $1$ if $x>0$ or $-1$ is $x<0$. If equation {eq}`sphere-plane-intersection-equation` returns a negative value then the sphere is moving away from the plane.
# 
# ````{prf:example}
# :class: seealso
# 
# A sphere centred at $(-2, 3, 0)$ with radius 1 is traveling along a straight line in the direction $(1, -1, -1)$. A plane passes through the point $(1, -4, 2)$ with a normal vector $(2, -1, 2)$. Does the sphere collide with the plane and if so, what is the co-ordinates of the centre of the sphere at the point of collision?
# 
# ```{dropdown} Solution
# 
# In this case $\mathbf{c} = (-2,3,0)$, $r=1$, $\mathbf{d} = (1, -1, -1)$, $\mathbf{p} = (1, -4, 2)$ and $\mathbf{n} = (2, -1, 2)$. First we check whether the sphere is traveling parallel to the plane
# 
# \begin{align*}
#     (\mathbf{c} - \mathbf{p}) \cdot \mathbf{n} & \left( 
#         \begin{pmatrix} -2 \\ 3 \\ 0 \end{pmatrix} - 
#         \begin{pmatrix} 1 \\ -4 \\ 2 \end{pmatrix}
#     \right) \cdot
#     \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}
#     = -17,
# \end{align*}
# 
# so the sphere is not moving parallel to the plane. Using equation {eq}`sphere-plane-intersection-equation` to calculate $t$
# 
# \begin{align*}
#     t &= \frac{\operatorname{sign}((\mathbf{c} - \mathbf{p}) \cdot \mathbf{n} )|\mathbf{n}|r + (\mathbf{p} - \mathbf{c}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}} \\
#     &= \frac{(-1) \left| 
#         \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}
#     \right|(1) + \left(
#         \begin{pmatrix} 1 \\ -4 \\ 2 \end{pmatrix} -
#         \begin{pmatrix} -2 \\ 3 \\ 0 \end{pmatrix}
#     \right) \cdot
#     \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}}{
#     \begin{pmatrix} 1 \\ -1 \\ -1 \end{pmatrix} \cdot
#     \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}
#     } \\
#     &= \frac{-3 + 17}{1} = 14.
# \end{align*}
# 
# So $t$ is positive so the sphere does collide with the plane. The centre of the sphere at the point of collision is
# 
# \begin{align*}
#     \mathbf{c} + t \mathbf{d} = 
#     \begin{pmatrix} -2 \\ 3 \\ 0 \end{pmatrix} + 14
#     \begin{pmatrix} 1 \\ -1 \\ -1 \end{pmatrix} =
#     \begin{pmatrix} 12 \\ -11 \\ -14 \end{pmatrix}.
# \end{align*}
# ```
# ````
