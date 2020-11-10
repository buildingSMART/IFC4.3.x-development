IfcReference
============
This entity is used to refer to a value of an attribute on an instance. It may
refer to the value of a scalar attribute or a value within a collection-based
attribute. Referenced attributes may be direct values, object references,
collections, inverse object references, and inverse collections. References
may be chained to form a path of object-attribute references.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstraintresource/lexical/ifcreference.htm)


Attribute definitions
---------------------
| Attribute           | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| InnerReference      |                                                                                                                                                                                                                                                                                                                                                                                                                |
| TypeIdentifier      | Optional identifier of the entity or type such as ''IfcMaterialLayerSet''. For entity, type, or select-based references within a collection, this resolves the reference to such type. \X\0DIf omitted, the type is assumed to be the same as the declared referencing attribute.\X\0D\X\0D> EXAMPLE  _IfcRelAssociatesMaterial_._RelatingMaterial_ may be resolved to _IfcMaterialLayerSet_.                  |
| AttributeIdentifier | Optionally identifies a direct or inverse attribute within an entity such as ''MaterialLayers''. \X\0DIf _TypeIdentifier_ is specified and refers to an entity, the attribute must exist within the referenced entity.\X\0DA null value indicates a reference to the type or entity itself, such as for indicating that the type of a value must match a specified constraint.                                 |
| InstanceName        | Optionally identifies an instance within a collection according to name. If the instance has an attribute called ''Name'', such attribute is used for comparison; otherwise the first STRING-based attribute of the entity is used.\X\0D\X\0D> EXAMPLE  _IfcRoot_-based entities such as _IfcPropertySet_ use the _Name_ attribute; _IfcRepresentation_ entities use the _RepresentationIdentifier_ attribute. |
| ListPositions       | Optionally identifies an instance within a collection according to position starting at 1. For referencing single-level collections, this attribute contains a single member; for referencing multi-level collections, then this LIST attribute contains multiple members starting from the outer-most index.                                                                                                  |

