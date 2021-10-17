Element Interference
====================



```
concept {
    IfcElement:IsInterferedByElements -> IfcRelInterferesElements:RelatedElement
    IfcRelInterferesElements:RelatingElement -> IfcElement
    IfcRelInterferesElements:InterferenceGeometry -> IfcConnectionVolumeGeometry
    IfcRelInterferesElements:InterferenceType -> IfcIdentifier
    IfcConnectionVolumeGeometry:VolumeOnRelatingElement -> IfcSolidModel
}
```
