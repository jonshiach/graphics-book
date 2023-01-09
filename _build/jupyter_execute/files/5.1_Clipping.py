#!/usr/bin/env python
# coding: utf-8

# (clipping-section)=
# # Clipping
# 
# ```{figure} /images/viewing_pipeline_clipped_screen_space.svg
# :figclass: margin
# ```
# 
# Consider the plot of the screen space from {prf:ref}`screen-space-example` where some of house object closest to the camera lies partially outside of the unit cube representation of the [viewing frustum](viewing-frustum-section). The region inside of this unit cube contains the space that is visible to the viewer and is known as the **visible region**. Any objects that are outside of the visible region needs to be ignored from this point onwards in the viewing pipeline and any objects that lie partially outside need to be **clipped** to the edges of the visible region.
# 
# ```{figure} /images/clipping.png
# :width: 400px
# :name: clipping-figure
# 
# Some objects are outside of the viewing region.
# ```
# 
# ## The Cyrus-Beck algorithm
# 
# The Cyrus-Beck aglorithm {cite:p}`cyrus:1978` calculates the intersection point between a line and a polygon. Consider the diagram in ?? which shows the line joining two points $\mathbf{a} = (a_x, a_y, a_z)$ and $\mathbf{b} = (b_x, b_y, b_z)$ that passess through the plane defined by the [normal vector](normal-vector-section) $\mathbf{n}$ and point $\mathbf{p}$. Clipping of the line $\mathbf{a} \to \mathbf{b}$ to the plane requires the calculation of the point where the line intersects with the plane, $\mathbf{c}$.
# 
# To calculate the intersection point $\mathbf{c}$ we use the vector formula for calculating the shortest distance between a point and a plane, equation {eq}`point-plane-distance-equation`
# 
# ```{math}
# :label: cyrus-beck-d-equation
# 
# d = (\mathbf{q} - \mathbf{p}) \cdot \frac{\mathbf{n}}{|\mathbf{n}|}.
# ```
# 
# The vector equation of the line $\mathbf{a} \to \mathbf{b}$ is
# 
# ```{math}
# :label: cyrus-beck-q-equation
# 
# \mathbf{q} = \mathbf{a} + t(\mathbf{b} - \mathbf{a}),
# ```
# 
# and substituting into equation {eq}`cyrus-beck-d-equation`
# 
# \begin{align*}
#     d &= (\mathbf{a} + t(\mathbf{b} - \mathbf{a}) - \mathbf{p}) \cdot \frac{\mathbf{n}}{|\mathbf{n}|}.
# \end{align*}
# 
# The intersection point $\mathbf{c}$ is where the distance to the plane is zero so setting $d=0$ and rearranging to make $t$ the subject gives
# 
# \begin{align*}
#      0 &= (\mathbf{a} + t(\mathbf{b} - \mathbf{a}) - \mathbf{p}) \cdot \frac{\mathbf{n}}{|\mathbf{n}|}\\
#      &= (\mathbf{a} - \mathbf{p}) \cdot \mathbf{n} + t(\mathbf{b} - \mathbf{a}) \cdot \mathbf{n} \\
#      t(\mathbf{a} - \mathbf{b}) \cdot \mathbf{n} &= (\mathbf{a} - \mathbf{p}) \cdot \mathbf{n} \\
#      t &= \frac{(\mathbf{a} - \mathbf{p}) \cdot \mathbf{n}}{(\mathbf{a} - \mathbf{b}) \cdot \mathbf{n}}
# \end{align*}
# 
# This expression for $t$ can be substituted into equation {eq}`cyrus-beck-q-equation` to give $\mathbf{c}$. 
# 
# 
# ## Cohen-Sutherland clipping algorithm
# 
# Each of the six faces that form the visible region are defined by defined by a normal vector $\mathbf{n}$ and the position $\mathbf{p}$ one of the vertices. The normal vectors for the edges of the screen space are assumed to point towards the interior of the screen space
# 
# \begin{align*}
#     \mathbf{n}_{\text{bottom}} &= \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, &
#     \mathbf{n}_{\text{front}} &= \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}, &
#     \mathbf{n}_{\text{right}} &= \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}, \\
#     \mathbf{n}_{\text{back}} &= \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, &
#     \mathbf{n}_{\text{left}} &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, &
#     \mathbf{n}_{\text{top}} &= \begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix},
# \end{align*}
# 
# where the edges labelled bottom, front, right, back, left and top are from the point of view of the viewer looking down the $z$ axis. The position vector $\mathbf{p}$ for the edges of the screen space can be any point on the plane so we can use
# 
# \begin{align*}
#     \mathbf{p}_{\text{bottom}} &= \begin{pmatrix} 0 \\ -1 \\ 0 \end{pmatrix}, &
#     \mathbf{p}_{\text{front}} &= \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}, &
#     \mathbf{p}_{\text{right}} &= \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \\
#     \mathbf{p}_{\text{back}} &= \begin{pmatrix} 0 \\ 0 \\ -1 \end{pmatrix}, &
#     \mathbf{p}_{\text{left}} &= \begin{pmatrix} -1 \\ 0 \\ 0 \end{pmatrix}, &
#     \mathbf{p}_{\text{top}} &= \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},
# \end{align*}
