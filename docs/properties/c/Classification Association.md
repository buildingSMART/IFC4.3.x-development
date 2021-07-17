Classification Association
==========================

The concept _Classification Association_ describes how objects and object types can be further described by associating references to external sources of information. The source of information can be:

* a classification system;
* a dictionary server;
* any external catalogue that classifies the object further;
* any service that combine the above features.

An individual item within the external source of information can be selected. It then applies the inherent meaning of the item to the _IfcObject_ or _IfcTypeObject_.

> NOTE&nbsp; The classification system or dictionary server that is used within the project itself can also be indicated at the level of _IfcProject_ or _IfcProjectLibrary_ either as an external source, or copied with all relevant classification items into the project data. Use the concept _Project Classification Information_ to utilize this functionality.

The main attributes to be provided for a _Classification Association_ are:

* _Identification_: holds the key provided for a specific references to classification items (or tables)
* _Name_: allows for a human interpretable designation of a classification notation
