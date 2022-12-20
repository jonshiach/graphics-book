#!/usr/bin/env python
# coding: utf-8

# # Shortest distance problems
# 
# ## Shortest distance between two points
# 
# In $\mathbb{R}^n$ the shortest distance, $d$, between two points $\mathbf{p}$ and $\mathbf{q}$ is the length of a straight line segment connecting them. If we think about this segment as of a vector, then
# 
# \begin{align*}
#     d = |\mathbf{p} - \mathbf{q}| = \sqrt{\displaystyle\sum_{i=1}^n (p_i-q_i)^2},
# \end{align*}
# 
# where $\mathbf{p} = (p_1,p_2,\dots,p_n)$ and $\mathbf{q} = (q_1,q_2,\dots,q_n)$.
# 
# ## Shortest distance between a line and a point
# 
# To find the shortest distance, $d$, between a line $\ell: \mathbf{p} + t\mathbf{d}$ and a point $\mathbf{r}$ in $\mathbb{R}^n$ we look at a plane they both lie in. Let $\mathbf{q}$ be a point on the line such that the vector $\mathbf{r} - \mathbf{q}$ is perpendicular to $\mathbf{d}$ ({numref}`point-line-distance-figure`) then
# 
# \begin{align*}
#     d = | \mathbf{r} - \mathbf{q} |.
# \end{align*}
# 
# ```{figure} ../images/point_line_distance.svg
# :name: point-line-distance-figure
# :width: 400px
# 
# The shortest distance of a point $\mathbf{r}$ from the line $\ell$ is the length of the chord $\mathbf{q} \to \mathbf{r}$ which is perpendicular to $\ell$.
# ```
# 
# Since $\mathbf{r} - \mathbf{q}$ is perpendicular to $\mathbf{d}$ so we calculate the position of $\mathbf{r}$ that satisfies
# 
# ```{math}
# :label: point-line-distance-equation
# 
# (\mathbf{r} - \mathbf{q}) \cdot \mathbf{d} = 0.
# ```
# 
# Substituting $\mathbf{r} = \mathbf{p} + t\mathbf{d}$ into equation {eq}`point-line-distance-equation` and rearranging to make $t$ the subject gives
# 
# \begin{align*}
#     (\mathbf{q} - \mathbf{p} - t \mathbf{d}) \cdot \mathbf{d} &= 0 \\
#     (\mathbf{q} - \mathbf{p}) \cdot \mathbf{d} - t \mathbf{d} \cdot \mathbf{d} &= 0 \\
#     \therefore t &= \frac{(\mathbf{q} - \mathbf{p}) \cdot \mathbf{d}}{ \mathbf{d} \cdot \mathbf{d}}.
# \end{align*}
# 
# This gives the value of the parameter $t$ that can be used to calculate the co-ordinates of the point $\mathbf{q}$ and therefore the shortest distance between the point $\mathbf{q}$ and the line $\ell$ is $|\mathbf{q} - \mathbf{r}|$.
# 
# ````{prf:theorem} The shortest distance between a point and a line
# :label: point-line-distance-theorem
# 
# The shortest distance between the point $\mathbf{r}$ and a line that passes through the point $\mathbf{p}$ in the direction $\mathbf{d}$ is $|\mathbf{r} - \mathbf{q}|$ where $\mathbf{q} = \mathbf{p} + t\mathbf{d}$ and 
# 
# ```{math}
# :label: point-line-t-equation
# 
# t = \frac{(\mathbf{q} - \mathbf{p}) \cdot \mathbf{d}}{ \mathbf{d} \cdot \mathbf{d}}.
# ```
# ````
# 
# ````{prf:example}
# 
# 
# Find the shortest distance between the point $\mathbf{r} = (2,2,2)$ and the line $\ell : (0, -2, 1) + t(1, 1, 1)$.
# 
# ```{dropdown} Solution
# 
# The direction vector is $\mathbf{d} = (1, 1, 1)$. Using equation {eq}`point-line-distance-equation`
# 
# \begin{align*}
#     t &= \frac{ \left( \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} 0 \\ -2 \\ 1 \end{pmatrix}\right) \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}}{
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
#     } \\
#     &= \frac{\begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix} \cdot 
#     \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
#     }{1 + 1 + 1} 
#     = \frac{2 + 4 + 1}{3} = \frac{7}{3}.
# \end{align*}
# 
# So the point on $\ell$ which is closest to $\mathbf{r}$ is
# 
# \begin{align*}
#     \mathbf{r} &= \begin{pmatrix} 0 \\ -2 \\ 1 \end{pmatrix} + \frac{7}{3} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}
#     = \begin{pmatrix} 7/3 \\ 1/3 \\ 10/3 \end{pmatrix},
# \end{align*}
# 
# and the shortest distance is $|\mathbf{r} - \mathbf{q}|$ so
# 
# \begin{align*}
#     \mathbf{q} - \mathbf{r} &= \begin{pmatrix} 7/3 \\ 1/3 \\ 10/3 \end{pmatrix} 
#     - \begin{pmatrix} 2 \\ 2 \\ 2 \end{pmatrix} 
#     = \begin{pmatrix} 1/3 \\ - 5/3 \\ 4/3 \end{pmatrix}, \\
#     \therefore d &= \sqrt{\left(\frac{1}{3}\right)^2 + \left(\frac{5}{3}\right)^2 + \left(\frac{4}{3}\right)^2}
#     = \sqrt{\frac{14}{3}} \approx 2.16.
# \end{align*}
# ```
# ````
# 
# ## Shortest distance between two lines
# 
# Given two lines described by $\ell_1: \mathbf{p}_1 + t\mathbf{d}_1$ and $\ell_2: \mathbf{p}_2 + t\mathbf{d}_2$ in $\mathbb{R}^n$ we have three situations to consider
# 
# - If the two lines intersect then obviously the shortest distance is obviously 0.   
# - If the two lines are parallel then any point on $\ell_1$ can gives the shortest distance between $\ell_1$ and $\ell_2$. Hence we simply choose a point $\mathbf{r}$ on $\ell_2$ and apply method for finding the distance between a point and a line ({prf:ref}`point-line-distance-theorem`).
# - If the two lines are skew then the shortest distance is the distance of the chord that is perpendicular to both $\ell_1$ and $\ell_2$ ({numref}`line-line-distance-figure`). 
# 
# ```{figure} ../images/line_line_distance.svg
# :name: line-line-distance-figure
# :width: 300px
# 
# The shortest distance between skew lines is the distance of the chord which is perpendicular to both lines.
# ```
# 
# If $\mathbf{q}_1$ and $\mathbf{q}_2$ are points on the lines $\ell_1$ and $\ell_2$ respectively then the chord $\mathbf{q}_1 \to \mathbf{q}_2$ is perpendicular to both lines has the direction vector $\mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2$. If $d$ is the distance between $\mathbf{q}_1$ and $\mathbf{q}_2$ then
# 
# ```{math}
# :label: line-line-distance-equation-1
# 
# \mathbf{q}_2 - \mathbf{q}_1 = d (\mathbf{d}_1 \times \mathbf{d}_2),
# ```
# 
# Let $\hat{\mathbf{n}} = \dfrac{\mathbf{d}_1 \times \mathbf{d}_2}{|\mathbf{d}_1 \times \mathbf{d}_2|}$ and substituting the equations of $\mathbf{q}_1$ and $\mathbf{q}_2$ equation {eq}`line-line-distance-equation-1` gives
# 
# \begin{align*}
#     \mathbf{q}_2 - \mathbf{q}_1 &= d \hat{\mathbf{n}}\\
#     (\mathbf{p}_2 + t_2 \mathbf{d}_2) - (\mathbf{p}_1 + t_1 \mathbf{d}_1) 
#     &= d \hat{\mathbf{n}}\\
#     (\mathbf{p}_2 + t_2 \mathbf{d}_2) \cdot \hat{\mathbf{n}} - (\mathbf{p}_1 + t_1 \mathbf{d}_1) \cdot \hat{\mathbf{n}} 
#     &= d \hat{\mathbf{n}} \cdot \hat{\mathbf{n}} \\
#     \mathbf{p}_2 \cdot \hat{\mathbf{n}} + t_2 \mathbf{d}_2 \cdot \hat{\mathbf{n}} - \mathbf{p}_1 \cdot \hat{\mathbf{n}} - t_1 \mathbf{d}_1 \cdot \hat{\mathbf{n}} 
#     &= d \hat{\mathbf{n}} \cdot \hat{\mathbf{n}}.
# \end{align*}
# 
# Since $\mathbf{n}$ is perpendicular to both $\ell_1$ and $\ell_2$ then $\mathbf{d}_1 \cdot \mathbf{n} = \mathbf{d}_2 \cdot \mathbf{n} = 0$ and $\hat{\mathbf{n}} \cdot \hat{\mathbf{n}} = 1$ then
# 
# \begin{align*}
#     \mathbf{p}_2 \cdot \hat{\mathbf{n}} - \mathbf{p}_1 \cdot \hat{\mathbf{n}} &= d,
# \end{align*}
# 
# which simplifies to
# 
# \begin{align*}
#     d &= (\mathbf{p}_2 - \mathbf{p}_1) \cdot \hat{\mathbf{n}}.
# \end{align*}
# 
# ````{prf:theorem} The shortest distance between two skew lines
# :label: line-line-distance-theorem
# 
# The shortest distance between two skew lines $\mathbf{q}_1 = \mathbf{p}_1 + t \mathbf{d}_1$ and $\mathbf{q}_2 = \mathbf{p}_2 + t \mathbf{d}_2$ is
# 
# ```{math}
# :label: line-line-distance-equation
# 
# d = (\mathbf{p}_2 - \mathbf{p}_1) \cdot \hat{\mathbf{n}}.
# ```
# 
# where $\mathbf{n} = \dfrac{\mathbf{d}_1 \times \mathbf{d}_2}{|\mathbf{d}_1 \times \mathbf{d}_2|}$.
# ````
# 
# ````{prf:example}
# 
# 
# Find the shortest distance between the two lines $\ell_1: (0, 1, 3) + t(1, 4, 2)$ and $\ell_2 : (1, 1, 3) + t(0, 2, 4)$.
# 
# ```{dropdown} Solution
# 
# Calculate $\hat{\mathbf{n}}$
# 
# \begin{align*}
#     \mathbf{n} &= \mathbf{d}_1 \times \mathbf{d}_2
#     = \begin{vmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         1 & 4 & 2 \\
#         0 & 2 & 4
#     \end{vmatrix} = 
#     \begin{pmatrix} 12 \\ -4 \\ 2 \end{pmatrix}, \\
#     |\mathbf{n}| &= \sqrt{12^2 + (-4)^2 + 2^2} = \sqrt{164} = 2\sqrt{41}, \\
#     \therefore \hat{\mathbf{n}} &= \frac{\mathbf{n}}{|\mathbf{n}|} = 
#     \begin{pmatrix} 6/\sqrt{41} \\ -2/\sqrt{41} \\ 1/\sqrt{41} \end{pmatrix} 
#     = \begin{pmatrix} 6\sqrt{41}/41 \\ -2\sqrt{41}/41 \\ \sqrt{41}/41 \end{pmatrix}.
# \end{align*}
# 
# Note that since $\mathbf{n}$ is non-zero, $\ell_1$ and $\ell_2$ are skew lines. Using equation {eq}`line-line-distance-equation`
# 
# \begin{align*}
#     d &= (\mathbf{p}_2 - \mathbf{p}_1) \cdot \hat{\mathbf{n}} \\
#     &= \left( \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} -
#     \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} \right) \cdot 
#     \begin{pmatrix} 6\sqrt{41}/41 \\ -2\sqrt{41}/41 \\ \sqrt{41}/41 \end{pmatrix} \\
#     &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \cdot 
#     \begin{pmatrix} 6\sqrt{41}/41 \\ -2\sqrt{41}/41 \\ \sqrt{41}/41 \end{pmatrix} \\
#     &= \frac{6 \sqrt{41}}{41}.
# \end{align*}
# ```
# ````
# 
# ## Shortest distance between a point and a plane
# 
# ```{figure} ../images/point_plane_distance.svg
# :width: 300px
# :name: point-plane-distance-figure
# 
# ```
# The shortest distance between a point $\mathbf{q}$ and the plane defined by the point $\mathbf{p}$ and the normal vector $\mathbf{n}$ is the length of a chord perpendicular to the plane to $\mathbf{q}$. The [geometric definition of the dot product](geometric-dot-product-definition) between the vectors $\mathbf{q} - \mathbf{p}$ and $\mathbf{n}$ is
# 
# 
# $$(\mathbf{q} - \mathbf{p}) \cdot \mathbf{n} = |\mathbf{q} - \mathbf{p}| |\mathbf{n}| \cos(\theta).$$(point-plane-distance-equation-1)
# 
# If we consider the right-angled triangle with the hypotenuse $|\mathbf{q} - \mathbf{p}|$ and adjacent side $d$ then
# 
# \begin{align*}
#     \cos(\theta) = \frac{d}{|\mathbf{q} - \mathbf{p}|},
# \end{align*}
# 
# which substituted into {eq}`point-plane-distance-equation-1` gives
# 
# \begin{align*}
#     (\mathbf{q} - \mathbf{p}) \cdot \mathbf{n} &= |\mathbf{q} - \mathbf{p}| |\mathbf{n}| \frac{d}{|\mathbf{q} - \mathbf{p}|} = |n|d
# \end{align*}
# 
# therefore
# 
# $$d = \frac{(\mathbf{q} - \mathbf{p}) \cdot \mathbf{n}}{|\mathbf{n}|}.$$
# 
# ````{prf:theorem}
# 
# The shortest distance between a point $\mathbf{q}$ and a plane defined by a point $\mathbf{p}$ and a unit normal vector $\hat{\mathbf{n}}$ is
# 
# ```{math}
# :label: point-plane-distance-equation
# 
# d = (\mathbf{q} - \mathbf{p}) \cdot \hat{\mathbf{n}}.
# ```
# ````
# 
# ````{prf:example}
# 
# 
# A plane is defined by the point $\mathbf{p} = (1, 1, 3)$ and the normal vector $\mathbf{n} = (1, -1, 1)$. Calculate the distance from the point $\mathbf{q} = (4, -3, 2)$ to the plane.
# 
# ```{dropdown} Solution
# 
# Normalise the normal vector
# 
# \begin{align*}
#     |\mathbf{n}| = \sqrt{1 + 1 + 1} = \sqrt{3}, \\
#     \therefore \hat{\mathbf{n}} = \frac{1}{\sqrt{3}}
#     \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} 
#     = \begin{pmatrix} \sqrt{3}/3 \\ -\sqrt{3}/3 \\ \sqrt{3}/3 \end{pmatrix}.
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     d &= \left( \begin{pmatrix} 4 \\ -3 \\ 2 \end{pmatrix} - 
#     \begin{pmatrix} 1 \\ 1 \\ 3 \end{pmatrix} \right) \cdot
#     \begin{pmatrix} \sqrt{3}/3 \\ -\sqrt{3}/3 \\ \sqrt{3}/3 \end{pmatrix} \\
#     &= \begin{pmatrix} 3 \\ -4 \\ -1 \end{pmatrix}\cdot
#     \begin{pmatrix} \sqrt{3}/3 \\ -\sqrt{3}/3 \\ \sqrt{3}/3 \end{pmatrix} \\
#     &= \sqrt{3} + \frac{4\sqrt{3}}{3} - \frac{\sqrt{3}}{3} 
#     = 2\sqrt{3} \approx 3.46.
# \end{align*}
# ```
# 
# ````
