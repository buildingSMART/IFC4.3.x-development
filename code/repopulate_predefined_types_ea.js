!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: 
 * Author: 
 * Purpose: 
 * Date: 
 */

elementsByPackages = {};

function visitPackage(p) {
	var P as EA.Package;
	P = p;
	
	for (var i = P.Elements.Count - 1; i >= 0; --i) {
		var E = P.Elements.GetAt(i);
		
		if (E.Name.indexOf(".") !== -1) {
			P.Elements.DeleteAt(i, false);
		} else {		
			elementsByPackages[E.Name] = elementsByPackages[E.Name] || [];
			elementsByPackages[E.Name].push(P);
		}
	}
	
	P.Elements.Refresh();
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub);
	}	
}

function main()
{
	Repository.EnableUIUpdates = false;
	Repository.EnableCache = true;	
	
	var P as EA.Package;
	var E as EA.Element;
	var A as EA.Attribute;
	var AT as EA.AttributeTag;
	
	visitPackage(Models.GetAt(0));
		
	data.forEach(s => {
		let en_nm = s.split(".")[0];
		P = elementsByPackages[en_nm][0];
		E = P.Elements.AddNew(s, "Class");
		E.StereotypeEx += ",PredefinedType";
		E.Update();
	});

	Repository.EnableUIUpdates = true;
	Repository.EnableCache = false;
	
	Repository.RefreshModelView(0);
}

data = /* output of extract_predefined_types.py */

main();