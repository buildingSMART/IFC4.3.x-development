# IfcPerformanceHistory

_IfcPerformanceHistory_ is used to document the actual performance of an occurrence instance over time. It includes machine-measured data from building automation systems and human-specified data such as task and resource usage. The data may represent actual conditions, predictions, or simulations.

The realtime data tracked by performance history takes the form of property sets where all properties are based on time series. Unlike design-based data at occurrences and types, performance-driven data is time-sensitive and may change in realtime by some measurement device. Data may be captured at irregular intervals such as when values change beyond established thresholds, or at regular intervals of specified duration.

#### Declaration use definition
_IfcPerformanceHistory_ may be declared within a project using _IfcRelDeclares_ where _RelatingContext_ refers to the _IfcProject_ and _RelatedDefinitions_ includes the _IfcPerformanceHistory_. Default units (used for property sets) are indicated by the declaring project. Only top-level objects are declared; nested performance history objects (through _IfcRelNests_) do not participate in such relationship.

> HISTORY&nbsp; New entity in IFC2x2.

## Attributes

### LifeCyclePhase
Describes the applicable building life-cycle phase. Typical values should be DESIGNDEVELOPMENT, SCHEMATICDEVELOPMENT, CONSTRUCTIONDOCUMENT, CONSTRUCTION, ASBUILT, COMMISSIONING, OPERATION, etc.

### PredefinedType
Predefined generic type for a performace history that is specified in an enumeration.
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## Concepts

### Aggregation

IfcPerformanceHistory may be decomposed into components using IfcRelNests where RelatingObject refers to the enclosing IfcPerformanceHistory and RelatedObjects contains one or more IfcPerformanceHistory components. Composition indicates breakdown of further detail and may correspond to the hierarchy of objects it represents.



### Classification

IfcPerformanceHistory may be classified using IfcRelAssociatesClassification where RelatingClassification refers to an IfcClassificationReference indicating a classification notation. Such classification notation may be used to identify the information such as an address within a building automation system, a work breakdown structure code for tasks, or a cost code for resource allocation.



### Control Assignment


### Property Sets for Performance

The property sets relating to this entity are defined by IfcPropertySet and attached by the IfcRelDefinesByProperties relationship. They are accessible by the IsDefinedBy inverse attribute. Applicable property sets are defined at assigned entities (primarily IfcDistributionElement subtypes) where IfcPropertySetTemplate.PropertySetType is PSET\_PERFORMANCEDRIVEN.


In addition to standard property sets defined within this specification, if the underlying information source provides metadata (specific type information), then custom property sets may capture such data, where corresponding IfcPropertySetTemplate and IfcPropertyTemplate objects may be defined for such information to be accessed by other applications.



