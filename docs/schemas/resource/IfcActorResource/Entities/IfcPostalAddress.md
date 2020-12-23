# IfcPostalAddress

This entity represents an address for delivery of paper based mail and other postal deliveries.

> HISTORY&nbsp; New entity in IFC2x.

## Attributes

### InternalLocation
An organization defined address for internal mail delivery.

### AddressLines
The postal address.
> NOTE&nbsp; A postal address may occupy several lines (or elements) when recorded. It is expected that normal usage will incorporate relevant elements of the following address concepts: A location within a building (e.g. 3rd Floor) Building name (e.g. Interoperability House) Street number (e.g. 6400) Street name (e.g. Alliance Boulevard). Typical content of address lines may vary in different countries.

### PostalBox
An address that is implied by an identifiable mail drop.

### Town
The name of a town.

### Region
The name of a region.
> NOTE&nbsp; The counties of the United Kingdom and the states of North America are examples of regions.

### PostalCode
The code that is used by the country's postal service.

### Country
The name of a country.

## Formal Propositions

### WR1
Requires that at least one attribute of internal location, address lines, town, region or country is asserted. It is not acceptable to have a postal address without at least one of these values.
