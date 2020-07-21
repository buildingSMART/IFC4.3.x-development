IfcPropertyDefinition
=====================
_IfcPropertyDefinition_ defines the generalization of all characteristics
(i.e. a grouping of individual properties), that may be assigned to objects.
Currently, subtypes of _IfcPropertyDefinition_ include property set
occurrences, property set templates, and property templates.  
  
* **Property set template** - _IfcPropertySetTemplate_, a collection of property templates that determine the definition of properties used within a project context.  
* **Property template** - _IfcPropertyTemplate_, a single template that determines the definition of a particular property used in the same project context. The template may determine the name, description, data type, the unit, or a standard expression for each property that is based on that template.  
* **Property set occurrence** - _IfcPropertySet_, a set of individual properties (that may or may not be determined by a property template) holding individual values, measure types and units, and are associated to an object occurrence or object type.  
  
> NOTE  The subtype hierarchy of _IfcPropertyDefinition_ also includes
> statically defined property sets as _IfcPreDefinedPropertySet_. Those are
> rarely used collections of fixed attributes combined in an entity
> definition. The _IfcPreDefinedPropertySet_ can not be determined by an
> _IfcPropertySetTemplate_.  
  
> NOTE  Individual properties, (subtypes of _IfcProperty_), are currently not
> included in the subtype hierarchy of _IfcPropertyDefinition_. This anomaly
> is due to upward compatibility reasons with earlier releases of this
> standard.  
  
Property definitions define information that is shared among multiple
instances of objects, either object occurrences or object types.
_IfcPropertyDefinition_''s (by their instantiable subtypes) can participate
within the following relationships:  
  
* **Assignment to a project context** - an _HasContext_ relationship to _IfcRelDeclares_ that establishes the project context in which this property definition is declared. This relationship is predominately applicable to subtypes of _IfcPropertyTemplateDefinition_.  
* **Association to external resources** - an _HasAssociation_ relationship to _IfcRelAssociates_ that refers to external sources of information (most notably a classification or document) and creates a uni-directional association. There is no dependency implied by the association.  
  
Subtypes are included in more specific relationships, see
_IfcPropertySetDefinition_ and _IfcPropertyTemplateDefinition_ for details.  
  
> HISTORY  New entity in IFC2.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcpropertydefinition.htm)


Associations
------------
| Attribute       | Description   |
|-----------------|---------------|
| HasContext      |               |
| HasAssociations |               |

