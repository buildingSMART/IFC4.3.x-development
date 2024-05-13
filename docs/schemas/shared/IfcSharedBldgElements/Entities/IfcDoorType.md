# IfcDoorType

The element type _IfcDoorType_ defines commonly shared information for occurrences of doors. The set of shared information may include:

* common properties within shared property sets
* common material information
* common operation type definitions
* common shape representations
<!-- end of definition -->
A door type defines the particular parameter of the lining and one (or several) panels through the _IfcDoorLiningProperties_ and the _IfcDoorPanelProperties_ as predefined property sets applicable to doors only.

It is used to define a door specification, or door style (i.e. the specific product information that is common to all occurrences of that door type). Door types may be exchanged without being already assigned to occurrences.

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

Occurrences of the _IfcDoorType_ within building models are represented by instances of _IfcDoor_.

> HISTORY  New entity in IFC4. The entity _IfcDoorType_ replaces the previous definition _IfcDoorStyle_ (which is deprecated in IFC4).

## Attributes

### PredefinedType


### OperationType
Type defining the general layout and operation of the door type in terms of the partitioning of panels and panel operations.

### ParameterTakesPrecedence
The Boolean value reflects, whether the parameter given in the attached lining and panel properties exactly define the geometry (TRUE), or whether the attached style shape take precedence (FALSE). In the last case the parameter have only informative value. If not provided, no such information can be inferred.

### UserDefinedOperationType
Designator for the user defined operation type, shall only be provided, if the value of _OperationType_ is set to USERDEFINED.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Door Type Attributes



### Property Sets for Types

Two subtypes of _IfcPreDefinedPropertySet_ are applicable to _IfcDoorType_:

* _IfcDoorLiningProperties_ - a single instance to define the shape parameters of the door lining
* _IfcDoorPanelProperties_ - one or several instances to define the shape parameters of the door panel(s)

### Type Body Geometry



