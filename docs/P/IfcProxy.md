IfcProxy
========
_IfcProxy_ is intended to be a kind of a container for wrapping objects which
are defined by associated properties, which may or may not have a geometric
representation and placement in space. A proxy may have a semantic meaning,
defined by the _Name_ attribute, and property definitions, attached through
the property assignment relationship, which definition may be outside of the
definitions given by the current release of IFC.  
  
The _ProxyType_ may give an indication to which high level semantic breakdown
of object the semantic definition of the proxy relates to. the _Tag_ attribute
may be used to assign a human or system interpretable identifier (such as a
serial number or bar code).  
  
> NOTE  Given that only a limited number of semantic constructs can be
> formally defined within IFC (and it will never be possible to define all),
> there has to be a mechanism for capturing those constructs that are not
> (yet) defined by IFC.  
  
> NOTE  Product proxies are a mechanism that allows to exchange data that is
> part of the project but not necessarily part of the IFC model. Those proxies
> may have geometric representations assigned.  
  
> HISTORY  New entity in IFC1.5.  
  
{ .deprecated}  
> DEPRECATION  The entity is deprecated and shall not be used.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcproxy.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                          |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ProxyType   | High level (and only) semantic meaning attached to the IfcProxy, defining the basic construct type behind the Proxy, e.g. Product or Process.                        |
| Tag         | The tag (or label) identifier at the particular instance of a product, e.g. the serial number, or the position number. It is the identifier at the occurrence level. |

Formal Propositions
-------------------
| Rule   | Description   |
|--------|---------------|
| WR1    |               |

