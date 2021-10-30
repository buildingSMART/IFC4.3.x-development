import sys

import append_xmi
import concept_extractor

if __name__ == "__main__":
    fn = sys.argv[1]
    
    c = append_xmi.context("..\schemas\IFC.xml")
    ifc_package = c.package_by_name("IFC4x3_RC4")
    views_package = c.insert(ifc_package, append_xmi.uml_package("Views"))
    gu_package = c.insert(views_package, append_xmi.uml_package("GeneralUsage"))
    
    x = concept_extractor.extractor(fn)
    
    # Axis Geometry
    axis_geom_package = c.insert(gu_package, append_xmi.uml_package("AxisGeometry"))    
    axis_geom = append_xmi.uml_class("AxisGeometry")
    c.insert(axis_geom_package, axis_geom)
    
    axis_concepts = x.concept_starting_with("Axis ")
    axis_entities = set(v[0] for v in axis_concepts)
    
    for entity in axis_entities:
        ids = [axis_geom.id, c.to_id[("uml:Class", entity)]]
        assoc = append_xmi.uml_assoc_class(f"{entity}AxisGeometryUsage", ids)
        c.insert(axis_geom_package, assoc)
        
    c.write("..\schemas\IFC_with_concepts.xml")