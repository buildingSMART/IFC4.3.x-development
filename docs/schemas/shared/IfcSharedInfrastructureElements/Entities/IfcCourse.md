# IfcCourse

A built element whose length greatly exceeds its thickness and often also its width, usually of a single material laid on site on top of another horizontal or nearly horizontal built element. A course is distinctive from a earthworks element in that a course is a graded granular (which can be bound or unbound) material that is generally processed in some fashion, where as earthworks elements are soil earthen based structure that can be formed by removal and transport of general ground material.
Structurally a course does not have capacity to carry loads over open span, or to be removed or replaced as a single unit. examples of courses include:
* Graded aggregate layers
* Graded sand layers
* Cement bounded material (CBM)
* Asphalt layers

NOTE For road applications, the following types of courses were identified but not added to the schema model due to the fact that the elements (including terms and definitions) can vary greatly between nations; instead, these would be typical values of the inherited attribute ObjectType:

- **Paving** : Type of Course directly in contact with traffic loads e.g. in gravel road (also Surface layer or Wearing course).
- **AnticapillaryLayer** : Type of Course, layer preventing capillary rise of water from underlying layers. Definition from PIARC: Protective bottom layer with no fines, designed to prevent capillary rise of water from the subgrade soil or from underlying layers.
- **AntifreezingLayer** : Type of Course, layer intended to prevent frost from penetrating into the subgrade. Also: Frost blanket course.
- **BaseCourse** : A layer immediately beneath the surface of binder course providing additional load distribution and contributing to the sub-surface drainage.
- **BinderCourse** : A layer to distribute loads to the base course.
- **CappingLayer** : Top layer of subgrade to improve its load bearing capacity. Definition from PIARC: Optional layer of granular or treated material on top of the subgrade and immediately below formation level, to provide improved foundation for the subbase layer [CEN].
- **DrainingCourse** : Layer of pervious material to relieve pore pressure or facilitate drainage of overlying layers.
- **TackCoat** : A thin coating of tar or asphalt applied before a road is laid to form an adhesive bond.
- **LayingCourse** : Type of Course, layer of material providing a bed for which block (stone) paving.
- **RegulatingCourse** : Type of Course, layer of variable thickness for adjusting a surface so meet specified even level. Also: Levelling course. Definition from PIARC: Course of variable thickness applied to an existing course or surface to provide the necessary profile for a further course of constant thickness (CEN).
- **Sealing** : A layer of impermeable material.
- **SubBaseCourse** : A layer between subgrade and base course. Definition from PIARC: Layer or layers of specified or selected material of designed thickness placed on a subgrade to support a base layer (or a cement concrete slab in the case of rigid pavements).
- **SeparationLayer** : A layer intended to prevent mixing of material from above layer with fine material or water in layer below. Definition from PIARC: Layer of material designed to prevent the ascent of water or fines from a lower layer.
- **AnticrackingLayer** : A layer intended to isolate surface layers from cracking in lower layer. Definition from PIARC Layer intended to prevent the reflection of cracks from a lower layer to the surface.
- **PrimeCoat** : An application of a low viscosity asphalt to a granular base in preparation for an initial layer of asphalt.
- **VergeFill** : Soft shoulder between paved surface and side slope.

## Attributes

### PredefinedType
Identifies the predefined type of a course element. This type may associate additional specific property sets.
NOTE  The PredefinedType shall only be used, if no _IfcCourseType_ is assigned, providing its own _IfcCourseType_.PredefinedType.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcCourseType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCourseType_.
