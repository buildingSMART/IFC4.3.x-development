!INC Local Scripts.EAConstants-JScript
 
elementByName = {};

function visitPackage(p) {
	var P as EA.Package;
	P = p;
	
	for (var i = 0; i < P.Elements.Count; ++i) {
		var E = P.Elements.GetAt(i);
		elementByName[E.Name] = E;
	}
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub);
	}
}
 
function main()
{
	visitPackage(Models.GetAt(0));
	
	data.forEach(tup => {
		if (tup[0] == "rename") {
			var E as EA.Element;
			
			let [_, cls, oldName, newName] = tup;
			Session.Output(cls);
			E = elementByName[cls];
			
			for (var i = 0; i < E.Attributes.Count; ++i) {
				var attr = E.Attributes.GetAt(i);
				if (attr.Name == oldName) {
					attr.Name = newName;
					attr.Update();
					break;
				}
			}
		}			
	});
}

data = /* data from read_normalization.py */;

main();