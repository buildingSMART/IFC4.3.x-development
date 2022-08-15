!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: 
 * Author: 
 * Purpose: 
 * Date: 
 */

var constraints_to_delete = ["correcttypeassigned", "correctstyleassigned", "correctpredefinedtype"];

function processElement(e) {
	var E as EA.Element;
	var C as EA.Constraint;
	
	E = e;
	
	for (var i = E.Constraints.Count - 1; i >= 0; --i) {
		C = E.Constraints.GetAt(i);
		let shouldDelete = constraints_to_delete.map(s => C.Name.toLowerCase().indexOf(s) !== -1).some(x => x);
		if (shouldDelete) {
			Session.Output(`Deleting ${E.Name}.${C.Name}`);
			E.Constraints.DeleteAt(i, true);
			E.Constraints.Refresh();
		}
	}
}

function visitPackage(p) {
	var P as EA.Package;
	P = p;
	
	for (var i = 0; i < P.Elements.Count; ++i) {
		var E = P.Elements.GetAt(i);
		processElement(E);
	}
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub);
	}	
}

function main()
{
	visitPackage(Models.GetAt(0));
}

main();