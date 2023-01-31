#!/usr/bin/env python
# coding: utf-8

# # Vector Geometry Exercises
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex1
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
# ```{solution} co-ordinate-geometry-ex1
# :label: co-ordinate-geometry-ex1-solution
# :class: dropdown
# 
# (a) $|\mathbf{a}| = \sqrt{1^2 + 0^2 + 3^2} = \sqrt{1 + 9} = \sqrt{10}$;
# 
# (b) $\hat{\mathbf{b}} = \dfrac{\mathbf{b}}{|\mathbf{b}|} = \dfrac{1}{\sqrt{14}} \begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} -\sqrt{14} / 7 \\ 3\sqrt{14} / 14 \\ \sqrt{14} / 14 \end{pmatrix}$;
# 
# (c) $ 3\mathbf{a} + 2 \mathbf{c} = 3 \begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix} + 2\begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 9 \end{pmatrix} + \begin{pmatrix} -4 \\ 6 \\ 2 \end{pmatrix} = \begin{pmatrix} -1 \\ 6 \\ 11 \end{pmatrix}$;
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
#     \begin{pmatrix} -9 \\ -5 \\ 3 \end{pmatrix}, \\
#     \therefore \mathbf{d} = \frac{\mathbf{a} \times \mathbf{b}}{|\mathbf{a} \times \mathbf{b}|}
#     = \frac{1}{\sqrt{115}} \begin{pmatrix} -9 \\ -5 \\ 3 \end{pmatrix}
#     = \begin{pmatrix} -9\sqrt{115}/115 \\ \sqrt{115}/23 \\ 3\sqrt{115}/115 \end{pmatrix}
# \end{align*}
# ```
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex2
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
# ```{solution} co-ordinate-geometry-ex2
# :label: co-ordinate-geometry-ex2-solution
# :class: dropdown
# 
# (a) 
# \begin{align*}
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 1 & 0 \\
#         1 & 1 & 0 & 0 
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - R_1 \end{array} &
#     \longrightarrow
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 1 & 0 \\
#         0 & 1 & -1 & 0 
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - R_2 \end{array} \\ \\
#     \longrightarrow
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 1 & 0 \\
#         0 & 0 & -2 & 0 
#     \end{array} \right)
#     \begin{array}{l} \\  \\ -\frac{1}{2}R_3 \end{array} &
#     \longrightarrow
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 1 & 0 \\
#         0 & 1 & 1 & 0 \\
#         0 & 0 & 1 & 0 
#     \end{array} \right)
#     \begin{array}{l} R_1 - R_3 \\ R_2 - R_3 \\ \phantom{x} \end{array} \\ \\ 
#     \longrightarrow
#     & \left( \begin{array}{ccc|c}
#         1 & 0 & 0 & 0 \\
#         0 & 1 & 0 & 0 \\
#         0 & 0 & 1 & 0 
#     \end{array} \right)
# \end{align*}
# Therefore the only solution to $\alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + \alpha_3 \mathbf{u}_3 = \mathbf{0}$ is $\alpha_1 = \alpha_2 = \alpha_3$ so $\{ \mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3 \}$ are linearly independent.
# 
# (b) $A_{E\to U} = (\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1}$
# 
# \begin{align*}
#     \begin{vmatrix} 
#         1 & 0 & 1 \\
#         0 & 1 & 1 \\
#         1 & 1 & 0 
#     \end{vmatrix} &= 
#     \begin{vmatrix} 1 & 1 \\ 1 & 0 \end{vmatrix} +
#     \begin{vmatrix} 0 & 1 \\ 1 & 1 \end{vmatrix}
#     = -1 - 1 = -2, \\
#     \operatorname{adj}\begin{pmatrix} 
#         1 & 0 & 1 \\
#         0 & 1 & 1 \\
#         1 & 1 & 0 
#     \end{pmatrix} &=
#     \begin{pmatrix}
#         -1 & 1 & -1 \\
#         1 & -1 & -1 \\
#         -1 & -1 & 1 
#     \end{pmatrix}^\mathrm{T} =
#     \begin{pmatrix}
#         -1 & 1 & -1 \\
#         1 & -1 & -1 \\ 
#         -1 & -1 & 1
#     \end{pmatrix}, \\
#     \therefore 
#     A_{E \to U} &= \begin{pmatrix} 
#         1 & 0 & 1 \\
#         0 & 1 & 1 \\
#         1 & 1 & 0 
#     \end{pmatrix}^{-1} = \frac{1}{-2}
#     \begin{pmatrix}
#         -1 & 1 & -1 \\
#         1 & -1 & -1 \\ 
#         -1 & -1 & 1
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix} 
#         1/2 & -1/2 & 1/2 \\
#         -1/2 & 1/2 & 1/2 \\
#         1/2 & 1/2 & -1/2
#     \end{pmatrix}.
# \end{align*}
# 
# (c) $[\mathbf{v}]_U = A_{E \to U} \mathbf{v}$
# \begin{align*}
#     [\mathbf{v}]_U  =
#     \begin{pmatrix} 
#         1/2 & -1/2 & 1/2 \\
#         -1/2 & 1/2 & 1/2 \\
#         1/2 & 1/2 & -1/2
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix} &= 
#     \begin{pmatrix} -6 \\ 0 \\ 2 \end{pmatrix}.
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
#     \end{array} \right)
#     \begin{array}{l}  \\ R_2 - R_3 \\ \phantom{x} \end{array} \\ \\
# \end{align*}
# 
# ```
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex3
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
# ```{solution} co-ordinate-geometry-ex3
# :label: co-ordinate-geometry-ex3-solution
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
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex4
# 
# A polygon has vertices with the co-ordinates $\mathbf{p}_1=(8,-2,1)$, $\mathbf{p}_2=(9,1,3)$ and $\mathbf{p}_3=(8,2,-2)$. 
# 
# (a) Determine the point-normal equation of the plane.
# 
# (b) Another point on the plane has co-ordinates $\mathbf{p}_4 = (x, 9, 0)$. Determine the value of $x$.
# ```
# 
# ```{solution} co-ordinate-geometry-ex4
# :label: co-ordinate-geometry-ex4-solution
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
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex5
# 
# A lighthouse is positioned at co-ordinates $\mathbf{q} = (400, 300, 100)$ (m) and a boat positioned at co-ordinates $(-500, 200, 100)$ (m) is traveling with the velocity $\mathbf{d} = (5, -10, 0) \text{ ms^{-1}}$.
# 
# How many seconds elapse when the boat is at its closest position to the lighthouse? How far is the boat from the lighthouse at its closest point?
# ```
# 
# ```{solution} co-ordinate-geometry-ex5
# :label: co-ordinate-geometry-ex5-solution
# :class: dropdown
# 
# This is a shortest distance problem between a point $\mathbf{q}$ and the line $\mathbf{p} + t \mathbf{d}$. 
# 
# \begin{align*}
#     t = \frac{(\mathbf{q} - \mathbf{p}) \cdot \mathbf{d}}{\mathbf{d} \cdot \mathbf{d}} =
#     \frac{\left(
#         \begin{pmatrix} 400 \\ 300 \\ 100 \end{pmatrix} -
#         \begin{pmatrix} -500 \\ 200 \\ 100 \end{pmatrix} \right) \cdot 
#         \begin{pmatrix} 5 \\ -10 \\ 0 \end{pmatrix}}{
#         \begin{pmatrix} 5 \\ -10 \\ 0 \end{pmatrix} \cdot
#         \begin{pmatrix} 5 \\ -10 \\ 0 \end{pmatrix}} \\
#     &= \frac{\begin{pmatrix} 900 \\ 100 \\ 0 \end{pmatrix} \cdot
#     \begin{pmatrix} 5 \\ -10 \\ 0 \end{pmatrix}}{125} 
#     = \frac{3500}{125} = 28,
# \end{align*}
# so the boat is closest to the lighthouse after 28 seconds.
# \begin{align*}
#     \mathbf{r} &= \mathbf{p} + t \mathbf{d} = \begin{pmatrix} -500 \\ 200 \\ 100 \end{pmatrix} + 28
#     \begin{pmatrix} 5 \\ -10 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} -360 \\ -80 \\ 100 \end{pmatrix}, \\
#     \therefore d &= |\mathbf{q} - \mathbf{r}| = \left| 
#     \begin{pmatrix} 400 \\ 300 \\ 100 \end{pmatrix} -
#     \begin{pmatrix} -360 \\ -80 \\ 100 \end{pmatrix} \right|
#     = | \begin{pmatrix} 760 \\ 380 \\ 0 \end{pmatrix} \right| = \sqrt{722000} = 849.7058
# \end{align*}
# At its closest point the boat is 849.71 metres from the lighthouse.
# ```
# 
# ```{exercise}
# :label: co-ordinate-geometry-ex6
# 
# In a computer game a character shoots a laser pistol from position $\mathbf{q} = (5, 1, 2)$ in the direction $\mathbf{d} = (2, -1, 1)$. The laser shot collides with a polygon that passes through the point $\mathbf{p} = (10, 0, -1)$ with the normal vector $\mathbf{n} = (-4, 1, 1)$.  
# ```
