IfcAddress
==========
This abstract entity represents various kinds of postal and telecom addresses.  
  
> NOTE  Entity adapted from **address** defined in ISO 10303-41.  
  
> HISTORY  New entity in IFC1.5.1.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcactorresource/lexical/ifcaddress.htm)


Attribute definitions
---------------------
| Attribute          | Description                                                                                                                                                                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfPerson           |                                                                                                                                                                                                                                                                                                                |
| OfOrganization     |                                                                                                                                                                                                                                                                                                                |
| Purpose            | Identifies the logical location of the address.                                                                                                                                                                                                                                                                |
| Description        | Text that relates the nature of the address.                                                                                                                                                                                                                                                                   |
| UserDefinedPurpose | Allows for specification of user specific purpose of the address beyond the \X\0Denumeration values provided by Purpose attribute of type IfcAddressTypeEnum. \X\0DWhen a value is provided for attribute UserDefinedPurpose, in parallel the \X\0Dattribute Purpose shall have enumeration value USERDEFINED. |

