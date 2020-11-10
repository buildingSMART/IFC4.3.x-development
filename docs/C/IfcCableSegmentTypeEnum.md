IfcCableSegmentTypeEnum
=======================
The _IfcCableSegmentTypeEnum_ defines the range of different types of cable
segment that can be specified.  
  
> HISTORY  New type in IFC2x2. Core and busbar segment added in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcelectricaldomain/lexical/ifccablesegmenttypeenum.htm)


Attribute definitions
---------------------
| Attribute           | Description                                                                                                                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CONTACTWIRESEGMENT  | An electric conductor of an overhead contact line with which the current collectors make contact. Note: definition from IEC60050 811-33-15.                                                                             |
| CORESEGMENT         | A self contained element of a cable that comprises one or more conductors and sheathing.The core of one lead is normally single wired or multiwired which are intertwined.                                              |
| WIREPAIRSEGMENT     | A pair of conductors contained in a copper cable. The pair is always used together to form a circuit to transmit data by means of electric signals.                                                                     |
| BUSBARSEGMENT       | Electrical conductor that makes a common connection between several electrical circuits. Properties of a busbar are the same as those of a cable segment and are captured by the cable segment property set.            |
| CONDUCTORSEGMENT    | A single linear element within a cable or an exposed wire (such as for grounding) with the specific purpose to lead electric current, data, or a telecommunications signal.                                             |
| FIBERTUBE           | A fiber tube is semi-rigid hollow plastic tube with a very small radius that houses and protects a certain number of optical fiber segments. An optical cable segment may contain many fiber tubes.                     |
| OPTICALCABLESEGMENT | An optical cable segment is a cable segment that contains a variable number of optical fiber segments.                                                                                                                  |
| STITCHWIRE          | A stitch wire consists of auxiliary wires and different components (clamp) used in stitched suspension.                                                                                                                 |
| FIBERSEGMENT        | A fiber segment is an individual optical fiber used in telecommunication systems to transmit data by means of optical signals.                                                                                          |
| CABLESEGMENT        | Cable with a specific purpose to lead electric current within a circuit or any other electric construction. Includes all types of electric cables, mainly several core segments or conductor segments wrapped together. |

