IfcGeometricRepresentationSubContext
====================================
_IfcGeometricRepresentationSubContext_ defines the context that applies to
several shape representations of a product being a sub context, sharing the
_WorldCoordinateSystem_, _CoordinateSpaceDimension_, _Precision_ and
_TrueNorth_ attributes with the parent _IfcGeometricRepresentationContext_.  
  
The _IfcGeometricRepresentationSubContext_ is used to define semantically
distinguished representation types for different information content,
dependent on the representation view and the target scale. It can be used to
control the level of detail of the shape representation that is most
applicable to this geometric representation context. In addition the sub
context is used to control the later appearance of the
_IfcShapeRepresentation_ within a plot view.  
  
> NOTE  If the _IfcShapeRepresentation_ using this sub context
> has_IfcStyledItem_''s assigned to the _Items_, the presentation style
> information (e.g. _IfcCurveStyle_, _IfcTextStyle_) associated with the
> _IfcStyledItem_ is given in target plot dimensions. For example, a line
> thickness (_IfcCurveStyle.CurveWidth_) is given by a thickness measure
> relating to the thickness for a plot within the (range of) target scale.  
  
Each _IfcProduct_ can then have several instances of subtypes of
_IfcRepresentation_, each being assigned to a different
_IfcGeometricRepresentationSubContext_). The applicable values for the
inherited _ContextIdentifier_ attribute shall be identical to the
_RepresentationIdentifier_ attrubute defined at _IfcShapeRepresentation_.  
  
> NOTE  The provision of a model view
> (_IfcGeometricRepresentationContext.ContextType_ = ''Model'') is mandatory.
> Instances of _IfcGeometricRepresentationSubContext_ relate to it as its
> _ParentContext_.  
  
> EXAMPLE  Instances of _IfcGeometricRepresentationSubContext_ can be used to
> handle the multi-view blocks or macros, which are used in CAD programs to
> store several scale and/or view dependent geometric representations of the
> same object. The application can then choose the most appropriate
> representation for showing the geometric shape of the product, depending on
> the target view and scale.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcrepresentationresource/lexical/ifcgeometricrepresentationsubcontext.htm)


