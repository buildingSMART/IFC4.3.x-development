IfcSameValidPrecision
=====================
The function compares the epsilon values (given as _Precision_ at
_IfcGeometricRepresentationContext_ and ensures that they are the same (with a
derivation tolerance) and within reasonable min and max values.  
  
> NOTE  In the above function the following three questionable ad-hoc values
> are used:

  
  

    * 0.000001 for the default precision (1E-6) 
  

    * 1.001 for the allowable deviation of the  
precision values and

  

    * 0.1 for setting the upper limit of the  
accepted precision values to about 0.1.  

  
  

  
  
> HISTORY  New function in IFC2x2  


