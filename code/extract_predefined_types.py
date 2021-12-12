def enumerate_predefined_types(schema):
    for ent in schema.entities.values():
        for attr in ent.attributes:
            if attr.name == 'PredefinedType':
                T = schema.types[attr.type]
                
                if T.type.__class__.__name__ == 'EnumerationType':
                    enum_types = [(T.name, T.type)]
                else:
                    enum_types = [(x, schema.types[x].type) for x in T.type.values]
                    
                for en_nm, enum_t in enum_types:
                    for v in enum_t.values:
                        yield ent.name, str(en_nm), v

if __name__ == "__main__":

    import sys
    import json
    sys.path.append("express_diff")

    import express_diff.express_parser
    schema = express_diff.express_parser.parse("../reference_schemas/IFC4x3_RC4.exp").schema
    
    json.dump(
        sorted(set(".".join((ty, v)) for _, ty, v in enumerate_predefined_types(schema))),
        open("predefined_types.json", "w"),
        indent=1
    )
