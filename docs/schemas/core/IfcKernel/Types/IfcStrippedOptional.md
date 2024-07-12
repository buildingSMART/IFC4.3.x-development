# IfcStrippedOptional

IfcStrippedOptional is a type never to be instantiated in population models, but serves a purpose for compatibility of exchanged models.<!-- end of definition -->

IFC-SPF (Step Physical File; ISO 10303 part 21) depends on a fixed ordering of attributes defined solely in the schema and not in the model files. This has an impact in two cases:

- **partial schema production** - When certain trees of entities are out of scope given a certain exchange, and this exchange is formalized into an EXPRESS schema, entity attributes pointing to the types that are out of scope can be changed to be of type *OPTIONAL IfcStrippedOptional* to maintain an attribute order and count in the population model that is consistent with the full EXPRESS schema.

- **type deletion from the schema** - In rare cases, types are deleted from the schema with other entities still pointing to that type. In those cases, the entity attributes pointing to the deleted type can be changed to be of type *OPTIONAL IfcStrippedOptional* to maintain a backwards compatible attribute order and count in the population model.