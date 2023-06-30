Surface Feature Adherence
=========================

An adherence indicates an external part composition relationship between the hosting structure, referred to as the "host", and the adhered components, referred to as the "adhering elements". The concept of adherence is used in various ways, examples are:

- Adherence is used on built elements to adhere surface features which modify the hosting element in the form of markings, surface treatments or defects.

Adherence is a bi-directional relationship, the relationship from hosting structure to its attached components is called adherence, and the relationship from the components to their hosting structure is called hosting.

```
concept {
    IfcElement:HasSurfaceFeatures -> IfcRelAdheresToElement:RelatingElement
    IfcRelAdheresToElement:RelatedSurfaceFeatures -> IfcSurfaceFeature
    IfcSurfaceFeature:Name -> IfcLabel
    IfcElement:HasSurfaceFeatures[binding="HasSurfaceFeatures"]
    IfcRelAdheresToElement:RelatedSurfaceFeatures[binding="RelatedSurfaceFeatures"]
    IfcSurfaceFeature:Name[binding="SurfaceFeatureName"]
}
```
