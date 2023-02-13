#!/usr/bin/env python
# coding: utf-8

# (object-space-section)=
# # Object space
# 
# ```{figure} /images/viewing_pipeline_object_space.svg
# :figclass: margin
# ```
# 
# Each object in a virtual world is defined in its own space where the centre of mass of the object is at the origin so that scaling, translation and rotation operations can be easily applied. 
# 
# `````{grid}
# 
# ````{grid-item}
# ```{figure} /images/house_object.svg
# :name: house-object-figure
# 
# House object
# ```
# ````
# 
# ````{grid-item}
# ```{figure} /images/tower_object.svg
# :name: tower-object-figure
# 
# Tower object
# ```
# ````
# 
# `````
# 
# A three-dimensional object is constructed using polygons for the **faces** of the object where each face is defined by its **vertices**. Since multiple faces of on object can share the same vertex we use one array to list the vertex co-ordinates and another array to list the vertices that defines each face. 
# 
# ````{figure} /images/cube_object.svg
# :name: cube-vertices-object
# :width: 300px
# 
# Vertex labeling for a unit cube object.
# ````
# 
# Consider the diagram in {numref}`cube-vertices-object` that shows a cube centred at the origin with side lengths of 2 which are parallel to the co-ordinates axes (called a *unit cube*). The eight vertices have been labeled $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_8$. The homogeneous co-ordinates of the vertices are
# 
# \begin{align*}
# 	\mathbf{v}_1 &= \begin{pmatrix} -1 \\ -1 \\ -1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_2 &= \begin{pmatrix} 1 \\ -1 \\ -1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_3 &= \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_4 &= \begin{pmatrix} -1 \\ 1 \\ -1 \\ 1 \end{pmatrix}, \\
# 	\mathbf{v}_5 &= \begin{pmatrix} -1 \\ -1 \\ 1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_6 &= \begin{pmatrix} 1 \\ -1 \\ 1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_7 &= \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix}, &
# 	\mathbf{v}_8 &= \begin{pmatrix} -1 \\ 1 \\ 1 \\ 1 \end{pmatrix}.
# \end{align*}
# 
# We can form a single matrix containing these vertices known as the **vertex matrix**
# 
# \begin{align*}
# 	V &= \begin{pmatrix}
# 		\uparrow & \uparrow & \uparrow & \uparrow & \uparrow & \uparrow & \uparrow & \uparrow\\
# 		\mathbf{v}_1 & \mathbf{v}_2 & \mathbf{v}_3 & \mathbf{v}_4 & \mathbf{v}_5 & \mathbf{v}_6 & \mathbf{v}_7 & \mathbf{v}_8 \\
# 		\downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow & \downarrow
# 	\end{pmatrix} \\
#     &= 
# 	\begin{pmatrix}
# 		-1 & 1 & 1 & -1 & -1 & 1 & 1 & -1 \\
# 		-1 & -1 & 1 & 1 & -1 & -1 & 1 & 1 \\
# 		-1 & -1 & -1 & -1 & 1 & 1 & 1 & 1 \\
# 		1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
# 	\end{pmatrix}.
# \end{align*}
# 
# The faces of the object are defined by a **face matrix** that links to the vertex matrix. The face matrix is an $m \times n$ matrix where $m$ is the number of faces of the object and $n$ is the number of sides for each face, so for the cube object the face matrix will be $6 \times 4$. The rows of the face matrix contain the column number of the vertex matrix corresponding to vertices of that face. For example, consider the faces of the cube object shown below. The face that represents the base has vertices $\mathbf{v}_1$, $\mathbf{v}_2$, $\mathbf{v}_3$ and $\mathbf{v}_4$ so the row of the face matrix will contain the numbers 1, 2, 3 and 4.
# 
# (cube-faces)=
# `````{grid}
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_base.svg
# ```
# <p align=center>base face</p>
# ````
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_front.svg
# ```
# <p align=center>front face</p>
# ````
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_right.svg
# ```
# <p align=center>right face</p>
# ````
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_back.svg
# ```
# <p align=center>back face</p>
# ````
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_left.svg
# ```
# <p align=center>left face</p>
# ````
# 
# ````{grid-item}
# :columns: 4
# ```{figure} /images/cube_top.svg
# ```
# <p align=center>top face</p>
# ````
# 
# `````
# 
# We also need to consider the order that the vertices are listed for each face. Objects are defined so that the {prf:ref}`normal vectors <normal-vector-definition>` for each face is pointing away from the centre of the object. We [have seen](normal-vector-section) that the normal vector to a plane that passes through the 3 points with position vectors $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ is calculated using 
# 
# \begin{align*}
# 	\mathbf{n} = (\mathbf{v}_2 - \mathbf{v}_1) \times (\mathbf{v}_3 - \mathbf{v}_2).
# \end{align*}
# 
# If $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ are ordered anti-clockwise when viewed from one side of the plane then the above equation will result in a normal vector pointing towards the viewer ({numref}`anticlockwise-vertices-figure`). Alternatively is the vertices are ordered clockwise when viewed from the side fo the plane then this will result in a normal vector pointing away from the viewer ({numref}`clockwise-vertices-figure`). 
# 
# `````{grid}
# 
# ````{grid-item}
# ```{figure} /images/normal_vertex_order_1.svg
# :name: anticlockwise-vertices-figure
# 
# Anti-clockwise ordering
# ```
# ````
# 
# ````{grid-item}
# ```{figure} /images/normal_vertex_order_2.svg
# :name: clockwise-vertices-figure
# 
# Clockwise ordering
# ```
# ````
# 
# `````
# 
# With this in mind the face matrix for the {ref}`cube object <cube-vertices-object>` is 
# 
# \begin{align*}
# 	F = 
#     \begin{pmatrix}
#         1 & 4 & 3 & 2 \\
#         1 & 2 & 6 & 5 \\
#         2 & 3 & 7 & 6 \\
#         3 & 4 & 8 & 7 \\
#         4 & 1 & 5 & 8 \\
#         5 & 6 & 7 & 8
#     \end{pmatrix}
#     \quad 
#     \begin{array}{l}
#         \textsf{(base)} \\
#         \textsf{(front)} \\
#         \textsf{(right)} \\
#         \textsf{(back)} \\
#         \textsf{(left)} \\
#         \textsf{(top)}
#     \end{array}
# \end{align*}
# Note that it does not matter which order the vertices are listing as columns in the world space vertex matrix or the faces listed in rows of the face matrix, as long as the face matrix correctly links to the vertex matrix.
# 
# 
# `````{prf:example}
# :class: seealso
# :label: object-space-example
# 
# A simple three-dimensional object that resembles a house is shown below (modelled on the house piece from the *Monopoly* board game)
# 
# ```{figure} /images/house_object_example.svg
# :width: 300px
# ```
# 
# The house has length of 2, width of 1, wall height 1 and roof height 2 and defined so that the center of the base is at the origin. Define the vertex and face matrices for this house object.
# 
# ````{dropdown} Solution
# 
# The homogeneous co-ordinates of the vertices $\mathbf{v}_1$ to $\mathbf{v}_{10}$ are
# 
# \begin{align*}
#     \mathbf{v}_1 &= \begin{pmatrix} -0.5 \\ -1 \\ 0 \\ 1 \end{pmatrix} &
#     \mathbf{v}_2 &= \begin{pmatrix} 0.5 \\ -1 \\ 0 \\ 1 \end{pmatrix} &
#     \mathbf{v}_3 &= \begin{pmatrix} 0.5 \\ 1 \\ 0 \\ 1 \end{pmatrix} \\
#     \mathbf{v}_4 &= \begin{pmatrix} -0.5 \\ 1 \\ 0 \\ 1 \end{pmatrix} &
#     \mathbf{v}_5 &= \begin{pmatrix} -0.5 \\ -1 \\ 1 \\ 1 \end{pmatrix} &
#     \mathbf{v}_6 &= \begin{pmatrix} 0.5 \\ -1 \\ 1 \\ 1 \end{pmatrix} \\
#     \mathbf{v}_7 &= \begin{pmatrix} 0.5 \\ 1 \\ 1 \\ 1 \end{pmatrix} &
#     \mathbf{v}_8 &= \begin{pmatrix} -0.5 \\ 1 \\ 1 \\ 1 \end{pmatrix} &
#     \mathbf{v}_9 &= \begin{pmatrix} 0 \\ -1 \\ 2 \\ 1 \end{pmatrix} \\
#     \mathbf{v}_{10} &= \begin{pmatrix} 0 \\ 1 \\ 2 \\ 1 \end{pmatrix},
# \end{align*}
# 
# so the vertex matrix is
# 
# \begin{align*}
#     V &=
#     \begin{pmatrix}
#         -0.5 & 0.5 & 0.5 & -0.5 & -0.5 & 0.5 & 0.5 & -0.5 & 0 & 0 \\
#         -1 & -1 & 1 & 1 & -1 & -1 & 1 & 1 & -1 & 1 \\
#         0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 & 2 \\
#         1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
#     \end{pmatrix}.
# \end{align*}
# 
# The house object has 7 faces: a base, 2 end walls, 2 side walls and 2 roofs. The base, side walls and roofs are 4-sided faces whereas the end walls are 5-sided faces. The face matrix for the house object that ensures the normal vectors are point away from the centre of the object is (vertices are listed in an anti-clockwise direction when looking towards the centre). Note that the last vertex of the 4-sided faces are repeated to ensure that each row of the face matrix has 5 elements.
#     
# \begin{align*}
#     F &=
#     \begin{pmatrix}
#         1 & 4 & 3 & 2 & 2 \\
#         1 & 2 & 6 & 9 & 5 \\
#         2 & 3 & 7 & 6 & 6 \\
#         3 & 4 & 8 & 10 & 7 \\
#         1 & 5 & 8 & 4 & 4 \\
#         6 & 7 & 10 & 9 & 9 \\
#         5 & 9 & 10 & 8 & 8
#     \end{pmatrix}
#     \quad 
#     \begin{array}{l}
#         \textsf{(base)} \\
#         \textsf{(front wall)} \\
#         \textsf{(right wall)} \\
#         \textsf{(back wall)} \\
#         \textsf{(left wall)} \\
#         \textsf{(right roof)} \\
#         \textsf{(left roof)}
#     \end{array}
# \end{align*}
#         
# ````
# 
# `````
# 
# ## MATLAB code
# 
# The following MATLAB code in defines the vertex and face matrices for the house object from {prf:ref}`object-space-example` and plots the object space. The vertex and face matrices are defined in `V` and `F` and the `patch()` command is then used to plot the object. Note that we only use the first three rows of the `V` array which has been transposed because MATLAB assumes the co-ordinates are listed in rows. The `FaceAlpha` is set to 0.75 so that the faces of the object are semi-transparent.
# 
# ```matlab
# # Define object
# V = [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0, 0 ;
#      -1,  -1,   1,    1,   -1,  -1,   1,    1,  -1, 1 ;
#       0,   0,   0,    0,    1,   1,   1,    1,   2, 2 ;
#       1,   1,   1,    1,    1,   1,   1,    1,   1, 1];
# 
# F = [4, 3, 2, 1, 1 ;    # base
#      1, 2, 6, 9, 5 ;    # front wall
#      2, 3, 7, 6, 6 ;    # right wall
#      3, 4, 8, 10, 7 ;   # back wall
#      1, 5, 8, 4, 4 ;    # left wall
#      6, 7, 10, 9, 9 ;   # right roof
#      5, 9, 10, 8, 8 ];  # left roof
# 
# # Plot object
# patch('Vertices', V(1:3,:)', 'Faces', F, FaceColor='white', FaceAlpha=0.75, LineWidth=2)
# xlabel('$x$', 'Interpreter', 'latex', 'FontSize', 18)
# ylabel('$y$', 'Interpreter', 'latex', 'FontSize', 18)
# zlabel('$z$', 'Interpreter', 'latex', 'FontSize', 18)
# view(45, 30)
# axis equal
# axis([-2, 2, -2, 2, 0, 2])
# grid on 
# ```
# 
# ```{figure} /images/object_space_example.png
# :width: 400px
# :name: object-space-example-figure
# 
# The object space from {prf:ref}`object-space-example`.
# 
# ```
