# IfcRailing

The railing is a frame assembly adjacent to human or vehicle circulation spaces and at some space boundaries where it is used in lieu of walls or to compl<font color="#ff0000">e</font>ment walls. <font color="#ff0000">REMOVE{</font> Designed to aid humans, either as an optional physical support, or to prevent injury or damage, either by falling or collision.<font color="#ff0000">}</font><font color="#ff0000">Designed as an optional physical support, or to prevent injury or damage, either by falling or collision.</font>  
> HISTORY New entity in IFC2.0

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcRailingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no railing type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcRailingType_.
