# IfcSecondOrderPolynomialSpiral

The _IfcSecondOrderPolynomialSpiral_ is a specialization of _IfcSpiral_. The curvature _κ_ and radius of the curvature _ρ_, at any point of the curve, are related to the arc length _s_ by the second order formulae:<!-- end of definition -->
>>
>> ![formula](../../../../figures/ifcsecondorderpolynomialspiral_curvature.PNG)
>>
> Interpretation of the parameters:
>>
>>
>> C = SELF\IfcSpiral.Position.Location
>> x = SELF\IfcSpiral.Position.P[1]
>> y = SELF\IfcSpiral.Position.P[2]
>> A<sub>2</sub> = QuadraticTerm
>> A<sub>1</sub> = LinearTerm
>> A<sub>0</sub> = ContantTerm
>>
> and the second order polynomial spiral is parameterized as:
>>
>> ![formula](../../../../figures/ifcspiral_parameterization.PNG)
>>
> where:
>>
>> ![formula](../../../../figures/ifcsecondorderpolynomialspiral_theta.PNG)
>>
> and the parametric range is: -∞ < _u_ < ∞.

## Attributes

### QuadraticTerm
The constant that defines the quadratic term in the equation which defines the relation between curvature and arc length for the curve.

### LinearTerm
The constant that defines the linear term in the equation which defines the relation between curvature and arc length for the curve.

### ConstantTerm
The constant that defines the constant term in the equation which defines the relation between curvature and arc length for the curve.
