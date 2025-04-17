python3 extract_concepts_from_xmi.py ../schemas/IFC.xml
python3 to_pset.py ../schemas/IFC.xml psd
python3 parse_xmi.py ../schemas/IFC.xml
python3 to_express.py ../schemas/IFC.xml IFC.exp
python3 express_to_xsd.py IFC.exp IFC.xsd
python3 change_log.py ..
python3 parse_examples.py ..
python3 templates_to_mvdxml.py IFC4.3.mvdxml
python3 determine_mvd_scope.py IFC.exp IFC4.3.mvdxml
# python3 translate.py build-cache
