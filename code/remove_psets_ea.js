!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: remove_psets.js
 * Author: Thomas Krijnen <thomas@aecgeeks.com>
 */

var psetsDeleted = 0;
var qsetsDeleted = 0;

function visitPackage(p, R) {
	var P as EA.Package;
	var el as EA.Element;
	
	P = p;
	Session.Output("Package: " + P.Name);

	for (var i = P.Elements.Count - 1; i >= 0; --i) {
		el = P.Elements.GetAt(i);
		
        const is_pset = el.Name.toLowerCase().startsWith("pset_");
        const is_qto = el.Name.toLowerCase().startsWith("qto_");
		
        if (is_pset || is_qto) {
            P.Elements.DeleteAt(i, false);
            if (is_pset) {
                psetsDeleted++;
            } else {
                qsetsDeleted++;                
            }
        }
	}
    
    P.Elements.Refresh();
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub, R ? R : sub);
	}	
}
 
function main() {
	visitPackage(Models.GetAt(0));
    
    Session.Output(`Removed ${psetsDeleted} psets`);
    Session.Output(`Removed ${qsetsDeleted} qsets`);
}

main();
