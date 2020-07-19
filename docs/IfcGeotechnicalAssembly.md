IfcGeotechnicalAssembly
=======================
Representation of the abstract concept of a geological and geotechnical model,
usually an interpretation but sometimes created direct from ground penetrating
measurement.  
Use of an assembly is optional but can carry the methodology and uncertainty
information.  
Such assemblies will include
[_IfcGeotechnicalStratum_]($element://{FAEFB134-3800-4995-B222-B921D7E287BF})
entity types and may include other entity types such as
[_IfcPile_]($element://{435B3F20-9735-4ef6-A7D1-67B825242110}),
[_IfcSlab_]($element://{A03DCC94-8D42-490e-A479-98F082D080E6}) or
[_IfcSensor_]($element://{5425D1CE-B48C-4017-9061-49FA37868B9D}) to represent
the capping, lining or logging equipment present.  
[ _IfcBorehole_]($element://{3C670EC4-0027-4bd5-A2D2-BFF02387AB99}) or
[_IfcGeoSlice_]($element://{441764EE-C125-4679-8415-F87449B952AD}) can have a
physical reality as a construction hazard alongside being the carrier for the
interpreted results. Geological hazards may be associated to any
[_IfcGeotechnicalAssembly_]($element://{85B77FDE-67EA-40a4-ADA4-ADD4C95A7D3E})
or
[_IfcGeotechnicalStratum_]($element://{FAEFB134-3800-4995-B222-B921D7E287BF}).  


