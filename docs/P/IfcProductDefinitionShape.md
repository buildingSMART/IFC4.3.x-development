IfcProductDefinitionShape
=========================
The _IfcProductDefinitionShape_ defines all shape relevant information about
an _IfcProduct_. It allows for multiple geometric shape representations of the
same product. The shape relevant information includes:  
  
* the shape representation including geometric representation items (for 3D solids, 2D annotations, etc.) and:   
* associated presentation information (line color, line type, surface rendering properties)  
* assignment to presentation layers (CAD layers for visibility control)   
* or the topological representation items for connectivity systems (vertex, edge, face representations) that may include geometric representation items (vertex points, edge curves, face surfaces)  
  
> NOTE  The definition of this entity relates to the ISO 10303 entity
> product_definition_shape. Please refer to ISO/IS 10303-41:1994 for the final
> definition of the formal standard.  
  
> HISTORY  New entity in IFC1.5  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcrepresentationresource/lexical/ifcproductdefinitionshape.htm)


Formal Propositions
-------------------
| Rule           | Description   |
|----------------|---------------|
| OnlyShapeModel |               |

Associations
------------
| Attribute       | Description   |
|-----------------|---------------|
| ShapeOfProduct  |               |
| HasShapeAspects |               |

