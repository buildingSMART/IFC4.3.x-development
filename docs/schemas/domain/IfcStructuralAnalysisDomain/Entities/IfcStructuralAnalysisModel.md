# IfcStructuralAnalysisModel

The [<font color="#0000ff"><u>IfcStructuralAnalysisModel</u></font>]($element://{1B899CB5-DD4C-4100-B26A-99E0094966B9}) is used to assemble all information needed to represent a structural analysis model. It encompasses certain general properties (such as analysis type), references to all contained structural members, structural supports or connections, as well as loads and the respective load results.  
Important functionalities for the description of an analysis model are derived from existing IFC entities:  
* <font color="#ff0000">From </font>[<font color="#ff0000"><u>IfcSystem</u></font>]($element://{34E3790C-B8FF-41f1-B5A1-BD382C9DBD21})<font color="#ff0000">  it inherits the ability to couple the built system via </font>[<font color="#ff0000"><u>IfcRelReferencedInSpatialStructure</u></font>]($element://{415054A4-1479-4c32-9A58-BC1E36A488CC})<font color="#ff0000">  to one or more </font>[<font color="#ff0000"><u>IfcSpatialElement</u></font>]($element://{AFD1B7AF-F4A3-42ba-BF29-741A1DEBF281})<font color="#ff0000"> subtypes as necessary.</font>
* From [<font color="#0000ff"><u>IfcGroup</u></font>]($element://{9F87A6C3-BA39-40f1-A16E-48328E412EAF}) it inherits the inverse attribute IsGroupedBy, pointing to the relationship class [<font color="#0000ff"><u>IfcRelAssignsToGroup</u></font>]($element://{EE5D94CF-E3EB-49fc-8035-8D06C0925A2E}) . This allows the grouping of structural members (instances of [<font color="#0000ff"><u>IfcStructuralMember</u></font>]($element://{EF388B25-4C37-4c31-8553-114B0B092F4F})), and supports (instances of [<font color="#0000ff"><u>IfcStructuralConnection</u></font>]($element://{B049EAAC-BAE8-4a7f-B18A-3271643E6A08})) which belong to a specific analysis model.

  
NOTE Loads (as instances of [<font color="#0000ff"><u>IfcStructuralAction</u></font>]($element://{E1748344-9C82-4cf0-A02F-B5C648F5EBA6})) are not included through IsGroupedBy. Loads are assigned through the LoadedBy attribute relationship, using load groups as a grouping mechanism. Only top-level load groups should be referenced via LoadedBy, i.e. load combinations if any load combinations exist, or load cases if no load combinations exist in this analysis model.   
NOTE Results (as instances of [<font color="#0000ff"><u>IfcStructuralReaction</u></font>]($element://{B11145E2-897B-4ab5-A23E-6428AC873F3A})) are not included through IsGroupedBy. Results are assigned through the HasResults attribute relationship, using result groups as a grouping mechanism.  
* From [<font color="#0000ff"><u>IfcObjectDefinition</u></font>]($element://{82D54863-CD3F-4127-90A2-82628ECFBDC9}) it inherits the inverse attribute IsDecomposedBy pointing to the relationship class [<font color="#0000ff"><u>IfcRelAggregates</u></font>]($element://{12F56CBC-A6CE-493c-8A50-E301CE73BBA5}). It provides the hierarchy between the separate (partial) analysis models.

  
HISTORY New entity in IFC2x2.  
************Informal Propositions****  
1. If one or more structural item (instance of a subtype of [<font color="#0000ff"><u>IfcStructuralItem</u></font>]($element://{5566F63A-CEB6-4ae0-B44E-E1C7CD08B669})) is grouped into an [<font color="#0000ff"><u>IfcStructuralAnalysisModel</u></font>]($element://{1B899CB5-DD4C-4100-B26A-99E0094966B9}), the attribute SharedPlacement shall be provided with a value.
2. The [<font color="#0000ff"><u>ObjectPlacement</u></font>]($element://{F6C7F65A-37A7-43a0-A6F5-ECCEEBA0A061}) of all structural items which are grouped into the same instance of [<font color="#0000ff"><u>IfcStructuralAnalysisModel</u></font>]($element://{1B899CB5-DD4C-4100-B26A-99E0094966B9}) shall refer to the same instance of [<font color="#0000ff"><u>IfcObjectPlacement</u></font>]($element://{F6C7F65A-37A7-43a0-A6F5-ECCEEBA0A061}) as [<font color="#0000ff"><u>IfcStructuralAnalysisModel</u></font>]($element://{1B899CB5-DD4C-4100-B26A-99E0094966B9}).SharedPlacement.

  
NOTE This rule is necessary to achieve consistent topology representations. The topology representations of structural items in an analysis model are meant to share vertices and edges und must therefore have the same object placement.  
NOTE A structural item may be grouped into more than one analysis model. In this case, all these models must use the same instance of [<font color="#0000ff"><u>IfcObjectPlacement</u></font>]($element://{F6C7F65A-37A7-43a0-A6F5-ECCEEBA0A061}).

## Attributes

### PredefinedType


### OrientationOf2DPlane


### LoadedBy


### HasResults


### SharedPlacement


## Formal Propositions

### HasObjectType
The attribute ObjectType shall be given if the predefined type is set to USERDEFINED.
