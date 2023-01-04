#!/usr/bin/env python
# coding: utf-8

# # Co-ordinate Geometry
# 
# ## Euclidean space
# 
# ```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Jusepe_de_Ribera_-_Euclid_-_2001.26_-_J._Paul_Getty_Museum.jpg/1024px-Jusepe_de_Ribera_-_Euclid_-_2001.26_-_J._Paul_Getty_Museum.jpg
# ---
# width: 200px
# alt: Euclid
# figclass : margin
# ---
# [Euclid](https://en.wikipedia.org/wiki/Euclid) (fl 300 BCE) {cite:p}`deribera:1630`
# ```
# 
# The field of computer graphics is almost soley concerned with the manipulation of objects in [**Euclidean space**](https://en.wikipedia.org/wiki/Euclidean_space). Attributed to the Greek mathematician [Euclid](https://en.wikipedia.org/wiki/Euclid), Euclidean space is a representation of physical space where the position of a point in the space can be described by the signed distance along perpendicular real numbers lines called **axes** (singular: axis). 
# 
# An $n$-dimensional Euclidean space is defined by $n$ perpendicular real axes and is referred to as $\mathbb{R}^n$. For example, consider the diagram of $\mathbb{R}^3$ in {numref}`R3-figure`. Here we have a representation of a 3-dimensional Euclidean space defined by the 3 axes labelled $x$, $y$ and $z$. This representation uses the [**right-hand rule**](https://en.wikipedia.org/wiki/Right-hand_rule) so-called because if we use the thumb on our right hand to represent the $x$ axis, the index finger for the $y$ axis and the middle finger for the $z$ axis then holding out the right hand palm up with the thumb and index finger at right-angles and the middle finger pointing up then we have the axis configuration shown in {numref}`R3-figure`. Doing similar with the left hand gives the **left-hand rule** where the $x$ axis is pointing in the opposite direction than in the right-hand rule. 
# 
# ```{figure} ../images/R3axes.svg
# :name: R3-figure
# :width: 150px
# :alt: Euclidean space axes
# 
# Euclidean space axes using the right-hand rule.
# ```
# 
# ## Co-ordinate systems
# 
# ```{figure} https://upload.wikimedia.org/wikipedia/commons/7/73/Frans_Hals_-_Portret_van_Ren%C3%A9_Descartes.jpg
# ---
# figclass: margin
# alt: Descartes
# figwidth: 200px
# ---
# 
# René Descartes (1596 - 1650) {cite:p}`hals:1700`
# ```
# 
# A **co-ordinate system** is a system that uses a sequence of numbers to determine the position of an object in Euclidean space. The numbers are known as **co-ordinates** and are represented in an ordered set of numbers enclosed in parenthesis known as a **tuple**. The most common example of a co-ordinate system is the **Cartesian co-ordinate system**, named after French mathematician and philosopher <a href="https://en.wikipedia.org/wiki/Ren%C3%A9_Descartes" target="_blank">René Descartes</a>), which uses perpendicular number lines to define points in the space. 
# 
# ```{figure} ../images/R3coordinates.svg
# :width: 300
# :name: R3-coordinates-figure
# 
# The co-ordinates of a point in $\mathbb{R}^3$ are represented as the 3-tuple $(x, y, z)$.
# ```
# 
# Consider {numref}`R3-coordinates-figure` where three number lines called **axes** (singular: axis) are labelled $x$, $y$ and $z$. The position of a point in this space is defined by the co-ordinates $(x, y, z)$ where $x$, $y$ and $z$ are the distances along the axes from zero. Since these values are real numbers a three-dimensional space is often denoted by $\mathbb{R}^3$. 
# 
# ## Homogeneous co-ordinates
# 
# **Homogeneous co-ordinates** are a system of co-ordinates that include an additional value in the tuple. The use of homogeneous co-ordinates is standard practice in computer graphics since they allow us to apply transformations such as translation and projection using matrix multiplication. The Cartesian co-ordinates $(x, y, z)$ are represented using homogeneous co-ordinates as $(\lambda x, \lambda y, \lambda z, \lambda)$ where $\lambda$ is some scalar quantity. Note that when $\lambda=1$ the homogeneous co-ordinates are $(x, y, z, 1)$. 
# 
# ```{prf:definition} Homogeneous co-ordinates
# :class: note
# 
# The homogeneous co-ordinates of a point $\mathbf{u}$ in $\mathbb{R}^n$ expressed using the Cartesian co-ordinates is the $(n+1)$-tuple $(\lambda u_1, \lambda u_2, \ldots, \lambda u_n, \lambda)$ where $\lambda \in \mathbb{R}\backslash \{0\}$. 
# 
# Note that a point with homogeneous co-ordinates $(u_1, u_2, \ldots, u_n, \lambda)$ has the Cartesian co-ordinates $\left(\dfrac{u_1}{\lambda}, \dfrac{u_2}{\lambda}, \ldots, \dfrac{u_n}{\lambda}\right)$.
# ```
# 
# ## Vectors
# 
# A **vector** is an object that has length and direction. In mathematical notation vectors are denoted in print using a boldface character or as an arrow over a character and underlined when handwritten
# 
# \begin{align*}
#     \mathbf{a}, \qquad \vec{a}, \qquad \underline{a}.
# \end{align*}
# 
# A vector in $\mathbb{R}^n$ is defined by the signed distance along each axis by an $n$-tuple. For example, let $\mathbf{a}$ be a vector in $\mathbb{R}^3$ defined by the 3-tuple $\mathbf{a} = (a_x, a_y, a_z)$ where $a_x,a_y,a_z \in \mathbb{R}$, then $\mathbf{a}$ can be represented geometrically as shown in {numref}`R3-vector-figure`.
# 
# ```{figure} ../images/vector.svg
# :width: 400
# :name: R3-vector-figure
# 
# A vector in $\mathbb{R}^3$.
# ```
# 
# The tuple representing a vector can be written as either a matrix consisting of a single row or a single column. So a vector in $\mathbb{R}^3$ can be represented as
# \begin{align*}
#     \mathbf{a} = (a_x, a_y, a_z) = \begin{pmatrix} a_x \\ a_y \\ a_z \end{pmatrix}.
# \end{align*}
# These representations are called **row vector** and **column vector** respectively.
# 
# ### Vector magnitude
# 
# The length of a vector $\mathbf{a}$ is known as the \textbf{magnitude} and is denoted using $|\mathbf{a}|$. 
# 
# ````{prf:definition} Vector magnitude
# :class: note
# :label: magnitude-definition
# 
# The magnitude of a vector in $\mathbb{R}^n$, $\mathbf{a} = (a_1, a_2, \ldots, a_n)$, is calculated using
# 
# ```{math}
# :label: magnitude-equation
# 
# |\mathbf{a}| = \sqrt{ \sum_{i=1}^n a_i^2 } = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}.
# ```
# 
# Note $|\mathbf{a}| > 0$. 
# ````
# 
# ````{prf:example}
# :class: seealso
# 
# Calculate the magnitude of the vector $\mathbf{a} = (3, 4, 0)$.
# 
# ```{dropdown} Solution
# \begin{align*}
#     |\mathbf{a}| = \sqrt{3^2 + 4^2 + 0} = \sqrt{25} = 5.
# \end{align*}
# ```
# 
# ````
# 
# ### Unit vectors
# 
# A **unit vector** is denoted by $\hat{\mathbf{a}}$ (referred to as '$\mathbf{a}$ hat') is a vector parallel to $\mathbf{a}$ with a magnitude of 1.
# 
# ````{prf:definition} Normalising a vector
#     
# The unit vector $\hat{\mathbf{a}}$ that is parallel to the vector $\mathbf{a}$ can be calculated using
# 
# ```{math}
# :label: normalising-vector-equation
# 
# \begin{align}
#     \hat{\mathbf{a}} = \frac{\mathbf{a}}{|\mathbf{a}|}.
# \end{align}
# ```
# 
# This is known as **normalising a vector**.
# ````
# 
# ````{prf:example}
# :class: seealso
# 
# Calculate a unit vector that is parallel to $\mathbf{a} = (3, 4, 0)$.
# 
# ```{dropdown} Solution
# \begin{align*}
#     \hat{\mathbf{a}} = \frac{(3, 4, 0)}{5} = \left( \frac{3}{5}, \frac{4}{5}, 0 \right).
# \end{align*}
# Checking that $|\hat{\mathbf{a}}|=1$
# \begin{align*}
#     |\hat{\mathbf{a}}| &= \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2 + 0^2} \\
#     &= \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = 1. \qquad \checkmark
# \end{align*}
# ```
# 
# ````
# 
# ### Vector addition and subtraction
# 
# The addition of two vectors is achieved by adding the corresponding elements in the tuples. Let $\mathbf{a}=(a_1,a_2,a_3)$ and $\mathbf{b}=(b_1,b_2,b_3)$ then the sum $\mathbf{a}+\mathbf{b}$ is calculated by
# \begin{align*}
# 	\mathbf{a} + \mathbf{b} &= 
#     \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} + 
#     \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = 
#     \begin{pmatrix} a_1 + b_1 \\ a_2 + b_2 \\ a_3 + b_3 \end{pmatrix}.
# \end{align*}
# Similarly the subtraction of two vectors is achieved by subtracting the corresponding element in the tuples, i.e.,
# \begin{align*}
# 	\mathbf{a} - \mathbf{b} &= 
#     \begin{pmatrix} a_1 \\ a_2 \\ a_3 \end{pmatrix} -
#     \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} = 
#     \begin{pmatrix} a_1 - b_1 \\ a_2 - b_2 \\ a_3 - b_3 \end{pmatrix}.
# \end{align*}
# 
# Thinking about this in a geometrical sence, the vector addition $\mathbf{a} + \mathbf{b}$ is achieved by placing the tail of $\mathbf{b}$ at the head of $\mathbf{a}$. The resulting vector points from the tail of $\mathbf{a}$ to the head of $\mathbf{b}$. The vector subtraction $\mathbf{a} - \mathbf{b}$ is achieved by reversing the direction of $\mathbf{b}$ and placing the tail at the head of $\mathbf{a}$.
# 
# ```{figure} ../images/vector_addition.svg
# :width: 400
# :name: vector-addition-figure
# 
# Vector addition and subtraction.
# ```
# 
# ### Scalar multiplication of a vector
# 
# The scalar multiple of a vector $\mathbf{a}=(a_1, a_2, a_3)$ by the scalar $k$ is defined by
# \begin{align*}
#     k\mathbf{a} = \begin{pmatrix} k a_1 \\ k a_2 \\ k a_3 \end{pmatrix}.
# \end{align*}
# The effect of multiplying a vector by a scalar is that the magnitude of the vector is scaled by the value of the scalar. If $k>0$ then the direction of the vector $k\mathbf{a}$ is the same as $\mathbf{a}$ whereas if $k<0$ then the vector $k\mathbf{a}$ points in the opposite direction to $\mathbf{a}$ ({numref}`scalar-vector-multiplication-figure`).
# 
# ```{figure} ../images/vector_scalar_multiplication.svg
# :width: 400
# :name: scalar-vector-multiplication-figure
# 
# Scalar multiples of the vector $\mathbf{a}$.
# ```
# 
# ### The dot product
# 
# The product of two vectors can be calculated in two ways: the **dot product** and the **cross product**. The dot product of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a}\cdot \mathbf{b}$ and returns a scalar quantity and the dot product is often referred to as the **scalar product**.
# 
# ````{prf:definition} Geometric definition of the dot product
# :class: note
# :label: geometric-dot-product-definition
# 
# The geometric definition of the dot product of two vectors, $\mathbf{a}, \mathbf{b} \in \mathbb{R}^n$, is
# 
# ```{math}
# :label: geometric-dot-product-equation
# 
# \begin{align}
# 	\mathbf{a} \cdot \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \cos(\theta),
# \end{align}	
# ```
# where $\theta$ is the angle between the two vectors ({numref}`angle-between-vectors-figure`).
# 
# ```{figure} ../images/angle_between_vectors.svg
# :width: 200px
# :name: angle-between-vectors-figure
# 
# The two vectors $\mathbf{a}$ and $\mathbf{b}$ and the angle between them $\theta$.
# ```
# 
# ````
# 
# 
# The value of a dot product can be computed using the algebraic definition of the dot product.
# 
# ````{prf:definition} Algebraic definition of the dot product
# 
# The dot product of two vectors $\mathbf{a}=(a_1, a_2, \ldots, a_n)$ and $\mathbf{b}= (b_1, b_2, \ldots, b_n)$ in $\mathbb{R}^n$ can be calculated using
# 
# ```{math}
# :label: dot-product-equation
# \begin{align}
#     \mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^n a_i b_i = a_1b_1 + a_2b_2 + \cdots + a_n b_n.
# \end{align}
# ```
# ````
# 
# For vectors $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c} \in \mathbb{R}^n$ the dot product has the following properties
# 
# - commutative: $\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}$;
# - distributive: $\mathbf{a} \cdot (\mathbf{b} + \mathbf{c}) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}$;
# - orthogonal: the non-zero vectors $\mathbf{a}$ and $\mathbf{b}$ are orthogonal (perpendicular) if $\mathbf{a} \cdot \mathbf{b} = 0$.
# 
# ````{prf:example}
# :class: seealso
# 
# (i) &emsp; Calculate the dot product of the two vectors $\mathbf{a}=(3,4,0)$ and $\mathbf{b}=(5, 12, 0)$.
# 
# ```{dropdown} Solution
# \begin{align*}
#     \mathbf{a}\cdot \mathbf{b} = 
#     \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} 5 \\ 12 \\ 0 \end{pmatrix} 
#     = 3 \times 5 + 4 \times 12 + 0 \times 0 = 15 + 48 = 63.
# \end{align*}
# ```
#         
# (ii) &emsp; Calculate the angle between the two vectors $\mathbf{a}=(3,4,0)$ and $\mathbf{b}=(5, 12, 0)$.
# 
# ```{dropdown} Solution
# \begin{align*}
#     \mathbf{a}\cdot \mathbf{b} &= |\mathbf{a}||\mathbf{b}|\cos(\theta)\\
#     \therefore \theta &= \cos^{-1}\left( \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}||\mathbf{b}|}\right) = \cos^{-1}\left(\frac{63}{5 \cdot 13}\right) = 0.2487.
# \end{align*}
# ```
# 
# (iii) &emsp; Two orthogonal vectors are $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(4, x, 6)$. Determine the value of $x$. 
# 
# ```{dropdown} Solution
# \begin{align*}
#     0 &= \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} \cdot
#     \begin{pmatrix} 4 \\ x \\ 6 \end{pmatrix} = 4 + 2x + 18, \\
#     \therefore x &= -11.
# \end{align*}
# ```
# 
# ````
# 
# ### The cross product
# 
# The **cross product** of two vectors $\mathbf{a}$ and $\mathbf{b}$ is denoted by $\mathbf{a} \times \mathbf{b}$ and returns a vector that is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$ ({numref}`cross-product-figure`). 
# 
# ```{figure} ../images/cross_product.svg
# :width: 300px
# :name: cross-product-figure
# 
# The cross product $\mathbf{a} \times \mathbf{b}$ is a vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}$.
# ```
# 
# ````{prf:definition} Geometric definition of the cross product
# :class: note
# 
# The cross product of two vectors, $\mathbf{a}, \mathbf{b} \in \mathbb{R}^3$, is defined by
# 
# ```{math}
# :label: geometric-cross-product-equation
# 
# \mathbf{a} \times \mathbf{b} = |\mathbf{a}| |\mathbf{b}| \sin(\theta) \hat{\mathbf{n}},
# ```
# 
# where $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$ and $\hat{\mathbf{n}}$ is a unit vector perpendicular to both $\mathbf{a}$ and $\mathbf{b}$.
# ````
# 
# The cross product of two vectors in $\mathbb{R}^3$ can be computed using the determinant formula.
# 
# 
# ````{prf:definition} Determinant formula for computing a cross product
# 
# The cross product of two vectors, $\mathbf{a}=(a_x, a_y, a_z)$ and $\mathbf{b}= (b_x, b_y, b_z)$, is computed using
# 
# ```{math}
# :label: cross-product-equation
# \begin{align}
# 	\mathbf{a} \times \mathbf{b} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} = 
#     \begin{pmatrix} a_y b_z - a_z b_y \\ a_z b_x - a_x b_z \\ a_x b_y - a_y b_z \end{pmatrix}.
# \end{align}
# ```
# ````
# 
# For vectors $\mathbf{a}$, $\mathbf{b}$, $\mathbf{c} \in \mathbb{R}^3$ and $k \in \mathbb{R}$ the cross product has the following properties:
# 
# - $\mathbf{a} \times \mathbf{a} = \mathbf{0}$;
# - $\mathbf{a} \times \mathbf{b} = -(\mathbf{b} \times \mathbf{a})$;
# - not commutative: $\mathbf{a} \times \mathbf{b} \neq \mathbf{b} \times \mathbf{a}$;
# - distributive: $\mathbf{a} \times (\mathbf{b} + \mathbf{c}) = \mathbf{a} \times \mathbf{b} + \mathbf{a} \times \mathbf{c}$;
# - scalar multiplication: $k\mathbf{a} \times \mathbf{b} = \mathbf{a} \times k\mathbf{b} = k(\mathbf{a} \times \mathbf{b})$.
# 
# 
# ````{prf:example}
# :class: seealso
# 
# Calculate the cross product of the two vectors $\mathbf{a}=(3,4,0)$ and $\mathbf{b}=(1, 2, 3)$.
# 
# ```{dropdown} Solution
# \begin{align*}
#     \mathbf{a} \times \mathbf{b} &= \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 3 & 4 & 0 \\ 1 & 2 & 3 \end{vmatrix} 
#     = \mathbf{i} \begin{vmatrix} 4 & 0 \\ 2 & 3 \end{vmatrix} - \mathbf{j}
#     \begin{vmatrix} 3 & 0 \\ 1 & 3 \end{vmatrix} + \mathbf{k}
#     \begin{vmatrix} 3 & 4 \\ 1 & 2 \end{vmatrix} \\ 
#     &= (4\cdot 3 - 0 \cdot 2)\mathbf{i} - (3 \cdot 3 - 0 \cdot 1)\mathbf{j} + (3 \cdot 2 - 4 \cdot 1)\mathbf{k} \\
#     &= \begin{pmatrix} 12 \\ -9 \\ 2 \end{pmatrix}.
# \end{align*}
# We can check that this vector is perpendicular to $\mathbf{a}$ and $\mathbf{b}$ using the dot product, e.g.,
# \begin{align*}
#     (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{a} &= \begin{pmatrix} 12 \\ -9 \\ 2 \end{pmatrix} \cdot
#     \begin{pmatrix} 3 \\ 4 \\ 0 \end{pmatrix} = 36 - 36 + 0 = 0, \\
#     (\mathbf{a} \times \mathbf{b}) \cdot \mathbf{b} &= \begin{pmatrix} 12 \\ -9 \\ 2 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = 12 - 18 + 6 = 0.
# \end{align*}
# ```
# 
# ````

# (basis-section)=
# ## Basis
# 
# A **basis** of a vector space $V$ is the set of vectors $\{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \}$ which are linearly independent (i.e., no vector in the basis can be represented as a linear combination of the other vectors in the basis) and span $V$. Every other vector $\mathbf{u}$ in $V$ can be expressed as a unique linear combination of the vectors in the basis, i.e.,
# 
# \begin{align*}
#     \mathbf{u} = \alpha_1 \mathbf{v}_1 + \alpha_2 \mathbf{v}_2 + \cdots + \alpha_n \mathbf{v}_n.
# \end{align*}
# 
# where $\alpha_i \in \mathbf{R}$. The **dimension** of a vector space $V$ is the number of vectors in the basis. For example, the basis for the Euclidean space $\mathbb{R}^3$ is commonly denoted as $\{ \mathbf{i}, \mathbf{j}, \mathbf{k} \}$ where 
# \begin{align*}
#     \mathbf{i} &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, &
#     \mathbf{j} &= \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{k} &= \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so $\mathbb{R}^3$ is known as a three-dimensional Euclidean space. The basis $\{ \mathbf{i}, \mathbf{j}, \mathbf{k} \}$ is the simplest basis for $\mathbb{R^3}$ in that it has the smallest number of non-zero values and those values are 1s. This basis is known as the standard basis.
# 
# ````{prf:definition} The standard basis
# :class: note
# 
# The **standard basis** for a vector space $\mathbb{R}^n$ is $E = \{ \mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n \}$ where $\mathbf{e}_i$ is column $i$ of the identity matrix, i.e.,
# 
# \begin{align*}
#     \mathbf{e}_1 &= \begin{pmatrix} 1  \\ 0 \\ \vdots \\ 0 \end{pmatrix}, &
#     \mathbf{e}_2 &= \begin{pmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix}, & \ldots, &&
#     \mathbf{e}_n &= \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# Note that in $\mathbb{R}^3$ it is common to use $\mathbf{i} = \mathbf{e}_1$, $\mathbf{j} = \mathbf{e}_2$ and $\mathbf{k} = \mathbf{e}_3$.
# ````
# 
# (change-of-basis-section)=
# ### Change of basis
# 
# Sometimes it is useful to write a vector with respect to a different basis which is known as the **change of basis**. For example let $\mathbf{a} \in \mathbb{R}^3$ and let $[\mathbf{a}]_U$ denote that $\mathbf{a}$ is represented with respect to the standard basis $E$. If we have another basis $U = \{ \mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ then we can repesent $\mathbf{a}$ with respect to this basis where $[\mathbf{a}]_U = (\alpha_1, \alpha_2, \alpha_3)$ such that
# 
# \begin{align*}
#     \alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \alpha_3 \mathbf{u}_3 = [\mathbf{a}]_E 
# \end{align*}
# 
# ````{prf:example}
# :class: seealso
# :label: change-of-basis-example-1
# 
# Represent the vector $[\mathbf{a}]_E = (4, 0, 5)$ with respect to the basis $U = \{(1, 1, 0), (1, -1, 1), (1, -1, -2)\}$.
# 
# ```{dropdown} Solution
# 
# We need to solve the system
# 
# \begin{align*}
#     \alpha_1 \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} + 
#     \alpha_2 \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} +
#     \alpha_3 \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix},
# \end{align*}
# 
# which can be written as the matrix equation
# 
# \begin{align*}
#     \begin{pmatrix}
#         1 & 1 & 1 \\
#         1 & -1 & -1 \\
#         0 & 1 & 2 
#     \end{pmatrix}
#     \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \alpha_3 \end{pmatrix} =
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix},
# \end{align*}
# 
# where $[\mathbf{a}]_U = (\alpha_1, \alpha_2, \alpha_3)$. Calculating the inverse of the coefficient matrix
# 
# \begin{align*}
#     \begin{pmatrix} 
#         1 & 1 & 1 \\
#         1 & -1 & -1 \\
#         0 & 1 & -2 
#     \end{pmatrix}^{-1} &=
#     \frac{1}{6}
#     \begin{pmatrix}
#         3 & 2 & 1 \\
#         3 & -2 & -1 \\
#         0 & 2 & -2
#     \end{pmatrix}^\mathrm{T} \\
#     &= \frac{1}{6} 
#     \begin{pmatrix}
#         3 & 3 & 0 \\
#         2 & -2 & 2 \\
#         1 & -1 & -2
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix} 
#         \frac{1}{2} & \frac{1}{2} & 0 \\
#         \frac{1}{3} & -\frac{1}{3} & \frac{1}{3} \\
#         \frac{1}{6} & -\frac{1}{6} & -\frac{1}{3}
#     \end{pmatrix},
# \end{align*}
# 
# so
# 
# \begin{align*}
#     [\mathbf{a}]_U = 
#     \begin{pmatrix} 
#         \frac{1}{2} & \frac{1}{2} & 0 \\
#         \frac{1}{3} & -\frac{1}{3} & \frac{1}{3} \\
#         \frac{1}{6} & -\frac{1}{6} & -\frac{1}{3}
#     \end{pmatrix}
#     \begin{pmatrix} 4 \\ 0 \\ 5 \end{pmatrix} =
#     \begin{pmatrix} 2 \\ 3 \\ -1 \end{pmatrix}.
# \end{align*}
# ```
# ````
# 
# The change of basis calculation shown in {prf:ref}`change-of-basis-example-1` was relatively straightforward as it involved changing from the standard basis. We can extend this method to change between two arbitrary basis. Let $U = \{ \mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$ and $W = \{ \mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_n \}$ be two basis for the vector space $V$ then the basis $U$ can be represnted with respect to $W$, i.e., 
# 
# ```{math}
# :label: U_W-equation
# 
# \begin{align}
#     \mathbf{u}_1 &= a_{11} \mathbf{w}_1 + a_{21} \mathbf{w}_2 + \cdots + a_{n1} \mathbf{w}_n, \\
#     \mathbf{u}_2 &= a_{12} \mathbf{w}_1 + a_{22} \mathbf{w}_2 + \cdots + a_{n2} \mathbf{w}_n, \\
#     & \vdots \\
#     \mathbf{u}_n &= a_{1n} \mathbf{w}_1 + a_{2n} \mathbf{w}_2 + \cdots + a_{nn} \mathbf{w}_n,
# \end{align}
# ```
# 
# where $a_{ij}$ are scalars. Given a vector $\mathbf{v} = (v_1, v_2, \ldots, v_n) \in V$ expressed with respect to the basis $U$ then
# 
# \begin{align*}
#     \mathbf{v} &= v_1 \mathbf{u}_1 + v_2 \mathbf{u}_2 + \cdots + v_n \mathbf{u}_n,
# \end{align*}
# 
# and substituting the expressions for $\mathbf{u}_i$ from equation {eq}`U_W-equation` then
# 
# \begin{align*}
#     \mathbf{v} &= v_1 (a_{11} \mathbf{w}_1 + a_{21} \mathbf{w}_2 + \cdots + a_{n1} \mathbf{w}_n) \\
#     & \quad + v_2 (a_{12} \mathbf{w}_1 + a_{22} \mathbf{w}_2 + \cdots + a_{n2} \mathbf{w}_n) + \cdots \\
#     & \quad + v_n (a_{1n} \mathbf{w}_1 + a_{2n} \mathbf{w}_2 + \cdots + a_{nn} \mathbf{w}_n).
# \end{align*}
# 
# Factorising by $\mathbf{w}_i$ this can be written as
# 
# \begin{align*}
#     \mathbf{v} &=  (a_{11} v_1 + a_{12} v_2 + \cdots + a_{1n} v_n) \mathbf{w}_1 \\
#     & \quad + (a_{21} v_1 + a_{22} v_2 + \cdots + a_{2n} v_n) \mathbf{w}_2 + \cdots \\
#     & \quad + (a_{n1} v_1 + a_{n2} v_2 + \cdots + a_{nn} v_n) \mathbf{w}_n.
# \end{align*}
# 
# So we know that $\mathbf{v}$ represented with respect to the basis $W$ is
# 
# \begin{align*}
#     [\mathbf{v}]_W = \begin{pmatrix} 
#         a_{11} & a_{12} & \cdots & a_{1n} \\
#         a_{21} & a_{22} & \cdots & a_{2n} \\
#         \vdots & \vdots & \ddots & \vdots \\
#         a_{n1} & a_{n2} & \cdots & a_{nn}
#     \end{pmatrix}
#     \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}.
# \end{align*}
# 
# The square matrix here is known as the **change of basis matrix** which changes the basis from $U$ to $W$ as is denoted by $A_{U \to W}$. Considering the expressions in equation {eq}`U_W-equation` then
# 
# \begin{align*}
#     A_{U \to W} = ( [\mathbf{u}_1]_W, [\mathbf{u}_2]_W, \ldots, [\mathbf{u}_n]_W ).
# \end{align*}
# 
# To calculate $A_{U \to W}$ we need to solve
# 
# \begin{align*}
#     a_{11} \mathbf{w}_1 + a_{21} \mathbf{w}_2 + \cdots + a_{n1} \mathbf{w}_n &= \mathbf{u}_1, \\
#     a_{12} \mathbf{w}_1 + a_{22} \mathbf{w}_2 + \cdots + a_{n2} \mathbf{w}_n &= \mathbf{u}_2, \\
#     & \vdots \\
#     a_{1n} \mathbf{w}_1 + a_{2n} \mathbf{w}_2 + \cdots + a_{nn} \mathbf{w}_n &= \mathbf{u}_n,
# \end{align*}
# 
# which can be done by row reducing the augmented matrix 
# 
# $$\left( 
# \begin{array}{cccc|cccc} 
#     \uparrow & \uparrow & & \uparrow & \uparrow & \uparrow & & \uparrow \\
#     \mathbf{w}_1 & \mathbf{w}_2 & \ldots & \mathbf{w}_n & \mathbf{u}_1 & \mathbf{u}_2 & \ldots & \mathbf{u}_n \\
#     \downarrow & \downarrow & & \downarrow & \downarrow & \downarrow &  & \downarrow 
# \end{array} \right)$$ 
# 
# to reduced row echelon form where $A_{U\to W}$ is the matrix to the right of the partition.
# 
# ````{prf:example}
# :class: seealso
# 
# $U$ and $W$ are two basis of $\mathbb{R}^n$ given by
# 
# \begin{align*}
#     U &= \left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right\}, \\
#     W &= \left\{ \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 1 \end{pmatrix} \right\}
# \end{align*}
# 
# (i) &emsp; Calculate the change of basis matrix $A_{U \to W}$
# 
# ```{dropdown} Solution
# To calculate $A_{U \to W}$ we need to reduce the following augmented matrix to reduced row echelon form
# 
# \begin{align*}
#     & \left( \begin{array}{cc|cc}
#         0 & -1 & 1 & 1 \\
#         1 & 1 & 0 & 1
#     \end{array} \right) 
#     \begin{array}{l} R_1 \leftrightarrow R_2 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow  
#     & \left( \begin{array}{cc|cc}
#         1 & 1 & 0 & 1 \\
#         0 & -1 & 1 & 1
#     \end{array}\right) 
#     \begin{array}{l} \\ -R_2 \end{array} \\ \\
#     \longrightarrow  
#     & \left( \begin{array}{cc|cc}
#         1 & 1 & 0 & 1 \\
#         0 & 1 & -1 & -1
#     \end{array} \right) 
#     \begin{array}{l} R_1 - R_2 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{cc|cc}
#         1 & 0 & 1 & 2 \\
#         0 & 1 & -1 & -1
#     \end{array} \right) 
# \end{align*}
# 
# therefore $A_{U\to W} = \begin{pmatrix} 1 & 2 \\ -1 & -1 \end{pmatrix}$.
# ```
# 
# (ii) &emsp; If $\mathbf{v} \in \mathbb{R}^2$ where $[\mathbf{v}]_U = (1,2)$, calculate $[\mathbf{v}]_W$
# 
# ```{dropdown} Solution
# \begin{align*}
#     [\mathbf{v}]_W &= A_{U \to W} [\mathbf{v}]_U = 
#     \begin{pmatrix} 1 & 2 \\ -1 & -1 \end{pmatrix}
#     \begin{pmatrix} 1 \\ 2 \end{pmatrix} 
#     = \begin{pmatrix} 5 \\ -3 \end{pmatrix}
# \end{align*}
# ```
# 
# ````
