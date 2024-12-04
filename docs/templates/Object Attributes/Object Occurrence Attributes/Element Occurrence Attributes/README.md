Element Occurrence Attributes
=============================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

Physical elements may be further identified via the _Tag_ attribute. This is a human readable identifier such as an element or item numbe. While there is no restriction on usage of such tags, it is recommended the _Tag_ is unique within its containing scope.

```
concept {
    IfcElement:Tag -> IfcIdentifier
}
```
