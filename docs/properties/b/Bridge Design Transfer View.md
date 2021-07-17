Bridge Design Transfer View
===========================

{#purpose .num}
### Purpose of the Bridge Design Transfer View
The purpose of the Bridge Design Transfer View is to provide building information with support for editing of interconnected elements. Such applications enable inserting, deleting, moving, and modifying physical building elements and spaces. The target scenario is that a preliminary design model is transferred to an engineer of a particular discipline, where geometric modifications may need to be made.

To enable such editing, higher-level design parameters must be preserved for those elements that affect multiple disciplines, and applications must generate downstream geometry consistently according to such parameters. The scope of parameters is limited to those that impact interconnected elements: for example, increasing retaining wall dimensions impacts composition of abutments; changing alignment parameters impacts geometry of a bridge deck, its piers and abutments; adjusting pipes or ducts may require resizing openings.

The Bridge Design Transfer View inherits all definitions from Design Transfer View adding only the bridge specific definitions that were added in IFC4x2. This means that all definitions from Design Transfer View are also available in Bridge Design Transfer View.
