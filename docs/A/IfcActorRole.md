IfcActorRole
============
This entity indicates a role which is performed by an actor, either a person,
an organization or a person related to an organization.  
  
> NOTE  The list of roles of the enumeration values of the _Role_ attribute
> can never be complete. Therefore using enumeration value USERDEFINED, the
> user can provide any role as a value of the attribute _UserDefinedRole_.  
  
> NOTE  Entity adapted from **organization_role** and **person_role** defined
> in ISO 10303-41.  
  
> HISTORY  New entity in IFC1.5.1.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcactorresource/lexical/ifcactorrole.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasExternalReference |                                                                                                                                                                                                                                                                             |
| Role                 | The name of the role played by an actor. If the Role has value USERDEFINED, then\X\0Dthe user defined role shall be provided as a value of the attribute UserDefinedRole.                                                                                                   |
| UserDefinedRole      | Allows for specification of user defined roles beyond the \X\0Denumeration values provided by Role attribute of type IfcRoleEnum. \X\0DWhen a value is provided for attribute UserDefinedRole in parallel \X\0Dthe attribute Role shall have enumeration value USERDEFINED. |
| Description          | A textual description relating the nature of the role played by an actor.                                                                                                                                                                                                   |

