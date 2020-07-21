IfcOwnerHistory
===============
_IfcOwnerHistory_ defines all history and identification related information.
In order to provide fast access it is directly attached to all independent
objects, relationships and properties.  
  
_IfcOwnerHistory_ is used to identify the creating and owning application and
user for the associated object, as well as capture the last modifying
application and user.  
  
> HISTORY  New entity in IFC1.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  ChangeAction is now optional and a related WHERE rule enforces
> conditions when it is asserted.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. If LastModifiedDate is defined but ChangeAction is not asserted, then the
state of ChangeAction is assumed to be UNDEFINED.  
2\. If both LastModifiedDate and ChangeAction are asserted, then the state of
ChangeAction applies to the value asserted in LastModifiedDate.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcutilityresource/lexical/ifcownerhistory.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| State            | Enumeration that defines the current access state of the object.                                                                                                                                                                         |
| ChangeAction     | Enumeration that defines the actions associated with changes made to the object.                                                                                                                                                         |
| LastModifiedDate | Date and Time expressed in UTC (Universal Time Coordinated, formerly Greenwich Mean Time or GMT) at which the last modification was made by LastModifyingUser and LastModifyingApplication.                                              |
| CreationDate     | The date and time expressed in UTC (Universal Time Coordinated, formerly Greenwich Mean Time or GMT) when first created by the original OwningApplication. Once defined this value remains unchanged through the lifetime of the entity. |

Formal Propositions
-------------------
| Rule                | Description   |
|---------------------|---------------|
| CorrectChangeAction |               |

Associations
------------
| Attribute                | Description   |
|--------------------------|---------------|
| LastModifyingUser        |               |
| OwningUser               |               |
|                          |               |
| OwningApplication        |               |
| LastModifyingApplication |               |

