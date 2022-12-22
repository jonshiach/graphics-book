#!/usr/bin/env python
# coding: utf-8

# # Scaling
# 
# **Scaling** is a linear transformation that moves a point closer or further away from the origin by a certain **scaling vector**. Consider the diagram shown in {numref}`scaling-figure` where the point at position $\mathbf{u}= (u_x, u_y, u_z)$ has been scaled by the scaling vector $\mathbf{s} = (s_x, s_y, s_z)$.
# 
# ```{figure} ../images/scaling.svg
# :name: scaling-figure
# :width: 300px
# 
# Scaling of the point $\mathbf{u} = (u_x, u_y, u_z)$ by the scaling vector $\mathbf{s} = (s_x, s_y, s_z)$. 
# ```
# 
# The co-ordinates of the scaled point $\mathbf{v}$ are easily calculated using
# 
# \begin{align*}
#     v_x &= s_xu_x, \\
#     v_y &= s_yu_y, \\
#     v_z &= s_zu_z,
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix} v_x \\ v_y \\ v_z \end{pmatrix} =
#     \begin{pmatrix}
#         s_x & 0 & 0 \\
#         0 & s_y & 0 \\
#         0 & 0 & s_z
#     \end{pmatrix}
#     \begin{pmatrix} u_x \\ u_y \\ u_z \end{pmatrix}.
# \end{align*}
# 
# Since the {prf:ref}`translation matrix <translation-matrix-definition>` requires homogeneous co-ordinates and we would like to combine transformations we can extend the square matrix above by adding the fourth row and column of the identity matrix to give the transformation matrix for scaling. 
# 
# ````{prf:definition} Scaling in $\mathbb{R}^3$
# 
# The scaling of a set of points in $\mathbb{R}^3$ expressed using homogeneous co-ordinates by the scaling vector $\mathbf{s} = (s_x, s_y, s_z)$ is the linear transformation with the transformation matrix
# 
# ```{math}
# :label: scaling-matrix-equation
# 
# \begin{align*}
#     S(\mathbf{s}) =
#     \begin{pmatrix} 
#         s_x & 0 & 0 & 0 \\
#         0 & s_y & 0 & 0 \\
#         0 & 0 & s_z & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# ```
# 
# The transformation matrix for inverse scaling is
# 
# ```{math}
# :label: inverse-scaling-matrix-equation
# 
# \begin{align*}
#     S(\mathbf{s}) =
#     \begin{pmatrix} 
#         1/s_x & 0 & 0 & 0 \\
#         0 & 1/s_y & 0 & 0 \\
#         0 & 0 & 1/s_z & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# ```
# ````
# 
# A scaling vector $\mathbf{s} = (1, 1, 1)$ will result in $S=I$ and the position of any point that is scaled will be unchanged. 
# 
# `````{prf:example}
# :class: seealso
# :label: scaling-example
# 
# A polygon is defined by three points with position vectors $\mathbf{p}_1 = (1, 0, 1)$, $\mathbf{p}_2 = (3, 0, 1)$ and $\mathbf{p}_3 = (2, 0, 3)$. The polygon is scaled by a the scaling vector $\mathbf{s} = (3, 1, 2)$. Calculate the positions of the three points after the scaling has been applied.
# 
# ````{dropdown} Solution
# 
# The homogeneous co-ordinate matrix is
# 
# \begin{align*}
#     P = \begin{pmatrix}
#         1 & 3 & 2 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# and the scaling matrix is
# 
# \begin{align*}
#     S = \begin{pmatrix}
#         3 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 2 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix},
# \end{align*}
# 
# Applying the transformation
# 
# \begin{align*}
#     S \cdot P = \begin{pmatrix}
#         3 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 2 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 3 & 2 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1
#     \end{pmatrix} =
#     \begin{pmatrix}
#         3 & 9 & 6 \\
#         0 & 0 & 0 \\
#         2 & 2 & 6 \\
#         1 & 1 & 1 
#     \end{pmatrix}.
# \end{align*}
# 
# So the vertex co-ordinates of the transformed polygon are $(3, 0, 2)$, $(9, 0, 2)$ and $(6, 0, 6)$. The original triangle and the translated triangle are plotted below look along the $y$-axis.
# 
# ```{glue:figure} scaling-plot
# ```
# 
# ````
# `````

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from myst_nb import glue
plt.rcParams['text.usetex'] = True

def scaling(s):
    return np.array([[s[0], 0, 0 ,0], [0, s[1], 0, 0], [0, 0, s[2], 0]])


P = np.array([[1, 3, 2],
              [0, 0, 0],
              [1, 1, 3],
              [1, 1, 1]])

s = np.array([3, 1, 2])
S = scaling(s)

P1 = np.dot(S, P)

# Plot polygons
fig, ax = plt.subplots()

plt.fill(P[0,:], P[2,:], fc='b', alpha=0.5)
plt.fill(P1[0,:], P1[2,:], fc='r', alpha=0.5)

plt.xlabel('$x$', fontsize=16)
plt.ylabel('$z$', fontsize=16)
ax.set_xlim([0, 10])
ax.set_ylim([0, 7])
ax.set_aspect('equal')

glue("scaling-plot", fig, display=False)


# ## Scaling about the centre of a shape
# 
# We have seen in {prf:ref}`scaling-example` that scaling the polygon resulted in the centre of the polygon shifting position and the aspect ratio of the polygon changed.. This was because scaling was applied to a shape whose centre was not at the origin. To preserve the position of the centre of a shape when scaling we first need to translate the points that define the shape to the origin, which means that the translation vector if $-\mathbf{c}$ where $\mathbf{c}$ is the centre of the shape. Then we can perform the scaling before using the inverse translation so that the centre of the shape is back at $\mathbf{c}$ ({numref}`scaling-about-centre-figure`). 
# 
# ```{figure} ../images/scaling_about_centre.svg
# :name: scaling-about-centre-figure
# 
# Steps required to rotate a polygon by its centre.
# ```
# 
# So we have the following composite transformation matrix
# \begin{align*}
#     A = T^{-1} \cdot S \cdot T
# \end{align*}
# 
# `````{prf:example}
# :class: seealso
# 
# Scale the polygon from {prf:ref}`scaling-example` by a factor of 2 in all three directions.
# 
# ````{dropdown} Solution
# 
# The homogeneous co-ordinate matrix is
# \begin{align*}
#     P = \begin{pmatrix}
#         1 & 3 & 2 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1
#     \end{pmatrix},
# \end{align*}
# 
# and since the polygon is a triangle the co-ordinates of the centre are the average of the vertices
# 
# \begin{align*}
#     \mathbf{c} = \frac{1}{3} \left(
#         \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} + 
#         \begin{pmatrix} 3 \\ 0 \\ 1 \end{pmatrix} +
#         \begin{pmatrix} 2 \\ 0 \\ 3 \end{pmatrix}
#     \right)
#     = \begin{pmatrix} 2 \\ 0 \\ 5/3 \end{pmatrix}.
# \end{align*}
# 
# The individual transformation matrices are
# 
# \begin{align*}
#     T(-\mathbf{c}) &= \begin{pmatrix}
#         1 & 0 & 0 & -2 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & -5/3 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     S(\mathbf{s}) &=
#     \begin{pmatrix}
#         2 & 0 & 0 & 0 \\
#         0 & 2 & 0 & 0 \\
#         0 & 0 & 2 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}, \\
#     T(\mathbf{c}) &= 
#     \begin{pmatrix}
#         1 & 0 & 0 & 2 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 5/3 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix},
# \end{align*}
# 
# which are multiplied to give the composite transformation matrix
# 
# \begin{align*}
#     A &= T(\mathbf{c}) \cdot S(\mathbf{s}) \cdot T(-\mathbf{c})
#     =
#     \begin{pmatrix} 
#         2 & 0 & 0 & -2 \\
#         0 & 2 & 0 & 0 \\
#         0 & 0 & 2 & -5/3 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# 
# Applying the composite transformation 
# \begin{align*}
#     A \cdot P &= \begin{pmatrix}
#         2 & 0 & 0 & -2 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 2 & -5/3 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 3 & 2 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1
#     \end{pmatrix} \\
#     &= 
#     \begin{pmatrix}
#         0 & 4 & 2 \\
#         0 & 0 & 0 \\
#         1/3 & 1/3 & 13/3 \\
#         1 & 1 & 1 
#     \end{pmatrix}.
# \end{align*}
# 
# 
# So the vertex co-ordinates of the translated polygon are $(0, 0, 1/3) \approx (0, 0, 0.33)$, $(4, 0, 1/3) \approx (4, 0, 0.33)$ and $(2, 0, 13/3) \approx (2, 0, 4.33)$. The original polygon and the translated polygon are plotted below looking along the $y$ axis.
# 
# ```{glue:figure} scaling-about-centre-plot
# ```
# 
# ````
# `````

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from myst_nb import glue
plt.rcParams['text.usetex'] = True

def scaling(s):
    return np.array([[s[0], 0, 0 ,0], [0, s[1], 0, 0], [0, 0, s[2], 0], [0, 0, 0, 1]])


def translation(t):
    return np.array([[1, 0, 0, t[0]], [0, 1, 0, t[1]], [0, 0, 1, t[2]], [0, 0, 0, 1]])


P = np.array([[1, 3, 2],
              [0, 0, 0],
              [1, 1, 3],
              [1, 1, 1]])

c = np.mean(P[:3,:], axis=1)
s = np.array([2, 2, 2])

T1 = translation(-c)
S = scaling(s)
T2 = translation(c)

A = np.linalg.multi_dot((T2, S, T1))
P1 = np.dot(A, P)

# Plot polygons
fig, ax = plt.subplots()

plt.fill(P[0,:], P[2,:], fc='b', alpha=0.5)
plt.fill(P1[0,:], P1[2,:], fc='r', alpha=0.5)

plt.xlabel('$x$', fontsize=16)
plt.ylabel('$z$', fontsize=16)
ax.set_xlim([0, 6])
ax.set_ylim([0, 5])
ax.set_aspect('equal')

glue("scaling-about-centre-plot", fig, display=False)

