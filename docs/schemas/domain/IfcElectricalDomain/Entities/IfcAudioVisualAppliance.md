# IfcAudioVisualAppliance

An audio-visual appliance is a device that displays, captures, transmits, or receives audio or video.

Audio-visual appliances may be fixed in place or may be able to be moved from one space to another. They may require an electrical supply that may be supplied either by an electrical circuit or provided from a local battery source. Audio-visual appliances may be connected to data circuits including specialist circuits for audio visual purposes only.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAudioVisualApplianceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no audio visual appliance type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAudioVisualApplianceType_.

## Concepts

### Composition


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


