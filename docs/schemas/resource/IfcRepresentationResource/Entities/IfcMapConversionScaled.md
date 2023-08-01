# IfcMapConversionScaled

An _IfcMapConversionScaled_ is a type of _IfcMapConversion_ that supplies factors for coordinate conversion. The usage is restricted to when factors are explicitly exchanged. 

> NOTE  Typically, these are relatively smaller facilities such as buildings where constant factors are agreed on a project.

For this transformation, _IfcMapConversionScaled_ data are used for:
1. a scaling of the three axes (x,y,z), by the same _IfcMapConversionScaled.Scale_
2. a multiplication of the x-axis by _IfcMapConversionScaled.FactorX_
3. a multiplication of the y-axis by _IfcMapConversionScaled.FactorY_
4. a multiplication of the z-axis by _IfcMapConversionScaled.FactorZ_
5. followed by an **anti-clockwise** rotation about the z-axis of $\theta$, where: 

$$
\theta=arctan\left(\frac{IfcMapConversionScaled.XAxisOrdinate}{IfcMapConversionScaled.XAxisAbscissa}\right)
$$

6. and then a translation in (x,y,z) of _IfcMapConversionScaled.Eastings_, _IfcMapConversionScaled.Northings_, _IfcMapConversionScaled.OrthogonalHeight_.

> HISTORY New entity in IFC4X3_ADD1

## Attributes

### FactorX
Factor by which the length measures in local engineering CS of X axis have to be multiplied to get map coordinates

### FactorY
Factor by which the length measures in local engineering CS of Y axis have to be multiplied to get map coordinates

### FactorZ
Factor by which the length measures in local engineering CS of Z axis have to be multiplied to get map coordinates
