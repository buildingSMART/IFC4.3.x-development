IfcSharedFacilitiesElements
===========================

The _IfcSharedFacilitiesElements_ schema defines basic concepts in the facilities management (FM) domain. This schema, along with _IfcProcessExtension_ and _IfcSharedMgmtElements_, provide a set of models that can be used by applications needing to share information concerning facilities management related issues.

The _IfcSharedFacilitiesElements_ schema supports ideas including:

* Furniture.
* Grouping of elements of system furniture into individual furniture items.
* Asset identification.
* Inventory of objects (including asset, furniture and space objects within separate inventories).

### 6.4.1.1 Furniture and System Furniture
In the _IfcProductExtension_ schema, the _IfcElement_ entity is decomposed into a number of subtypes. One of these is the _IfcFurnishingElement_ entity from the _IfcFurniture_ and _IfcSystemFurnitureElement_ entities are derived.

Figure 1 illustrates a furniture object (instance of the _IfcFurniture_ entity, which is considered to be a discrete item of furniture in its own right (for example, a table or chair).

![Furniture](../../../../figures/ifcsharedfacilitieselements-fig01.gif)

Figure 1 - Furniture

Figure 2 illustrates a system furniture element object (instance of the _IfcSystemFurnitureElement_ entity), which is an identifiable item (such as a modesty panel, side, or desktop) that participates in the assembly of a discrete item of furniture.

![SystemFurnitureElements](../../../../figures/ifcsharedfacilitieselements-fig02.gif)

Figure 2 &mdash; System furniture element

Each _IfcFurniture_ object and each _IfcSystemFurnitureElement_ object is of a particular type. It may be a chair, desk, table etc for discrete furniture or modesty panel, side panel, desktop etc. for system furniture. Specification of the type is left to the user of the application providing the information. For applications however, there are a number of predefined property sets for types of furniture that can be assigned to furniture objects. Other property sets may be defined as necessary.

### 6.4.1.2 Asset Identification
An _IfcAsset_ allows for the grouping of objects to form a unit that has an identifiable financial value and/or upon which specific facilities management operations take place, as shown in Figure 3.

Each asset carries a unique identifier, cost, ownership,location and other information that is required.

![Assets](../../../../figures/ifcsharedfacilitieselements-fig03.gif)

Figure 3 &mdash; Asset identification

### 6.4.1.3 Inventory
An _IfcInventory_ provides a list of objects of a particular type, the type of objects that are contained being identified by the _IfcInventoryTypeEnum_.

Each inventory has one or more responsible persons and an organizational jurisdiction (which is valuable in facilities management situations where more than one functional group or organization is concerned).
