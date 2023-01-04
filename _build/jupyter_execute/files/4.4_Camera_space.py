#!/usr/bin/env python
# coding: utf-8

# # Camera space
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
# Next we need to transform from the $(x,y,z)$ axes to the $(x^\ast, y^\ast, z^\ast)$ axes. Let $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ be a [basis](basis-section) for the new axes where $\mathbf{u}=(u_1,u_2,u_3)$, $\mathbf{v} = (v_1, v_2, v_3)$ and $\mathbf{w} = (w_1, w_2, w_3)$ are unit vectors pointing in the $x^\ast$, $y^\ast$ and $z^\ast$ directions respectively. The $\mathbf{w}$ vector is calculated using
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
# Note that the order of the vectors in the cross products when calculating $\mathbf{u}$ and $\mathbf{v}$ are important as the cross product is not commutative. The [change of basis matrix](change-of-basis-section) for going from the standard basis $E = \{\mathbf{i}, \mathbf{j}, \mathbf{k}\}$ to the new basis $V = \{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ is
# 
# \begin{align*}
# 	R_{E \to V} =
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
# 	A &= T(-\mathbf{p}) \cdot R_{E \to V} = 
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
# 
# The world space from {prf:ref}`world-space-example` is viewed from position $\mathbf{p} = (6, 5, 0.5)$ looking towards the centre of view at $\mathbf{c} = (2, 2, 1)$. Calculate the camera space co-ordinates of the virtual environment.
# 
# ````{dropdown} Solution
# Calculate the basis $\{ \mathbf{u}, \mathbf{v}, \mathbf{w}\}$ for the camera space
# \begin{align*}
#     \mathbf{w} &= \frac{\mathbf{p} - \mathbf{c}}{|\mathbf{p} - \mathbf{c}|} 
#     = \frac{(4, 3, -0.5)}{\sqrt{4^2 + 3^2 + (-0.5)^2}} = (0.7960, 0.5970, -0.0995), \\
#     \mathbf{u} &= \frac{\mathbf{k} \times \mathbf{w}}{|\mathbf{k} \times \mathbf{w}|}
#     = \frac{ \det
#     \begin{pmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         0 & 0 & 1 \\
#         0.7960 & 0.5970 & -0.0995
#     \end{pmatrix}
#     }{
#     \left| \det
#     \begin{pmatrix} 
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         0 & 0 & 1 \\
#         0.7960 & 0.5970 & -0.0995
#     \end{pmatrix}
#     \right|
#     }
#     = (-0.6, 0.8, 0), \\
#     \mathbf{v} &= \mathbf{w} \times \mathbf{u} = \det
#     \begin{pmatrix}
#         \mathbf{i} & \mathbf{j} & \mathbf{k} \\
#         0.7960 & 0.5970 & -0.0995 \\
#         -0.6 & 0.8 & 0
#     \end{pmatrix}
#     = (0.0796, 0.0597, 0.9950).
# \end{align*}
# So the change of basis matrix is
# \begin{align*}
#     R = \begin{pmatrix}
#         -0.6 & 0.8 & 0 & 0 \\
#         0.0796 & 0.0597 & 0.9950 & 0 \\
#         0.7960 & 0.5970 & -0.0995 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# We can check that $R$ is correct by multiplying it by the homogeneous form of $\mathbf{p} - \mathbf{c}$ to see if it points along the positive $z^\ast$ direction
# \begin{align*}
#     R \cdot (\mathbf{p} - \mathbf{c}) = 
#     \begin{pmatrix}
#         -0.6 & 0.8 & 0 & 0 \\
#         0.0796 & 0.0597 & 0.9950 & 0 \\
#         0.7960 & 0.5970 & -0.0995 & 0 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         4 \\ 3 \\ -0.5 \\ 1
#     \end{pmatrix} =
#     \begin{pmatrix}
#         0 \\ 0 \\ 5.0249 \\ 1
#     \end{pmatrix}.
# \end{align*}
# Since the $x$ and $y$ values are 0 and the $z$ value is positive then $R$ is correct. The alignment transformation matrix is 
# \begin{align*}
#     A = \begin{pmatrix}
#         u_1 & u_2 & u_3 & -\mathbf{p} \cdot \mathbf{u} \\
#         v_1 & v_2 & v_2 & -\mathbf{p} \cdot \mathbf{v} \\
#         w_1 & w_2 & w_3 & -\mathbf{p} \cdot \mathbf{w}\\
#         0 & 0 & 0 & 1
#     \end{pmatrix} =
#     \begin{pmatrix}
#         -0.6000 & 0.8000 & 0.0000 & -0.4000 \\
#         0.0796 & 0.0597 & 0.9950 & -1.2736 \\
#         0.7960 & 0.5970 & -0.0995 & -7.7115 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}.
# \end{align*}
# Applying the alignment transformation to the world space co-ordinates
# \begin{align*}
#     V_{\text{camera}} &= A \cdot V_{\text{world}}
#     = \begin{pmatrix}
#         -0.6000 & 0.8000 & 0.0000 & -0.4000 \\
#         0.0796 & 0.0597 & 0.9950 & -1.2736 \\
#         0.7960 & 0.5970 & -0.0995 & -7.7115 \\
#         0 & 0 & 0 & 1
#     \end{pmatrix}
#     \begin{pmatrix}
#         2 & 2 & 4 & 4 & \cdots \\
#         4 & 3 & 3 & 4 & \cdots \\
#         0 & 0 & 0 & 0 & \cdots \\
#         1 & 1 & 1 & 1 & \cdots 
#     \end{pmatrix} \\
#     &= \begin{pmatrix}
#         1.6000 & 0.8000 & -0.4000 & 0.4000 & \cdots \\
#         -0.8745 & -0.9353 & -0.7761 & -0.7164 & \cdots \\
#         -3.7314 & -4.3284 & -2.7364 & -2.1393 & \cdots \\
#         1 & 1 & 1 & 1 & \cdots
#     \end{pmatrix}.
# \end{align*}
# 
# ````
# `````
# 
