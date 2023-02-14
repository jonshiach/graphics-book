#!/usr/bin/env python
# coding: utf-8

# (translation-section)=
# # Translation
# 
# **Translation** is a linear transformation that moves a set of points by the vector $\mathbf{t}$ ({numref}`translation-figure`).
# 
# ```{figure} ../images/translation.svg
# :name: translation-figure
# :width: 250px
# 
# The translation of a point $\mathbf{u}$ by the translation vector $\mathbf{t}$ to the point $\mathbf{v}$
# ```
# 
# Using vector addition it is easy to see that
# 
# $$\mathbf{v} = \mathbf{u} + \mathbf{t}.$$
# 
# To represent translation using a single transformation matrix we need a matrix $T(\mathbf{t})$ that satisfies
# 
# \begin{align*}
#     T(\mathbf{t}) \begin{pmatrix} u_1 \\ u_2 \\ u_3 \end{pmatrix}  = \begin{pmatrix} u_1 + t_1 \\ u_2 + t_2 \\ u_3 + t_3 \end{pmatrix}.
# \end{align*}
# 
# Unfortunately the matrix $T(\mathbf{t})$ does not exist which is independent of $u_1$, $u_2$ and $u_3$ so we can use a trick which makes use of **homogeneous co-ordinates**.
# 
# ```{prf:definition} Homogeneous co-ordinates
# :label: homogeneous-coordinates-definition
# 
# The homogeneous co-ordinates of a point $\mathbf{u}$ in $\mathbb{R}^3$ expressed using the Cartesian co-ordinates is the 4-tuple $(w x, w y, w z, w)$ where $w \in \mathbb{R}\backslash \{0\}$. 
# 
# Note that a point with homogeneous co-ordinates $(x, y, z, 1)$ has the Cartesian co-ordinates $(x, y, z)$.
# ```
# 
# If $\mathbf{u}= (u_x, u_x, u_y, 1)$ expressed using homogeneous co-ordinates then the translation by the translation vector $\mathbf{t} = (t_x, t_y, t_z)$ is
# 
# \begin{align*}
#     v_x &= u_x + t_x, \\
#     v_y &= u_y + t_y, \\
#     v_z &= u_z + t_z,
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix} v_x \\ v_y \\ v_z \\ 1 \end{pmatrix} &= 
#     \begin{pmatrix}
#         1 & 0 & 0 & t_x \\
#         0 & 1 & 0 & t_y \\
#         0 & 0 & 1 & t_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} u_x \\ u_y \\ u_z \\ 1 \end{pmatrix}.
# \end{align*}
# 
# The square matrix is the transformation matrix for translating a point of set of points by the translation vector $\mathbf{t}$.
# 
# ````{prf:definition} Translation matrix
# :label: translation-matrix-definition
# 
# The transformation matrix for the translation of a vector in $\mathbb{R}^3$ expressed using homogeneous co-ordinates by the translation vector $\mathbf{t} = (t_x, t_y, t_z)$ is
# 
# ```{math}
# :label: translation-matrix-equation
# 
# \begin{align*}
#     T(\mathbf{t}) = \begin{pmatrix}
#         1 & 0 & 0 & t_x \\
#         0 & 1 & 0 & t_y \\
#         0 & 0 & 1 & t_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# ```
# The transformation matrix for inverse translation is
# 
# ```{math}
# :label: inverse-translation-matrix-equation
# 
# \begin{align*}
#     T^{-1}(\mathbf{t}) = T(\mathbf{-t}) = \begin{pmatrix}
#         1 & 0 & 0 & -t_x \\
#         0 & 1 & 0 & -t_y \\
#         0 & 0 & 1 & -t_z \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
# \end{align*}
# ```
# 
# ````
# 
# `````{prf:example}
# :class: seealso
# 
# A triangle is defined by three point with position vectors $\mathbf{p}_1 = (1, 0, 1)$, $\mathbf{p}_2 = (3, 0, 1)$ and $\mathbf{p}_3 = (2, 0, 3)$. The triangle is translated by the translation vector $\mathbf{t} = (3, 0, 1)$. Calculate the positions of the triangle vertices of the translated triangle.
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
#     \end{pmatrix},
# \end{align*}
# 
# and the translation matrix is
# 
# \begin{align*}
#     T(3, 0, 1) &= \begin{pmatrix} 
#         1 & 0 & 0 & 3 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 1 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the transformation
# 
# \begin{align*}
#     T(3,0,1) \cdot P &= 
#     \begin{pmatrix} 
#         1 & 0 & 0 & 3 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 1 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         1 & 3 & 2 \\
#         0 & 0 & 0 \\
#         1 & 1 & 3 \\
#         1 & 1 & 1 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         4 & 6 & 5 \\
#         0 & 0 & 0 \\
#         2 & 2 & 4 \\
#         1 & 1 & 1 
#     \end{pmatrix}.
# \end{align*}
# 
# So the vertex co-ordinates of the translated triangle are $(4,0,2)$, $(6, 0, 2)$ and $(5, 0, 4)$. The original triangle and the translated triangle are plotted below looking along the $y$-axis.
# 
# ```{figure} /images/translation_example.png
# :width: 400px
# ```
# ````
# 
# `````
