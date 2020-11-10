IfcDistributionSystem
=====================
A distribution system is a network designed to receive, store, maintain,
distribute, or control the flow of a distribution media. A common example is a
heating hot water system that consists of a pump, a tank, and an
interconnected piping system for distributing hot water to terminals.  
The group
[_IfcDistributionSystem_]($element://{4EDF40D6-B0CB-4feb-9A1A-2EAFA23D7E07})
defines the occurrence of a specialized system for use within the context of
building services or utilities for built facilities.  
Important functionalities for the description of a distribution system are
derived from existing IFC entities:  

  

  * From [_IfcSystem_]($element://{34E3790C-B8FF-41f1-B5A1-BD382C9DBD21}) it inherits the ability to couple the built system via [_IfcRelReferencedInSpatialStructure_]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC}) to one or more [_IfcSpatialElement_]($element://{AFD1B7AF-F4A3-42ba-BF29-741A1DEBF281}) subtypes as necessary.
  

  * From [_IfcGroup_]($element://{9F87A6C3-BA39-40f1-A16E-48328E412EAF}) it inherits the inverse attribute IsGroupedBy, pointing to the relationship class [_IfcRelAssignsToGroup_]($element://{EE5D94CF-E3EB-49fc-8035-8D06C0925A2E}) . This allows the grouping of distribution elements (instances of [_IfcDistributionElement_]($element://{D6FBAB6B-EDC4-4561-883E-6AD51D97F2F1}) subtypes).
  

  * From [_IfcObjectDefinition_]($element://{82D54863-CD3F-4127-90A2-82628ECFBDC9}) it inherits the inverse attribute IsDecomposedBy pointing to the relationship class [_IfcRelAggregates_]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}). It provides the hierarchy between the separate (partial) distribution systems. For example, an electrical main circuit may be aggregated into branch circuits.
  

  
HISTORY New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgserviceelements/lexical/ifcdistributionsystem.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType |                                                                                                                                                                                                                                                                                                                                          |
| LongName       | Long name for a distribution system, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.\X\0D> NOTE  In many scenarios the _Name_ attribute refers to the short name or number of a distribution system or branch circuit, and the _LongName_ refers to a descriptive name. |

