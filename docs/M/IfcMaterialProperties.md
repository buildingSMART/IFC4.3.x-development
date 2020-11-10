IfcMaterialProperties
=====================
The _IfcMaterialProperties_ assigns a set of material properties to associated
material definitions. The set may be identified by a _Name_ and a
_Description_. The _IfcProperty_ (instantiable subtypes) is used to express
the individual material properties by name, description, value and unit.  
  
> NOTE  The set of material properties can be assigned to an individual
> _IfcMaterial_, a set or composite of materials (_IfcMaterialConstituent_,
> _IfcMaterialConstituentSet_), or set or individual material layer
> (_IfcMaterialLayer_, _IfcMaterialLayerSet_), or a set or individual material
> profile (_IfcMaterialProfile_, _IfcMaterialProfileSet_)  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Entity made non-abstract. The subtypes
> IfcMechanicalMaterialProperties, IfcThermalMaterialProperties,
> IfcHygroscopicMaterialProperties, IfcGeneralMaterialProperties,
> IfcOpticalMaterialProperties, IfcWaterProperties, IfcFuelProperties,
> IfcProductsOfCombustionProperties, IfcExtendedMaterialProperties have been
> deleted, use _IfcMaterialProperties_ instead.  
  
  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmaterialresource/lexical/ifcmaterialproperties.htm)


Attribute definitions
---------------------
| Attribute   | Description   |
|-------------|---------------|
| Material    |               |

