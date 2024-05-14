# IfcSpecularRoughness

The _IfcSpecularRoughness_ defines the datatype for the reflection resulting from the roughness of a surface through the height of surface impurities where the specular highlight is made sharper with small values for the roughness, such as 0.1. Applies to "glass", "metal", "mirror" and "plastic" reflection models. Larger values, close to 1.0 decrease the specular fall-off.<!-- end of definition -->

_IfcSpecularRoughness_ is of type REAL. It is constraint to values between (and including) 0 and 1.

> NOTE The datatype relates to the definition of "shininess" in [ISO/IEC 14772-1](../content/bibliography.htm#IEC-14772-1), which is the reciprocate value to the specular roughness.

> HISTORY New type in IFC2x2.

## Formal Propositions

### WR1
Specular roughness shall be given as a non-negative value less than or equal to 1.0
