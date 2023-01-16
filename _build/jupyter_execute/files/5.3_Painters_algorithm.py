#!/usr/bin/env python
# coding: utf-8

# # Painter's algorithm
# 
# We saw in the previous section that applying [backface culling](backface-culling-section) produces the view of the screen space shown in {numref}`backface-culling-example-figure-2`.
# 
# ```{figure} /images/backface_culling_example.png
# :width: 400px
# :name: backface-culling-example-figure-2
# 
# The screen space from {prf:ref}`screen-space-example` after [backface culling](backface-culling-section) has been applied.
# ```
# 
#  Here the faces of the church object that should appear in the background partially obscure the faces of the house object in the foreground. To correct this we can apply **painter's algorithm** which is named after the order of which an oil painter will paint a scene. This is to start with the background elements, followed by the middle ground elements and finishing with the foreground elements ({numref}`painters-algorithm-figure`). 
# 
# ```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Painter%27s_algorithm.svg/600px-Painter%27s_algorithm.svg.png
# :name: painters-algorithm-figure
# 
# The steps an oil painter uses to paint a scene {cite:p}`painters:2011`
# ```
# 
# The painter's algorithm is simple. We order the polygons that are front facing in ascending order by the vertex with the largest $z$ co-ordinate. This means that when we render the polygons in order, those polygons that are closest to the viewer are rendered last therefore obscuring any polygons that are further away from the viewer.
# 
# ```{prf:algorithm} Painter's algorithm
# :label: painters-algorithm
# 
# **Inputs** A the front facing space polygons defined by a homogeneous vertex matrix $V$, and a face matrix $F$. 
# 
# **Outputs** A face matrix containing the screen space polygons listed in descending order by $z$ distance.
# 
# - For each face in $F$
#     - $distance \gets $ the largest $z$ co-ordinate of the vertices in the current face
# - Sort $F$ in ascending order of $distance$
# - Return $F$
# ```
# 
# ## MATLAB code
# 
# The MATLAB function `painters(V, F)` takes inputs of the vertex and face matrix of a screen space `V` and `F` and returns a face matrix with the faces listed in ascending order by the $z$ distance from the nearest vertex to the viewer. 
# 
# ```matlab
# function Fpainter = painters(V, F)
# 
# distance = -1 * ones(size(F, 1), 1);
# for i = 1 : size(F, 1)
#     for j = 1 : size(F, 2)
#         distance(i) = max(distance(i), V(3,F(i,j)));
#     end
# end
# 
# [~, idx] = sort(distance);
# Fpainter = F(idx, :);
# 
# end
# ```
# 
# The affect of the painters algorithm is shown in {numref}`painters-algorithm-example-figure`. 
# 
# ```{figure} /images/painters_example.png
# :width: 400px
# :name: painters-algorithm-example-figure
# 
# The polygons in the screen space are rendered in ascending order of their $z$ distance
# ```
# 
# 
