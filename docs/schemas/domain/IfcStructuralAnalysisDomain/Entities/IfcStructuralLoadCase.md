# IfcStructuralLoadCase

A load case is a load group, commonly used to group loads from the same action source.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### SelfWeightCoefficients
The self weight coefficients specify ratios at which loads due to weight of members shall be included in the load case.  These loads are not explicitly modeled as instances of _IfcStructuralAction_.  Instead they shall be calculated according to geometry, section, and material of each member.

The three components of the self weight vector correspond with the x,y,z directions of the so-called global coordinates, i.e. the directions of the shared _ObjectPlacement_ of all items in an _IfcStructuralAnalysisModel_. For example, if the object placement defines a z axis which is upright like the _IfcProject_'s world coordinate system, then the self weight coefficients would typically be [0.,0.,-1.] in a load case of dead loads with self weight.

The overall coefficient in the inherited attribute _Coefficient_ shall not be applied to _SelfWeightCoefficients_ of the same instance of _IfcStructuralLoadCase_. It only applies to actions and load groups which are grouped below the load case, not to the load case's computed self weight.

## Formal Propositions

### IsLoadCasePredefinedType
An instance of this subtype of structural load group cannot be of any other type than that of a load case.
