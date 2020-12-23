# IfcProfileDef

_IfcProfileDef_ is the supertype of all definitions of standard and arbitrary profiles within IFC. It is used to define a standard set of commonly used section profiles by their parameters or by their explicit curve geometry.

* Parameterized profiles are 2D primitives, which are used within the industry to describe cross sections by a description of its parameters.
* Arbitrary profiles are cross sections defined by an outer boundary as bounded curve, which may also include holes, defined by inner boundaries.
* Derived profiles, based on a transformation of a parent profile, are also part of the profile definitions available.
* In addition composite profiles can be defined, which include two or more profile definitions to define the resulting profile.

> HISTORY&nbsp; New entity in IFC1.5, the capabilities have been extended in IFC2x. Profiles can now support swept surfaces and swept area solids with inner boundaries. It had been renamed from IfcAttDrivenProfileDef.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Changed from ABSTRACT to non-abstract for uses which do not require an explicitly defined geometry. Added inverse attributes _HasProperties_ and _HasExternalReference_.

**Use in material association**

Beams, columns, and similarly shaped building elements and their type objects may be associated with a section profile definition, combined with material definition, by means of _IfcRelAssociatesMaterial_ together with _IfcMaterialProfileSet_ and _IfcMaterialProfileSetUsage_. This way, building elements and element types with same section and material can share a common section profile definition and association.

The profile definition in material association is required to be consistent with shape representations of the respective building elements.

A higher-level description of spatial aligment of the section profile of a member (such as centered, bottom-left, in the geometric centroid, and more) can be provided within _IfcMaterialProfileSetUsage_ by means of a cardinal point reference. This can be used redundant to geometric data in order to convey design intent.

**Use in shape models**

Profile definitions are used within the geometry and geometric model resource to create either swept surfaces, swept area solids, or sectioned spines.

The purpose of the profile definition within the swept surfaces or swept area solids is to define a uniform cross section being swept:

* along a line (extrusion) using _IfcSurfaceOfLinearExtrusion_ or _IfcExtrudedAreaSolid_
* along a circular arc (revolution) using _IfcSurfaceOfRevolution_ or _IfcRevolvedAreaSolid_
* along a directrix lying on a reference surface using _IfcSurfaceCurveSweptAreaSolid_

The purpose of the profile definition within the sectioned spine is to define a varying cross sections at several positions along a spine curve. The subtype _IfcDerivedProfileDef_ is particularly suited to provide the consecutive profiles to be based on transformations of the start profile and thus maintaining the identity of vertices and edges.

> NOTE&nbsp; Subtypes of the _IfcProfileDef_ contain parameterized profiles (as subtypes of _IfcParameterizedProfileDef_) which establish their own 2D position coordinate system, profiles given by explicit curve geometry (either open or closed profiles) and two special types for composite profiles and derived profiles, based on a 2D Cartesian transformation.

An _IfcProfileDef_ is treated as bounded area if it is used within swept area solids. In this case, the inside of the profile is part of the profile. The attribute _ProfileType_ is set to AREA. An _IfcProfileDef_ is treated as a curve if it is used within swept surfaces. In this case, the inside of the profile (if the curve is closed) is not part of the profile. The attribute _ProfileType_ is set to CURVE.

Figure 1 illustrates use of parameterized profiles within a swept area solid.

<table><tr><td>
<table border="1" cellpadding="2" cellspacing="2" frame="border" width="100%">
  <tbody>
    <tr valign="top">
      <td align="left" valign="top" width="420">

<img src="../../../../figures/ifcprofiledef-layout1.gif" alt="Example of standard profile definition" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Position</u><br>
The <em>IfcProfileDef</em> is defined within the underlying
coordinate system which is defined by the swept surface or swept area solid
that uses the profile definition. It is the xy plane</p>

      <ul>
        <li>of <em>IfcSweptSurface.Position</em> or</li>
        <li>of <em>IfcSweptAreaSolid.Position</em> or</li>
        <li>of each list member of <em>IfcSectionedSpine.CrossSectionPositions</em>.</li>
      </ul>

<p>In the figure to the left, the z axis of the position coordinate system points outwards of the drawing plane.</p>

<p><font size="-1">Note: The subtype <em>IfcParameterizedProfileDef</em> optionally provides an additional 2D position coordinate system relative to the underlying coordinate system of the <em>IfcProfileDef</em>.</font></p>

      </td>
    </tr>
    <tr>
      <td width="420">

<img src="../../../../figures/ifcprofiledef-layout5.gif" alt="use within swept area solids" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Sweeping</u></p>

<p>In the later use of the <em>IfcProfileDef</em>
within the swept surface or swept area solid,&nbsp; e.g. the <em>IfcExtrudedAreaSolid</em>
(here used as an example), the profile boundaries (here based on the 2D
position coordinate system of <em>IfcParameterizedProfileDef</em>)
are placed within the xy plane of the 3D position coordinate system of
the swept surface or swept area solid.</p>

<p>The profile is inserted into the underlying coordinate system either:</p>

      <ul>
        <li>directly in case of using <em>IfcArbitraryClosedProfileDef</em>
        and <em>IfcArbitraryOpenProfileDef</em>,</li>

        <li>through an intermediate position coordinate system in case of
        using <em>IfcParameterizedProfileDef</em>.</li>

        <li>through an 2D Cartesian transformation operator (applied directly
        to the curve position when using arbitrary profile definitions,
        or applied to the position coordinate system when using parameterized
        profile definitions) in case of using <em>IfcDerivedProfileDef</em>.</li>

        <li>when using <em>IfcCompositeProfileDef</em> the insertion depends on
        the subtype of the included sub-profiles.</li>
      </ul>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Profile sweeping</p></td></tr>
</table>

**Profile types**

Results of the different usage of the _ProfileType_ attribute are demonstrated here. The _ProfileType_ defines whether the inside (the bounded area) is part of the profile definition (Area) or not (Curve). Figure 2 illustrates the resulting area or curve depending on _ProfileType_.

<table><tr><td>
<table border="1" cellpadding="2" cellspacing="2" frame="border" width="100%">
  <tbody>
    <tr>
      <td width="420">

<img src="../../../../figures/ifcprofiledef-layout3.gif" alt="area without thickness" height="225" width="300"><br>
ProfileType = AREA

      </td>
      <td align="left" valign="top">

<img src="../../../../figures/ifcprofiledef-layout4.gif" alt="closed curve" height="225" width="300"><br>
ProfileType = CURVE

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 2 &mdash; Profile types</p></td></tr>
</table>

**Profile specification by external reference**

If the profile is standardized by a norm or a catalogue, a reference to this norm or catalogue should be provided by means of _HasExternalReference_. This inverse relationship is used to associate an _IfcExternalReference_ (notably _IfcClassificationReference_ or _IfcLibraryReference_) with the profile.

_IfcClassificationReference_ is used to refer to a profile norm (a common standard or manufacturer's standard). In this case,

* _IfcClassificationReference.ItemReference_ contains the formal profile designation from the norm. (On the other hand, _IfcProfileDef.ProfileName_ contains a displayable name which may not necessarily be the same as the formal designation.)
* _IfcClassificationReference.Name_ carries the short name of the profile norm.
* Optionally, the norm can be further described by _IfcClassificationReference.ReferencedSource_.

_IfcLibraryReference_ is used to refer to a library which contains profile definitions. In this case,

* _IfcLibraryReference.ItemReference_ contains the identifier of the profile within the library and is meant to be machine-readable (in contrast to _IfcProfileDef.ProfileName_ which should be human-readable).
* _IfcLibraryReference.Location_ and ._Name_ or ._ReferencedLibrary_ further describe the library.

If an external reference is provided, sending systems shall ensure that the shape of the profile definition object agrees with the definitions in the referenced classification or library.

**Direct instances of _IfcProfileDef_**

Usually, only subtypes of _IfcProfileDef_ should be instantiated. In some special cases, e.g. if the profile object is used for purposes other than geometric models (e.g. for structural analysis models), it may be possible to directly instantiate _IfcProfileDef_ and further specify the profile only by external reference or by profile properties. The latter are tracked by the inverse attribute _HasProperties_.

## Attributes

### ProfileType
Defines the type of geometry into which this profile definition shall be resolved, either a curve or a surface area. In case of curve the profile should be referenced by a swept surface, in case of area the profile should be referenced by a swept area solid.

### ProfileName
Human-readable name of the profile, for example according to a standard profile table. As noted above, machine-readable standardized profile designations should be provided in _IfcExternalReference.ItemReference_.

### HasExternalReference
Reference to external information, e.g. library, classification, or document information, which is associated with the profile.
{ .change-ifc2x4}
> IFC4 CHANGE New inverse attribute

### HasProperties
Additional properties of the profile, for example mechanical properties.
{ .change-ifc2x4}
> IFC4 CHANGE New inverse attribute
