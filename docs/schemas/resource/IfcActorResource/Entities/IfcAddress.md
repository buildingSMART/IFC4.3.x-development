This abstract entity represents various kinds of postal and telecom addresses.

<!-- end of short definition -->


> NOTE Entity adapted from **address** defined in ISO 10303-41.

> HISTORY New entity in IFC1.5.1.

## Attributes

### Purpose
Identifies the logical location of the address.

### Description
Text that relates the nature of the address.

### UserDefinedPurpose
Allows for specification of user specific purpose of the address beyond the
enumeration values provided by Purpose attribute of type IfcAddressTypeEnum.
When a value is provided for attribute UserDefinedPurpose, in parallel the
attribute Purpose shall have enumeration value USERDEFINED.

### OfPerson
The inverse relationship to Person to whom address is associated.

### OfOrganization
The inverse relationship to Organization to whom address is associated.

## Formal Propositions

### WR1
Either attribute value Purpose is not given, or
when attribute Purpose has enumeration value USERDEFINED
then attribute UserDefinedPurpose shall also have a value.
