# IfcTelecomAddress

This entity represents an address to which telephone, electronic mail and other forms of telecommunications should be addressed.
<!-- end of short definition -->

> HISTORY New entity in IFC2x.

> IFC4 CHANGE Added attribute _MessagingIDs_. Type of attribute _WWWHomePageURL_ compatibly changed from _IfcLabel_ to _IfcURIReference_.

> IFC4.3.0.0 DEPRECATION This entity is deprecated. Use Pset_Address instead, which is applicable to IfcActor, IfcBuilding and IfcSite.

## Attributes

### TelephoneNumbers
The list of telephone numbers at which telephone messages may be received.

### FacsimileNumbers
The list of fax numbers at which fax messages may be received.

### PagerNumber
The pager number at which paging messages may be received.

### ElectronicMailAddresses
The list of Email addresses at which Email messages may be received.

### WWWHomePageURL
The world wide web address at which the preliminary page of information for the person or organization can be located.
> NOTE Information on the world wide web for a person or organization may be separated into a number of pages and across a number of host sites, all of which may be linked together. It is assumed that all such information may be referenced from a single page that is termed the home page for that person or organization.

### MessagingIDs
IDs or addresses for any other means of telecommunication, for example instant messaging, voice-over-IP, or file transfer protocols. The communication protocol is indicated by the URI value with scheme designations such as irc:, sip:, or ftp:.

## Formal Propositions

### MinimumDataProvided
Requires that at least one attribute of telephone numbers, facsimile numbers, pager number, electronic mail addresses, world wide web home page URL, or messaging ID is asserted. It is not acceptable to have a telecommunications address without at least one of these values.
