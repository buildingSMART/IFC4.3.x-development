IfcThirdOrderPolynomialSpiral
=============================

The _IfcThirdOrderPolynomialSpiral_ is a specialization of _IfcSpiral_. The curvature _κ_ and radius of the curvature _ρ_, at any point of the curve, are related to the arc length _s_ by the third order formulae:
>>
>> ![formula](../../../../../../figures/ifcthirdorderpolynomialspiral_curvature.PNG)
>> 
> Interpretation of the parameters:
>> 
>> 
>> C = SELF\IfcSpiral.Position.Location   
>> x = SELF\IfcSpiral.Position.P[1]   
>> y = SELF\IfcSpiral.Position.P[2]  
>> A<sub>3</sub> = CubicTerm     
>> A<sub>2</sub> = QuadraticTerm  
>> A<sub>1</sub> = LinearTerm  
>> A<sub>0</sub> = ContantTerm  
>> 
> and the third order polynomial spiral is parameterized as:
>> 
>> ![formula](../../../../../../figures/ifcspiral_parameterization.PNG)
>>
> where:
>>
>> ![formula](../../../../../../figures/ifcthirdorderpolynomialspiral_theta.PNG)
>>
> and the parametric range is: -&infin; &lt; _u_ &lt; &infin;.
