IfcBuiltSystem
==============
A built system is a group by which built elements are grouped according to a
common function within the facility.  
The group [_IfcBuiltSystem_]($element://{82D4F6FB-
FD80-404d-96F2-AF2FB5C64E6C}) defines the occurrence of a specialized system
for use within the context of a facilities physical or finishing fabric.
Important functionalities for the description of a built system are derived
from supertypes:  

  

  * From [_IfcSystem_]($element://{34E3790C-B8FF-41f1-B5A1-BD382C9DBD21}) it inherits the ability to couple the built system via [_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) to one or more [_IfcSpatialElement_]($element://{AFD1B7AF-F4A3-42ba-BF29-741A1DEBF281}) subtypes as necessary.
  

  * From [_IfcGroup_]($element://{9F87A6C3-BA39-40f1-A16E-48328E412EAF}) it inherits the inverse attribute IsGroupedBy, pointing to the relationship class [_IfcRelAssignsToGroup_]($element://{EE5D94CF-E3EB-49fc-8035-8D06C0925A2E}) . This allows the grouping of built elements (instances of [_IfcBuiltElement_]($element://{8ED417F7-860C-4172-9660-46F4EB8D97F3}) subtypes, [_IfcFurnishingElement_]($element://{28B94458-C9C9-46ee-A7C9-809447C745E5}) subtypes, [_IfcElementAssembly_]($element://{37A21453-AB05-44b6-8887-DD9BF7647B60}) and [_IfcTransportElement_]($element://{9CF73480-06BE-4997-B578-8F3958E77111})).
  

  * From [_IfcObjectDefinition_]($element://{82D54863-CD3F-4127-90A2-82628ECFBDC9}) it inherits the inverse attribute IsDecomposedBy pointing to the relationship class [_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}). It provides the hierarchy between the separate (partial) building systems.
  


