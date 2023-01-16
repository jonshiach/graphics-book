#!/usr/bin/env python
# coding: utf-8

# # Virtual environments
# 
# A virtual environment is a computer generated world which which is viewed from a point within the environment. Virtual environments are usually three dimensional and used primarily in computer games, movies and television and virtual reality simulations. In this chapter we will look at home virtual environments are defined and the mathematical operations used to view the virtual environment on a two-dimensional display.
# 
# ```{figure} https://www.gamespot.com/a/uploads/scale_landscape/1581/15811374/3686824-last%20of%20us%20seattle%20day%201.jpg
# :width: 400px
# 
# A screen shot of the Seattle environment from *The Last of Us Part II* {cite:p}`naughtydog:2020`.
# ```
# 
# (viewing-pipeline-section)=
# ## The viewing pipeline
# 
# The steps required to construct a virtual environment and display it so it can be viewed by a computer user are summarised in a flow diagram known as **the viewing pipeline** which is shown in {numref}`viewing-pipeline-figure`. 
# 
# ```{figure} ../images/viewing_pipeline.svg
# :name: viewing-pipeline-figure
# :width: 400px
# 
# The viewing pipeline
# ```
# 
# The steps are as follows
# 
# - [**Object space**](object-space-section): Primitive objects that are used to build your virtual environment are defined within their own space such that the origin passes through the centre of the object (or sometimes the centre of the bases of the object). For example, a virtual environment that describes a street scene may have objects for buildings, cars, bus stops, street lights etc. 
# 	
# - [**World space**](world-space-section): The virtual environment is constructed by copying the objects into the world space and applying scaling, rotation and translation transformations. 
# 	
# - [**Camera space**](camera-space-section): To view the virtual environment we place a virtual camera in the world space and use translation and rotation transformations so that the position of the camera is at the origin looking along the $z$ axis in the negative direction. 
# 	
# - [**Screen space**](screen-space-section): The camera space is projected onto a two-dimensional projection plane using perspective projection so that the further objects are from the camera the smaller they appear giving the illusion of depth. 
# 	
# - [**Clipped screen space**](clipping-and-hsd-section): Any objects in the screen space that are outside of the region that visible to the camera are removed and objects that lie partially outside are clipped to the edges. In addition, the surfaces that should not be visible to the viewer are removed so to give the appearance of solid surfaces. 
# 	
# - [**Raster**](rasterisation-section): The colours of the individual pixels on a display screen are determined from the information obtained about the virtual environment up to this point and any lighting conditions used. This information is stored in a **raster array** where each element corresponds to a pixel on the display.
# 	
# - **Display**: The raster array is sent to the display hardware. 
# 
# If the position and/or direction of the virtual camera used to calculate the camera space changes, e.g., through the actions of a player or a computer game, the steps from the camera space to the display are repeated. This will typically be 30 or 60 times per second which highlights the computational demands placed on computer hardware and the need for all calculations to be as efficient as possible. 
