# IfcOrganization

A named and structured grouping with a corporate identity.

> NOTE&nbsp; The relationships between _IfcOrganization_'s, like between department within a company, can be expressed using the objectified relationship _IfcOrganizationRelationship_.

> NOTE&nbsp; Entity adapted from **organization** defined in ISO&nbsp;10303-41.

> HISTORY&nbsp; New entity in IFC1.5.1.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute 'Id' renamed to _Identification_.

## Attributes

### Identification
Identification of the organization.

### Name
The word, or group of words, by which the organization is referred to.

### Description
Text that relates the nature of the organization.

### Roles
Roles played by the organization.

### Addresses
Postal and telecom addresses of an organization.
> NOTE&nbsp; There may be several addresses related to an organization.

### IsRelatedBy
The inverse relationship for relationship RelatedOrganizations of IfcOrganizationRelationship.

### Relates
The inverse relationship for relationship RelatingOrganization of IfcOrganizationRelationship.

### Engages
Inverse relationship to IfcPersonAndOrganization relationships in which IfcOrganization is engaged.
