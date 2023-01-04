#!/usr/bin/env python
# coding: utf-8

# (camera-space-section)=
# # Camera space
# 
# ```{figure} /images/viewing_pipeline_camera_space.svg
# :figclass: margin
# ```
# 
# The next step in the [viewing pipeline](viewing-pipeline-section) is to align the world space to the camera space. Imagine you are viewing a virtual environment through a camera positioned in the world space at $\mathbf{p}$ and pointed towards the point with position $\mathbf{c}$ known as the **centre of view** ({numref}`camera-space-figure`). We want to transform the world space so that $\mathbf{p}$ is at the origin of a new space with axes $x^\ast$, $y^\ast$ and $z^\ast$ where, from our point of view, $x^\ast$ points to the right, $y^{\ast}$ points up and $z^\ast$ points towards us. The reason we want this new axes configuration is so that the $x$ and $y$ co-ordinates match the horizontal and vertical axes of the display.
# 
# ```{figure} /images/camera_space.svg
# :width: 600px
# :name: camera-space-figure
# 
# The world space is transformed so that the viewer $\mathbf{p}$ is the origin of a new co-ordinate axes $x^\ast$, $y^\ast$ and $z^\ast$.
# ```
# 
# The first transformation is to translate the world space by $-\mathbf{p}$ so that the viewer is positioned at the origin. The {prf:ref}`matrix <translation-matrix-definition>` that performs this translation is
# 
# \begin{align*}
# 	T = \begin{pmatrix}
# 		1 & 0 & 0 & -p_x \\
# 		0 & 1 & 0 & -p_y \\
# 		0 & 0 & 1 & -p_z \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}.
# \end{align*}
# 
# Next we need to transform from the $(x,y,z)$ axes to the $(x^\ast, y^\ast, z^\ast)$ axes. Let $C = \{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ be a [basis](basis-section) for the new axes where $\mathbf{u}=(u_1,u_2,u_3)$, $\mathbf{v} = (v_1, v_2, v_3)$ and $\mathbf{w} = (w_1, w_2, w_3)$ are unit vectors pointing in the $x^\ast$, $y^\ast$ and $z^\ast$ directions respectively. The $\mathbf{w}$ vector is calculated using
# 
# \begin{align*}
# 	\mathbf{w} = \frac{\mathbf{p} - \mathbf{c}}{|\mathbf{p} - \mathbf{c}|}.
# \end{align*} 
# 
# The $\mathbf{u}$ vector is perpendicular to the plane that $\mathbf{w}$ and $\mathbf{k}$ lie on so 
# 
# \begin{align*}
# 	\mathbf{u} = \frac{\mathbf{k} \times \mathbf{w}}{|\mathbf{k} \times \mathbf{w}|}.
# \end{align*}
# 
# The $\mathbf{v}$ vector is perpendicular to the plane that $\mathbf{u}$ and $\mathbf{w}$ lie on so
# \begin{align*}
# 	\mathbf{v} = \mathbf{w} \times \mathbf{u}.
# \end{align*}
# 
# Note that the order of the vectors in the cross products when calculating $\mathbf{u}$ and $\mathbf{v}$ are important as the cross product is not commutative. The [change of basis matrix](change-of-basis-section) for going from the standard basis $E = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ to the new basis $C = \{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is
# 
# \begin{align*}
# 	R_{E \to C} =
# 	\begin{pmatrix}
# 		u_1 & u_2 & u_3 & 0 \\
# 		v_1 & v_2 & v_2 & 0 \\
# 		w_1 & w_2 & w_3 & 0 \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}.
# \end{align*}
# 
# Combining the translation and change of basis matrix gives
# 
# \begin{align*}
# 	A &= T(-\mathbf{p}) \cdot R_{E \to C} = 
# 	\begin{pmatrix}
# 		u_1 & u_2 & u_3 & 0 \\
# 		v_1 & v_2 & v_2 & 0 \\
# 		w_1 & w_2 & w_3 & 0 \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}
# 	\begin{pmatrix}
# 		1 & 0 & 0 & -p_x \\
# 		0 & 1 & 0 & -p_y \\
# 		0 & 0 & 1 & -p_z \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix} \\
#     &=
# 	\begin{pmatrix}
# 		u_1 & u_2 & u_3 & -p_x u_1 - p_y u_2 - p_z u_3 \\
# 		v_1 & v_2 & v_2 & -p_x v_1 - p_y v_2 - p_z v_3 \\
# 		w_1 & w_2 & w_3 & -p_x w_1 - p_y w_2 - p_z w_3 \\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix} \\
# 	&=
# 	\begin{pmatrix}
# 		u_1 & u_2 & u_3 & -\mathbf{p} \cdot \mathbf{u} \\
# 		v_1 & v_2 & v_2 & -\mathbf{p} \cdot \mathbf{v} \\
# 		w_1 & w_2 & w_3 & -\mathbf{p} \cdot \mathbf{w}\\
# 		0 & 0 & 0 & 1
# 	\end{pmatrix}.
# \end{align*}
# 
# $A$ is the **alignment transformation matrix** that aligns the world space to the camera space. This is applied to the world space vertex matrix to give the camera space vertex matrix
# 
# \begin{align*}
# 	V_{\text{camera}} = A \cdot V_{\text{world}}
# \end{align*}
# 
# Note that every time the view position changes or the centre of view changes the alignment transformation matrix will need to be recalculated and applied to calculate the camera space vertices. In a computer game this typically happens 30 or 60 times a second as the player is moving the camera. The player traversing a virtual environment feels like they are moving through the world space, what actually happens is the player remains are the origin looking down the $z^\ast$ axis and it is the world space that moves around them. 
# 
# `````{prf:example}
# :class: seealso
# :label: camera-space-example
# 
# The world space from {prf:ref}`world-space-example` is viewed from position $\mathbf{p} = (5, 5, 1.75)$ looking towards the centre of view at $\mathbf{c} = (4, 4, 1.5)$. Calculate the camera space co-ordinates of the virtual environment.
# 
# ````{dropdown} Solution
# Calculate the basis $\{ \mathbf{u}, \mathbf{v}, \mathbf{w}\}$ for the camera space
# \begin{align*}
#     \mathbf{w} &= \frac{\mathbf{p} - \mathbf{c}}{|\mathbf{p} - \mathbf{c}|} = 
#     \frac{1}{\sqrt{1^2 + 1^2 + (0.25)^2}}
#     \begin{pmatrix} 1 \\ 1 \\ 0.25 \end{pmatrix} \approx 
#     \begin{pmatrix} 0.6963 \\ 0.6963 \\ 0.1741 \end{pmatrix}, \\
#     \mathbf{u} &= \frac{\mathbf{k} \times \mathbf{w}}{|\mathbf{k} \times \mathbf{w}|}
#     = \frac{
#         \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \times
#         \begin{pmatrix} 0.6963 \\ 0.6963 \\ 0.1741 \end{pmatrix}
#     }{ 
#         \left| 
#         \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \times
#         \begin{pmatrix} 0.6963 \\ 0.6963 \\ 0.1741 \end{pmatrix}
#         \right| 
#     }
#     \approx \begin{pmatrix} -0.7071 \\ 0.7071 \\ 0 \end{pmatrix} , \\
#     \mathbf{v} &= \mathbf{w} \times \mathbf{u} =
#     \begin{pmatrix} 0.6963 \\ 0.6963 \\ 0.1741 \end{pmatrix} \times
#     \begin{pmatrix} -0.7071 \\ 0.7071 \\ 0 \end{pmatrix} \approx
#     \begin{pmatrix} -0.1231 \\ -0.1231 \\ 0.9847 \end{pmatrix}.
# \end{align*}
# 
# So the change of basis matrix is
# 
# \begin{align*}
#     R_{E \to C} &= 
#     \begin{pmatrix}
#         u_1 & u_2 & u_3 & -\mathbf{p} \cdot \mathbf{u} \\
#         v_1 & v_2 & v_2 & -\mathbf{p} \cdot \mathbf{v} \\
#         w_1 & w_2 & w_3 & -\mathbf{p} \cdot \mathbf{w}\\
#         0 & 0 & 0 & 1
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -0.7071 & 0.7071 & 0 & 0 \\
#         -1.1231 & -0.1231 & 0.9847 & 0 \\
#         0.6963 & 0.6963 & 0.1741 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# We can check whether the change of basis matrix is correct by multiplying it by the homogeneous co-ordinates for $\mathbf{p} - \mathbf{c}$ and check that the $x$ and $y$ co-ordinates are zero and the $z$ co-ordinate is positive. 
# 
# \begin{align*}
#     R_{E \to C} \cdot (\mathbf{p} - \mathbf{c}) &=
#     \begin{pmatrix}
#         -0.7071 & 0.7071 & 0 & 0 \\
#         -1.1231 & -0.1231 & 0.9847 & 0 \\
#         0.6963 & 0.6963 & 0.1741 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix} 1 \\ 1 \\ 0.25 \\ 1 \end{pmatrix} \\ 
#     &=
#     \begin{pmatrix} 0 \\ 0 \\ 1.4361 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so the change of basis matrix is correct. The fourth column of the alignment matrix requires the calculation of the following dot products
# 
# \begin{align*}
#     -\mathbf{p} \cdot \mathbf{u} &= 
#     -\begin{pmatrix} 5 \\ 5 \\ 1.75 \end{pmatrix} \cdot
#     \begin{pmatrix} -0.7071 \\ 0.7071 \\ 0 \end{pmatrix} = 0, \\
#     -\mathbf{p} \cdot \mathbf{v} &= 
#     -\begin{pmatrix} 5 \\ 5 \\ 1.75 \end{pmatrix} \cdot
#     \begin{pmatrix} -0.1231 \\ -0.1231 \\ 0.9847 \end{pmatrix} = -0.4924, \\
#     -\mathbf{p} \cdot \mathbf{w} &= 
#     -\begin{pmatrix} 5 \\ 5 \\ 1.75 \end{pmatrix} \cdot
#     \begin{pmatrix} 0.6963 \\ 0.6963 \\ 0.1741 \end{pmatrix} = -7.2677, \\
# \end{align*}
# 
# therefore the alignment matrix is
# 
# \begin{align*}
#     A &= 
#     \begin{pmatrix}
#         u_1 & u_2 & u_3 & -\mathbf{p} \cdot \mathbf{u} \\
#         v_1 & v_2 & v_2 & -\mathbf{p} \cdot \mathbf{v} \\
#         w_1 & w_2 & w_3 & -\mathbf{p} \cdot \mathbf{w}\\
#         0 & 0 & 0 & 1
#     \end{pmatrix} \\
#     &=
#     \begin{pmatrix}
#         -0.7071 & 0.7071 & 0 & 0 \\
#         -1.1231 & -0.1231 & 0.9847 & -0.4924 \\
#         0.6963 & 0.6963 & 0.1741 & -7.2677 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# Applying the alignment transformation to the world space co-ordinates to calculate the camera space co-ordinates
# 
# \begin{align*}
#     V_{\text{camera}} &= A \cdot V_{\text{world}} \\
#     &= 
#     \begin{pmatrix}
#         -0.7071 & 0.7071 & 0 & 0 \\
#         -1.1231 & -0.1231 & 0.9847 & -0.4924 \\
#         0.6963 & 0.6963 & 0.1741 & -7.2677 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         2 & 2 & 4 & 4 & \cdots \\
#         4 & 3 & 3 & 4 & \cdots \\
#         0 & 0 & 0 & 0 & \cdots \\
#         1 & 1 & 1 & 1 & \cdots
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         1.4142 &   0.7071 &  -0.7071 &        0 & \cdots \\
#         -1.2309 &  -1.1078 &  -1.3540 &  -1.4771 & \cdots \\
#         -3.0899 &  -3.7862 &  -2.3936 &  -1.6973 & \cdots \\
#         1.0000 &   1.0000 &   1.0000 &   1.0000 & \cdots 
#     \end{pmatrix}.
# \end{align*}
# 
# ````
# `````
# 
# ## MATLAB code
# 
# The MATLAB code below calculates the camera space co-ordinates for the virtual world from {prf:ref}`world-space-example` and the viewing parameters from {prf:ref}`camera-space-example` where it is assumed that the world space homogeneous co-ordinates are contained in `Vworld`. Note that the camera space is viewed looking down the $z$ axis using the `view(0,90)` command.
# 
# ```matlab
# % Define camera position and centre of view
# p = [5, 5, 1.75];
# c = [4, 4, 1.5];
# k = [0, 0, 1];
# 
# % Calculate basis vectors
# w = (p - c) / norm(p - c);
# u = cross(k, w) / norm(cross(k, w));
# v = cross(w, u);
# 
# % Calculate change of basis matrix
# A = [ u, -dot(p, u) ; 
#       v, -dot(p, v) ;
#       w, -dot(p, w) ;
#       0, 0, 0, 1 ];
# 
# % Align world space to the camera
# Vcamera = A * Vworld;
# 
# % Plot world space
# patch('Vertices', Vcamera(1:3,:)', 'Faces', F, FaceColor='w', FaceAlpha=0.75, LineWidth=2)
# xlabel('$x$', 'Interpreter', 'latex', 'FontSize', 18)
# ylabel('$y$', 'Interpreter', 'latex', 'FontSize', 18)
# zlabel('$z$', 'Interpreter', 'latex', 'FontSize', 18)
# view(0,90)  % align the plot so that we are looking down the z axis
# axis([-4, 4, -3, 3, -8, 0])
# grid on
# box on
# ```
# 
# ```{figure} /images/camera_space_example.svg
# 
# The camera space from {prf:ref}`camera-space-example`.
# ```
