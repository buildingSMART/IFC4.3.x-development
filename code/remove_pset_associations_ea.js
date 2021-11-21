!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: process_deprecation_ea.js
 * Author: Thomas Krijnen <thomas@aecgeeks.com>
 */

var psetAssociationsDeleted = 0;
var qsetAssociationsDeleted = 0;

function removeAssociationsOfType(e, ty) {
    var E as EA.Element;
    E = e;
    
    let n = 0;
    
    for (var i = el.Connectors.Count -1; i >= 0; --i) {
		var con as EA.Connector;
		con = el.Connectors.GetAt(i);
		if (con.MetaType == ty) {
			el.Connectors.DeleteAt(i, false);
			n += 1;
		}
	}
    
    el.Connectors.Refresh();
    
    return n;
}

function processElement(e) {
    var E as EA.Element;
    E = e;	
    
    if (el.Name.toLowerCase().startsWith("pset_")) {
        psetAssociationsDeleted += removeAssociationsOfType(el, "Realisation");
    } else if (el.Name.toLowerCase().startsWith("qto_")) {
        qsetAssociationsDeleted += removeAssociationsOfType(el, "Dependency");
    }
}

function visitPackage(p, R) {
	var P as EA.Package;
	P = p;
	Session.Output("Package: " + P.Name);

	for (var i = 0; i < P.Elements.Count; ++i) {
		processElement(P.Elements.GetAt(i));
	}
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub, R ? R : sub);
	}	
}
 
function main() {
	visitPackage(Models.GetAt(0));
    
    Session.Output(`Removed ${psetAssociationsDeleted} pset associations`);
    Session.Output(`Removed ${qsetAssociationsDeleted} qset associations`);
}

main();
