Project Context
===============

All project data sets shall contain a single _IfcProject_ instance indicating overall context and a directory of objects contained within. The context definition may include:

* the default units
* the geometric representation context for the shape representations
* the global positioning of the project coordinate system
* the reference to classification systems, or other external information sources, used
* the registry of object types and property templates used in the project context

```
concept {
    IfcContext:LongName -> IfcLabel_0
    IfcContext:ObjectType -> IfcLabel_1
    IfcContext:Phase -> IfcLabel_2
}
```
