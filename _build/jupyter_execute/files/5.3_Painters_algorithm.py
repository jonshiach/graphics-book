#!/usr/bin/env python
# coding: utf-8

# # Painter's algorithm
# 
# ```{figure} /images/backface_culling_example_2.png
# :width: 500px
# ```
# 
# ```{figure} https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Painter%27s_algorithm.svg/600px-Painter%27s_algorithm.svg.png
# :name: painters-algorithm-figure-1
# 
# The steps an oil painter uses to paint a scene {cite:p}`painters:2011`
# ```
# 
# ## MATLAB code
# 
# The MATLAB function `painters(V, F, p)` takes inputs of the vertex and face matrix of a screen space `V` and `F` as well as the position of the viewer and returns a face matrix with the faces listed in ascending order by the $z$ distance from the nearest vertex to the viewer. 
# 
# ```matlab
# function Fpainter = painters(V, F, p)
# 
# z = -1e6 * ones(size(F, 1), 1);
# for i = 1 : size(F, 1)
#     for j = 1 : size(F, 2)
#         z(i) = max(z(i), norm(V(1:3,F(i,j)) - p));
#     end
# end
# 
# [~, idx] = sort(z);
# Fpainter = F(idx, :);
# 
# end
# ```
# 
# The affect of the painters algorithm is shown in {numref}`painters-algorithm-example-figure`. 
# 
# ```{figure} /images/painters_example.png
# :width: 500px
# :name: painters-algorithm-example-figure
# 
# The polygons in the screen space are rendered in ascending order of their $z$ distance
# ```
# 
# 
