# IfcMaterialRelationship

_IfcMaterialRelationship_ defines a relationship between part and whole in material definitions (as in composite materials). The parts, expressed by the set of _RelatedMaterials_, are material constituents of which a single material aggregate is composed.<!-- end of definition -->

> HISTORY New entity in IFC4

## Attributes

### RelatingMaterial
Reference to the relating material (the composite).

### RelatedMaterials
Reference to related materials (as constituents of composite material).

### Expression
Information about the material relationship referring for example to the amount of related materials in the composite material.
> NOTE  Any formal meaning of the _Expression_ string value has to be established in model view definitions or implementer agreements. No such formal language is provided as part of this specification.
