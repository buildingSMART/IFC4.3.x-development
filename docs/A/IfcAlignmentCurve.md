IfcAlignmentCurve
=================
The alignment curve is a parameterized space curve which represents the
geometry of any track section. It is defined by three alignments (= layouts),
which are to be regarded as independent from each other:  

  

  1. an horizontal alignment (2D)
  

  2. a vertical alignment (1D)
  

  3. a cant alignment (1D) (synonym = superelevation)
  

  
Each of these three alignments is defined by a sequence of ordered geometric
segments composed of various geometry types that are linked together in a
chain.


Attribute definitions
---------------------
| Attribute                       | Description                                                                                  |
|---------------------------------|----------------------------------------------------------------------------------------------|
| Acceptable tangential tolerance | Parameter used to check if the tangential continuity of two geometric segments is respected. |

