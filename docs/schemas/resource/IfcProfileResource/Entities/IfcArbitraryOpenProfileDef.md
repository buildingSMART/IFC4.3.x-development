# IfcArbitraryOpenProfileDef

The open profile _IfcArbitraryOpenProfileDef_ defines an arbitrary two-dimensional open profile for the use within the swept surface geometry. It is given by an open boundary from which the surface can be constructed.<!-- end of definition -->

> HISTORY  New entity in IFC2x.

**Informal Propositions**

1. The _Curve_ has to be an open curve.

Figure 1 illustrates the arbitrary open profile definition. The _Curve_ is defined in the underlying coordinate system. The underlying coordinate system is defined by the swept surface that uses the profile definition. It is the xy plane of:

* _IfcSweptSurface.Position_

The _Curve_ attribute defines a two dimensional open bounded curve.

![arbitrary profile without boundaries](../../../../figures/ifcarbitraryprofiledef-layout3.gif "Figure 1 — Arbitrary open profile")

## Attributes

### Curve
Open bounded curve defining the profile.

## Formal Propositions

### WR11
The profile type is a .CURVE., an open profile can only be used to define a swept surface.
> NOTE This does not apply to the subtype _IfcCenterLineProfileDef_.

### WR12
The dimensionality of the curve shall be 2.
