# IfcColumn

<An _IfcColumn_ is a vertical structural member which often is aligned with a structural grid intersection. It represents a vertical, or nearly vertical, structural member that transmits, through compression, the weight of the structure above to other structural elements below. It represents such a member from an architectural point of view. It is not required to be load bearing.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 6707-1  
> structural member of slender form, usually vertical, that transmits to its base the forces, primarily in compression, that are applied to it.

> NOTE&nbsp; The representation of a column in a structural analysis model is provided by _IfcStructuralCurveMember_ being part of an _IfcStructuralAnalysisModel_.

> NOTE&nbsp; For any longitudial structural member, not constrained to be predominately horizontal nor vertical, or where this semantic information is irrelevant, the entity _IfcMember_ exists.

The IFC specification provides two entities for column occurrences:

* _IfcColumnStandardCase_ used for all occurrences of columns, tthat have a profile defined that is swept along a directrix. The profile might be changed uniformly by a taper definition along the directrix. The profile parameter and its cardinal point of insertion can be fully described by the _IfcMaterialProfileSetUsage_. These beams are always represented geometricly by an 'Axis' and a 'SweptSolid' or 'AdvancedSweptSolid' shape representation (or by a 'Clipping' geometry based on the swept solid), if a 3D geometric representation is assigned. In addition they have to have a corresponding _IfcMaterialProfileSetUsage_ assigned. 
>> NOTE&nbsp; View definitions and implementer agreements may further constrain the applicable geometry types, for example by excluding tapering from an _IfcColumnStandardCase_ implementation. 
* _IfcColumn_ used for all other occurrences of columns, particularly for columns with changing profile sizes along the extrusion, or columns defined by non-linear extrusion, or columns having only 'Brep', or 'SurfaceModel' geometry.

> HISTORY&nbsp; New entity in IFC1.0

## Attributes

### PredefinedType
Predefined generic type for a column that is specified in an enumeration. There may be a property set given specificly for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcColumnType_ is assigned, providing its own _IfcColumnType.PredefinedType_.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcColumnType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no column type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcColumnType_.
