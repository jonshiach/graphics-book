(3D-worlds-section)=

# 3D Worlds

In the [previous lab](transformations-section) we looked at the transformations can can be applied to the vertex co-ordinates $(x, y, z, 1)$ but all of our examples were using transformations in 2D. In this lab we will take the step into the third spatial dimension and look at 3D worlds.

## 3D models

To demonstrate building a simple 3D world we are going to need a 3D object. One of the simplest 3D objects is a **unit cube** which is a cube centred at (0,0,0) and has side lengths of 2 parallel to the co-ordinate axes ({numref}`unit-cube-figure`) so the co-ordinates of the 8 corners of the cube are combinations of $-1$ and $1$. Since we use triangles as our base shape a cube consists of 12 triangles (6 sides each made out of 2 triangles).

```{figure} ../_images/06_Unit_cube.svg
:width: 500
:name: unit-cube-figure

A unit cube centred at $(0,0,0)$ with side lengths of 2.
```

Open the **Lab06_3D_Worlds.cpp** file in the **Lab06_3D_Worlds** project and you will see that the `vertices`, `uv` and `indices` arrays have been defined for our unit cube.

```cpp
// Define cube object
// Define vertices
const float vertices[] = {
    // front
    -1.0f, -1.0f,  1.0f,    //              + ------ +
     1.0f, -1.0f,  1.0f,    //             /|       /|
     1.0f,  1.0f,  1.0f,    //   y        / |      / |
    -1.0f, -1.0f,  1.0f,    //   |       + ------ +  |
     1.0f,  1.0f,  1.0f,    //   + - x   |  + ----|- +
    -1.0f,  1.0f,  1.0f,    //  /        | /      | /
    // right                // z         |/       |/
     1.0f, -1.0f,  1.0f,    //           + ------ +
     1.0f, -1.0f, -1.0f,
     1.0f,  1.0f, -1.0f,
     1.0f, -1.0f,  1.0f,
     1.0f,  1.0f, -1.0f,
     1.0f,  1.0f,  1.0f,
    // etc.
};

// Define texture coordinates
const float uv[] = {
    // front
    0.0f, 0.0f,     // vertex co-ordinates are the same for each side
    1.0f, 0.0f,     // of the cube so repeat every six vertices
    1.0f, 1.0f,
    0.0f, 0.0f,
    1.0f, 1.0f,
    0.0f, 1.0f,
    // right
    0.0f, 0.0f,
    1.0f, 0.0f,
    1.0f, 1.0f,
    0.0f, 0.0f,
    1.0f, 1.0f,
    0.0f, 1.0f,
    // etc.
};

// Define indices
unsigned int indices[] = {
    // front
    0, 1, 2, 3, 4, 5,
    // right
    6, 7, 8, 9, 10, 11,
    // etc.
};
```

If you compile and run this program you will see that the crate texture fills the window.

```{figure} ../_images/06_3D_worlds.png
:width: 500
:name: cube-figure

A unit cube.
```

---

## Co-ordinate systems

OpenGL uses a co-ordinate system with the $x$ axis pointing horizontally to the right, the $y$ axis pointing vertically upwards and the $z$ axis pointing horizontally towards the viewer. To simplify things when it comes to displaying the 3D world, the axes are limited to a range from $-1$ to $1$ so any object outside of this range will not be shown on the display. These are known as **Normalised Device Co-ordinates (NDC)**.

```{figure} ../_images/06_NDC.svg
:width: 600
:name: NDC-figure

Normalised Device Co-ordinates (NDC)
```

The steps used in the creation of a 3D world and eventually displaying it on screen requires that we transform through several intermediate co-ordinate systems:

- **Model space** - each individual 3D object that will appear in the 3D world is defined in its own space usually with the volume centre of the object at $(0,0,0)$ to make the transformations easier
- **World space** - the 3D world is constructed by transforming the individual 3D objects using translation, rotation and scaling transformations
- **View space** - the world space is transformed so that it is viewed from $(0,0,0)$ looking down the $z$-axis
- **Screen space** - the view space is transformed so that the co-ordinates are expressed using normalised device co-ordinates

```{figure} ../_images/06_mvp.svg
:width: 500

Transformations between the model, world, view and screen spaces.
```

## Model, view and projection matrices

We saw in [Lab 5](transformations-section) that we apply a transformation by multiplying the object co-ordinates by a transformation matrix. Since we are transforming between difference co-ordinate spaces we have 3 main transformation matrices

- the model matrix - a transformation matrix that combines scaling, rotation and translation transformations that is unique for each object in the world space
- the view matrix - a transformation matrix that combines translation and rotation transformations that is applied to every object in the world space
- the projection matrix - a transformation matrix that combines projection and scalingg that is applied to every object in the world space

(model-matrix-section)=

### The Model matrix

In [5. Transformations](transformations-section) we saw that we can combine transformations such as translation, scaling and rotation by multiplying the individual transformation matrices together. Lets compute a model matrix for our cube where it is scaled down by a factor of 0.5 in each co-ordinate direction, rotated about the $y$-axis using the time of the current frame as the rotation angle and translated backwards down the $z$-axis so that its centre is at $(0, 0, -4)$. Add the following code inside the rendering loop before we call the `glDrawArrays()` function.

```cpp
// Calculate the model matrix
rotationAngle += deltaTime * Maths::radians(0.25 * 360.0f);
mat4 translate = Maths::translate(vec3(0.0f, 0.0f, -4.0f));
mat4 scale     = Maths::scale(vec3(0.5f, 0.5f, 0.5f));
mat4 rotate    = Maths::rotate(rotationAngle, vec3(0.0f, 1.0f, 0.0f));
mat4 model     = translate * rotate * scale;
```

Here we have calculated the individual transformation matrices for translation, scaling and rotation and multiply them together to create the model matrix. Note that the `rotationAngle` variable has been declared before and `main()` function and here it is updated so the cube performs one rotation every 4 seconds.

(view-matrix-section)=

### The View matrix

To view the world space we create a virtual camera and place it in the world space. We need to translate the whole of the world space so that the camera is at $(0,0,0)$ and the rotate the world space so that the camera is pointing down the $z$-axis ({numref}`view-space-figure`).

```{figure} ../_images/06_view_space.svg
:width: 350
:name: view-space-figure

The view space.
```

To calculate the world space to view space transformation we require three vectors

- $\vec{eye}$ - the co-ordinates of the camera position
- $\vec{target}$ - the co-ordinates of the target point that the camera is pointing
- $\vec{worldUp}$ - a vector pointing straight up in the world space which allows us to orientate the camera, this is usually $(0,1,0)$

```{figure} ../_images/06_view_space_alignment.svg
:width: 400
:name: view-space-alignment-figure

The vectors used in the transformation to the view space.
```

The $\vec{eye}$ and $\vec{target}$ vectors are either determined by the user through keyboard, mouse or controller inputs or through some predetermined routine. To determine the view space transformation we first translate the camera position to $(0,0,0)$ using the following translation matrix

$$ \begin{align*}
    Translate =
    \begin{pmatrix}
        1 & 0 & 0 & -e_x \\
        0 & 1 & 0 & -e_y \\
        0 & 0 & 1 & -e_z \\
        0 & 0 & 0 & 1
    \end{pmatrix}
\end{align*}, $$

where $\vec{eye} = (e_x, e_y, e_z)$. The next step is to align the world space so that the direction vector is pointing down the $z$-axis. To do this we use vectors $\vec{right}$, $\vec{up}$ and $\vec{front}$ which are unit vectors at right-angles to each other the point in directions relative to the camera ({numref}`view-space-alignment-figure`).

The $\vec{front}$ vector points directly forward of the camera and is calculated using

$$ \vec{front} = \operatorname{normalise}(\vec{target} - \vec{eye}).$$

The $\vec{right}$ vector points to the right of the camera so is at right-angles to both the $\vec{front}$ and $\vec{worldUp}$ vectors. We can use the [cross product](cross-product-section) between the two vectors to calculate this (note that the order of the vectors is important).

$$ \vec{right} = \operatorname{normalise}(\vec{front} \times \vec{worldUp}) .$$

The $\vec{up}$ vector points in the up direction of the camera and is at right-angles to the $\vec{front}$ and $\vec{right}$ vectors we have already calculated. So this can be calculated using another cross product (we don't need to normalise this this both $\vec{right}$ and $\vec{front}$ are unit vectors).

$$ \vec{up} = \vec{right} \times \vec{front}.$$

Once these vectors have been calculated the transformation matrix to rotate the $\vec{front}$ vector so that it points down the $z$-axis is

$$ Rotate = \begin{pmatrix}
    r_x  & r_y  & r_z & 0 \\
    u_x  & u_y  & u_z & 0 \\
    -f_x & -f_y & -f_z & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}.$$

where $\vec{right} = (r_x, r_y, r_z)$, $\vec{up} = (u_x, u_y, u_z)$ and $\vec{front} = (f_x, f_y, f_z)$. The translation matrix and rotation matrix are multiplied together to form the view matrix which transforms the world space co-ordinates to the view space.

$$ \begin{align*}
    \view &= Rotate \cdot Translate \\
    &=
    \begin{pmatrix}
        r_x  & r_y  & r_z & 0 \\
        u_x  & u_y  & u_z & 0 \\
        -f_x & -f_y & -f_z & 0 \\
        0 & 0 & 0 & 1
    \end{pmatrix}
    \begin{pmatrix}
        1 & 0 & 0 & -e_x \\
        0 & 1 & 0 & -e_y \\
        0 & 0 & 1 & -e_z \\
        0 & 0 & 0 & 1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
         r_x &  r_y  &  r_z & - e_xr_x - e_yr_y - e_zr_z \\
         u_x &  u_y  &  u_z & - e_xu_x - e_yu_y - e_zu_z \\
        -f_x & -f_y  &  f_z &   e_xf_x + e_yf_y + e_zf_z \\
        0 & 0 & 0 & 1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
         r_x &  r_y  &  r_z & -\vec{eye} \cdot \vec{right} \\
         u_x &  u_y  &  u_z & -\vec{eye} \cdot \vec{up} \\
        -f_x & -f_y  & -f_z &  \vec{eye} \cdot \vec{front} \\
        0 & 0 & 0 & 1
    \end{pmatrix}
\end{align*} $$

Lets move the camera back a bit to look at our cube from the position $(1,1,0)$ looking towards the center of the cube at $(0,0,-4)$. Add the following code after we have calculated the model matrix.

```cpp
// Calculate the view matrix
vec3 eye     = vec3(1.0f, 1.0f,  0.0f);
vec3 target  = vec3(0.0f, 0.0f, -4.0f);
vec3 worldUp = vec3(0.0f, 1.0f,  0.0f);
vec3 front   = (target - eye).normalise();
vec3 right   = front.cross(worldUp).normalise();
vec3 up      = right.cross(front);

mat4 view = mat4(1.0f);
view[0]   =   right.x, view[4] =   right.y, view[8]  =   right.z;
view[1]   =   up.x,    view[5] =   up.y,    view[9]  =   up.z;
view[2]   = - front.x, view[6] = - front.y, view[10] = - front.z;
view[12]  = - eye.dot(right);
view[13]  = - eye.dot(up);
view[14]  =   eye.dot(front);
view[15]  =   1.0f; 
```

Here we have specified the $\vec{eye}$, $\vec{target}$ and $\vec{worldUp}$ vectors and use them to calculate the $\vec{front}$, $\vec{right}$ and $\vec{up}$ camera vectors using methods from our `vec3` class. We then use these to calculate the view matrix.

### The Projection matrix

The next step is to project the view space onto the screen space. Any fragments with co-ordinates outside of the range $-1$ to $1$ are **clipped** and ignored by the shaders. The simplest type of projection is **orthographic projection** where the co-ordinates in the view space are transformed to the screen space by simple translation and scaling transformations.

The region of the view space that will form the screen space is defined by a cuboid bounded by a left, right, bottom, top, near and far clipping planes. Any objects outside of the cuboid are clipped ({numref}`orthographic-projection-figure`).

```{figure} ../_images/06_orthographic_projection.svg
:width: 600
:name: orthographic-projection-figure

Orthographic projection.
```

Here $l$, $r$, $b$, $t$, $n$ and $f$ are the left, right, bottom, top, near and far co-ordinates respectively, The **orthographic projection matrix** is calculated using

$$ \begin{align*}
    Projection_{orth} =
    \begin{pmatrix}
        \dfrac{2}{r - l} & 0 & 0 & -\dfrac{r + l}{r - l} \\
        0 & \dfrac{2}{t - b} & 0 & -\dfrac{t + b}{t - b} \\
        0 & 0 & \dfrac{2}{n - f} &  \dfrac{n + f}{n - f} \\
        0 & 0 & 0 & 1
    \end{pmatrix}
\end{align*}. $$

You don't really need to know how this matrix is derived but if you are interested click on the dropdown link below.

```{dropdown} Derivation of the orthographic projection matrix

To derive the orthographic projection we first need to translate the co-ordinates so that the centre of the cuboid that represents the clipping volume to $(0,0,0)$. The centre co-ordinates are calculated using the average of the edge co-ordinates, e.g., for the $x$ co-ordinate this would be $\dfrac{r + l}{2}$, so the translation matrix is

$$ \begin{align*}
    Translate = 
    \begin{pmatrix}
        1 & 0 & 0 & -\dfrac{r + l}{2} \\
        0 & 1 & 0 & -\dfrac{t + b}{2} \\
        0 & 0 & 1 &  \dfrac{n + f}{2}  \\
        0 & 0 & 0 & 1
    \end{pmatrix}
\end{align*} $$

The second step is to scale the clipping volume so that the co-ordinates are between $-1$ and $1$. This is done by dividing the distance between the edges of the screen space by the distance between the clipping planes, e.g., for the $x$ co-ordinate this would be $\dfrac{1 - (-1)}{r - l}=\dfrac{2}{r - l}$, so the scaling matrix is

$$ \begin{align*}
    Scale = 
    \begin{pmatrix}
        \dfrac{2}{r - l} & 0 & 0 & 0 \\
        0 & \dfrac{2}{t - b} & 0 & 0 \\
        0 & 0 & \dfrac{2}{n - f} & 0 \\
        0 & 0 & 0 & 1
    \end{pmatrix}.
\end{align*} $$

Combining the translation and scaling matrices gives the orthographic projection matrix

$$ \begin{align*}
    Projection_{orth} &= Scale \cdot Translate \\
    &=
    \begin{pmatrix}
        \dfrac{2}{r - l} & 0 & 0 & -\dfrac{r + l}{r - l} \\
        0 & \dfrac{2}{t - b} & 0 & -\dfrac{t + b}{t - b} \\
        0 & 0 & \dfrac{2}{n - f} &  \dfrac{n + f}{n - f} \\
        0 & 0 & 0 & 1
    \end{pmatrix}
\end{align*} $$
```

Lets calculate the orthographic projection matrix using $l = -2$, $r = 2$, $b = -2$, $t = 2$, $n = 0$, $f = 10$. Add the following code after we have calculated the view matrix.

```cpp
// Calculate orthographic projection matrix
float l, r, b, t, n, f;
l = - 2.0f, r = 2.0f;
b = - 2.0f, t = 2.0f;
n =   0.0f, f = 10.0f;

mat4 projection = mat4(1.0f);
projection[0]  =   2.0f / (r - l);
projection[5]  =   2.0f / (t - b);
projection[10] =   2.0f / (n - f);
projection[12] = - (r + l) / (r - l);
projection[13] = - (t + b) / (t - b);
projection[14] =   (n + f) / (n - f);
```

### The MVP matrix

Now that we have the model, view and projection matrices we need to apply them to our objects. We could do this in our `main()` function but this would mean sending lots of vertex buffers to the GPU and very inefficient. Much better to send a single $4 \times 4$ matrix to the shader and perform the calculations using the GPU since the vertex buffer is already in the GPU memory.

So in our `main()` function we combine the model, view and projection matrices to form a single matrix called the **MVP matrix**.

$$ \mvp = Projection \cdot \view \cdot \model. $$

We need a way to send the MVP matrix to the vertex shader. We do this using a uniform in the same way as we did for the texture locations in [3. Textures](uniforms-section), enter the following code after we have calculated the projection matrix.

```cpp
//Calculate the MVP matrix and send it to the vertex shader
mat4 mvp = projection * view * model;
unsigned int mvpID = glGetUniformLocation(shaderID, "mvp");
glUniformMatrix4fv(mvpID, 1, GL_FALSE, &mvp[0]);
```

Here after calculating the `mvp` matrix we get the location of the uniform and point OpenGL to the first element of the matrix using the <a href="https://registry.khronos.org/OpenGL-Refpages/gl4/html/glUniform.xhtml" target="_blank">`glUniformMatrix4fv()`</a> function.

We also need to update the vertex shader so that is uses the MVP matrix. Edit the **vertexShader.glsl** file in the **Lab06_3D_Worlds** project so that the `gl_Position` vector is calculated by applying the MVP matrix to the vertex position.

```cpp
#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec2 UV;

out vec2 uv;

uniform mat4 mvp;

void main()
{
    // Output vertex position
    gl_Position = mvp * vec4(position, 1.0);
    
    // Output texture co-ordinates
    uv = UV;
}
```

Compile and run the program and you should see the following.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/06_orthogonal_cube_no_depth_test.mp4" type="video/mp4">
</video>
</center>

---

## The depth test

Our rendering of the cube doesn't look quite right. What is happening here is that some parts of the sides of the cube that are further away from where we are viewing it (e.g., the bottom side) have been rendered after the sides that are closer to us ({numref}`depth-test-1-figure`).

```{figure} ../_images/06_depth_test.svg
:width: 300
:name: depth-test-1-figure

Rendering the far triangle after the near triangle.
```

To overcome this issue OpenGL uses a **depth test** when computing the fragment shader. When OpenGL creates a frame buffer it also creates another buffer called a **z buffer** (or **depth buffer**) where the $z$ co-ordinate of each pixel in the frame buffer is stored and initialises all the values to $-1$ (the furthest possible $z$ co-ordinate in the screen space). When the fragment shader is called it checks whether the fragment has a $z$ co-ordinate more than that already stored in the depth buffer and if so it updates the colour of the fragment and stores its $z$ co-ordinate in the depth-buffer as the current nearest fragment (if the fragment has a $z$ co-ordinate less than what is already in the depth buffer the fragment shader does nothing). This means once the fragment shader has been called for all fragments of all objects, the pixels contain colours of the objects closest to the camera.

To enable depth testing we simply add the following function before after the creation of the window.

```cpp
// Enable depth test
glEnable(GL_DEPTH_TEST);
```

We also need to clear the depth buffer at the start of each frame, change `glClear(GL_COLOR_BUFFER_BIT);` to the following.

```cpp
// Clear the window
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```

Make these changes to your code and you should get a much better result.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/06_orthogonal_cube_depth_test.mp4" type="video/mp4">
</video>
</center>

---

## Perspective projection

The problem with using orthographic projection is that is does not give us any clues to how far an object is from the viewer. We would expect that objects further away from the camera would appear smaller whereas objects closer to the camera would appear larger.

Perspective project uses the same near and far clipping planes as orthographic projection but the clipping planes on the sides are not parallel, rather they angle in such that the four planes meet at $(0,0,0)$ ({numref}`perspective-projection-figure`). The clipping volume bounded by the size clipping planes is called the **viewing frustum**. 

```{figure} ../_images/06_perspective_projection.svg
:width: 600
:name: perspective-projection-figure

Perspective projection.
```

The shape of the viewing frustum is determined by four factors:

- $n$ -- the distance from $(0,0,0)$ to the near clipping plane
- $f$ -- the distance from $(0,0,0)$ to the far clipping plane
- $fov$ -- the **field of view** angle between the bottom and top clipping planes (used to determine how much of the view space is visible)
- $aspect$ -- the width-to-height **aspect ratio** of the window

Given these four factors we can calculate the **perspective projection matrix** using

$$ \begin{align*}
    Projection_{pers} =
    \begin{pmatrix}
        \dfrac{n}{r} & 0 & 0 & 0 \\
        0 & \dfrac{n}{t} & 0 & 0 \\
        0 & 0 & -\dfrac{f + n}{f - n} & - \dfrac{2fn}{f - n} \\
        0 & 0 & -1 & 0
    \end{pmatrix},
\end{align*} $$

where $t = n \cdot \tan\left(\dfrac{fov}{2}\right)$ and $r = \textsf{aspect} \cdot t$. You don't really need to know how this is derived but it you are interested click on the dropdown below.

````{dropdown} Derivation of the perspective projection matrix

The mapping of a point in the view space with co-ordinates $(x, y, z)$ onto the near clipping plane to the point $(x', y', -n)$ is shown in {numref}`perspective-mapping-figure`.

```{figure} ../_images/06_perspective_projection_mapping.svg
:width: 500
:name: perspective-mapping-figure

Mapping of the point at $(x,y,z)$ onto the near plane using perspective.
```

The ratio of $x$ to $-z$ distance is the same as the ratio of $x'$ to $n$ distance (and similar for $y'$) so

$$ \begin{align*}
    \dfrac{x}{-z} &= \dfrac{x'}{n} &\implies
    x' &= -\frac{nx}{z}, \\
    \dfrac{y}{-z} &= \dfrac{y'}{n} &\implies
    y' &= -\frac{ny}{z},
\end{align*} $$

So we are mapping $(x, y)$ to $\left( -\dfrac{nx}{z}, -\dfrac{ny}{z} \right)$. As well as the perspective mapping we also need to ensure that the mapped co-ordinates $(x', y', z')$ are between $-1$ and $1$. Consider the mapping of the $x$ co-ordinate

$$ \begin{align*}
    l &\leq x' \leq r \\
    -r &\leq x' \leq r  && \textsf{(since $l= -r$)} \\
    -1 &\leq \frac{x'}{r} \leq 1 && \textsf{(divide by $r$)}
\end{align*} $$

Since $x' = -\dfrac{nx}{z}$ then

$$ \begin{align*}
    -1 &\leq -\frac{nx}{rz}\leq 1
\end{align*} $$

and doing similar for $y$ we get

$$ \begin{align*}
    -1 &\leq -\frac{ny}{tz}\leq 1
\end{align*} $$

If we use [homogeneous co-ordinates](homogeneous-coordinates-section) then this mapping can be represented by the matrix equation

$$ \begin{align*}
    \begin{pmatrix}
        \dfrac{n}{r} & 0 & 0 & 0 \\
        0 & \dfrac{n}{t} & 0 & 0 \\
        0 & 0 & A & B \\
        0 & 0 & -1 & 0
    \end{pmatrix}
    \begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}
    =
    \begin{pmatrix} 
        \dfrac{nx}{r} \\ 
        \dfrac{ny}{t} \\ 
        Az + B \\ 
        -z 
    \end{pmatrix}
\end{align*} $$

where $A$ and $B$ are placeholder variables for now. Since we divide homogeneous co-ordinates by the fourth element then

$$ \left( -\dfrac{nx}{rz}, -\dfrac{ny}{tz}, \dfrac{Az + B}{-z}, 1 \right)^\mathsf{T}, $$

so the mapping for $x'$ and $y'$ is correct. We need $z'$ to be between $-1$ and $1$ so $A$ and $B$ must satisfy

$$ \begin{align*}
    \textsf{near plane:} &&\frac{Az + B}{-z} &= -1, & \implies  Az + B &= z, \\
    \textsf{far plane:} && \frac{Az + B}{-z} &= 1, & \implies Az + B &= -z.
\end{align*} $$

At the near clipping plane $z = -n$ and at the far clipping plane $z = -f$ so

$$ \begin{align*}
    -A n + B &= -n, \\
    -A f + B &= f.
\end{align*} $$

Subtracting the first equation from the second gives

$$ \begin{align*}
    -A (f - n) &= f + n \\
    \therefore A &= -\frac{f + n}{f - n}.
\end{align*} $$

Substituting $A$ in the second equation gives

$$ \begin{align*}
    \left(\frac{f + n}{f - n}\right) n + B &= -n \\
    B &= -n \left( 1 +  \frac{f + n}{f - n}\right) \\
    &= -n \left( \frac{f - n + f + n}{f - n}\right) \\
    &= - \frac{2 \cdot f \cdot n}{f - n}.
\end{align*} $$

So the perspective projection matrix is

$$ \begin{align*}
    Projection_{pers} = 
    \begin{pmatrix}
        \dfrac{n}{r} & 0 & 0 & 0 \\
        0 & \dfrac{n}{t} & 0 & 0 \\
        0 & 0 & -\dfrac{f + n}{f - n} & - \dfrac{2fn}{f - n} \\
        0 & 0 & -1 & 0
    \end{pmatrix}.
\end{align*} $$

We now need to calculate the values of $r$ and $t$. The $t$ co-ordinate is the opposite side of a right angled triangle with angle $\dfrac{fov}{2}$ and adjacent side $n$ so it is easily calculated using trigonometry 

$$ \begin{align*}
    \tan \left( \frac{fov}{2} \right) 
    &= \frac{t}{n} \\
    t &= n \tan \left( \frac{fov}{2} \right).
\end{align*} $$

Since $\textsf{aspect}$ with the width of the window divided by the height and $l = -r$ and $b = -t$ then

$$ \begin{align*}
    aspect &= \frac{r - l}{t - b} = \frac{2r}{2t} \\
    \therefore r &= aspect \times t.
\end{align*} $$
````

Lets apply perspective projection to our cube using a near and far clipping planes at $n=0.2$ and $f=10$ respectively and a field of view angle of $fov = 45^\circ$. Comment out the code use to calculate the orthogonal projection matrix and add the following code.

```cpp
// Calculate perspective projection matrix
float r, t, n, f, fov, aspect;
fov = Maths::radians(45.0f);
aspect = 1024.0f / 768.0f;
n = 0.2f;
f = 100.0f;
t = n * tan(fov / 2.0f);
r = aspect * t;

mat4 projection;
projection[0]  =   n / r;
projection[5]  =   n / t;
projection[10] = - (f + n) / (f - n);
projection[11] = - 1.0f;
projection[14] = - 2.0f * f * n / (f - n);
```

Run your program and you should see the following.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/06_perspective_cube.mp4" type="video/mp4">
</video>
</center>

(changing-the-fov-section)=

### Changing the fov angle

The field of view angle determines how much of the view space we can see in the screen space where the larger the angle the more we can see. When we increase the field of view angle it appears to the user that our view is zooming out whereas a decrease has the effect of zooming in (this is used a lot in first person shooter games to model the effect of a pair of binoculars or a sniper scope).

Experiment with the affect of changing the field of view angle.

`````{grid}
````{grid-item}
```{figure} ../_images/06_fov_15.png

$fov = 15^\circ$
```
````

````{grid-item}
```{figure} ../_images/06_fov_90.png

$fov = 90^\circ$
```
````
`````

---

## A camera class

Our render loop is starting to look a bit messy so we are going to create a `Camera` class to handle all operations relating to the calculation of the view and projection matrices. In the **common/** folder there is a header file and code file called **camera.hpp** and **camera.cpp** which are currently empty. Enter the following code into **camera.hpp**.

```cpp
#pragma once

#include <iostream>
using namespace std;

#include <common/maths.hpp>

class Camera
{
public:
    // Projection parameters
    float fov    = Maths::radians(45.0f);
    float aspect = 1024.0f / 768.0f;
    float near   = 0.2f;
    float far    = 100.0f;
    
    // Camera vectors
    vec3 eye;
    vec3 target;
    vec3 up;
    vec3 worldUp = vec3(0.0f, 1.0f, 0.0f);
    
    // Transformation matrices
    mat4 view;
    mat4 projection;
    
    // Constructor
    Camera(const vec3 &position);
    
    // Methods
    void calculateMatrices();
};
```

You should be familiar with class declarations by now. Here we have declared a `Camera` class with attributes of the float variables, `vec3` and `mat4` objects used above. We also have a constructor method and a method to calculate the view and projection matrices.

In the **camera.cpp** file add the following code.

```cpp
#include <common/camera.hpp>

Camera::Camera(const vec3 &position)
{
    eye = position;
}

void Camera::calculateMatrices()
{
    // Calculate the view matrix
    view = Maths::lookAt(eye, target, worldUp);
    
    // Calculate the projection matrix
    projection = Maths::perspective(fov, aspect, near, far);
}
```

The `Camera()` constructor takes in a single input of a `vec3` object containing the co-ordinates of the camera position and instantiates the $\vec{eye}$ vector. The `calculateMatrices()` method calculates the view and projection matrices. These both use functions from the `Maths` class which we haven't yet defined so lets do this now. In the `Maths` class declare the following functions.

```cpp
// View and projection matrices
static mat4 lookAt(vec3 eye, vec3 target, vec3 worldUp);
static mat4 orthographic(const float l,   const float r,
                         const float b,   const float t,
                         const float n,   const float f);
static mat4 perspective( const float fov, const float aspect,
                         const float n,   const float f);
```

Then define these functions in the **maths.cpp** file.

```cpp
mat4 Maths::lookAt(vec3 eye, vec3 target, vec3 worldUp)
{
    vec3 front = (target - eye).normalise();
    vec3 right = front.cross(worldUp).normalise();
    vec3 up    = right.cross(front);
    
    mat4 view;
    view[0]  =   right.x, view[4] =   right.y, view[8]  =   right.z;
    view[1]  =   up.x,    view[5] =   up.y,    view[9]  =   up.z;
    view[2]  = - front.x, view[6] = - front.y, view[10] = - front.z;
    view[12] = - eye.dot(right);
    view[13] = - eye.dot(up);
    view[14] =   eye.dot(front);
    view[15] =   1.0f;
    
    return view;
}

mat4 Maths::orthographic(const float l, const float r,
                         const float b, const float t,
                         const float n, const float f)
{
    mat4 projection = mat4(1.0f);
    projection[0]  =   2.0f / (r - l);
    projection[5]  =   2.0f / (t - b);
    projection[10] =   2.0f / (n - f);
    projection[12] = - (r + l) / (r - l);
    projection[13] = - (t + b) / (t - b);
    projection[14] =   (n + f) / (n - f);
    
    return projection;
}

mat4 Maths::perspective(const float fov, const float aspect, const float n,
                        const float f)
{
    float t = n * tan(fov / 2.0f);
    float r = aspect * t;

    mat4 projection;
    projection[0]  =   n / r;
    projection[5]  =   n / t;
    projection[10] = - (f + n) / (f - n);
    projection[11] = - 1.0f;
    projection[14] = - 2.0f * f * n / (f - n);
    
    return projection;
}
```

So now we have a `Camera` class lets use it to calculate our view and projection matrices. First create a `Camera` object by entering the following code before the `main()` function.

```cpp
// Create camera object
Camera camera(glm::vec3(0.0f, 0.0f, 5.0f));
```

Then calculate the view and projection matrices just before we calculate the MVP matrix by adding the following code.

```cpp
// Calculate view and projection matrices
camera.target = vec3(0.0f, 0.0f, -4.0f);
camera.calculateMatrices();
```

Here we needed to specify the $\vec{target}$ camera vector so that the camera is looking at the centre of the cube before invoking the `calculateMatrices()` method. The last thing we need to do is to use th e view and projection matrices from the `camera` object when calculating the MVP matrix. Edit your code so that it looks like the following.

```cpp
//Calculate the MVP matrix and send it to the vertex shader
mat4 mvp = camera.projection * camera.view * model;
```

Compile and run your code to check that everything is working correctly.

---

## Multiple objects

The last thing we are going to do in this lab is to add some more cubes to our 3D world. We can do this by defining the position of each cube and then, in the render loop, we loop through each cube and calculate its model matrix, calculate the MVP matrix and then render the current cube. Add the following code to your program before the render loop.

```cpp
// Cube positions
vec3 pos[] = {
    vec3( 0.0f,  0.0f,  0.0f),
    vec3( 2.0f,  5.0f, -10.0f),
    vec3(-3.0f, -2.0f, -3.0f),
    vec3(-4.0f, -2.0f, -8.0f),
    vec3( 2.0f,  2.0f, -6.0f),
    vec3(-4.0f,  3.0f, -8.0f),
    vec3( 0.0f, -2.0f, -5.0f),
    vec3( 4.0f,  2.0f, -4.0f),
    vec3( 2.0f,  0.0f, -2.0f),
    vec3(-1.0f,  1.0f, -2.0f)
};

// Cube rotation angles
float angle[10];
for (unsigned int i = 0 ; i < 10 ; i++)
    angle[i] = Maths::radians(20.0f * i);
```

This creates two arrays of `vec3` objects: `pos` that contain the co-ordinates of the centres of 10 cubes and `angle` that contains a rotation angle based on the loop variable `i`. In the **render loop** replace the code used to calculate the model matrix and render the cube with the following.

```cpp
// Loop through cubes and draw each one
for (int i = 0; i < 10; i++)
{
    // Calculate the model matrix
    mat4 translate = Maths::translate(pos[i]);
    mat4 scale     = Maths::scale(vec3(0.5f, 0.5f, 0.5f));
    mat4 rotate    = Maths::rotate(angle[i], vec3(1.0f, 1.0f, 1.0f));
    mat4 model     = translate * rotate * scale;

    // Calculate the MVP matrix
    mat4 mvp = camera.projection * camera.view * model;

    // Send MVP matrix to the vertex shader
    unsigned int mvpID = glGetUniformLocation(shaderID, "mvp");
    glUniformMatrix4fv(mvpID, 1, GL_FALSE, &mvp[0]);

    // Draw the triangles
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glDrawElements(GL_TRIANGLES, sizeof(indices) / sizeof(unsigned int), 
                   GL_UNSIGNED_INT, 0);
}
```

Here we loop through each of the elements of the `pos` array which are `vec3` objects containing the co-ordinates of each cube. These are used to calculate the translation matrix for the current cube, which is also scaled down by one half in each co-ordinate direction and rotated about the vector $(1, 1, 1)$ using the rotation angle for the current cube.

Note that since the camera is in the same position for each cube we calculate these before looping through each cube. Change the position of the camera to $(0, 0, 5)$ by changing the `camera` object declaration (before the `main()` function) and change $\vec{target}$ camera vector in the `camera` object creation so that the camera looks at $(0,0,0)$.

Run your program and you should see the following.

```{figure} ../_images/06_multiple_cubes.png
:width: 500
```

---

## Exercises

1. Change the projection matrix so that it use orthographic projection.

```{figure} ../_images/06_Ex1.png
:width: 400
```

2. Move the camera position o that it moves in a circle centred at the first cube with radius 10 with a rotation speed such that it completes one full rotation every 5 seconds. Hint: $x = c_x + r\cos(\theta)$ and $z = c_z + r\sin(\theta)$ gives the $x$ and $y$ co-ordinates on a circle centred at $(c_x, c_y, c_z)$ with radius $r$.

<center>
<video controls muted="true" loop="true" width="400">
    <source src="../_static/06_Ex2.mp4" type="video/mp4">
</video>
</center>

3. Rotate the cubes that have an odd index number about the vector $(1,1,1)$ so that they complete one full rotation every 2 seconds. Hint: `x % y` returns the remainder when `x` is divided by `y`, e.g., `3 % 2` will return `1`.

<center>
<video controls muted="true" loop="true" width="400">
    <source src="../_static/06_Ex3.mp4" type="video/mp4">
</video>
</center>

1. Add a feature to your program that allows the user to increase or decrease the field of view angle using the up and down arrow keys. Your code should limit the field of view angle so it is never less than $10^\circ$ or greater than $90^\circ$. Hint: The `keyboardInput()` function at the bottom of the **main.cpp** file checks if the <a href="https://www.glfw.org/docs/3.3/group__keys.html" target="_blank">escape key</a> has been pressed and quits the application if it has.

<center>
<video controls muted="true" loop="true" width="400">
    <source src="../_static/06_Ex4.mp4" type="video/mp4">
</video>
</center>
