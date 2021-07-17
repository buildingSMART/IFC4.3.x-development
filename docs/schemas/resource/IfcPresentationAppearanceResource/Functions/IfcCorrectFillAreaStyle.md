# IfcCorrectFillAreaStyle

This function returns true if the different fill area styles are assigned correctly to the _IfcFillAreaStyle_. Only certain combinations of the entity types provided by the _IfcFillStyleSelect_ are allowed.

Return false:

* if more then one externally defined style is assigned 
* if an externally defined style is given and any other internal style definition is attached additionally 
* if more then one background colour is assigned 
* if both, a hatching and a tiling is assigned 

otherwise return true

> <font color="#0000FF"><small>HISTORY  New function
      in Release IFC2x3 TC1.</small></font>
