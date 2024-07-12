# IfcDeepFoundation

Deep foundation is a type of foundation that transfers loads deeper than shallow foundation below the soft soils not capable of bearing the above structure. Depending on the soil strength it might have to reach down to the rock layer.
<!-- end of short definition -->


Deep foundation is a new supertype incorporating the existing _IfcPile_ and the new _IfcCaissonFoundation_.

## Formal Propositions

### CorrectTypeAssigned
Either there is no deep foundation type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDeepFoundationType_.
