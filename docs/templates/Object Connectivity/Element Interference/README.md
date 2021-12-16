Element Interference
====================



```
concept {
    IfcElement_0:IsInterferedByElements -> IfcRelInterferesElements:RelatedElement
    IfcRelInterferesElements:RelatingElement -> IfcElement_1
    IfcRelInterferesElements:InterferenceGeometry -> IfcConnectionVolumeGeometry
    IfcRelInterferesElements:InterferenceType -> IfcIdentifier
    IfcConnectionVolumeGeometry:VolumeOnRelatingElement -> IfcSolidModel
}
```
