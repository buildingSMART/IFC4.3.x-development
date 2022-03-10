A conforming software application is required to support a well defined Model View Definition (MVD) of the data schema and referenced data. A particular model view definition is defined to support one or many recognized work flows in the building construction and facility management industry sector. Each work flow identifies data exchange requirements that are to be supported by the conforming software applications.

buildingSMART International publishes official model view definitions and exchange requirements as related specifications. The official website for publication of this specification, related model view definitions and exchange requirements, and supporting materials such as implementer agreements, example data sets, references to development tools, discussion forum and issue database, and certification programs is [technical.buildingsmart.org](https://technical.buildingsmart.org). The documentation is deposited at [standards.buildingsmart.org](https://standards.buildingsmart.org).

The IFC specification includes terms, concepts and data specification items that originate from use within disciplines, trades, and professions of the construction and facility management industry sector. Terms and concepts uses the plain English words, the data items within the data specification follow a naming convention.

* the data item names for types, entities, rules and functions start with the prefix "Ifc" and continue with the English words in CamelCase naming convention (no underscore, first letter in word in upper case);
* the attribute names within an entity follow the CamelCase naming convention with no prefix;
* the property set definitions that are part of this standard start with the prefix "Pset_" and continue with the English words in CamelCase naming convention;
* the quantity set definitions that are part of this standard start with the prefix "Qto_" and continue with the English words in CamelCase naming convention.
  
The data schema architecture of IFC defines four conceptual layers, each individual schema is assigned to exactly one conceptual layer. The figure below shows the schema architecture IFC 4 layered architecture.

![Figure 1 — Data schema architecture with conceptual layers](https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/b3911e98eaf9adc5287c41d2e55beda1688be5d6/content/IFC4_layered_architecture.png)

1. **Resource layer** — the lowest layer includes all individual schemas containing resource definitions, those definitions do not include an globally unique identifier and shall not be used independently of a definition declared at a higher layer;
2. **Core layer** — the next layer includes the kernel schema and the core extension schemas, containing the most general entity definitions, all entities defined at the core layer, or above carry a globally unique id and optionally owner and history information;
3. **Interoperability layer** — the next layer includes schemas containing entity definitions that are specific to a general product, process or resource specialization used across several disciplines, those definitions are typically utilized for inter-domain exchange and sharing of construction information;
4. **Domain layer** — the highest layer includes schemas containing entity definitions that are specializations of products, processes or resources specific to a certain discipline, those definitions are typically utilized for intra-domain exchange and sharing of information.
