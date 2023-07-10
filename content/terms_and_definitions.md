# Terms, definitions, and abbreviated terms TL

For the purpose of this document, the following definitions apply.

## actor

person, organization or organizational unit involved in a process

[SOURCE: ISO 29841-1:2016, 3.1, modified - The words “such as a department, team, etc.” have been removed.]

## attributes

### attribute

essential traits, qualities, or properties of an entity

Note 1 to entry:  An attribute declaration establishes a relationship between the entity data type and the data type referenced by the attribute.

[SOURCE: ISO 10303-11:2004, 9.2.1, modified - Definition and Note 1 to entry adapted from normative text.]

### derived attribute

\<data modelling\> attribute whose value is computed in some manner

[SOURCE: ISO 10303-11:2004, 9.2.1 - Definition adapted from normative text.]

### explicit attribute

\<data modelling\> attribute whose value shall be supplied by an implementation in order to create an entity instance

[SOURCE: ISO 10303-11:2004, 9.2.1 - Definition adapted from normative text]

### inverse attribute

\<data modelling\> attribute whose value consists of the entity instances that use the entity in a particular role

[SOURCE: ISO 10303-11:2004, 9.2.1 - Definition adapted from normative text]

## building information modelling

use of a shared digital representation of an asset to facilitate design, construction and operation processes to form a reliable basis for decisions

[SOURCE: ISO 29481‑1:2016, 3.2, modified - The words “built object” have been replaced with “asset”. The words “including buildings, bridges, roads, process plants, etc.” have been removed. Note 1 to entry has been removed.]

## classification

act of assigning objects to classes according to criteria

[SOURCE: ISO 22274:2013, 3.5, modified - The word "process" has been replaced by "act"]

## classification system

systematic collection of classes organized according to a known set of rules, and into which objects may be grouped

[SOURCE: ISO 22274:2013, 3.6, modified - Note 1 to entry has been removed. The examples have been removed.]

## compatibility

### backward compatibility

ability for an exchange structure, written against a previous release of a specification, to be readable by an application supporting a later version

### forward compatibility
upward compatibility

ability for an exchange structure, written against a new release of a specification, to still be readable by an application supporting a previous version

Note 1 to entry:  The reading application should not lose functionality provided by the earlier version of the standard.

Note 2 to entry:  Forward compatibility may not be considered explicitly in development of this standard but seen as a desirable property where possible.

## concepts

### concept

unit of knowledge created by a unique combination of characteristics

[SOURCE: ISO 5127:2017, 3.1.1.02]

### concept root

entity to which the concept template is applied

Note 1 to entry:  The concept root is the root of a graph of connected entities and attributes.

EXAMPLE   A root concept representing a wall, air outlet, or construction task is the root of a graph of connected entities and attributes, representing e.g., geometry, material, or breakdown structure.

### concept template
unit of functionality

collection of objects and their relationships that defines one concept such that removal of any component would render the concept incomplete or ambiguous

EXAMPLE  An example of a concept template in the context of a concept root, such as a wall, would consist of the collection of all entities and attributes required to specify a material definition independently of how it is utilized later.

[SOURCE: ISO 10303-1:2021, 3.1.61, modified - unit of functionality used as admitted term, replaced "application objects and their relationships" by "entities and attributes", words "within the application context" removed, Example added]

### concept usage

use of a concept template in context of a concept root

Note 1 to entry:  The use of a concept template may include applying constraints to its usage.

EXAMPLE  The use of a concept template for material definitions for a particular concept root representing a wall.

## constraint

adaptation of a data type that restricts its range or operations

[SOURCE: ISO 2382:2015, 2122397]

## control

regulation of variables within specified limits

Note 1 to entry: Variables include scope, time and cost

## data dictionary

database that contains metadata

[SOURCE: ISO 12006-3:2022, 3.1]

## data types

### data type

domain of values

[SOURCE: ISO 10303-11:2004, 3.3.5, modified - The word "a" was removed.]

### enumeration data type

data type having as its domain a set of names

[SOURCE: ISO 10302-11:2004, 8.4.1, modified - Definition adapted from normative text]

### select data type

data type that enables a choice among several named data types

[SOURCE: ISO 10302-11:2004, 8.4.2, modified - Definition adapted from normative text]

## deprecation

act of marking a schema construct to be deleted in a future major release of a specification

Note 1 to entry:  Complying interpreters shall still be able to import deprecated definitions.

Note 2 to entry:  Complying interpreters shall consider modifying export using the proposed alternative definitions instead of the deprecated ones.

## element

physical object with a stated function, form and position

## entity

class of information defined by common properties

[SOURCE: ISO 10303-11:2004, 3.3.6]

## external reference

locator for referencing information stored outside of the populated schema

## exchange structure

computer-interpretable format used for storing, accessing, transferring, and archiving data

[SOURCE: ISO 10303-1:2021, 3.1.36]

## facility
built asset

physical structure, including the related site, serving one or more main purposes

[SOURCE: ISO 12911:2012, 3.9, modified - The words "related site works" have been replaced with "the related site". The admitted term "built asset" has been added.]

## feature

parametric information and additional property information modifying the shape representation of an element to which it applies

## group

named collection of objects

Note 1 to entry: collection of objects that are semantically related under consideration of a particular purpose

## identification

act of recognizing an object in a particular domain as distinct from other objects

[SOURCE: ISO 24760-1:2011, 3.2.1, modified - the word "entity" has been replaced with "object" and the word "process" with "act".]

## information

meaningful data

[SOURCE: ISO 9000:2015, 3.8.2]  

## instance

\<data modelling\> named value

[SOURCE: ISO 10303-11:2004, 3.3.10]

## library

catalogue, database or holder of data, that is relevant to information in the data set

Note 1 to entry:  It is information referenced from an external source that is not copied into the data set.

## model
population

\<data modeling\> collection of entity data type instances.

Note 1 to entry: In scope of this standard models are populations of the ISO 16739-1 schema.

[SOURCE ISO 10303-11:2004, 3.3.16, modified - Note 1 to entry added]

## model

\<information management\>  description of the organization of data in a manner that reflects an information structure

Note 1 to entry: Information models and building information models are examples of a model.

[SOURCE: ISO 5127:2017, 3.1.13.33, modified - Note 1 to entry added]

## model view definition

subset of a schema satisfying particular data requirements

Note 1 to entry:  The particular data requirements may be stated within one or several exchange requirements

Note 2 to entry:  Beside being a subset of a schema, a model view definition may also impose additional constraints to the population of the subset schema

## object

any part of the perceivable or conceivable world

Note 1 to entry: An object is something abstract or physical toward which thought, feeling, or action is directed.

[SOURCE: ISO 12006-2:2015, 3.1.1]

## occurrence

use of a typical item at a specific place in a design

Note 1 to entry: Each occurrence is a separate item that refers to the typical item.

EXAMPLE  Chairs are catalogue items. One instance of the chair type, such as the Le Corbusier LC2 chair, is a typical item. Four instances of individual occurrences of the Le Corbusier LC2 chair are part of an interior design of the entrance hall and each has an individual placement in space.

[SOURCE: 10303-212:2001, 3.7.13, modified - The sentence "Each occurrence is a separate item that refers to the typical item." has been removed from the definition and added as a Note to entry. EXAMPLE has been replaced by another example from the construction domain.]

## process

set of interrelated or interacting activities that use inputs to deliver an intended result

[SOURCE: ISO 9000:2015, 3.4.1, modified - The notes to entry have been removed.]

## product

thing or substance produced by a natural or artificial process

EXAMPLE  Products that are not a physical thing or substance, but that have information and location are included, such as alignments or grids.

[SOURCE: ISO 10303-1:2021, 3.1.49, modified - EXAMPLE has been replaced by another example from the construction domain.]

## project

\<data modelling\> context information for data sets according to schema

Note 1 to entry: Context information may include default units, representation context and precision.

## project

\<construction\>  unique process, consisting of a set of coordinated and controlled activities undertaken to achieve an objective

[SOURCE: ISO 9000:2015, 3.4.2, modified — reference to characteristics related to timing, requirements, costs and resources was deleted and Notes to entry were deleted.]

## property

defined characteristic suitable for the description and differentiation of an object

[SOURCE: ISO 22274:2013, 3.25, modified - The words "the objects in a class" have been replaced with "an object". The Example has been removed.]

## property set

named set of properties grouped under some characteristics

## proxy

object that does not hold a specific object type information

## quantity

property of a phenomenon, body, or substance, where the property has a magnitude that can be expressed by means of a number and a reference

EXAMPLE Length, area, volume, weight, count, or time are typical examples for a quantity

[SOURCE: ISO 80000-1:2009, 3.1, modified - The notes to entry have been removed, Example has been added.]

## quantity value

number and reference together expressing magnitude of a quantity

[SOURCE: ISO 80000-1:2009, 3.19, modified - Examples have been removed. Notes to entry have been removed.]

## relationship

connection between two or more entities

[SOURCE: ISO 5127:2017, 3.1.1.12, modified - The word "intelligent" has been removed.  The word "elements" has been replaced with "entities".]

## representation

organized collection of associated data elements, collected together for one or more specific uses

EXAMPLE  geometric shapes or topological items are examples of data elements to be used in graphical representations

[SOURCE: ISO 10303-43:2018]

## resource

object used in a process to achieve a result

[SOURCE: ISO 12006-2:2015, 3.2.5, modified - The term "resource" is used as the preferred term. The words "construction object", "construction process" and "construction results" have been replaced with "object", "process" and "results" respectively.]

## schema

definition of the structure to organize data for storage, exchange and sharing, using a formal language

Note 1 to entry: The formal languages ISO 10303-11 EXPRESS and W3C XML Schema Definition Language are currently used to define the schemata of this standard.

## space

limited three-dimensional extent defined physically or notionally

[SOURCE: ISO 12006-2:2015, 3.1.8]

## template

structure for specifying a property definition

# Abbreviated terms

* AEC: Architecture, Engineering, and Construction
* AEC-FM: Architecture, Engineering, Construction, and Facilities Management
* BIM: Building Information Modeling
* GUID: Globally Unique Identifier
* IFC: Industry Foundation Classes
* IFD: International Framework for Dictionaries
* MVD: Model View Definition
* SPF or SPFF: STEP Physical File
* STEP: Standard for the Exchange of Product data
* URI: Uniform Resource Identifier
* UUID: Universally Unique Identifier
* XML: Extensible Markup Language
