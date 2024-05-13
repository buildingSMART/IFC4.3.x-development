# IfcMapConversionScaled

An _IfcMapConversionScaled_ is a type of _IfcMapConversion_ that supplies factors for coordinate conversion. The usage is restricted to when factors are explicitly exchanged. <!-- end of definition -->

> NOTE  Typically, these are relatively smaller facilities such as buildings where constant factors are agreed on a project.

> HISTORY New entity in IFC4X3_ADD1

For this transformation, _IfcMapConversionScaled_ data are used for:

1. a scaling of the three axes (x,y,z), by the same _IfcMapConversionScaled.Scale_
2. a multiplication of the x-axis by _IfcMapConversionScaled.FactorX_
3. a multiplication of the y-axis by _IfcMapConversionScaled.FactorY_
4. a multiplication of the z-axis by _IfcMapConversionScaled.FactorZ_
5. followed by an **anti-clockwise** rotation about the z-axis of *θ*, where:
  $$
  \theta=arctan\left(\frac{\text{XAxisOrdinate}}{\text{XAxisAbscissa}}\right)
  $$
6. and then a translation in (x,y,z) of _IfcMapConversionScaled.Eastings_, _IfcMapConversionScaled.Northings_, _IfcMapConversionScaled.OrthogonalHeight_.

**Equations**

Below are the relevant equations for _IfcMapConversionScaled_. The equations are given: a) in transformation matrix form, useful for programmers to understand the exact sequence of operations and b) in a simplified equation form, which is sufficient for calculating a single point.

a) matrix form

$$
\begin{bmatrix}
x'\\\\
y'\\\\
z'
\end{bmatrix}
= \begin{bmatrix}
cos\theta & -sin\theta & 0 \\\\
sin\theta & cos\theta & 0 \\\\
0 & 0 & 1
\end{bmatrix} \cdot 
\begin{bmatrix}
\text{FactorX} & 0 & 0 \\\\
0 & \text{FactorY} & 0 \\\\
0 & 0 & \text{FactorZ}
\end{bmatrix} \cdot 
\begin{bmatrix}
\text{Scale} & 0 & 0 \\\\
0 & \text{Scale} & 0 \\\\
0 & 0 & \text{Scale}
\end{bmatrix} \cdot 
\begin{bmatrix}
x \\\\
y \\\\
z
\end{bmatrix} +
\begin{bmatrix}
\text{Eastings} \\\\
\text{Northings} \\\\
\text{OrthogonalHeight}
\end{bmatrix}
$$

b) equation form

$$
\begin{align}
x' &= \text{Scale} \cdot \text{FactorX} \cdot cos\theta \cdot x-\text{Scale} \cdot \text{FactorY} \cdot sin\theta \cdot y+\text{Eastings} \\\\
y' &= \text{Scale} \cdot \text{FactorX} \cdot sin\theta \cdot x+\text{Scale} \cdot \text{FactorY} \cdot cos\theta \cdot y+\text{Northings} \\\\
z' &= \text{Scale} \cdot \text{FactorZ} \cdot z+\text{OrthogonalHeight}
\end{align}
$$