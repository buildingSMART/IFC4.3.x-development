IfcSeventhOrderPolynomialSpiral
===============================

The _IfcSeventhOrderPolynomialSpiral_ is a specialization of _IfcSpiral_. The curvature _κ_ and radius of the curvature _ρ_, at any point of the curve, are related to the arc length _s_ by the seventh order formulae:
>>
>> ![formula](../../../../../../figures/ifcseventhorderpolynomialspiral_curvature.PNG)
>> 
> Interpretation of the parameters:
>> 
>> 
>> C = SELF\IfcSpiral.Position.Location   
>> x = SELF\IfcSpiral.Position.P[1]   
>> y = SELF\IfcSpiral.Position.P[2]  
>> A<sub>7</sub> = SepticTerm     
>> A<sub>6</sub> = SexticTerm  
>> A<sub>5</sub> = QuinticTerm  
>> A<sub>4</sub> = QuarticTerm 
>> A<sub>3</sub> = CubicTerm     
>> A<sub>2</sub> = QuadraticTerm  
>> A<sub>1</sub> = LinearTerm  
>> A<sub>0</sub> = ContantTerm  
>> 
> and the seventh order polynomial spiral is parameterized as:
>> 
>> ![formula](../../../../../../figures/ifcspiral_parameterization.PNG)
>>
> where:
>>
>> ![formula](../../../../../../figures/ifcseventhorderpolynomialspiral_theta.PNG)
>>
> and the parametric range is: -&infin; &lt; _u_ &lt; &infin;.
