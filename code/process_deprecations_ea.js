!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: process_deprecation_ea.js
 * Author: Thomas Krijnen <thomas@aecgeeks.com>
 */
 
function visitPackage(p, R) {
	var P as EA.Package;
	P = p;
	Session.Output("Package: " + P.Name);
	
	// Taken from output of import_deprecations.py
	const deprecatedClasses = ["IfcCivilElement", "IfcCivilElementType", "IfcOpeningStandardCase", "IfcRelServicesBuildings", "IfcGeographicElementTypeEnum", "IfcDoorStyle", "IfcWindowStyle", "IfcElectricDistributionBoard", "IfcElectricDistributionBoardType", "IfcElectricDistributionBoardTypeEnum", "IfcVibrationIsolator", "IfcVibrationIsolatorType", "IfcBeamStandardCase", "IfcBuildingElementProxy", "IfcBuildingElementProxyType", "IfcBuildingSystem", "IfcColumnStandardCase", "IfcDoorStandardCase", "IfcMemberStandardCase", "IfcPlateStandardCase", "IfcSlabElementedCase", "IfcSlabStandardCase", "IfcWallElementedCase", "IfcWallStandardCase", "IfcWindowStandardCase", "IfcBuildingSystemTypeEnum", "IfcVibrationDamper", "IfcVibrationDamperType"]

	for (var i = 0; i < P.Elements.Count; ++i) {
		var E as EA.Element;
		E = P.Elements.GetAt(i);	
		
		if (deprecatedClasses.indexOf(E.Name) !== -1) {
			E.StereotypeEx += ",deprecated";
			
			E.Update();
			E.Refresh();
		}
		
		Session.Output(E.Name + " " + E.StereotypeEx);		
	}
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub, R ? R : sub);
	}	
}
 
function main() {
	visitPackage(Models.GetAt(0));
}

main();
