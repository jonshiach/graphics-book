(moving-the-camera-section)=

# Moving the camera

In the [previous lab](3D-worlds-section) we saw how we use transformations to build a 3D world, align the world to the camera position and project the view space onto the screen space. We also created a Camera class to contains functions to perform these calculations. The next step is to modify the Camera class to by able to move and direct the camera around the 3D world.

Compile and run the **Lab07_Moving_the_camera** project and you will see the multiple cube example we created at the end of the last lab.

```{figure} ../_images/07_Moving_the_camera.png
:width: 500
:name: moving-the-camera-figure

Multiple cubes from [6. 3D Worlds](3D-worlds-section).
```

## Using keyboard input to move the camera

The first thing we need to do is add a method to our `Camera` class to move the camera in the world space. We want to be able to move the camera forward and backwards, left and right, up and down. Recall the [view matrix](view-matrix-section) from the [previous lab](3D-worlds-section)

$$ \begin{align*}
    View &=
    \begin{pmatrix}
        r_x & r_y & r_z & -\vec{eye} \cdot \vec{right} \\
        u_x & u_y & u_z & -\vec{eye} \cdot \vec{up} \\
        -f_x & -f_y &- f_z & \vec{eye} \cdot \vec{front} \\
        0 & 0 & 0 & 1
    \end{pmatrix},
\end{align*} $$

where $\vec{right} = (r_x, r_y, r_z)$, $\vec{up} = (u_x, u_y, u_z)$, $\vec{front} = (f_x, f_y, f_z)$ and $\vec{eye}$ are the camera vectors seen in {numref}`camera-vectors-figure`.

```{figure} ../_images/06_View_space_alignment.svg
:width: 400
:name: camera-vectors-figure

Camera vectors
```

Since these three vectors point to the right, up and to the front of the camera we can use these to move the camera in those directions. For example, to move the camera forwards and backwards we simply add and subtract the $\vec{front}$ vector to the camera position which is the $\vec{eye}$ vector ({numref}`camera-movement-figure`).

```{figure} ../_images/07_camera_movement.svg
:width: 500
:name: camera-movement-figure

Moving the camera forwards and backwards.
```

First we need to extract the $\vec{right}$, $\vec{up}$ and $\vec{front}$ vectors from the view matrix. Add the following camera vectors to the class definition in the **camera.hpp** file so they can be accessed outside of the `lookAt()` function

```cpp
vec3 right   = vec3(1.0f, 0.0f,  0.0f);
vec3 up      = vec3(0.0f, 1.0f,  0.0f);
vec3 front   = vec3(0.0f, 0.0f, -1.0f);
```

and in the **camera.cpp** file add the following code to the `calculateMatrices()` function after the view matrix is calculated.

```cpp
// Update camera vectors
right.x =   view[0], right.y =   view[4], right.z =   view[8];
up.x    =   view[1], up.y    =   view[5], up.z    =   view[9];
front.x = - view[2], front.y = - view[6], front.z = - view[10];
```

Note that the third row of the view matrix is $-\vec{front}$ so we need to change the sign of the these elements. We now need a class method to move the camera, add the following method declaration to the `Camera` class.

```cpp
void move(const string direction);
```

Then define this method in the **camera.cpp** folder by entering the following code.

```cpp
void Camera::move(const string direction)
{ 
    // Move camera
    if (direction == "forward")
        eye += front;
    
    if (direction == "backward")
        eye -= front;
    
    if (direction == "left")
        eye -= right;
    
    if (direction == "right")
        eye += right;
}
```

Here we add/subtract the $\vec{front}$ or $\vec{right}$ vectors to/from the $\vec{eye}$ vector depending on the value of the string `direction`.

### Getting the keyboard input

We need to get keyboard input from the user and use it to invoke our `move()` method. If you take a look at the **Lab07_Moving_the_camera.cpp** file at the bottom we have the function `keyboardInput()` which currently contains a single if statement that uses the function `glfwGetKey()` to detect whether the escape key has been pressed. This is called in the render loop so that at each frame the program is checking for keyboard inputs. Add the following code to the `keyboardInput()` function.

```cpp
// Move camera
if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
    camera.move("forward");

if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
    camera.move("backward");

if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
    camera.move("left");

if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
    camera.move("right");
```

Here we've used the classic WSAD key combination to control the movement of the camera. Run your program and experiment with moving the camera.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/07_keyboard_1.mp4" type="video/mp4">
</video>
</center>

You will notice that when the camera is moved left to right using the A and D keys the camera rotates around the first cube. This because our camera is always pointing towards $(0,0,0)$ as the `lookat()` function uses the $\vec{target}$ vector to calculate the view matrix. To fix this we simply change `target` to `eye + front` in the function call to `lookAt()` so that the camera is always pointing forwards (for now).

```cpp
// Calculate the view matrix
view = Maths::lookAt(eye, eye + front, worldUp);
```

Run your program and you should see that the camera always points down the $z$-axis.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/07_keyboard_2.mp4" type="video/mp4">
</video>
</center>

## Controlling the speed of the camera.

Playing around with the camera movement you will also notice that the controls are quite sensitive and not very satisfying to use. To fix this we can control the speed at which the camera moves in the world space.  Add an attribute for the camera speed to the `Camera` class by adding the following code to the `Camera` class method.

```cpp
// Camera parameters
float cameraSpeed = 5.0f;
```

Speed is distance divided by time so to ensure that the camera moves at our chosen speed of 5 units per second we need to input the `deltaTime` variable (the time that has elapsed between the two successive iterations of the render loop) into the `move()` method. Edit the method declaration so that it takes in a second input of `deltaTime`

```cpp
void move(const string direction, const float deltaTime);
```

and edit the `move()` method definition so it uses `mouseSpeed` and `deltaTime` to move the $\vec{eye}$ vector in the chosen direction and at the chosen speed, e.g.,

```cpp
if (direction == "forward")
    eye += cameraSpeed * deltaTime * front;
```

and do similar for the other three directions. Since $\vec{front}$ and $\vec{right}$ are unit vectors our camera now moves at 5 units per second (of course we can change this to suit out needs, e.g., simulating a character sprinting in a first person shooter game).

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/07_keyboard_3.mp4" type="video/mp4">
</video>
</center>

## Using the mouse to point the camera

We can now move the camera position using keyboard inputs but we can't yet point the camera in a difference direction. This is usually done using mouse inputs but can also done using keyboard or game controllers.

First we need to capture the mouse inputs. Take a look at the `main()` function, just after the window is created we call the `glfwSetInputMode()` which enables use to capture the keyboard inputs. So to capture the mouse input we need to do similar. Enter the following code just after we capture the keyboard inputs.

```cpp
// Capture mouse inputs
glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);
glfwPollEvents();
glfwSetCursorPos(window, 1024 / 2, 768 / 2);
glfwSetCursorPosCallback(window, mouseCallback);
```

These functions are:

- `glfwSetInputMode()` - captures the mouse input (in addition to the earlier call to the same function to capture the keyboard inputs) and hides the mouse cursor
- `glfwPollEvents()` - processes any events in the event queue, in other words it checks for a mouse input right away
- `glfwSetCursorPos()` - specifies the position of the mouse cursor in the window, here we have set this to the centre of the window
- `glfwSetCursorPosCallback()` - specifies that we call the callback function `mouseCallBack()` (not yet written) which is executed when GLFW detects a change in the cursor position.

### Yaw, pitch and roll

The direction which the camera is pointing is governed by three angles called $yaw$, $pitch$ and $roll$ which are collectively known as <a href="https://en.wikipedia.org/wiki/Euler_angles" target="_blank">**Euler angles**</a>. The name of these come from the aviation industry where they are related to the direction that an aircraft is facing. A plane on the ground first needs to taxi to the end of a runway which is does by steering left and right in the horizontal direction by changing its $yaw$ angle. Then on take off it can point its nose upwards in the vertical direction by changing its $pitch$ angle. Once airborne the plane can move its wingtips up and down thus changing its $roll$ angle. Our camera is analogous to the plane ({numref}`yaw-pitch-roll-figure`).

```{figure} /_images/07_yaw_pitch_roll.svg
:width: 250
:name: yaw-pitch-roll-figure

Yaw, pitch and roll
```

To point our camera we only need the $yaw$ and $pitch$ angles which we are going to change using mouse inputs such that when the mouse is moved left and right the $yaw$ angle changes and when the mouse is moved up and down the $pitch$ angle changes. The problem we have is that our `lookAt()` function uses the $\vec{front}$ vector to calculate the $view$ matrix so we need some way of calculating the $\vec{front}$ vector from the $yaw$ and $pitch$ angles.

To do this we look at what happens to the vector $(0,0,1)$, that points along the $z$-axis, when the mouse cursor is moved. If the mouse cursor is moved to the left then the vector $(0,0,1)$ is rotated anti-clockwise about the $y$-axis.

```{figure} /_images/07_yaw.svg
:name: yaw-figure
:width: 300

Yaw movement is rotation about the $y$-axis.
```

The [rotation matrix](rotation-section) for rotating anti-clockwise about the $y$-axis is

$$ \begin{align*}
    R_y =
    \begin{pmatrix}
        \cos(yaw) & 0 & \sin(yaw) \\
        0 & 1 & 0 \\
        -\sin(yaw) & 0 & \cos(yaw)
    \end{pmatrix}.
\end{align*} $$

Similarly, if the cursor is moved downwards then this represents a rotation of the $(0,0,1)$ vector clockwise about the $x$-axis.

```{figure} /_images/07_pitch.svg
:name: pitch-figure
:width: 300

Pitch movement is rotation about the $x$-axis.
```

The rotation matrix for rotating clockwise about the $x$-axis is (note that the negative sign is now next to the lower left $\sin$ function as opposed to the upper-right for rotating [anti-clockwise](rotation-section) about the $x$-axis)

$$ \begin{align*}
  R_x &= 
  \begin{pmatrix}
    1 & 0 & 0 \\
    0 &   \cos(pitch) & \sin(pitch) \\
    0 &  -\sin(pitch) &  \cos(pitch)
  \end{pmatrix}.
\end{align*} $$

Applying the $yaw$ and $pitch$ rotations to the $(0,0,1)$ vector means calculating $\vec{front} = R_y\cdot R_x \cdot (0, 0, 1)^\mathsf{T}$

$$ \begin{align*}
    R_y \cdot R_x \cdot \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} &=
    \begin{pmatrix}
         \cos(yaw) & 0 & \sin(yaw) \\
         0 & 1 & 0 \\
        -\sin(yaw) & 0 & \cos(yaw)
    \end{pmatrix}
    \begin{pmatrix}
        1 & 0 & 0 \\
        0 &  \cos(pitch) & -\sin(pitch) \\
        0 & -\sin(pitch) &  \cos(pitch)
    \end{pmatrix}
    \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\
    &=
    \begin{pmatrix}
          \cos(yaw) & -\sin(yaw) \sin(pitch) & \sin(yaw) \cos(pitch) \\
         0          & \cos(pitch)            & \sin(pitch) \\
         -\sin(yaw) & -\cos(yaw) \sin(pitch) & \cos(yaw) \cos(pitch)
    \end{pmatrix}
    \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \\
    &=
    \begin{pmatrix}
        \sin(yaw) \cos(pitch) \\
        \sin(pitch) \\
        \cos(yaw) \cos(pitch)
    \end{pmatrix}.
\end{align*} $$

So the $\vec{front}$ vector is

$$ \vec{front} = \operatorname{normalise} (\sin(yaw)\cos(pitch), \sin(pitch), \cos(yaw)\cos(pitch)). $$

To apply this to our `Camera` class we need to add attributes for the $yaw$, $pitch$ and $roll$ Euler angles. Add the following code to the camera parameters in the `Camera` class declaration.

```cpp
float yaw         = Maths::radians(180.0f);
float pitch       = 0.0f;
float roll        = 0.0f;
```

Here we have set the $pitch$ and $roll$ angles to $0^\circ$ and $yaw$ to $180^\circ$ since the $\vec{front}$ vector is initially pointing down the negative $z$-axis. Then in the **Camera.cpp** file edit the `calculateMatrices()` method so that the $\vec{front}$ vector is calculated from the Euler angles prior to calculating the view matrix

```cpp
// Calculate view matrix
front.x = sin(yaw) * cos(pitch);
front.y = sin(pitch);
front.z = cos(yaw) * cos(pitch);
front.normalise();

view = Maths::lookAt(eye, eye + front, worldUp);
```

### Pointing the camera

The $yaw$ and $pitch$ Euler angles are to be changed using a callback function that handles the mouse movement. In the **Lab07_Moving_the_camera.cpp** file add the following function prototype near the top of the file where we have one for the `keyboardInputs()` function.

```cpp
void mouseCallback(GLFWwindow *window, double xPos, double yPos);
```

Then at the bottom of the file define the function by entering the following code.

```cpp
void mouseCallback(GLFWwindow *window, double xPos, double yPos)
{
    // Update yaw and pitch angles
    float xOffset = float(1024 / 2 - xPos);
    float yOffset = float( 768 / 2 - yPos);
    camera.yaw   += xOffset;
    camera.pitch += yOffset;
    
    // Reset mouse cursor position to centre
    glfwSetCursorPos(window, 1024 / 2, 768 / 2);
}
```

This function takes inputs of a pointer to the `window` object and two variables `xPos` and `yPos` which are the number of pixels across and down from the left-hand and top edges of the window respectively. The variables `xOffset` and `yOffset` are calculated as the distance of the cursor from the centre of the window in the horizontal and vertical directions respectively. A positive offset value meaning the cursor is to the left and below the centre ({numref}`cursor-figure`).

```{figure} ../_images/07_cursor.svg
:width: 300
:name: cursor-figure

$x$ and $y$ offset values are the distance in pixels from the window centre.
```

The $yaw$ and $pitch$ attributes of the `camera` object are incremented by the offset values. For example, if the cursor is moved to the left then `xOffset` is a positive value so that $yaw$ angle increases and the camera rotates anti-clockwise about the $y$-axis ({numref}`yaw-figure`). Similarly, if the cursor is moved downwards then `yOffset` is positive and the $pitch$ angle increases and the camera rotates clockwise about the $x$-axis ({numref}`pitch-figure`). After incrementing the $yaw$ and $pitch$ angles we reset the mouse cursor to the centre of the window. If we didn't do this the cursor would soon go outside of our window and we wouldn't be able to point the camera in a different direction.

If you compile and run your program you may notice that the mouse controls are far too sensitive and we need to slow down the speed of rotation. To do this add an attribute to the camera parameters called `mouseSpeed` and initialise it to some small number (you may need to experiment with this value to dial in the sensitivity you want).

```cpp
float mouseSpeed = 0.001f;
```

Then change the `yaw` and `pitch` calculations in the `mouseCallback()` function to the following

```cpp
camera.yaw   += camera.mouseSpeed * xOffset;
camera.pitch += camera.mouseSpeed * yOffset;
```

Running the program and we can now move around our world space and point the camera in any direction we want (well, almost any direction).

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/07_mouse.mp4" type="video/mp4">
</video>
</center>

---

## Changing the field of view angle using scroll wheel

Recall in the [previous lab](changing-the-fov-section) that changing the field of view angle used in the calculation of the perspective projection matrix had the effect of zooming in and out of the scene. We can use the scroll wheel to control the field of view angle. To do this we need another callback function for the scroll wheel, after we use the `glfwSetCursorCallback()` add the following code.

```cpp
glfwSetScrollCallback(window, scrollCallback);
```

This tells GLFW that we want something to happen when the scroll wheel is used. We need to declare and define the `scrollCallback()` function so add a function prototype before the `main()` function

```cpp
void scrollCallback(GLFWwindow *window, double xOffset, double yOffset);
```

and then at the bottom of the file define the function

```cpp
void scrollCallback(GLFWwindow *window, double xOffset, double yOffset)
{
    // Change field of view angle
    camera.fov += 0.05f * (float)yOffset;
    
    // Restrict the fov angle
    if (camera.fov < Maths::radians(5.0f))
        camera.fov = Maths::radians(5.0f);
    
    if (camera.fov > Maths::radians(120.0f))
        camera.fov = Maths::radians(120.0f);
}
```

Most scroll wheels only return a horizontal scroll value which we have called `yOffset` and the $fov$ angle is incremented or decremented based on this value (which is also multiplied by 0.05 to limit the changes, you may need to experiment with this value to get it right). We also need to limit the range of values that the $fov$ angle can take which we have done using the if statements.

Run your program and play around with the scroll wheel and you should see something like the following.

<center>
<video controls muted="true" loop="true" width="500">
    <source src="../_static/07_scroll_wheel.mp4" type="video/mp4">
</video>
</center>

It may seem like the position of the camera is changing but what is actually happening is that changes to the field of view angle is changing the size of the viewing frustum thus causing the cubes to change size. It is a common trope in first-person shooter games to render the outline of a scope or binoculars to remind the player that they are zooming in and not moving forward.

---

## Back face culling

Whilst moving your camera around your 3D world you may notice that we can move through objects and view them from the inside. All surfaces of the cubes are rendered, including those not visible from the camera because they are on the far side of the cubes. This is a waste of resources as OpenGL is calculating the vertex and fragment shaders for objects that won't be shown in the frame. To overcome this we can cull (omit) any surface of an object that is **back facing** the camera in a method called **back face culling**.

(normal-vector-section)=

A **normal vector** (often just referred to as a **normal**) is a vector denoted by $\vec{n}$ that is perpendicular to a surface at a given point ({numref}`normal-vector-figure`).

```{figure} /_images/07_normal_vector.svg
:width: 250
:name: normal-vector-figure

The surface normal vector.
```

Since in computer graphics are surfaces are triangles, we can easily calculate a normal vector using a [cross product](cross-product-section). If a triangle has vertices $\vec{v}_0$, $\vec{v}_1$ and $\vec{v}_2$ then the normal vector can be calculated using

$$ \vec{n} = (\vec{v}_1 - \vec{v}_0) \times (\vec{v}_2 - \vec{v}_1). $$

A surface is said to be back facing it its normal vector is pointing away from the camera position. If we only render the front facing surfaces then, assuming the surfaces are opaque, we should not notice any difference and we have halved the number of surfaces the shader has to deal with ({numref}`backface-culling-figure`). 

```{figure} /_images/07_backface_culling.svg
:width: 300
:name: backface-culling-figure

Back face culling removes surfaces with vectors pointing away from the camera.
```

But how do we know if a surface is back facing? Consider {numref}`back-facing-figure` which shows a back facing surface.

```{figure} /_images/07_Back_facing.svg
:width: 400
:name: back-facing-figure

A back facing surface.
```

Here $\vec{v}$ is a vector pointing from the camera to a point on the surface. Recall that the [dot product](dot-product-section) is related to the angle between two vectors, i.e.,

$$ \vec{n} \cdot \text{v} = | \vec{n} | | \vec{v} | \cos(\theta). $$

If we have a back facing surface then $\theta$ is less than 90$^\circ$ and $\cos(\theta)$ is a positive number so

$$\begin{align*}
  \vec{n} \cdot \text{v} > 0.
\end{align*}$$

So to apply back face culling the vertex shader just has to calculate the dot product between the $\vec{n}$ and $\vec{v}$ vectors and if it is a positive number it ignores the surface from then on. To apply back face culling in OpenGL all we need to do is add the following code to the `main()` function near where we invoke the depth testing.

```cpp
// Enable back face culling
glEnable(GL_CULL_FACE);
```

Compile and run your program and use the keyboard and mouse to put the camera inside a cube. You will now see that the back faces haven't been rendered.

---

## Exercises

1. Change the `calculateMatrices()` Camera class method so that the camera position always has a $y$ co-ordinate of 0, i.e., like a first person shooter game where the player cannot fly around the world.
2. Add the ability for the user to perform a jump by pressing the space bar. The jump should last for 1 second and the camera should follow a smooth arc. Hint: the function $y = \tt height \cdot \sin(\pi \cdot \tt time)$ produces values of $y=0$ when $\tt time = 0$ or $\tt time = 1$ and $y = \tt height$ when $\tt time = 0.5$.
3. Write your own class called `MyLib` with static member functions for each of the functions you have used from the glm library (e.g., `lookAt()`) and make use of them to calculate the `model`, `view` and `projection` matrices (you may make use of `glm::mat4` and `glm::vec3` types).
