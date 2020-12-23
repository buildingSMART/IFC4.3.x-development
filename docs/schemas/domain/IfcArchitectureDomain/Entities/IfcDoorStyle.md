# IfcDoorStyle

Definition: The door style, _IfcDoorStyle_, defines a particular style of doors, which may be included into the spatial context of the building model through instances of _IfcDoor_. A door style defines the overall parameter of the door style and refers to the particular parameter of the lining and one (or several) panels through the _IfcDoorLiningProperties_ and the _IfcDoorPanelProperties_.

The door entity, _IfcDoor_, defines a particular occurrence of a door inserted in the spatial context of a project. The actual parameter of the door and/or its shape is defined at the _IfcDoorStyle_, to which the _IfcDoor_ is related by the inverse relationship _IsDefinedBy_ pointing to _IfcRelDefinedByType_. The _IfcDoorStyle_ also defines the particular attributes for the lining_, IfcDoorLiningProperties_, and panels, _IfcDoorPanelProperties_.

The _IfcDoorStyle_ defines the baseline geometry, or the representation map, for all occurrences of the door style, given by the _IfcDoor_, pointing to this style. The representation of the door style may be given by the agreed set of minimal parameters, defined for the door lining and the door panel(s), or it may be given by a geometric representation used by the _IfcRepresentationMap_. The attribute _ParameterTakesPrecedence_ decides, whether the set of parameters can be used to exactly represent the shape of the door style (TRUE), or whether the attached _IfcRepresentationMap_ holds the exact representation (FALSE).

The _IfcDoorStyleOperationTypeEnum_ defines the general layout of the door style. Depending on the enumerator, the appropriate instances of _IfcDoorLiningProperties_ and _IfcDoorPanelProperties_ are attached in the list of _HasPropertySets_. The _IfcDoorStyleOperationTypeEnum_ mainly determines the hinge side (left hung, or right hung), the operation (swinging, sliding, folding, etc.) and the number of panels.

See geometry use definitions at _IfcDoorStyleOperationTypeEnum_ for the correct usage of opening symbols for different operation types.

> HISTORY&nbsp; New entity in IFC2x.

{ .deprecated}
> DEPRECATION&nbsp; The entity is deprecated and shall not be used. The new entity _IfcDoorType_ shall be used instead.

## Attributes

### OperationType
Type defining the general layout and operation of the door style.

### ConstructionType
Type defining the basic construction and material type of the door.

### ParameterTakesPrecedence
The Boolean value reflects, whether the parameter given in the attached lining and panel properties exactly define the geometry (TRUE), or whether the attached style shape take precedence (FALSE). In the last case the parameter have only informative value.

### Sizeable
The Boolean indicates, whether the attached _IfcMappedRepresentation_ (if given) can be sized (using scale factor of transformation), or not (FALSE). If not, the _IfcMappedRepresentation_ should be _IfcShapeRepresentation_ of the _IfcDoor_ (using _IfcMappedItem_ as the _Item_) with the scale factor = 1.
