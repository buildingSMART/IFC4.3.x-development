IfcApproval
===========
An _IfcApproval_ represents information about approval processes such as for a
plan, a design, a proposal, or a change order in a construction or facilities
management project. _IfcApproval_ is referenced by _IfcRelAssociatesApproval_
in _IfcControlExtension_ schema, and thereby can be related to all subtypes of
_IfcRoot_. An approval may also be given to resource objects using
_IfcResourceApprovalRelationship_  
  
> HISTORY  New entity in IFC2.0  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attributes Identifier and Name made optional, where rule added
> to require at least one of them being asserted. Inverse attributes
> ApprovedObjects, ApprovedResources and HasExternalReferences added. Inverse
> attribute Properties deleted (more general relationship via inverse
> ApprovedResources to be used instead).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcapprovalresource/lexical/ifcapproval.htm)


Attribute definitions
---------------------
| Attribute             | Description                                                                                                                                                                                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasExternalReferences |                                                                                                                                                                                                                                                                    |
| IsRelatedWith         |                                                                                                                                                                                                                                                                    |
| Relates               |                                                                                                                                                                                                                                                                    |
| ApprovedObjects       |                                                                                                                                                                                                                                                                    |
| ApprovedResources     |                                                                                                                                                                                                                                                                    |
| Identifier            | A computer interpretable identifier by which the approval is known.                                                                                                                                                                                                |
| Name                  | A human readable name given to an approval.                                                                                                                                                                                                                        |
| Description           | A general textual description of a design, work task, plan, etc. that is being approved for.                                                                                                                                                                       |
| TimeOfApproval        | Date and time when the result of the approval process is produced.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  Attribute data type changed to _IfcDateTime_ using ISO 8601 representation, renamed from ApprovalDateTime and made OPTIONAL.                           |
| Status                | The result or current status of the approval, e.g. Requested, Processed, Approved, Not Approved.                                                                                                                                                                   |
| Level                 | Level of the approval e.g. Draft v.s. Completed design.                                                                                                                                                                                                            |
| Qualifier             | Textual description of special constraints or conditions for the approval.                                                                                                                                                                                         |
| RequestingApproval    | The actor that is acting in the role specified at _IfcOrganization_ or individually at _IfcPerson_ and requesting an approval.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute for approval request replacing IfcApprovalActorRelationship (being deleted). |
| GivingApproval        | The actor that is acting in the role specified at _IfcOrganization_ or individually at _IfcPerson_ and giving an approval.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute for approval provision replacing IfcApprovalActorRelationship (being deleted).   |

