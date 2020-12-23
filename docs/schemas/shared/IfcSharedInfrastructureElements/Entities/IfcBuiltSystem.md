# IfcBuiltSystem

A built system is a group by which built elements are grouped according to a common function within the facility.
The group [<font color="#0000ff"><u>IfcBuiltSystem</u></font>]($element://{82D4F6FB-FD80-404d-96F2-AF2FB5C64E6C})  defines the occurrence of a specialized system for use within the context of a facilities physical or finishing fabric. Important functionalities for the description of a built system are derived from supertypes:
* From [<font color="#0000ff"><u>IfcSystem</u></font>]($element://{34E3790C-B8FF-41f1-B5A1-BD382C9DBD21}) it inherits the ability to couple the built system via [<font color="#0000ff"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) to one or more [<font color="#0000ff"><u>IfcSpatialElement</u></font>]($element://{AFD1B7AF-F4A3-42ba-BF29-741A1DEBF281}) subtypes as necessary.
* From [<font color="#0000ff"><u>IfcGroup</u></font>]($element://{9F87A6C3-BA39-40f1-A16E-48328E412EAF}) it inherits the inverse attribute IsGroupedBy, pointing to the relationship class [<font color="#0000ff"><u>IfcRelAssignsToGroup</u></font>]($element://{EE5D94CF-E3EB-49fc-8035-8D06C0925A2E}) . This allows the grouping of built elements (instances of [<font color="#0000ff"><u>IfcBuiltElement</u></font>]($element://{8ED417F7-860C-4172-9660-46F4EB8D97F3}) subtypes, [<font color="#0000ff"><u>IfcFurnishingElement</u></font>]($element://{28B94458-C9C9-46ee-A7C9-809447C745E5}) subtypes, [<font color="#0000ff"><u>IfcElementAssembly</u></font>]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) and [<font color="#0000ff"><u>IfcTransportElement</u></font>]($element://{9CF73480-06BE-4997-B578-8F3958E77111})).
* From [<font color="#0000ff"><u>IfcObjectDefinition</u></font>]($element://{82D54863-CD3F-4127-90A2-82628ECFBDC9}) it inherits the inverse attribute IsDecomposedBy pointing to the relationship class [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}). It provides the hierarchy between the separate (partial) building systems.

## Attributes

### PredefinedType


### LongName
Long name for a built system, used for informal purposes. It should be used, if available, in conjunction with the inherited Name attribute.
NOTE  In many scenarios the Name attribute refers to the short name or number of a built system, and the LongName refers to a descriptive name.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
