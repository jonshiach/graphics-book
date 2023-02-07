#!/usr/bin/env python
# coding: utf-8

# # Vector Geometry Exercises
# 
# ```{exercise}
# :label: vector-geometry-ex1
# 
# Given the following vectors
# 
# \begin{align*}
#     \mathbf{a} &= \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix}, &
#     \mathbf{b} &= \begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix}, &
#     \mathbf{c} &= \begin{pmatrix} 2 \\ 5 \\ -3 \end{pmatrix},
# \end{align*}
# 
# calculate:
# 
# (a) $| \mathbf{a} |$;
# 
# (b) $\hat{\mathbf{b}}$;
# 
# (c) $ 3\mathbf{a} + 2 \mathbf{c}$;
# 
# (d) $ \mathbf{a} \cdot \mathbf{b}$;
# 
# (e) the angle between $\mathbf{a}$ and $\mathbf{c}$;
# 
# (f) $\mathbf{b} \times \mathbf{c}$;
# 
# (g) a unit vector $\mathbf{d}$ which is perpendicular to $\mathbf{a}$ and $\mathbf{b}$
# 
# ```
# 
# ```{solution} vector-geometry-ex1
# :label: vector-geometry-ex1-solution
# :class: dropdown
# 
# (a) $|\mathbf{a}| = \sqrt{1^2 + 0^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}$;
# 
# (b) $\hat{\mathbf{b}} = \dfrac{\mathbf{b}}{|\mathbf{b}|} = \dfrac{1}{\sqrt{14}} \begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} -\sqrt{14} / 7 \\ 3\sqrt{14} / 14 \\ \sqrt{14} / 14 \end{pmatrix}$;
# 
# (c) $ 3\mathbf{a} + 2 \mathbf{c} = 3 \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} + 2\begin{pmatrix} 2 \\ 5 \\ -3 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 9 \end{pmatrix} + \begin{pmatrix} 4 \\ 10 \\ -6 \end{pmatrix} = \begin{pmatrix} 7 \\ 10 \\ 3 \end{pmatrix}$;
# 
# (d) $ \mathbf{a} \cdot \mathbf{b} = \mathbf{a} = \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} \cdot \begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix} 1(-2) + 0(3) + 3(1) = 1$;
# 
# (e) $\theta = \cos^{-1} \left( \dfrac{\mathbf{a} \cdot \mathbf{c}}{|\mathbf{a}||\mathbf{c}|} \right) = \cos^{-1} \left( \dfrac{-7}{\sqrt{10}\sqrt{38}} \right) \approx 1.938$;
# 
# (f) 
# \begin{align*}
#     \mathbf{b} \times \mathbf{c} &= 
#     \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -2 & 3 & 1 \\ 2 & 5 & -3 \end{vmatrix} = 
#     \begin{vmatrix} 3 & 1 \\ 5 & -3 \end{vmatrix} \mathbf{i} - 
#     \begin{vmatrix} -2 & 1 \\ 2 & -3 \end{vmatrix} \mathbf{j} + 
#     \begin{vmatrix} -2 & 3 \\ 2 & 5 \end{vmatrix} \mathbf{k} \\
#     &= -14\mathbf{i} - 4\mathbf{j} - 16\mathbf{k} = \begin{pmatrix} -14 \\ -4 \\ -16 \end{pmatrix}
# \end{align*}
# 
# (g) 
# \begin{align*}
#     \mathbf{a} \times \mathbf{b} = 
#     \begin{vmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k}  \\
#         1 & 0 & 3 \\ 
#         -2 & 3 & 1 
#     \end{vmatrix} =
#     \begin{pmatrix} -9 \\ -7 \\ 3 \end{pmatrix}, \\
#     \therefore \mathbf{d} = \frac{\mathbf{a} \times \mathbf{b}}{|\mathbf{a} \times \mathbf{b}|}
#     = \frac{1}{\sqrt{139}} \begin{pmatrix} -9 \\ -7 \\ 3 \end{pmatrix}
#     = \begin{pmatrix} -9\sqrt{139}/139 \\ -7\sqrt{139}/139 \\ 3\sqrt{139}/139 \end{pmatrix}
# \end{align*}
# ```

# ```{exercise}
# :label: vector-geometry-ex2
# 
# A basis in $\mathbb{R}^3$ is $U = \{ \mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3 \}$ where
# 
# \begin{align*}
#     \mathbf{u}_1 &= \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} &, 
#     \mathbf{u}_2 &= \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} &,  
#     \mathbf{u}_3 &= \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}.
# \end{align*}
# 
# (a) Show that $\{ \mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3 \}$ are linearly independent;
# 
# (b) Calculate the change of basis matrix $A_{E \to U}$ that can be used to change the basis from the standard basis to $U$;
# 
# (c) Given the vector $\mathbf{v} = (2, -1, 3)_E$, determine $[\mathbf{v}]_U$ (the vector $\mathbf{v}$ represented with respect to the basis $U$);
# 
# (d) Another basis in $\mathbb{R}^3$ is $W = \{(-1, 1, 1), (0, 1, 0), (0, 1, -1) \}$, calculate the change of basis matrix $A_{U\to W}$ and hence $[\mathbf{v}]_W$. 
# ```
# 
# ```{solution} vector-geometry-ex2
# :label: vector-geometry-ex2-solution
# :class: dropdown
# 
# (a) A set of vectors is linearly independent if the determinant of the matrix formed by the column vectors is non-zero.
# 
# \begin{align*}
#     \det 
#     \begin{pmatrix}
#         1 & 0 & 1 \\
#         0 & 1 & 1 \\
#         1 & 1 & 0 
#     \end{pmatrix} &=
#     \begin{vmatrix} 1 & 1 \\ 1 & 0 \end{vmatrix} + 
#     \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix} \\
#     &= -1 - 1 = -2,
# \end{align*}
# 
# so $\mathbf{u}_1$, $\mathbf{u}_2$ and $\mathbf{u}_3$ are linearly independent.
# 
# (b) $A_{E\to U} = (\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1}$. Using Gauss-Jordan elimination to calculate the inverse matrix
# 
# \begin{align*}
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 & 1 & 1 & 0 & 0 \\ 
#         0 & 1 & 1 & 0 & 1 & 0 \\
#         1 & 1 & 0 & 0 & 0 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - R_1 \end{array} \\ \\
#     \longrightarrow \qquad
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 &  1 &  1 & 0 & 0 \\ 
#         0 & 1 &  1 &  0 & 1 & 0 \\
#         0 & 1 & -1 & -1 & 0 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - R_2 \end{array} \\ \\
#     \longrightarrow \qquad
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 &  1 &  1 &  0 & 0 \\ 
#         0 & 1 &  1 &  0 &  1 & 0 \\
#         0 & 0 & -2 & -1 & -1 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ \\ -\frac{1}{2}R_3 \end{array} \\ \\
#     \longrightarrow \qquad
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 &  1 &  1   &  0   & 0 \\ 
#         0 & 1 &  1 &  0   &  1   & 0 \\
#         0 & 0 &  1 &  1/2 &  1/2 & -1/2
#     \end{array} \right)
#     \begin{array}{l} R_1 - R_3 \\ R_2 - R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow \qquad
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 &  0 &  1/2 & -1/2 &  1/2 \\ 
#         0 & 1 &  0 & -1/2 &  1/2 &  1/2 \\
#         0 & 0 &  1 &  1/2 &  1/2 & -1/2
#     \end{array} \right)
# \end{align*}
# 
# therefore
# 
# \begin{align*}
#     A_{E \to U} &= 
#     \begin{pmatrix} 
#         1/2 & -1/2 & 1/2 \\
#         -1/2 & 1/2 & 1/2 \\
#         1/2 & 1/2 & -1/2
#     \end{pmatrix}.
# \end{align*}
# 
# (c)
# \begin{align*}
#     [\mathbf{v}]_U &= A_{E \to U} \mathbf{v} \\
#     &=
#     \begin{pmatrix} 
#         1/2 & -1/2 & 1/2 \\
#         -1/2 & 1/2 & 1/2 \\
#         1/2 & 1/2 & -1/2
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} 
#     = 
#     \begin{pmatrix} 3 \\ 0 \\ -1 \end{pmatrix}.
# \end{align*}
# 
# (d) 
# \begin{align*}
#     & \left( \begin{array}{ccc|ccc}
#         -1 & 0 & 0 & 1 & 0 & 1 \\
#         1 & 1 & 1 & 0 & 1 & 1 \\
#         1 & 0 & -1 & 1 & 1 & 0 
#     \end{array} \right)
#     \begin{array}{l} -R_1 \\ \phantom{x} \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 & 0 & -1 & 0 & -1 \\
#         1 & 1 & 1 & 0 & 1 & 1 \\
#         1 & 0 & -1 & 1 & 1 & 0 
#     \end{array} \right)
#     \begin{array}{l}  \\ R_2 - R_1 \\ R_3 - R_1 \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 & 0 & -1 & 0 & -1 \\
#         0 & 1 & 1 & 1 & 1 & 2 \\
#         0 & 0 & -1 & 2 & 1 & 1 
#     \end{array} \right)
#     \begin{array}{l}  \\ \\ -R_3 \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 & 0 & -1 & 0 & -1 \\
#         0 & 1 & 1 & 1 & 1 & 2 \\
#         0 & 0 & 1 & -2 & -1 & -1 
#     \end{array} \right)
#     \begin{array}{l}  \\ R_2 - R_3 \\ \phantom{x} \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{ccc|ccc}
#         1 & 0 & 0 & -1 & 0 & -1 \\
#         0 & 1 & 0 & 3 & 2 & 3 \\
#         0 & 0 & 1 & -2 & -1 & -1 
#     \end{array} \right),
# \end{align*}
# Therefore $A_{U \to W} = \begin{pmatrix} -1 & 0 & -1 \\ 3 & 2 & 3 \\ -2 & -1 & -1 \end{pmatrix}$. 
# \begin{align*}
#     [\mathbf{v}]_W &= A_{U \to W} [\mathbf{v}]_U \\
#     &= \begin{pmatrix} -1 & 0 & -1 \\ 3 & 2 & 3 \\ -2 & -1 & -1 \end{pmatrix}
#     \begin{pmatrix} 3 \\ 0 \\ -1 \end{pmatrix} = 
#     \begin{pmatrix} -2 \\ 6 \\ -5 \end{pmatrix}.
# \end{align*}
# 
# ```

# ```{exercise}
# :label: vector-geometry-ex3
# 
# A straight line $\ell$ in $\mathbb{R}^3$ passes through the two points $\mathbf{p}_1 = (-1, 1, 2)$ and $\mathbf{p}_2 = (2, -3, 0)$.
# 
# (a) Find the vector equation of $\ell$.
# 
# (b) Calculate the position of a point two-thirds along the chord $\mathbf{p}_1 \to \mathbf{p}_2$.
# 
# (c) Does $\ell$ pass through the point $(-7, 9, 6)$?
# ```
# 
# ```{solution} vector-geometry-ex3
# :label: vector-geometry-ex3-solution
# :class: dropdown
# 
# (a) 
# \begin{align*}
#     \mathbf{d} &= 
#     \begin{pmatrix} 2 \\ -3 \\ 0 \end{pmatrix} -
#     \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} =
#     \begin{pmatrix} 3 \\ -4 \\ -2 \end{pmatrix}, \\
#     \therefore \mathbf{q} &= \mathbf{p}_1 + t \mathbf{d} =
#     \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} + t
#     \begin{pmatrix} 3 \\ - 4\\ -2 \end{pmatrix}.
# \end{align*}
# 
# (b) $\mathbf{p}_1 + \dfrac{2}{3} \mathbf{d} = \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} + \dfrac{2}{3}
#     \begin{pmatrix} 3 \\ - 4\\ -2 \end{pmatrix} = 
#     \begin{pmatrix} 1 \\ -5/3 \\ 2/3 \end{pmatrix}.$
# 
# (c) 
# \begin{align*}
#     \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} + t
#     \begin{pmatrix} 3 \\ - 4\\ -2 \end{pmatrix} &=
#     \begin{pmatrix} -7 \\ 9 \\ 6 \end{pmatrix} \\
#     \begin{pmatrix} -1 + 3t \\ 1 - 4t \\ 2 - 2t \end{pmatrix} &=
#     \begin{pmatrix} -7 \\ 9 \\ 6 \end{pmatrix} 
# \end{align*}
# 
# The first equation gives $t = -2$ and substituting into the other two equations gives $1 - 4(-2) = 9$ and $2 - 2(-2) = 6$ so $\ell$ passes through $(-7,9,6)$.
# ```

# ```{exercise}
# :label: vector-geometry-ex4
# 
# A polygon has vertices with the co-ordinates $\mathbf{p}_1=(8,-2,1)$, $\mathbf{p}_2=(9,1,3)$ and $\mathbf{p}_3=(8,2,-2)$. 
# 
# (a) Determine the point-normal equation of the plane that passes through the polygon.
# 
# (b) Another point on the plane has co-ordinates $\mathbf{p}_4 = (x, 9, 0)$. Determine the value of $x$.
# ```
# 
# ```{solution} vector-geometry-ex4
# :label: vector-geometry-ex4-solution
# :class: dropdown
# 
# (a) 
# \begin{align*}
#     \mathbf{n} &= (\mathbf{p}_2 - \mathbf{p}_1) \times (\mathbf{p}_3 - \mathbf{p}_1) \\
#     &= \left(
#     \begin{pmatrix} 9 \\ 1 \\ 3 \end{pmatrix} - 
#     \begin{pmatrix} 8 \\ -2 \\ 1 \end{pmatrix}
#     \right) \times \left(
#     \begin{pmatrix} 8 \\ 2 \\ - 2 \end{pmatrix} -
#     \begin{pmatrix} 8 \\ -2 \\ 1 \end{pmatrix}
#     \right) =
#     \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix} \times
#     \begin{pmatrix} 0 \\ 4 \\ -3 \end{pmatrix} \\ 
#     &=
#     \begin{pmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         1 & 3 & 2 \\
#         0 & 4 & -3 
#     \end{pmatrix} =
#     \begin{pmatrix} -17 \\ 3 \\ 4 \end{pmatrix}, \\
#     s &= \mathbf{n} \cdot \mathbf{p}_1 = 
#     \begin{pmatrix} -17 \\ 3 \\ 4 \end{pmatrix} \cdot
#     \begin{pmatrix} 8 \\ -2 \\ 1 \end{pmatrix} = -138, \\
#     \therefore \mathbf{n} \cdot \mathbf{p} &= -138.
# \end{align*}
# 
# (b) 
# \begin{align*}
#     \mathbf{n} \cdot \mathbf{p}_4 &= 
#     \begin{pmatrix} -17 \\ 3 \\ 4 \end{pmatrix} \cdot
#     \begin{pmatrix} x \\ 9 \\ 0 \end{pmatrix} 
#     = -17x + 27 + 0, \\
#     \therefore -17x + 27 &= -138 \\
#     x &= \frac{165}{17}.
# \end{align*}
# ```

# ```{exercise}
# :label: vector-geometry-ex5
# 
# Two lines are defined by the vector equations $(1, 0, 1) + t_1(2, -1, 3)$ and $(1, 4, 7) + t_2(2, 0, -1)$.
# 
# (a) find the point of intersection or show that they are skew;
# 
# (b) find the shortest distance between the two lines;
# ```
# 
# ```{solution} vector-geometry-ex5
# :label: vector-geometry-ex5-solution
# :class: dropdown
# 
# (a) Setting the two lines equal to each other
# 
# \begin{align*}
#     1 + 2t_1 &= 1 + 2t_2, \\
#     -t_1 &= 4, \\
#     1 + 3t_1 &= 7 - t_2.
# \end{align*}
# 
# The second equation gives $t_1 = -4$ which substituted into the first equation gives $t_2 = -4$. Substituting both $t_1$ and $t_2$ into the third equation gives $-11 \neq 11$ which is a contradiction so the two lines do not intersect.
# 
# The direction vectors are $\mathbf{d}_1 = (2, -1, 3)$ and $\mathbf{d}_2 = (2, 0, -1)$. For the two lines to be parallel we need a scalar $k$ such that $\mathbf{d}_1 = k\mathbf{d}_2$
# 
# \begin{align*}
#     2 &= 2k, \\
#     -1 &= 0, \\
#     -1 &= -k,
# \end{align*}
# 
# the second equation is a contradiction so no value of $k$ exists and the two lines are not parallel. Since the lines do not intersect and they are not parallel they are skew.
# 
# (b) Calculate the unit vector $\hat{\mathbf{n}}$ which is perpendicular to both of the lines
# \begin{align*}
#     \mathbf{n} &= \mathbf{d}_1 \times \mathbf{d}_2 \\
#     &=
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} \times
#     \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} \\
#     &= 
#     \begin{vmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         2 & -1 & 3 \\
#         2 & 0 & -1
#     \end{vmatrix}
#     = 
#     \begin{pmatrix} 1 \\ 8 \\ 2 \end{pmatrix}, \\
#     |\mathbf{n}| &= \sqrt{1^2 + 8^2 + 2^2} 
#     = \sqrt{69}\\
#     \therefore \hat{\mathbf{n}}
#     &= \frac{\sqrt{69}}{69}
#     \begin{pmatrix} 1 \\ 8 \\ 2 \end{pmatrix}
# \end{align*}
# 
# Using equation {eq}`line-line-distance-equation`
# 
# \begin{align*}
#     
#     d &= (\mathbf{p}_2 - \mathbf{p}_1) \cdot \hat{\mathbf{n}} \\
#     &= \left(
#         \begin{pmatrix} 1 \\ 4 \\ 7 \end{pmatrix} -
#         \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}
#     \right) \cdot \frac{1}{\sqrt{69}} 
#     \begin{pmatrix} 1 \\ 8 \\ 2 \end{pmatrix} \\
#     &= \frac{0 + 32 + 12}{\sqrt{69}} = \frac{44 \sqrt{69}}{69}.
# \end{align*}
# ```

# ```{exercise}
# :label: vector-geometry-ex7
# 
# In computer game a projectile is fired from position $(0, 5, -10)$ with velocity $(100, 100, 200)$ towards a wall that is modelled by the plane with normal vector $(-3, 0, -2)$ and the point at position $(10, 10, 0)$.
# 
# Calculate the position where the projectile will collide with the wall.
# ```
# 
# ```{solution} vector-geometry-ex7
# :label: vector-geometry-ex7-solution
# :class: dropdown
# 
# Let $\mathbf{q} = (0, 5, -10)$, $\mathbf{d} = (100, 100, 200)$, $\mathbf{n} = (-3, 0, -2)$ and $\mathbf{p} = (10, 10, 0)$. Using equation {eq}`line-plane-intersection-equation`
# 
# \begin{align*}
#     t &= \frac{(\mathbf{p} - \mathbf{q}) \cdot \mathbf{n}}{\mathbf{d} \cdot \mathbf{n}} \\
#     &= \frac{
#         \left(
#             \begin{pmatrix} 10 \\ 10 \\ 0 \end{pmatrix} -
#             \begin{pmatrix} 0 \\ 5 \\ -10 \end{pmatrix}
#         \right)
#         \cdot
#         \begin{pmatrix} -3 \\ 0 \\ -2 \end{pmatrix}
#     }{
#         \begin{pmatrix} 100 \\ 100 \\ 200 \end{pmatrix} \cdot
#         \begin{pmatrix} -3 \\ 0 \\ -2 \end{pmatrix}
#     } \\
#     &= \frac{-30 + 0 - 20}{-300 + 0 - 400} = \frac{-50}{-700} = \frac{1}{14}, \\
#     \therefore \mathbf{r} &= \mathbf{p} + t \mathbf{d} \\
#     &= 
#     \begin{pmatrix} 0 \\ 5 \\ -10 \end{pmatrix} + \frac{1}{14}
#     \begin{pmatrix} 100 \\ 100 \\ 200 \end{pmatrix} \\
#     &=
#     \begin{pmatrix} 120/7 \\ 120/7 \\ 100/7 \end{pmatrix}
#     \approx
#     \begin{pmatrix} 17.1429 \\ 17.1429 \\ 14.2857 \end{pmatrix}.
# \end{align*}
# ```

# ```{exercise}
# :label: vector-geometry-ex999
# 
# A point is at co-ordinates $(-1,0,25)$ m travels along a straight line with velocity $(5, 2, -1)$ m/s and an observer watches the object from a point at position $(4, 6, 6)$ m.
# 
# (a) Calculate the time $t$ at which the object makes its closest approach to the viewer.
# 
# (b) What is the distance between the observer and the object when it makes its closest approach?
# ```
# 
# ```{solution} vector-geometry-ex999
# :label: vector-geometry-ex999-solution
# :class: dropdown
# 
# (a) This is a shortest distance problem between the point $\mathbf{q}=(4,6,6)$ and the line defined by the point $\mathbf{p} = (-1, 0, 25)$ and the direction vector $\mathbf{d} = (5, 2, -1)$. Using equation {eq}`point-line-t-equation` we have
# 
# \begin{align*}
#     t &= \frac{(\mathbf{q} - \mathbf{p}) \cdot \mathbf{d}}{\mathbf{d} \cdot \mathbf{d}} \\
#     &= \frac{
#         \left( 
#             \begin{pmatrix} 4 \\ 6 \\ 6 \end{pmatrix} -
#             \begin{pmatrix} -1 \\ 0 \\ 25 \end{pmatrix}
#         \right) \cdot
#         \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix}
#     }{
#         \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix} \cdot
#         \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix}
#     } \\
#     &= \frac{25 + 12 + 19}{25 + 4 + 1} = \frac{28}{15} \approx 1.8667.
# \end{align*}
# 
# So the point makes its closest approach after 1.87 seconds. 
# 
# (b) The point at closest approach is
# 
# \begin{align*}
#     \mathbf{r} &= \mathbf{p} + t \mathbf{d} \\
#     &= \begin{pmatrix} -1 \\ 0 \\ 25 \end{pmatrix} + \frac{28}{15}
#     \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix} \\
#     &= \begin{pmatrix} 25/3 \\ 56/15 \\ 347/15 \end{pmatrix}
#     \approx
#     \begin{pmatrix} 8.3333 \\ 3.7333 \\ 23.1333 \end{pmatrix}, 
# \end{align*}
# 
# so the distance between the observer and the point at the closest approach is
# 
# \begin{align*}
#     | \mathbf{q} - \mathbf{r} | &=
#     \left|
#         \begin{pmatrix} 4 \\ 6 \\ 6 \end{pmatrix} - 
#         \begin{pmatrix} 25/3 \\ 56/15 \\ 347/15 \end{pmatrix}
#     \right| 
#     = \left|
#         \begin{pmatrix} -13/3 \\ 34/15 \\ -257/15 \end{pmatrix}
#     \right| \\
#     &= \sqrt{\left(\frac{13}{3}\right)^2 + \left(\frac{34}{15}\right)^2 + \left(\frac{257}{15}\right)^2} \\
#     &= \frac{\sqrt{71430}}{15} \approx 17.8176 \text{ m}.
# \end{align*}
# ```

# ````{exercise}
# :label: vector-geometry-ex8
# 
# Two spherical objects are moving along straight lines. The centre of the first sphere is at $\mathbf{p}_1$ and is travelling in the direction $\mathbf{d}_1$ and the second sphere is at $\mathbf{p}_2$ and is travelling in the direction $\mathbf{d}_2$. Both spheres have the same radius $r$.
# 
# ```{figure} /images/sphere_sphere_collision.svg
# ```
# 
# (a) Derive the following formula for the calculation of $t$ (hint: how far appart are $\mathbf{c}_1$ and $\mathbf{c}_2$ at the point of collision?)
# 
# $$ 0 = t^2 (\mathbf{d}_1 - \mathbf{d}_2)^2 + 2t(\mathbf{p}_1 - \mathbf{p}_2) \cdot (\mathbf{d}_1 - \mathbf{d}_2) + (\mathbf{p}_1 - \mathbf{p}_2)^2 - 4t^2.$$
# 
# (b) Write down a test for determining whether the spheres collide or not.
# 
# (c) Given that $\mathbf{p}_1 = (67/3, 91/3, 103/3)$, $\mathbf{d}_1 = (-7, -13, -10)$, $\mathbf{p}_2 = (4/3, -9, -10)$, $\mathbf{d}_2 = (2, 3, 9)$ and $r = 1$, show that the spheres will collide and hence calculate the positions of the centres of the spheres at this time.
# ````
# 
# ```{solution} vector-geometry-ex8
# :label: vector-geometry-ex8-solution
# :class: dropdown
# 
# (a) The spheres collide when the distance between their centres is $2r$
# 
# \begin{align*}
#     2r &= | \mathbf{c}_1 - \mathbf{c}_2 | \\
#     &= | \mathbf{p}_1 + t\mathbf{d}_1 - \mathbf{p}_2 - t\mathbf{d}_2 | \\
#     4r^2 &= ((\mathbf{p}_1 - \mathbf{p}_2) + t(\mathbf{d}_1 - \mathbf{d}_2))^2 \\
#     0 &= t^2 (\mathbf{d}_1 - \mathbf{d}_2)^2 + 2t(\mathbf{p}_1 - \mathbf{p}_2) \cdot (\mathbf{d}_1 - \mathbf{d}_2) + (\mathbf{p}_1 - \mathbf{p}_2)^2 - 4r^2.
# \end{align*}
# 
# (b) Let $a = (\mathbf{d}_1 - \mathbf{d}_2)^2$, $b = 2 (\mathbf{p}_1 - \mathbf{p}_2) \cdot (\mathbf{d}_1 - \mathbf{d}_2)$ and $c = (\mathbf{p}_1 - \mathbf{p}_2)^2 - 4r^2$ then
# 
# $$ b^2 - 4ac 
# \begin{cases}
#     \leq 0, & \text{spheres do not collide}, \\
#     > 0, & \text{spheres collide}.
# \end{cases}$$
# 
# (c) 
# \begin{align*}
#     \mathbf{p}_1 - \mathbf{p}_2 &=
#      \left(
#         \begin{pmatrix} 67/3 \\ 91/3 \\ 103/3 \end{pmatrix} -
#         \begin{pmatrix} 4/3 \\ -9 \\ -10 \end{pmatrix}
#     \right)   
#     = \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix}, \\
#     \mathbf{d}_1 - \mathbf{d}_2 &= 
#     \left(
#         \begin{pmatrix} -7 \\ -13 \\ -10 \end{pmatrix} -
#         \begin{pmatrix} 2 \\ 3 \\ 9 \end{pmatrix}
#     \right)
#     \begin{pmatrix} -9 \\ -16 \\ -19 \end{pmatrix}, \\
#     a &= (\mathbf{p}_1 - \mathbf{p}_2)^2 = 
#     \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix} \cdot
#     \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix} = 698, \\
#     b &= 2 (\mathbf{p}_1 - \mathbf{p}_2) \cdot (\mathbf{d}_1 - \mathbf{d}_2) \\
#     &= 2 \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix} \cdot
#     \begin{pmatrix} -9 \\ -16 \\ -19 \end{pmatrix} 
#     = -\frac{9964}{3}, \\
#     c &= (\mathbf{p}_1 - \mathbf{p}_2)^2 - 4r^2 \\
#     &= \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix} \cdot
#     \begin{pmatrix} 21 \\ 118/3 \\ 133/3 \end{pmatrix} - 4(1^2) 
#     = \frac{35546}{9},  \\
#     \therefore b^2 - 4ac &= \left( \frac{9964}{3} \right)^2 - 4(698) \left(\frac{35546}{9} \right) = 4096.  
# \end{align*}
# 
# Since $b^2 - 4ac = 4096 > 0$ the two spheres collide. Calculating the value of $t$
# 
# $$ t = \frac{-b \pm \sqrt{b^2}}{2a} = \frac{\frac{9964}{3} \pm \sqrt{4096}}{2(698)} = \frac{7}{3}, \frac{2539}{1047}.$$
# 
# Therefore the spheres collide at $t = 7/3$. Calculating the positions of the centres of the spheres at the point of collision
# 
# \begin{align*}
#     \mathbf{c}_1 &= \mathbf{p}_1 + t\mathbf{d}_1 = 
#     \begin{pmatrix} 67/3 \\ 91/3 \\ 103/3 \end{pmatrix} + \frac{7}{3}
#     \begin{pmatrix} -7 \\ -13 \\ -10 \end{pmatrix} = 
#     \begin{pmatrix} 6 \\ 0 \\ 11 \end{pmatrix}, \\
#     \mathbf{c}_2 &= \mathbf{p}_2 + t\mathbf{d}_2 =
#     \begin{pmatrix} 4/3 \\ -9 \\ -10 \end{pmatrix} + \frac{7}{3}
#     \begin{pmatrix} 2 \\ 3 \\ 9 \end{pmatrix} =
#     \begin{pmatrix} 6 \\ -2 \\ 11 \end{pmatrix}.
# \end{align*}
# ```

# ```{exercise}
# :label: vector-geometry-ex9
#         
# Two planes are defined by their normal vectors $\mathbf{n}_1 = (1, -1, 2)$ and $\mathbf{n}_2 = (-2, 1, 3)$ and pass through the points $\mathbf{p}_1 = (1, 0, 3)$ and $\mathbf{p}_2 = (4, 1, 1)$ respectively. 
# 
# Determine the equation of the line of intersection.
# ```
# 
# ```{solution} vector-geometry-ex9
# :label: vector-geometry-ex9-solution
# :class: dropdown
# 
# Calculate the vector perpendicular to both $\mathbf{n}_1$ and $\mathbf{n}_2$
# 
# \begin{align*}
#     \mathbf{d} &= \mathbf{n}_1 \times \mathbf{n}_2
#     = 
#     \begin{vmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         1 & -1 & 2 \\
#         -2 & 1 & 3
#     \end{vmatrix}
#     = 
#     \begin{pmatrix} -5 \\ -7 \\ -1 \end{pmatrix}.
# \end{align*}
# 
# Calculate the scalars in the point-normal form of the equation of a plane
# 
# \begin{align*}
#     s_1 &= \mathbf{n}_1 \cdot \mathbf{p}_1 = 
#     \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} \cdot
#     \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} = 7 \\
#     s_2 &= \mathbf{n}_2 \cdot \mathbf{p}_2 = 
#     \begin{pmatrix} -2 \\ 1 \\ 3 \end{pmatrix} \cdot
#     \begin{pmatrix} 4 \\ 1 \\ 1 \end{pmatrix} = -4.
# \end{align*}
# 
# Let $\mathbf{r} = (x, 0, 0)$ be a point on the line of intersection then
# 
# \begin{align*}
#     x = \frac{s_1 - s_2}{n_{1x} - n_{2x}} = \frac{7+4}{1+2} = \frac{11}{3},
# \end{align*}
# 
# so the equation of the line of intersection is $(11/3, 0, 0) + t(-5, -7, -1)$.
#         
# ```

# <!-- ```{exercise}
# :label: vector-geometry-ex6
# 
# In a computer game a character shoots a laser pistol from position $\mathbf{q} = (5, 1, 2)$ in the direction $\mathbf{d} = (2, -1, 1)$. The laser shot collides with a polygon that passes through the point $\mathbf{p} = (10, 0, -1)$ with the normal vector $\mathbf{n} = (-4, 1, 1)$.  
# ``` -->
