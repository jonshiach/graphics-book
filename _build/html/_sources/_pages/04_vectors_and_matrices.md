(vectors-and-matrices-section)=

# Vectors and Matrices

Computer graphics relies heavily on mathematics of vectors and matrices. In this lab we will be revising the important concepts needed for computer graphics as well as creating a library to handle all of the calculations. This library will be used in the upcoming labs so it is important that it works.

---

## Vectors

A vector in is an object with magnitude (length) and direction. A vector is denoted by a lower case letter in boldface, e.g., $\vec{a}$, and represented mathematically by the 3-tuple

$$ \vec{a} = (a_x, a_y, a_z), $$

where $a_x$, $a_y$ and $a_z$ are the lengths of the vector in the $x$, $y$, and $z$ directions.

```{figure} ../_images/04_Vector.svg
:height: 200

The vector $\vec{a} = (a_x, a_y, a_z)$.
```

### Creating a vector class

We are going to create a class that handles the vector operations we will be needing for handling 3D graphics. In the **Headers/** folder of the **Lab04_Vectors_and_matrices** project is the header file **Maths.hpp**. This shared by all of our projects so anything you add to this file will be available to the other projects.

At the moment the **maths.hpp** file is empty and does nothing so enter the following code to give it some purpose.

```cpp
#pragma once

// 3-element vector class
class vec3
{
public:
    float x, y, z;
    
    // Constructors
    vec3();
    vec3(const float& x, const float& y, const float& z);
    vec3(const vec3 &b);
};
```

Here we have created a class called `vec3` which will handle 3-element vectors. We could create a class to handle vectors of any size but we will only be using 3-element vectors so lets not complicate things. The class has three float attributes `x`, `y` and `z` for the 3 elements and 3 constructors for creating a vector object.

We now need to define the constructors, in the **maths.cpp** file found in the **source/** folder enter the following code.

```cpp
#include <iostream>
#include <cmath>

#include <common/maths.hpp>

// =============================================================================
// Vector class methods

vec3::vec3() {};

vec3::vec3(const float &x, const float &y, const float &z)
{
    this->x = x;
    this->y = y;
    this->z = z;
}

vec3::vec3(const vec3 &b)
{
    this->x = b.x;
    this->y = b.y;
    this->z = b.z;
}
```

After importing the **iostream** (for I/O operations) and **cmath** (for maths functions such as `sqrt()`, `cos()`, `sin()` etc.) libraries we have defined our three constructors. The first one is trivial and is used when we want to assign values to the vector at a later time. The second constructor instantiates `x`, `y` and `z` to three values passed in as arguments and the third does similar but the input is another `vec3` object.

We will now create a vector object using our new class. Edit the **Lab04_Vectors_and_matrices.cpp** file so that it looks like the following.

```cpp
#include <iostream>

#include <common/maths.hpp>

int main() {

    // Vectors
    printf("Vectors\n");
    printf("--------------------------------------------------\n");
    
    // Defining vectors
    vec3 a = vec3(3.0f, 0.0f, 4.0f);
    vec3 b = vec3(1.0f, 2.0f, 3.0f);

    return 0;
}
```

Here we have imported the **iostream** and **maths.hpp** libraries. Inside the `main()` function we've created two vector objects `a` and `b`. Compiling and running the code just prints the heading text to the console, we need a way of printing vectors to the console.

### Printing a vector

In the `vec3` class add a method prototype for `print()` method by entering the following code.

```cpp
// Methods
void print();
```

Then define the method in the **maths.cpp** file.

```cpp
void vec3::print()
{
    printf("[%7.3f %7.3f %7.3f ]\n", x, y, z);
}
```

This is a simple method that uses the `printf()` function to print the values of the `x`, `y` and `z` attributes to the console. We can now print our two vectors, back in the `main()` function add the following code.

```cpp
printf("a = "); a.print();
printf("b = "); b.print();
```

The output should look like the following.

```text
Vectors
--------------------------------------------------
Defining vectors:

a = [  3.000   0.000   4.000 ]
b = [  1.000   2.000   3.000 ]
```

(vector-magnitude-section)=

### Vector magnitude

The **magnitude** of a vector $\vec{a} = (a_x, a_y, a_z)$ is denoted by $|\vec{a}|$ is the length from the tail of the vector to the head.

```{figure} ../_images/04_Vector_magnitude.svg
:height: 100

The magnitude of $\vec{a}$ is the length of the vector.
```

The magnitude is calculated using an extension of Pythagoras' theorem

$$ |\vec{a}| = \sqrt{a_x^2 + a_y^2 + a_z^2}. $$(eq:vector-magnitude)

For example, the magnitude of the vector $\vec{u} = (3, 0, 4)$ is 

$$ | \vec{u} | = \sqrt{3^2 + 0^2 + 4^2} = \sqrt{9 + 0 + 16} = \sqrt{25} = 5. $$

Add a method prototype to the `vec3` class called `length()` that returns a float value.

```cpp
float length();
```

Define the function in the **maths.cpp** file.

```cpp
float vec3::length()
{
    return sqrt(x * x + y * y + z * z);
}
```

Lets use the `length()` method to calculate the lengths of our two vectors. In the main program add the following code.

```cpp
// Vector length
printf("\nVector length:\n\n");
printf("length(a) = %0.3f\n", a.length());
printf("length(b) = %0.3f\n", b.length());
```

Running the program you should see the following printed to the console.

```text
Vector length:

length(a) = 5.000
length(b) = 3.742
```

Since we will be using these methods in the upcoming labs it is important that they work correctly so we will be checking each method we create.

(unit-vectors-section)=

### Unit vectors

A **unit vector** is a vector that has a length of 1. We can find a unit vector that points in the same direction as a non-zero vector $\vec{a}$, which is denoted by $\hat{\vec{a}}$ (pronounced *a-hat*), by dividing by its magnitude, i.e.,

$$ \hat{\vec{a}} = \frac{\vec{a}}{|\vec{a}|}. $$(eq:unit-vector)

This process is called **normalising a vector**. For example, to determine a unit vector pointing in the same direction as $\vec{a} = (3, 0, 4)$ we normalise it by dividing by its magnitude which we have already calculated is 5.

$$ \begin{align*}
    \hat{\vec{a}} &= \frac{(3, 0, 4)}{5} = \left( \frac{3}{5}, 0, \frac{4}{5} \right) = (0.6, 0, 0.8).
\end{align*} $$

Checking that $\hat{\vec{a}}$ has a magnitude of 1

$$ |\hat{\vec{a}}| = \sqrt{0.6^2 + 0^2 + 0.8^2} = \sqrt{0.36 + 0.64} = \sqrt{1} = 1.$$

We will using unit vectors a lot so we will need a method to normalise a vector. In the **maths.hpp** file add the function prototype `normalise()` that returns a `vec3` object. Then in the **maths.cpp** file define the method by entering the following code.

```cpp
vec3 vec3::normalise()
{
    float len = length();
    x /= len;
    y /= len;
    z /= len;
    
    return vec3(x, y, z);
}
```

Here we use our `length()` method to calculate the length of the vector object, divide each of the attributes by the length and return another `vec3` object. To check this workds, in the main program enter the following code.

```cpp
// Normalising vectors
vec3 aHat = a; // copy a and b vectors to avoid overwriting them
vec3 bHat = b;
aHat.normalise();
bHat.normalise();
printf("aHat         = "); aHat.print();
printf("bHat         = "); bHat.print();
printf("length(aHat) = %0.3f\n", aHat.length());
printf("length(bHat) = %0.3f\n", bHat.length());
```

Running your program you should see the following printed to the console.

```text
Normalising vectors:

aHat         = [  0.600   0.000   0.800 ]
bHat         = [  0.267   0.535   0.802 ]
length(aHat) = 1.000
length(bHat) = 1.000
```

### Arithmetic operations on vectors

To work with vector we define the arithmetic operations of addition and subtraction of two vectors and multiplication and division by a scalar.

#### Vector addition and subtraction

The addition and subtraction of two vectors $\vec{a} = (a_x, a_y, a_z)$ and $\vec{b} = (b_x, b_y, b_z)$ is defined by

$$ \vec{a} \pm \vec{b} = (a_x \pm b_x, a_y \pm b_y, a_z \pm b_z). $$(eq:vector-addition)

For example, given the vectors $\vec{a} = (3,0,4)$ and $\vec{b} = (1, 2, 3)$

$$ \begin{align*}
    \vec{a} + \vec{b} &= (3, 0, 4) + (1, 2, 3) = (3 + 1, 0 + 2, 4 + 3) = (4, 2, 7), \\
    \vec{a} - \vec{b} &= (3, 0, 4) - (1, 2, 3) = (3 - 1, 0 - 2, 4 - 3) = (2, -2, 1).
\end{align*} $$

<!-- Its important to understand what is happening in a geometrical sense when we add and subtract vectors. Take a look at {numref}`vector-addition-figure`, here the vector $\vec{b}$ has been added to the vector $\vec{a}$ where the tail of $\vec{b}$ is placed at the head of $\vec{a}$. The resulting vector $\vec{a} + \vec{b}$ points from the tail of $\vec{a}$ to the head of $\vec{b}$. 

With the subtraction of the vector $\vec{b}$ we do similar but instead multiply $\vec{b}$ by $-1$ thereby reversing its direction.

```{figure} ../_images/04_Vector_addition.svg
:height: 180
:name: vector-addition-figure

Vector addition and subtraction.
``` -->

#### Multiplication and division by a scalar

Multiplication and division of a vector $\vec{a} = (a_x, a_y, a_z)$ by a scalar $k$ are defined by

$$ \begin{align*}
    k \vec{a} &= (ka_x, ka_y, ka_z), \\
    \frac{\vec{a}}{k} &= \left(\frac{a_x}{k}, \frac{a_y}{k}, \frac{a_z}{k} \right).
\end{align*} $$

Multiplying or dividing a vector by a positive scalar has the effect of scaling the length of the vector. Multiplying or dividing by a negative scalar reverses the direction of the vector.

```{figure} ../_images/04_vector_multiplication.svg
:height: 180
```

For example, multiplying the vector $\vec{a} = (3, 0, 4)$ by the scalar 2 gives

$$ 2\vec{a} = 2(3,0,4) = (6, 0, 8), $$

which has the magnitude

$$ |2 \vec{a} | = \sqrt{6^2 + 0^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10 = 2 |\vec{a}|. $$

#### Operator overloading

Of course we will want to be able to perform arithmetic operations on our vector objects. To do this C++ provides a method of defining the arithmetic operators used for standard data types for class objects. This is known as **operator overloading**. For example, to overload the `+` operator for a `vec3` object define a method prototype for the class using the following code.

```cpp
// Operator overloading   
vec3 operator+(const vec3 &b);
```

Then in the **maths.cpp** file we define the method.

```cpp
vec3 vec3::operator+(const vec3 &b)
{
    return vec3(x + b.x, y + b.y, z + b.z);
}
```

Test whether this works by entering the following code into the main program.

```cpp
// Arithmetic operations on vectors
printf("\nArithmetic operations on vectors:\n\n");
printf("a + b  = "); (a + b).print();
```

Running the program you should see the following printed to the console.

```text
Arithmetic operations on vectors:

a + b  = [  4.000   2.000   7.000 ]
```

Doing similar for the other arithmetic operators the function prototypes are

```cpp
vec3 operator-(const vec3 &b);
vec3 operator/(const float &k);
friend vec3 operator*(const float &k, const vec3 &b);
vec3 operator*(const vec3 &b);
vec3 &operator+=(const vec3 &b);
vec3 &operator-=(const vec3 &b);
```

and the method definitions are (I'll forgive you if you want to paste this code instead of typing it out).

```cpp
vec3 vec3::operator-(const vec3 &b)
{
    return vec3(x - b.x, y - b.y, z - b.z);
}

vec3 operator*(const float &k, const vec3& b)
{
    return vec3(k * b.x, k * b.y, k * b.z);
}

vec3 vec3::operator*(const vec3 &b)
{
    return vec3(x * b.x, y * b.y, z * b.z);
}

vec3 &vec3::operator+=(const vec3 &b)
{
    x += b.x;
    y += b.y;
    z += b.z;
    return *this;
}

vec3 &vec3::operator-=(const vec3 &b)
{
    x -= b.x;
    y -= b.y;
    z -= b.z;
    return *this;
}
```

Test these by adding the following to the main program.

```cpp
printf("a - b  = "); (a - b).print();
printf("2a     = "); (2.0f * a).print();
printf("a * b  = "); (a * b).print();
vec3 temp = a;   // save a in a temporary vector since += overwrites a
printf("a += b = "); (a += b).print();
a = temp;        // restore a
printf("a -= b = "); (a -= b).print();
a = temp;
```

And the following should be printed to the console.

```text
a - b  = [  2.000  -2.000   1.000 ]
2a     = [  6.000   0.000   8.000 ]
a * b  = [  3.000   0.000  12.000 ]
a += b = [  4.000   2.000   7.000 ]
a -= b = [  2.000  -2.000   1.000 ]
```

### Dot and cross products

In the previous section we overloaded the `*` operator to calculate the result of multiplying the corresponding elements of two matrices, e.g., $a * b = (a_xb_x, a_yb_y, a_zb_z)$ (known as **element-wise** multiplication). In addition to this there are two other ways in which we can calculate the product of two matrices, these are the dot and cross products.

(dot-product-section)=

#### The dot product

The **dot product** between two vectors $\vec{a} = (a_x, a_y, a_z)$ and $\vec{b} = (b_x, b_y, b_z)$ is denoted by $\vec{a} \cdot \vec{b}$ and returns a scalar. The dot product is calculated using

$$ \vec{a} \cdot \vec{b} = a_xb_x + a_yb_y + a_zb_z. $$(eq:dot-product)

The dot product is related to the angle $\theta$ between the two vectors ({numref}`angle-between-vectors-figure`) by

$$ \vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos(\theta). $$(eq:dot-product-geometric)

```{figure} ../_images/04_Dot_product.svg
:height: 125
:name: angle-between-vectors-figure

The angle $\theta$ between the vectors $\vec{a}$ and $\vec{b}$.
```

A useful result for computer graphics is that if $\theta=90^\circ$ then $\cos(\theta) = 0$ and equation {eq}`eq:dot-product-geometric` becomes

$$ \vec{a} \cdot \vec{b} = 0. $$

In order words, if the dot product of two vectors is zero then the two vectors are perpendicular. For example, given the vectors $\vec{a} = (3, 0, 4)$ and $\vec{b} = (1, 2, 3)$ the dot product between these is

$$ \begin{align*}
    \vec{a} \cdot \vec{b} &= (3, 0, 4) \cdot (1, 2, 3)
    = 3 + 0 + 12
    = 15.
\end{align*} $$

Add a method prototype to the `vec3` class called `dot()` that returns a float value by entering the following code

```cpp
float dot(const vec3 &b);
```

Then in the **math.cpp** file add the following definition

```cpp
float vec3::dot(const vec3 &b)
{
    return x * b.x + y * b.y + z * b.z;
}
```

Test our `dot()` method be adding the following to the main program.

```cpp
// Dot and cross products
printf("\nDot and cross products:\n\n");
printf("a . b       = %0.3f\n", a.dot(b));
```

The following should be printed to the console.

```text
Dot and cross products:

a . b       = 15.000
```

(cross-product-section)=

#### The cross product

The **cross product** between two vectors $\vec{a} = (a_x, a_y, a_z)$ and $\vec{b} = (b_x, b_y, b_z)$ is denoted by $\vec{a} \times \vec{b}$ and returns a vector. The cross product is calculated using

$$ \vec{a} \times \vec{b} = (a_yb_z - a_zb_y, a_zb_x - a_xb_z, a_xb_y - a_yb_x). $$(eq:cross-product)

The cross product between two vectors produces another vector that is perpendicular to both of the vectors ({numref}`cross-product-figure`). This is another incredibly useful result as it allows us to calculate a [**normal vector**](normal-vector-section) to a polygon which are used in calculating how light is reflected off surfaces (see [9. Lighting](lighting-section)).

```{figure} ../_images/04_cross_product.svg
:height: 200
:name: cross-product-figure

The cross product between two vectors gives a vector that is perpendicular to both vectors.
```

For example, given the vectors $\vec{a} = (3,0,4)$ and $\vec{b} = (1, 2, 3)$ the cross product $\vec{a} \times \vec{b}$ is

$$ \begin{align*}
    \vec{a} \times \vec{b} &= (3, 0, 4) \times (1, 2, 3) \\
    &= (0 \times 3 - 4 \times 2, 4 \times 1 - 3 \times 3, 3 \times 2 - 0 \times 3) \\
    &= (-8, -5, 6).
\end{align*} $$

We can show that $\vec{a} \times \vec{b}$ is perpendicular to both $\vec{a}$ and $\vec{b}$ using the dot product

$$ \begin{align*}
    \vec{a} \cdot (\vec{a} \times \vec{b}) &= (3, 0, 4) \cdot (-8, -5, 6) = -24 + 0 + 24 = 0, \\
    \vec{b} \cdot (\vec{a} \times \vec{b}) &= (1, 2, 3) \cdot (-8, -5, 6) = - 8 - 10 + 18 = 0.
\end{align*} $$

Add a method prototype to the `vec3` class called `cross()` that returns a `vec3` object by entering the following code.

```cpp
vec3 cross(const vec3 &b);
```

Then in the **math.cpp** file add the following definition

```cpp
vec3 vec3::cross(const vec3 &b)
{
    return vec3(y * b.z - z * b.y, z * b.x - x * b.z, x * b.y - y * b.x);
}
```

Test our `cross()` method be adding the following to the main program.

```cpp
printf("a x b       = "); a.cross(b).print();
printf("a . (a x b) = %0.3f\n", a.dot(a.cross(b)));
printf("b . (a x b) = %0.3f\n", b.dot(a.cross(b)));
```

The following should be printed to the console.

```text
a x b       = [ -8.000  -5.000   6.000 ]
a . (a x b) = 0.000
b . (a x b) = 0.000
```

---

## Matrices

Another type of mathematic object that is fundamental to computer graphics is the matrix. A matrix is a rectangular array of numbers.

$$ \begin{align*}
    A =
    \begin{pmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
    \end{pmatrix}
\end{align*} $$

It is common to use uppercase characters for the name of a matrix and lowercase characters for the individual elements. The elements of a matrix are referenced by an **index** which is a pair of numbers, the first of which is the horizontal row number and the second is the vertical column number so $a_{ij}$ is the element in row $i$ and column $j$ of the matrix $A$.  

We refer to the size of a matrix by the number of rows by the number of columns. Here the matrix $A$ has $m$ rows and $n$ columns so we call this matrix a $m \times n$ matrix.

### A $4 \times 4$ matrix class

All of the matrices we use for computer graphics are $4\times 4$ matrices (for reasons that will be explained later) therefore we will need to create a class for handling $4\times 4$ matrices. In the **maths.hpp** file create a class called `mat4` be entering the following code.

```cpp
// 4x4 matrix class
class mat4
{
public:
    // Constructors
    mat4();
    mat4(const float &k);
    mat4(const mat4 &B);
    mat4(const float A00, const float A01, const float A02, const float A03,
         const float A10, const float A11, const float A12, const float A13,
         const float A20, const float A21, const float A22, const float A23,
         const float A30, const float A31, const float A32, const float A33);
    
    // Mathods
    void print();
    
private:
    float A[16];
};
```

This syntax should be fairly familiar to you by now. Here we have the following constructors and methods:

- `mat4()` - a trivial constructor for creating a matrix object whose elements are to be defined later
- `mat4(const float &k)` - a constructor to create a matrix where all the elements are zero apart from the elements on the main diagonal going from the top-left element down to the bottom-right element
- `mat4(const mat4 &B)` - a constructor to creating a matrix object with values from another matrix (i.e., copying a matrix)
- `mat4(const float A00, ...)` - a constructor to create a matrix where the values of all 16 elements are given
- `print()` - a method to print the matrix.

The only attribute we have is `A` which is a 16 element array of floats that will be used to store the values of the elements.

(column-major-order-section)=

### Column-major order

Before we define the constructors we need to look at how to store the values of a matrix. Linear memory is a contiguous block of addresses that can be sequentially accessed. So a 1D array is stored in adjacent memory locations. Since matrices are 2D we have a choice whether to store the elements in the rows or columns in adjacent locations. These are known as **column-major order** and **row-major order**. Consider the $4 \times 4$ matrix

$$ \begin{align*}
    \begin{pmatrix}
        a & b & c & d \\
        e & f & g & h \\
        i & j & k & l \\
        m & n & o & p
    \end{pmatrix}.
\end{align*} $$

Using column-major order this will be stored in the memory as

$$ \underbrace{a, e, i, m}_{\textsf{column 1}}, \quad \underbrace{b, f, j, n}_{\textsf{column 2}}, \quad \underbrace{c, g, k, o}_{\textsf{column 3}}, \quad \underbrace{d, h, l, p}_{\textsf{column 4}} $$

i.e., we move down and across the matrix. Alternatively, using row-major order the matrix will be stored as

$$ \underbrace{a, b, c, d}_{\textsf{column 1}}, \quad \underbrace{e, f, g, h}_{\textsf{column 2}}, \quad \underbrace{i, j, k, l}_{\textsf{column 3}}, \quad \underbrace{m, n, o, p}_{\textsf{column 4}} $$

i.e., we move across and down the matrix. The choice of whether to use column-major or row-major order is arbitrary but OpenGL uses column-major order so it makes sense we should as well (incidentally Microsoft's graphics library directX uses row-major order).

Using column major order the array indices for the elements a $4 \times 4$ matrix will be

$$ \begin{pmatrix}
    a_0 & a_4 & a_8 & a_{12} \\
    a_1 & a_5 & a_9 & a_{13} \\
    a_2 & a_6 & a_{10} & a_{14} \\
    a_3 & a_7 & a_{11} & a_{15}
\end{pmatrix} $$

With this in mind lets define the constructors for the `mat4` class. In the **maths.cpp** file enter the following code.

```cpp
// =============================================================================
// mat4 class methods
mat4::mat4() {
    for (unsigned int i = 0 ; i < 16 ; i++)
        A[i] = 0.0f;
}

mat4::mat4(const float &k)
{
    A[0] = k,    A[4] = 0.0f, A[8]  = 0.0f, A[12] = 0.0f;
    A[1] = 0.0f, A[5] = k,    A[9]  = 0.0f, A[13] = 0.0f;
    A[2] = 0.0f, A[6] = 0.0f, A[10] = k,    A[14] = 0.0f;
    A[3] = 0.0f, A[7] = 0.0f, A[11] = 0.0f, A[15] = k;
}

mat4::mat4(const float A00, const float A01, const float A02, const float A03,
           const float A10, const float A11, const float A12, const float A13,
           const float A20, const float A21, const float A22, const float A23,
           const float A30, const float A31, const float A32, const float A33)
{
    A[0] = A00, A[4] = A01, A[8]  = A02, A[12] = A03;
    A[1] = A10, A[5] = A11, A[9]  = A12, A[13] = A13;
    A[2] = A20, A[6] = A21, A[10] = A22, A[14] = A23;
    A[3] = A30, A[7] = A31, A[11] = A32, A[15] = A33;
}

mat4::mat4(const mat4 &B)
{
    for (unsigned int i = 0 ; i < 16 ; i++)
        A[i] = B.A[i];
}

void mat4::print()
{
    for (unsigned int i = 0 ; i < 4 ; i++)
        printf("[ %7.3f %7.3f %7.3f %7.3f ]\n", A[i], A[i+4], A[i+8], A[i+12]);
}
```

Lets create some matrix objects. Enter the following code into the main program.

```cpp
// Matrices
printf("\nMatrices\n");
printf("--------------------------------------------------\n");

// Defining matrices
mat4 A(1.0f, 2.0f, 3.0f, 4.0f,
       5.0f, 0.0f, 1.0f, 2.0f,
       3.0f, 4.0f, 5.0f, 0.0f,
       1.0f, 2.0f, 3.0f, 4.0f);
mat4 B(2.0f, 4.0f, 6.0f, 8.0f,
       0.0f, 1.0f, 3.0f, 5.0f,
       7.0f, 9.0f, 2.0f, 4.0f,
       6.0f, 8.0f, 0.0f, 1.0f);
mat4 I(1.0f);

printf("Defining matrices:\n");
printf("\nA =\n"); A.print();
printf("\nB =\n"); B.print();
```

Run your program and the following should be printed to the console.

```text
Matrices
--------------------------------------------------
Defining matrices:

A =
[   1.000   2.000   3.000   4.000 ]
[   5.000   0.000   1.000   2.000 ]
[   3.000   4.000   5.000   0.000 ]
[   1.000   2.000   3.000   4.000 ]

B =
[   2.000   4.000   6.000   8.000 ]
[   0.000   1.000   3.000   5.000 ]
[   7.000   9.000   2.000   4.000 ]
[   6.000   8.000   0.000   1.000 ]
```

(transpose-section)=
### Matrix transpose

The **transpose** of a matrix $A$ is denoted by $A^\mathsf{T}$ and is defined by swapping the rows and columns of $A$. For example, the matrix $A$ which we defined in our code is

$$ \begin{align*}
    A =
    \begin{pmatrix}
        1 & 2 & 3 & 4 \\
        5 & 0 & 1 & 2 \\
        3 & 4 & 5 & 0 \\
        1 & 2 & 3 & 4
    \end{pmatrix},
\end{align*} $$

so the transpose of $A$ is

$$ \begin{align*}
    A^\mathsf{T} =
    \begin{pmatrix}
        1 & 5 & 3 & 1 \\
        2 & 0 & 4 & 2 \\
        3 & 1 & 5 & 3 \\
        4 & 2 & 0 & 4
    \end{pmatrix}.
\end{align*} $$

Define a `mat4` class method called `transpose()` that returns a `mat4` object be entering the following code.

```cpp
mat4 transpose();
```

Then define the method in the **maths.cpp** file 

```cpp
mat4 mat4::transpose()
{
    return mat4(A[0],  A[1],  A[2],  A[3],
                A[4],  A[5],  A[6],  A[7],
                A[8],  A[9],  A[10], A[11],
                A[12], A[13], A[14], A[15]);
}
```

Test the method by entering the following code into the main program.

```cpp
// Operations on matrices
printf("\nOperations on matrices:\n\n");
printf("A^T = \n"); A.transpose().print();
```

Run your program and the following should be printed to the console.

```text
Operations on matrices:

A^T = 
[   1.000   5.000   3.000   1.000 ]
[   2.000   0.000   4.000   2.000 ]
[   3.000   1.000   5.000   3.000 ]
[   4.000   2.000   0.000   4.000 ]
```

### Arithmetic operations on matrices

The arithmetic operations on matrices for addition and subtraction of two matrices and multiplying and dividing by a scalar are the same as for vectors so we will not be going over these here. However, we do need to overload the operators so in the `mat4` class define the following method prototypes.

```cpp
// Operator overloading
mat4 operator+(mat4 &B);
mat4 operator-(mat4 &B);
friend mat4 operator*(const float& k, mat4 &B);
mat4 operator/(const float &k);
float& operator[](const unsigned int &index);
```

Here in addition to overloading `+`, `-`, `*` and `/` we are overloading `[]` for indexing a `mat4` object. Define these methods in the **maths.cpp** file.

```cpp
float& mat4::operator[](const unsigned int& index)
{
    return A[index];
}

mat4 mat4::operator+(mat4 &B)
{
    mat4 APlusB;
    for (unsigned int i = 0 ; i < 16 ; i++)
        APlusB[i] = A[i] + B[i];
    
    return APlusB;
}

mat4 mat4::operator-(mat4 &B)
{
    mat4 AMinusB;
    for (unsigned int i = 0 ; i < 16 ; i++)
        AMinusB[i] = A[i] - B[i];
    
    return AMinusB;
}

mat4 operator*(const float &k, mat4 &B)
{
    mat4 kB;
    for (unsigned int i = 0 ; i < 16 ; i++)
        kB[i] = k * B[i];
    
    return kB;
}

mat4 mat4::operator/(const float &k)
{
    mat4 ADivK;
    for (unsigned int i = 0 ; i < 16 ; i++)
        ADivK[i] = A[i] / k;
    
    return ADivK;
}
```

Test each of these by entering the following code into the main program.

```cpp
printf("\nA + B =\n"); (A + B).print();
printf("\nA - B =\n"); (A - B).print();
printf("\n2A =\n");    (2.0f * A).print();
printf("\nA / 3 =\n"); (A / 3.0f).print();
```

Running the program should print the following to the console.

```text
A + B =
[   3.000   6.000   9.000  12.000 ]
[   5.000   1.000   4.000   7.000 ]
[  10.000  13.000   7.000   4.000 ]
[   7.000  10.000   3.000   5.000 ]

A - B =
[  -1.000  -2.000  -3.000  -4.000 ]
[   5.000  -1.000  -2.000  -3.000 ]
[  -4.000  -5.000   3.000  -4.000 ]
[  -5.000  -6.000   3.000   3.000 ]

2A =
[   2.000   4.000   6.000   8.000 ]
[  10.000   0.000   2.000   4.000 ]
[   6.000   8.000  10.000   0.000 ]
[   2.000   4.000   6.000   8.000 ]

A / 3 =
[   0.333   0.667   1.000   1.333 ]
[   1.667   0.000   0.333   0.667 ]
[   1.000   1.333   1.667   0.000 ]
[   0.333   0.667   1.000   1.333 ]
```

You should make sure to check these are correct by doing the calculations using a pen and paper.

(matrix-multiplication-section)=
### Matrix multiplication

So multiplication of a matrix by a scalar is the same for matrices as it is for vectors. However, the multiplication of two matrices $A$ and $B$ is defined in a very specific way. If $A$ and $B$ are two matrices then the element in row $i$ and column $j$ of the matrix $AB$ is calculated using

$$ [AB]_{ij} = \vec{a}_i \cdot \vec{b}_j, $$(eq:matrix-multiplication)

where $\vec{a}_i$ is the vector formed from row $i$ of $A$ and $\vec{b}_j$ is the vector formed from column $j$ of $B$. For example, given the $2\times 2$ matrices $A$ and $B$

$$ \begin{align*}
    A &= \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, &
    B &= \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix},
\end{align*} $$

then the multiplication $AB$ is

$$ \begin{align*}
    AB &=
    \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
    \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} =
    \begin{pmatrix}
        (1, 2) \cdot (5, 7) & (1,2) \cdot (6, 8) \\
        (3, 4) \cdot (5, 7) & (3, 4) \cdot (6, 8)
    \end{pmatrix} \\
    &=
    \begin{pmatrix} 5 + 14 & 6 + 16 \\ 15 + 28 & 18 + 32 \end{pmatrix} =
    \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}.
\end{align*} $$

Note that unlike numbers where is doesn't matter which way round they are when we multiplied (i.e., $1 \times 2 = 2 \times 1 = 2$) this is **not** the case with matrices. For example, lets calculate $BA$

$$ \begin{align*}
    BA &=
    \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
    \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} =
    \begin{pmatrix}
        (5, 6) \cdot (1, 3) & (5, 6) \cdot (2, 4) \\
        (7, 8) \cdot (1, 3) & (7, 8) \cdot (2, 4)
    \end{pmatrix} \\
    &=
    \begin{pmatrix} 5 + 18 & 10 + 24 \\ 7 + 24 & 14 + 32 \end{pmatrix} =
    \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix}.
\end{align*} $$

So based on these two examples we can see that $AB \neq BA$ which is very important when it comes to calculating [transformations](transformations-section). We are going to overload the `*` operator for multiplying matrices. In the `mat4` class define the method prototype by entering the following code.

```cpp
mat4 operator*(mat4 &B);
```

In the **maths.cpp** file define the method by entering the following code.

```cpp
mat4 mat4::operator*(mat4 &B)
{
    mat4 AB;
    for (unsigned int i = 0 ; i < 4 ; i++)
        for (unsigned int j = 0 ; j < 4 ; j++)
            for (unsigned int k = 0 ; k < 4 ; k++)
                AB[i + 4 * j] += A[i + 4 * k] * B[4 * j + k];

    return AB;
}
```

Here we have three nested for loops. The first two are used to loop through the rows and columns of the resulting matrix $AB$. The third loop loops through values of $k = 0, 1, 2, 3$ and calculate the dot products for each element of $AB$. Check our method is correct by entering the following code into the main program.

```cpp
printf("\nAB = \n"); (A * B).print();
printf("\nBA = \n"); (B * A).print();
```

Running the program and the following should be printed to the console.

```text
AB = 
[  47.000  65.000  18.000  34.000 ]
[  29.000  45.000  32.000  46.000 ]
[  41.000  61.000  40.000  64.000 ]
[  47.000  65.000  18.000  34.000 ]

BA = 
[  48.000  44.000  64.000  48.000 ]
[  19.000  22.000  31.000  22.000 ]
[  62.000  30.000  52.000  62.000 ]
[  47.000  14.000  29.000  44.000 ]
```

How do we know this is correct? I'm afraid we are going to have to calculate these by hand.

$$ \begin{align*}
    AB &=
    \begin{pmatrix}
        1 & 2 & 3 & 4 \\
        5 & 0 & 1 & 2 \\
        3 & 4 & 5 & 0 \\
        1 & 2 & 3 & 4
    \end{pmatrix}
    \begin{pmatrix}
        2 & 4 & 6 & 8 \\
        0 & 1 & 3 & 5 \\
        7 & 9 & 2 & 4 \\
        6 & 8 & 0 & 1
    \end{pmatrix} \\
    &= 
    \begin{pmatrix}
         2 + 0 + 21 + 24 &  4 + 2 + 27 + 32 &  6 +  6 +  6 + 0 &  8 + 10 + 12 + 4 \\
        10 + 0 +  7 + 12 & 20 + 0 +  9 + 16 & 30 +  0 +  2 + 0 & 40 +  0 +  4 + 2 \\
         6 + 0 + 28 +  0 & 12 + 4 + 45 +  0 & 18 + 12 + 10 + 0 & 24 + 20 + 20 + 0 \\
         2 + 0 + 21 + 24 &  4 + 2 + 27 + 32 &  6 +  6 +  6 + 0 &  8 + 10 + 12 + 4
    \end{pmatrix} \\
    &= 
    \begin{pmatrix}
        47 & 65 & 18 & 34 \\
        29 & 45 & 32 & 46 \\
        34 & 61 & 40 & 64 \\
        47 & 65 & 18 & 44
    \end{pmatrix}.
\end{align*} $$

So our matrix multiplication method is correct for $AB$ (I'll leave you to check that $BA$ is correct).

(identity-matrix-section)=
### The identity matrix

The **identity matrix** is a special square matrix (a matrix witht the same number of rows and columns) where all the elements are zero apart from the elements on the diagonal line from the top-left element down to the bottom-right element (known as the **main diagonal**). For example the $4\times 4$ identity matrix is

$$ I = \begin{pmatrix}
    1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
\end{pmatrix}.$$

The identity element is similar to the number 1 in that if we multiply any matrix by an identity matrix the result is unchanged. For example

$$ \begin{align*}
    \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
    \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} =
    \begin{pmatrix}
        (1,0) \cdot (1, 3) & (1,0) \cdot (2, 4) \\
        (0,1) \cdot (1,3) & (0,1) \cdot (2,4)
    \end{pmatrix} =
    \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.
\end{align*} $$

We can generate a $4 \times 4$ identity matrix by using our `mat4(k)` constructor we defined earlier. 

```cpp
// Identity matrix
printf("\nThe identity matrix:\n\n");
mat4 I(1.0f);
printf("I = \n"); I.print();
```

Run your program and you should see the following printed to the console.

```text
The identity matrix:

I = 
[   1.000   0.000   0.000   0.000 ]
[   0.000   1.000   0.000   0.000 ]
[   0.000   0.000   1.000   0.000 ]
[   0.000   0.000   0.000   1.000 ]
```

(inverse-matrix-section)=

---

(vectors-exercises)=

## Exercises

1. Three points have the co-ordinates $P = (5, 1, 3)$, $Q = (10, 7, 4)$ and $R = (0, 5, -3)$. Use your maths library to output the following:

    (a) The vector $\vec{p}$ that points from P to Q;<br>
    (b) The vector $\vec{q}$ that points from Q to R;<br>
    (c) The vector $\vec{r}$ that points from R to P;<br>
    (d) The length of the vector $\vec{p}$;<br>
    (e) A unit vector that points in the direction of the vector $\vec{q}$;<br>
    (f) The dot product $\vec{p} \cdot \vec{q}$;<br>
    (g) The cross product $\vec{q} \times \vec{r}$.

2. The three matrices $A$, $B$ and $C$ are defined as

$$ \begin{align*}
    A &= \begin{pmatrix} -1 & 3 \\ 2 & -5 \end{pmatrix}, &
    B &= \begin{pmatrix} 0 & 2 \\ 7 & 1 \end{pmatrix}, &
    C &= \begin{pmatrix} 3 & 2 \\ -3 & -4 \end{pmatrix}.
\end{align*} $$

&emsp;&emsp; Use C++ code to output the following:

&emsp;&emsp; (a) $AB$;<br>
&emsp;&emsp; (b) $ABC$;<br>
&emsp;&emsp; (c) $CBA$;<br>
&emsp;&emsp; (d) $A^\mathsf{T}B$;<br>
&emsp;&emsp; (f) $A^{-1}$.