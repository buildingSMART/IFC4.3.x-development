# IfcDerivedProfileDef

_IfcDerivedProfileDef_ defines the profile by transformation from the parent profile. The transformation is given by a two dimensional transformation operator. Transformation includes translation, rotation, mirror and scaling. The latter can be uniform or non uniform. The derived profiles may be used to define swept surfaces, swept area solids or sectioned spines.

The transformation effects the position, rotation, mirroring or scale of the profile at the underlying coordinate system, i.e. the coordinate system defined by the swept surface or swept area solid that uses the profile definition. It is the xy plane of either:

* _IfcSweptSurface.Position_
* _IfcSweptAreaSolid.Position_

or in case of sectioned spines the xy plane of each list member of _IfcSectionedSpine.CrossSectionPositions_. The position and potential rotation of the _ParentProfile_ within the underlying coordinate system is taken into consideration before applying the Cartesian transformation operator.

Note, if only mirroring is required, _IfcMirroredProfileDef_ should be used instead.

> HISTORY&nbsp; New entity in IFC2x.

Figure 1 illustrates examples of derived profiles.

<table>
<tr><td>
<table border="1" cellpadding="2" cellspacing="2">
  <tbody>
    <tr>
      <td align="left" valign="top" width="405">

<img src="../../../../../../figures/ifcderivedprofiledef-layout1.gif" alt="uniform" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em>
is defined using the <em>IfcCartesianTransformationOperator2D</em>
(CTO), which is applied to the parent profile definition. <br>
</p>

<p><u>Example</u><br>
The example shows an uniform scaling and a transformation
of an <em>IfcRectangleProfileDef</em>
to match the lower-left cardinal point. The attributes of the CTO are:<br>
</p>

      <blockquote><tt>Axis1 = NIL (defaults to 1.,0.)<br>
      Axis2 = NIL (defaults to 0.,1.)<br>
      LocalOrigin = IfcCartesianPoint(&lt;1/2 XDim&gt;,&lt;1/2 YDim&gt;)<br>
      Scale = 2.<br>
      </tt></blockquote>

<font size="-1">Note: The <em>ParentProfile</em> has a <em>Position</em>
= <em>IfcCartesianPoint</em>(&lt;1/2 XDim&gt;,&lt;1/2 YDim&gt;) already.</font><br>

      </td>
    </tr>
    <tr>
      <td align="left" valign="top" width="405">

<img src="../../../../../../figures/ifcderivedprofiledef-layout2.gif" alt="non uniform" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em> is defined using
non uniform transformationsby applying the <em>IfcCartesianTransformationOperator2DnonUniform</em>
as a subtype of the 2D CTO.</p>

<p><u>Example</u><br>
The example shows a non-uniform scaling and a translation of an <em>IfcRectangleProfileDef</em>
to match the lower-left cardinal point. The attributes of the CTO are:</p>

      <blockquote><tt>Axis1 = NIL (defaults to 1.,0.)<br>
      Axis2 = NIL (defaults to 0.,1.)<br>
      LocalOrigin = IfcCartesianPoint(0.,&lt;1/2 YDim)<br>
      Scale&nbsp; = 1.<br>
      Scale2 = 2.<br>
      </tt></blockquote>

<font size="-1">Note: The <em>ParentProfile</em> has a <em>Position</em>
= <em>IfcCartesianPoint</em>(&lt;1/2 XDim&gt;,&lt;1/2 YDim&gt;) already.</font>

      </td>
    </tr>
    <tr>
      <td align="left" valign="top">

<img alt="mirroring" src="../../../../../../figures/ifcderivedprofiledef-layout3.gif" border="0" height="300" width="400">

      </td>
      <td align="left" valign="top">

<p><u>Parameter</u><br>
The <em>IfcDerivedProfileDef</em>
is defined using mirroring by applying the <em>IfcCartesianTransformationOperator2D</em>
(CTO) to the parent profile.</p>

<p><u>Example</u><br>
The example shows a mirroring of an <em>IfcLShapeProfileDef</em>
to match the centre cardinal point. The attributes of the CTO are:</p>

      <blockquote><tt>Axis1 = (-1.,0.)<br>
      Axis2 = NIL (defaults to 0.,1.)<br>
      LocalOrigin = IfcCartesianPoint(0.,0.)<br>
      Scale = NIL (defaults to 1.)<br>
      </tt></blockquote>

<font size="-1">Note: The <em>ParentProfile</em> has a <em>Position</em> = <em>IfcCartesianPoint</em>(0.,0.).</font>

<p>This example is for illustration only.
If the transformation results only in mirroring like shown in the example, then
<em>IfcMirroredProfileDef</em> should be used instead of <em>IfcDerivedProfileDef</em>.</p>

      </td>
    </tr>
    <tr>
      <td colspan="2" rowspan="1" align="left" valign="top" width="405">

<font size="-1">Note: The following color map applies:</font><br>

      <ul>
        <li><font size="-1">black coordinate axes show the
		underlying coordinate system of the swept surface, swept area solid, or
		sectioned spine</font></li>

        <li><font size="-1"><font color="#ff0000">red coordinate axes</font>
		show the position coordinate system of the parent profile</font></li>

        <li><font size="-1"><font color="#993300">brown coordinate axes</font>
		show the position coordinate system of the derived profile</font></li>
      </ul>

      </td>
    </tr>
  </tbody>
</table>
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Derived profile</p></td></tr>
</table>

## Attributes

### ParentProfile
The parent profile provides the origin of the transformation.

### Operator
Transformation operator applied to the parent profile.

### Label
The name by which the transformation may be referred to. The actual meaning of the name has to be defined in the context of applications.

## Formal Propositions

### InvariantProfileType
The profile type of the derived profile shall be the same as the type of the parent profile, i.e. both shall be either AREA or CURVE.
