python3 extract_concepts_from_xmi.py ../schemas/IFC.xml
python3 to_pset.py ../schemas/IFC.xml psd
python3 parse_xmi.py ../schemas/IFC.xml
python3 to_express.py ../schemas/IFC.xml IFC.exp
python3 express_to_xsd.py IFC.exp IFC.xsd
python3 change_log.py ..
python3 parse_examples.py ..
