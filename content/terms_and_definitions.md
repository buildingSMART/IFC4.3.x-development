# Terms, definitions, and abbreviated terms

For the purpose of this document, the following definitions apply.

## 3.1.1 actor

person, an organization, or person acting on behalf of an organization

> NOTE A specialization of the general term object.

## 3.1.2 attribute

definition from ISO iso 10303-11, chapter  9.2.1.
unit of information within an entity, defined by a particular type or reference to a particular entity

> NOTE There are three kinds of attributes: direct attributes, inverse attributes and derived attributes.

## 3.1.2.1 direct attribute

scalar values or collections including Set (unordered, unique), List (ordered), or Array (ordered, sparse) as defined in [ISO 10303-11]

> NOTE Similar to the term "field" in common programming languages.

## 3.1.2.2 inverse attribute

unit of information defining queries for obtaining related data and enforcing referential integrity

> NOTE Similar to the term "navigation property" in entity-relational programming frameworks.

## 3.1.2.3 derived attribute

unit of information computed from other attributes using an expression defined in the schema

## 3.1.2.4 constraints on attributes

data type restricting the values of attributes

> NOTE The most general constraint is about the existence of attribute values. There are basically two types: mandatory and optional attributes. Values of mandatory attributes must be provided whereas values of optional attributes may be omitted.

> NOTE For aggregation data types such as Set, List, or Array, the existence constraint is often refined by a minimal and maximal number of elements, which is also known as cardinality.

## 3.1.3 classification

categorization, the act of distributing things into classes or categories of the same type

## 3.1.4 constraint

restriction for a specified reason

> NOTE A specialization of the general term control.

## 3.1.5 control

directive to meet specified requirements such as for scope, time, or cost

> NOTE A specialization of the general term object.

## 3.1.6 dictionary

collection of words, terms or concepts, with their definition

## 3.1.7 element

tangible physical product that can be described by its shape representation, material representations, and other properties

> NOTE A specialization of the general term product.

## 3.1.7.1 element occurrence

element's position within the project coordinate system and its containment within the spatial structure

## 3.1.8 entity

class of information defined by common attributes and constraints as defined in ISO 10303-11

> NOTE Similar to the term "class" in common programming languages but describing data structure only (not behavior such as methods).

## 3.1.9 external reference

link to information outside the data set, with direct relevance to the specific information the link originates from inside the data set

## 3.1.10 feature

parametric information and additional property information modifying the shape representation of an element to which it applies

## 3.1.11 group

collection of information that fulfills a specified purpose

> NOTE A specialization of the general term object.

## 3.1.12 identification

capability to find, retrieve, report, change, or delete specific instances without ambiguity

## 3.1.13 instance

occurrence of an entity

> NOTE Similar to the term "instance of a class" in object oriented programming.

## 3.1.14 library

catalogue, database or holder of data, that is relevant to information in the data set

> NOTE It is information referenced from an external source that is not copied into the data set.

## 3.1.15 model

a data set, governed by the structure of an underlying schema, to meet certain data requirements

> NOTE  Information models and building information models are examples for a model.

> NOTE  In scope of this standard IFC models are populations of the IFC schema.

## 3.1.16 model view

subset of a schema, representing the data structure required to fulfill the data requirements within one or several exchange scenarios

> NOTE  Beside being a subset of a schema, a model view (or model view definition) may also impose additional constraints to the population of the subset schema

## 3.1.16.1 concept

rules on using a subset of the schema structure identified as a concept template to enable a certain functionality within the context of a concept root contained in a model view

> NOTE  The utilization of material definitions for a particular concept root representing a wall is an example of a concept.

## 3.1.16.2 concept template

the specification of a subset of the schema structure to enable a certain unit of functionality

> NOTE  The identification of the entities, attributes and constraints needed to express a material definition independently on how it is utilized later in the context of a wall is an example of a concept template.

## 3.1.16.3 concept root

an entity of a schema used to assign concepts to describe the required functionality

> NOTE  A root concept often describes a model element, such as wall, air outlet, construction task, or similar, that is the root of a graph of connected entities and attributes defining the specific information items required, such as geometry, material, breakdown structure, etc.

## 3.1.17 object

anything perceivable or conceivable that has a distinct existence, albeit not material

## 3.1.17.1 object occurrence

characteristics of an object as an individual

> NOTE Similar to "object", "instance", "individual" in other publications.

## 3.1.17.2 object type

common characteristics shared by multiple object-occurrences

> NOTE Similar to "class", "template", "type" in other publications.

## 3.1.18 process

object-occurrence located in time, indicating "when"

## 3.1.19 product

physical or conceptual object that occurs in space

> NOTE It is specialization of the general term object.

## 3.1.20 project

encapsulation of related information for a particular purpose providing context for information contained within

> NOTE Context information may include default measurement units or representation context and precision.

## 3.1.21 property

unit of information that is dynamically defined as a particular entity instance

> NOTE Similar to "late-bound" or "run-time" in programming terminology.

## 3.1.21.1 property occurrence

unit of information providing a value for a property identified by name

## 3.1.21.2 property template

metadata for a property including name, description, and data type

> NOTE Similar in concept to "extension property" in common programming languages.

## 3.1.21.3 property set occurrence

unit of information containing a set of property occurrences, each having a unique name within the property set

## 3.1.21.4 property set template

set of property templates serving a common purpose and having applicability to objects of a particular entity

> NOTE Similar in concept to "extension class" in common programming languages.

## 3.1.22 proxy

object that does not hold a specific object type information

> NOTE a specialization of object occurrence.

## 3.1.23 quantity

measurement of a scope-based metric, specifically length, area, volume, weight, count, or time

## 3.1.24 relationship

unit of information describing an interaction between items

## 3.1.25 representation

unit of information describing how an object is displayed, such as physical shape or topology

## 3.1.26 resource

entity with limited availability such as materials, labor, or equipment

> NOTE a specialization of the general term object.

> NOTE the "resource definition data schemas" section is unrelated to this concept.

## 3.1.27 schema

the definition of the structure to organize data for storage, exchange and sharing, using a formal language

> NOTE  The formal languages EXPRESS ISO 10303-11 and XML Schema W3C Recommendation are currently used to define the schemata of this standard

## 3.1.28 space

area or volume bounded actually or theoretically

> NOTE a specialization of the general term product.

## 3.1.29 type

basic information construct derived from a primitive, an enumeration, or a select of entities

> NOTE Similar to the "Type" construct as defined in ISO 10303-11.

> NOTE Similar in concept to "typedef" or "value type" in common programming languages.

## 3.1.29.1 select

construct that allows an attribute value to be one of multiple types or entities

> NOTE Similar to the "Select" construct as defined in ISO 10303-11.

> NOTE Similar to a "marker interface" in common programming languages.

## 3.1.29.2 enumeration

construct that allows an attribute value to be one of multiple predefined values identified by name

> NOTE Similar to the "Enumeration" construct as defined in ISO 10303-11.

> NOTE Similar in concept to "enum" in common programming languages.

## 3.1.30 deprecation

The act of marking a schema construct to be deleted in a future major release of this standard

> NOTE Complying interpreters shall still be able to import deprecated definitions.

> NOTE Complying interpreters shall consider to modify export using the proposed alternative definitions instead of the deprecated ones.

## 3.1.31 compatibility

## 3.1.31.1 backward compatibility

The ability for a data file, written against a previous release of the standard, to be readable by an application supporting a later version.

## 3.1.31.2 forward compatibility

The ability for a data file, written against a new release of the
standard, to still be readable by an application supporting a previous
version of the standard and for the reading application in this scenario not to lose functionality
provided by the earlier version of the standard.

> NOTE Forward compatibility is not explicitly considered in the development of this release, but seen as a desirable property where possible.

# 3.2 Abbreviated terms

* AEC: Architecture, Engineering, and Construction
* AEC-FM: Architecture, Engineering, Construction, and Facilities Management
* BIM: Building Information Modeling
* GUID: Globally Unique Identifier
* IFC: Industry Foundation Classes
* IFD: International Framework for Dictionaries
* MVD: Model View Definition
* SPF or SPFF: STEP Physical File
* STEP: STandard for the Exchange of Product data
* URI: Uniform Resource Identifier
* UUID: Universally Unique Identifier
* XML: Extensible Markup Language
