IfcKernel
=========

The schema _IfcKernel_ defines the most abstract part or core part of the specification. It captures general constructs, that are basically founded by their different semantic meaning in common understanding of an object model, like object, property and relationship. Those are then specialized into non-AEC/FM specific constructs, like product, process, control and resource, which form the main entry points for the next level within the schema architecture, the Core Extension layer.

The _IfcKernel_ also specifies the basic attributes and relationships, such as relative location of products in space, sequence of processes in time, or general purpose grouping and nesting mechanism. It also lays the foundation of extensibility of specification by providing:

* proxy definitions;
* type object definitions;
* property set definitions;
* property set template definitions. 

#### 5.1.1.1 Root definition
Each entity defined outside of the Resource layer of the schema architecture inherits directly or indirectly from the _IfcRoot_ entity. _IfcRoot_ provides for the fundamental capabilities of:

* identification - assigning a globally unique identifier (the GUID)
* optional ownership and change information
* optional name and description attribution 

There are three fundamental entity types in the IFC model, which are all derived from _IfcRoot_. They form the first level of specialization within the entity hierarchy.

* object definitions are the generalization of any semantically treated thing (or item) within the IFC model.
* relationships are the generalization of all relationships among things (or items) that are treaded as objectified relationships between different entities
* property definitions are the generalization of all characteristics that may be assigned to object definitions.

#### 5.1.1.2 Object definitions
An object definition is the abstract supertype, _IfcObjectDefinition_, and stands for all physically tangible items, such as wall, beam or covering, physically existing items, such as spaces, or conceptual items, such as grids or virtual boundaries. It also stands for processes such as work tasks, for controls such as cost items, for resources such as labor resource, or for actors such as persons involved in the design process.

Object definitions are specialized into object occurrences, _IfcObject_, indicating any individual object in space, time or another representation context, into object types, _IfcTypeObject_ indicating the common definitions as a type, or article that are identical for all object occurrences, and basic project or library context, _IfcContext_.

An object and object type gets its information from the relationships in which it is involved. This includes the definition relationship to property information, or the typing relationship to assign an underlying object type to an object.

#### 5.1.1.3 Relationship definitions
Relationships are predominately being defined as the objectified relationship, _IfcRelationship_. The objectified relationship handles relationships among objects. This allows to keep relationship specific properties directly at the relationship object and to uncouple the relationship semantics from the object attributes.

The introduction of the objectified relationships also allows the development of a separate subtype tree for relationship semantics.

#### 5.1.1.4 Property definition
The property definition, _IfcPropertyDefinition_, is the generalization of all characteristics of objects. Shared among multiple object instances, it reflects the specific information of an object type, but it may also represent the occurrence information of the actual object in the project context, if it is assigned only to a single object instance.

The property definition gets applied to the objects using the concept of relationships.

#### 5.1.1.5 Object entity subtype tree
There are six fundamental entity types in the IFC model, which are all derived from _IfcObject_.

* products - are physical object (manufactured, supplied or created) for incorporation into a project. They may be physically existing or tangible. Products may be defined by shape representations and have a location in the coordinate space.
* processes - are actions taking place in a project with the intent of acquiring, constructing, or maintaining objects. Processes are placed in sequence in time.
* controls - are concepts that control or constrain other objects. Controls can be seen as guide, specification, regulation, constraint or other requirement applied to an object that has to be fulfilled.
* resources - are concepts that describe the use of an object mainly within a process.
* actors - are human agents that are involved in a project during its full life cycle.
* groups - are arbitrary collections of objects.

#### 5.1.1.6 Relationship entity subtype tree
There are sixfundamental relationship types in the IFC model, which are all derived from _IfcRelationship_. A relationship may have an informal purpose descriptor assigned, which denotes a particular purpose of applying this relationship.

* assignment - is a generalization of "link" relationships among instances of objects and its various subtypes. A link denotes the specific association through which one object (the client) applies the services of other objects (the suppliers), or through which one object may navigate to other objects.
* association - refers to external sources of information (most notably a classification, library or document) and associates it to objects or property definitions.
* decomposition - defines the general concept of elements being composed or decomposed. The decomposition relationship denotes a whole/part hierarchy with the ability to navigate from the whole (the composition) to the parts and vice versa.
* definition - uses a type definition or property set definition (seen as partial type information) to define the properties of the object instance. It is a specific - occurrence relationship 
* connectivity - handles the connectivity of objects. 
* declaration - handles the link between object definitions and property definitions and the declaring context.

#### 5.1.1.7 Property definition entity subtype tree
There are two fundamental concepts of property definition types, which are all derived from _IfcPropertyDefinition_.

* property and property set template - defines the syntax and data types for property sets and individual properties.
* property set occurrence - defines shareable and extensible property sets attachable to occurrences of objects. The property set is regarded as a partial type information as it establishes a subset of common shared property information among occurrence objects. 

> HISTORY&nbsp; New schema in IFC1.5
