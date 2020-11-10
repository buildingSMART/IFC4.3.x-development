IfcSignal
=========
A signal is an active device that conveys information or instructions to
users, by means of an audio, visual signal or a combination of both.  
The primary distinction from an
[_IfcSign_]($element://{4BE0513F-EDAF-4911-92C7-421EA6CD62A3}) is that a
signal is active and therefore a subtype of
[_IfcFlowTerminal_]($element://{AE61BBF2-82B0-4caf-B137-1EBEB79B2BB6}) usually
requiring power and data connections for its operation.  
An instance of
[_IfcSignal_]($element://{15911371-83A2-4660-B0A2-B479E9560615}) represents a
singular signalling device in a larger assembled unit or connected system,
such as an individual frame within a railway signal, a single light unit in a
traffic light system or an audio signal or light mounted on a navigational
buoy.  
Signals can be physically aggregated together into an assembly which can
include multiple signal instances (and also sign instances) and the associated
supporting structural elements such as a simple pole or a rigid frame gantry
(see Signal Assembly for examples).  
Signals can be logically (functionally) grouped together into a signalling
system (a type of distribution system) to represent a connected group of
signals for example a group of traffic lights controlling an road
intersection.


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                              |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType | Identifies the predefined type of a signal from which the type modelled, may be set. This type may associate additional specific property sets.NOTE The PredefinedType shall only be used, if no [_IfcSignalType_]($element://{ABB9523D-45C0-45dd-9E66-2BD5B046E9FE})[ __]($element://{B8D00EA4-C9E5-4f74-AB2A-D8235B911718})is assigned, providing its own IfcSignType .PredefinedType. |

