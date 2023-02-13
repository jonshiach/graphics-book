#!/usr/bin/env python
# coding: utf-8

# # Linear Transformations Exercises
# 
# ```{exercise}
# :label: transformations-ex1
# 
# A linear transformation $T: \mathbb{R}^3 \to \mathbb{R}^3$ is defined by $T(x,y,z) = (x + 2y - z, 3x + z, 2x - y + 3z)$. Determine the transformation matrix for $T$ and use it to calculate $T(2, 5, 1)$.
# ```
# 
# ```{solution} transformations-ex1
# :label: transformations-ex1-solution
# :class: dropdown
# 
# \begin{align*}
#     T(\mathbf{e}_1) &= T \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = 
#     \begin{pmatrix} 1 \\ 3 \\ 2 \end{pmatrix}, \\
#     T(\mathbf{e}_2) &= T \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} =
#     \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix}, \\
#     T(\mathbf{e}_3) &= T \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} -1 \\ 1 \\ 3 \end{pmatrix},
# \end{align*}
# therefore the transformation matrix is
# \begin{align*}
#     A &= \begin{pmatrix}
#         1 & 2 & -1 \\
#         3 & 0 & 1 \\
#         2 & -1 & 3
#     \end{pmatrix}.
# \end{align*}
# Calculating $T(2, 5, 1)$
# \begin{align*}
#     T\begin{pmatrix} 2 \\ 5 \\ 1 \end{pmatrix} &= 
#     \begin{pmatrix}
#         1 & 2 & -1 \\
#         3 & 0 & 1 \\
#         2 & -1 & 3
#     \end{pmatrix}
#     \begin{pmatrix} 2 \\ 5 \\ 1 \end{pmatrix} =
#     \begin{pmatrix} 11 \\ 7 \\ 2 \end{pmatrix}.
# \end{align*}
# ```
# 
# ```{exercise}
# :label: transformations-ex2
# 
# $T: \mathbb{R}^3 \to \mathbb{R}^3$ is a linear transformation such that
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} &= \begin{pmatrix} 1 \\ -2 \\ -4 \end{pmatrix}, &
#     T\begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} &= \begin{pmatrix} 6 \\ 5 \\ 10 \end{pmatrix}, &
#     T\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix} &= \begin{pmatrix} 2 \\ 4 \\ 7 \end{pmatrix}.
# \end{align*}
# 
# Find the transformation matrix for $T$.
# ```
# 
# ```{solution} transformations-ex2
# :label: transformations-ex2-solution
# :class: dropdown
# 
# The transformation matrix is determined using equation {eq}`determining-the-transformation-matrix` which is
# 
# $$A = (T(\mathbf{u}_1), T(\mathbf{u}_2), \ldots, T(\mathbf{u}_n)) \cdot (\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n)^{-1}.$$
# 
# Using Gauss-Jordan elimination to calculate the inverse of $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1}$ 
# 
# \begin{align*}
#     & \left( \begin{array}{rrr|rrr}
#        1 & 0 & -1 & 1 & 0 & 0 \\
#        -1 & 1 & 1 & 0 & 1 & 0 \\
#        0 & 2 & 1 & 0 & 0 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ R_2 + R_1 \\ \phantom{x} \end{array} \\ \\ 
#     \longrightarrow \qquad 
#     & \left( \begin{array}{rrr|rrr}
#        1 & 0 & -1 & 1 & 0 & 0 \\
#        0 & 1 & 0 & 1 & 1 & 0 \\
#        0 & 2 & 1 & 0 & 0 & 1
#     \end{array} \right)
#     \begin{array}{l} \\ \\ R_3 - 2 R_2 \end{array} \\ \\ 
#     \longrightarrow \qquad  
#     & \left( \begin{array}{rrr|rrr}
#        1 & 0 & -1 & 1 & 0 & 0 \\
#        0 & 1 & 0 & 1 & 1 & 0 \\
#        0 & 0 & 1 & -2 & -2 & 1
#     \end{array} \right)
#     \begin{array}{l} R_1 + R_3 \\ \phantom{x} \\ \phantom{x} \end{array} \\ \\ 
#     \longrightarrow \qquad
#     & \left( \begin{array}{rrr|rrr}
#        1 & 0 & 0 & -1 & -2 & 1 \\
#        0 & 1 & 0 & 1 & 1 & 0 \\
#        0 & 0 & 1 & -2 & -2 & 1
#     \end{array} \right)
# \end{align*}
# 
# So $(\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3)^{-1} = \begin{pmatrix}  -1 & -2 & 1 \\ 1 & 1 & 0 \\ -2 & -2 & 1 \end{pmatrix}$ and
# 
# \begin{align*}
#     A &= \begin{pmatrix} 1 & 6 & 2 \\ -2 & 5 & 4 \\ -4 & 10 & 7 \end{pmatrix}
#     \begin{pmatrix} 
#         -1 & -2 & 1 \\
#         1 & 1 & 0 \\
#         -2 & -2 & 1
#     \end{pmatrix}
#     = \begin{pmatrix} 1 & 0 & 3 \\ -1 & 1 & 2 \\ 0 & 4 & 3 \end{pmatrix}.
# \end{align*}
# 
# Checking $A$
# 
# \begin{align*}
#     T\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} &=
#     \begin{pmatrix} 1 & 0 & 3 \\ -1 & 1 & 2 \\ 0 & 4 & 3 \end{pmatrix}
#     \begin{pmatrix}1 \\ -1 \\ 0 \end{pmatrix} 
#     = \begin{pmatrix} 1 \\ -2 \\ - 4 \end{pmatrix} \quad \checkmark
# \end{align*}
# 
# ```
# 
# ```{exercise}
# :label: transformations-ex3
# 
# An equilateral triangle is defined in $\mathbb{R}^2$ is centered $(3, 2)$ at the origin with side lengths 2 and with one side parallel to the $x$-axis. The triangle is to be translated by the translation vector $\mathbf{t} = (3, 1)$. 
# 
# (a) determine the co-ordinates off the three vertices of the triangle before the translation has been applied;
# 
# (b) determine the transformation matrix for the translation;
# 
# (c) using MATLAB, calculate the vertex co-ordinates of the translated triangle;
# 
# (d) plot the pre and post-translated triangle on the same axes.
# 
# ```
# 
# ````{solution} transformations-ex3
# :label: transformations-ex3-solution
# :class: dropdown
# 
# (a) Since the side lengths are 2 then the height of the triangle is $h = \sqrt{3}$. Let $(x_1,y_1)$, $(x_2,y_2)$ and $(x_3,y_3)$ be the vertex co-ordinates then $x_1 = 2$, $x_2 = 4$, $x_3 = 3$, $y_2 = y_1$ and $y_3 = y_1 + h$. The triangle is centred at $(3, 2)$ with a side parallel to the $x$-axis so
# 
# \begin{align*}
#     2 &= \frac{y_1 + y_2 + y_3}{3} = \frac{y_1 + y_1 + y_1 + h}{3} = \frac{3y_1 + \sqrt{3}}{3} \\
#     \therefore y_1 &= 2 - \frac{\sqrt{3}}{3} \approx 1.4226,
# \end{align*}
# 
# so the vertex co-ordinates are
# 
# \begin{align*}
#     &\begin{pmatrix} 2 \\ 2 - \sqrt{3}/3 \end{pmatrix}, &
#     &\begin{pmatrix} 4 \\ 2 - \sqrt{3}/3 \end{pmatrix}, &
#     &\begin{pmatrix} 3 \\ 2 + 2\sqrt{3}/3 \end{pmatrix}.
# \end{align*}
# 
# (b) $ T \begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{pmatrix}$
# 
# (c)
# 
# ```matlab
# clear
# 
# % Define vertex array
# P = [ 2, 4, 3 ;
#       2 - sqrt(3)/3, 2 - sqrt(3)/3, 2 + 2 * sqrt(3)/3 ;
#       1, 1, 1 ];
# 
# % Define translation matrix
# T = @(t) [1, 0, t(1) ; 
#           0, 1, t(2) ;
#           0, 0, 1 ];
# 
# % Apply translation
# t = [3 ; 1];
# P1 = T(t) * P
# ```
# 
# $$P_1 = 
# \begin{pmatrix}
#     5 & 7 & 6 \\
#     2.4226 & 2.4226 & 4.1547 \\
#     1 & 1 & 1 
# \end{pmatrix}
# $$
# 
# (d)
# 
# ```matlab
# figure
# patch(P(1,:), P(2,:), 'b', FaceAlpha=0.5)
# patch(P1(1,:), P1(2,:), 'r', FaceAlpha=0.5)
# axis equal
# axis([0, 8, 0, 5])
# xlabel('$x$', FontSize=12, Interpreter='latex')
# ylabel('$y$', FontSize=12, Interpreter='latex')
# ```
# 
# ```{figure} /images/exercise_12d.png
# :width: 400px
# ```
# 
# ````
# 
# ```{exercise}
# :label: transformations-ex4
# 
# The translated triangle from {ref}`transformations-ex3` is scaled by a factor of 0.5 in both directions. In MATLAB, calculate the vertex co-ordinates of the scaled triangle and produce a plot showing the pre and post scaled triangle on the same axes.
# ```
# 
# ````{solution} transformations-ex4
# :label: transformations-ex4-solution
# :class: dropdown
# 
# ```matlab
# % Calculate centre of the triangle
# c = mean(P1, 2);
# 
# % Define scaling matrix
# S = @(s) [ s(1), 0, 0 ;
#            0, s(2), 0 ;
#            0, 0, 1 ];
# 
# % Apply transformations (remembering to translate to and from origin)
# s = [0.5 ; 0.5];
# P2 = T(c) * S(s) * T(-c) * P1;
# 
# % Plot pre and post scaled triangle
# figure
# patch(P1(1,:), P1(2,:), 'b', FaceAlpha=0.5)
# patch(P2(1,:), P2(2,:), 'r', FaceAlpha=0.5)
# axis equal
# axis([0, 8, 0, 5])
# xlabel('$x$', FontSize=12, Interpreter='latex')
# ylabel('$y$', FontSize=12, Interpreter='latex')
# ```
# 
# ```{figure} /images/exercise_13.png
# :width: 400px
# ```
# 
# ````
# 
# ```{exercise}
# :label: transformations-ex5
# 
# The translated triangle from {ref}`transformations-ex3` is rotated by $\theta=\pi/4$ anti-clockwise about its centre. In MATLAB, calculate the vertex co-ordinates of the rotated triangle and produce a plot showing the pre and post rotated triangle on the same axes.
# ```
# 
# ````{solution} transformations-ex5
# :label: transformations-ex5-solution
# :class: dropdown
# 
# ```matlab
# % Calculate centre of the triangle
# c = mean(P1, 2);
# 
# % Define rotation matrix
# R = @(th) [ cos(th), -sin(th), 0 ;
#             sin(th), cos(th), 0 ;
#             0, 0, 1 ];
# 
# % Apply transformations (remembering to translate to and from origin)
# theta = pi / 4;
# P3 = T(c) * R(theta) * T(-c) * P1;
# 
# % Plot pre and post scaled triangle
# figure
# patch(P1(1,:), P1(2,:), 'b', FaceAlpha=0.5)
# patch(P3(1,:), P3(2,:), 'r', FaceAlpha=0.5)
# axis equal
# axis([0, 8, 0, 5])
# xlabel('$x$', FontSize=12, Interpreter='latex')
# ylabel('$y$', FontSize=12, Interpreter='latex')
# ```
# 
# ```{figure} /images/exercise_14.png
# :width: 400px
# ```
# 
# ````
# 
# ````{exercise}
# :label: transformations-ex6
# 
# The MATLAB code below produces a 5 second animation of a point $\mathbf{p}$ travelling in a circular arc centred at $(10,10)$ with radius 8. The point performs one full rotation per second.
# 
# ```matlab
# % Define arc parameters
# c = [10 ; 10];
# r = 8;
# 
# % Loop through animation frames
# fps = 60;
# for t = 0 : 1/fps : 5
# 
#     % Calculate point position
#     phi = t * 2 * pi;
#     p = c + r * [cos(phi) ; sin(phi)];
# 
#     % Plot point
#     clf
#     plot(p(1), p(2), 'bo', MarkerFaceColor='b')
#     axis equal
#     axis([0, 20, 0, 20])
#     title(sprintf('time = %1.2f s', t))
#     xlabel('$x$', FontSize=12, Interpreter='latex')
#     ylabel('$y$', FontSize=12, Interpreter='latex')
#     box on
#     drawnow
# end
# ```
# 
#  Copy this code into a MATLAB live script and edit it so that it does the following:
# 
#  (a) animate a square with side lengths 1 travelling with a centre at $\mathbf{p}$. (Hint: define the square vertices so it is centred at the origin).
# 
#  (b) the square from part (a) is scaled by the scaling vector $\mathbf{s} = (2+\cos(5t), 2+\cos(5t))$ about its centre;
# 
#  (c) the square rotates in an clockwise direction about its centre so that the square performs 8 rotations per second.
# 
# ````
# 
# ````{solution} transformations-ex6
# :label: transformations-ex6-solution
# :class: dropdown
# 
# ```matlab
# clear
# 
# % Define arc parameters
# c = [10 ; 10];
# r = 8;
# 
# % Define square centred at the origin
# P = [ -0.5,  0.5, 0.5, -0.5 ;
#       -0.5, -0.5, 0.5,  0.5 ;
#        1,    1,   1,    1 ];
# 
# % Define transformation matrices
# T = @(t) [1, 0, t(1) ; 
#           0, 1, t(2) ;
#           0, 0, 1 ];
# S = @(s) [ s(1), 0, 0 ;
#            0, s(2), 0 ;
#            0, 0, 1 ];
# R = @(th) [ cos(th), -sin(th), 0 ;
#             sin(th), cos(th), 0 ;
#             0, 0, 1 ];
# 
# fps = 60;
# for t = 0 : 1/fps : 5
# 
#     % Calculate square centre position
#     phi = t * 2 * pi;
#     p = c + r * [cos(phi) ; sin(phi)];
# 
#     % Transform square
#     P1 = T(p) * R(-8*t) * S([2+cos(5*t), 2+cos(5*t)]) * P;
#     
#     % Plot square
#     clf
#     patch(P1(1,:), P1(2,:), 'b', FaceAlpha=0.5)
#     axis equal
#     axis([0, 20, 0, 20])
#     title(sprintf('time = %1.2f s', t))
#     xlabel('$x$', FontSize=12, Interpreter='latex')
#     ylabel('$y$', FontSize=12, Interpreter='latex')
#     box on
#     drawnow
# end
# ```
# 
# ```{figure} /images/exercise_15.png
# :width: 400px
# ```
# 
# <img src="/images/programming.gif" alt="Computer man" style="width:48px;height:48px;">
# 
# ````
