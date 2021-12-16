!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: recreate_property_sets.js
 * Author: Thomas Krijnen <thomas@aecgeeks.com>
 */
 
packageByName = {};
elementsByPackages = {};
elementByName = {}

function deleteByName(nm) {
	if (nm in elementsByPackages) {
		for (let p of elementsByPackages[nm]) {
			for (var i = p.Elements.Count - 1; i >= 0; --i) {
				if (p.Elements.GetAt(i).Name == nm) {
					p.Elements.DeleteAt(i, false);
				}
			}
			p.Elements.Refresh();
		}
	}
	elementsByPackages[nm] = []
	elementByName[nm] = null;
}
 
function visitPackage(p) {
	var P as EA.Package;
	P = p;
	packageByName[P.Name] = P;
	
	for (var i = 0; i < P.Elements.Count; ++i) {
		var E = P.Elements.GetAt(i);
		elementByName[E.Name] = E;
		
		elementsByPackages[E.Name] = elementsByPackages[E.Name] || [];
		elementsByPackages[E.Name].push(P);
	}
	
	for (var i = 0; i < P.Packages.Count; ++i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(sub);
	}	
}

function createPropertyType(Prop, Ts, Pack) {
	var name = Prop.Name.substr(8) + Ts.map(e => e.Name.replace("Ifc", "")).reverse().join("Over");
	if (name in elementByName) {
		return elementByName[name];
	}
	
	let params = [];
	
	for (var i = 0; i < Prop.TemplateParameters.Count; ++i) {
		var TP = EA.TemplateParameter;
		TP = Prop.TemplateParameters.GetAt(i);
		params.push(TP.Name);
	}
	
	if (params.length != Ts.length) {
		Session.Output("Params: " + params.join(","));
		Session.Output("Actual: " + Ts.map(e => e.Name).join(","));
		throw new Error("Unexpected amount of template arguments");
	}
	
	var E as EA.Element;
	var C as EA.Connector;
	var TB as EA.TemplateBinding;
		
	E = Pack.Elements.AddNew(name, "Class");
	E.Update();
	Pack.Elements.Refresh();

	C = E.Connectors.AddNew("", "TemplateBinding");
	C.SupplierID = Prop.ElementID;
	C.Update();
	E.Connectors.Refresh();
	
	for (let i = 0; i < params.length; ++i) {
		TB = C.TemplateBindings.AddNew(
			params[i],
			Ts[i].ElementGUID
		);
		TB.Update();	
	}
	
	C.TemplateBindings.Refresh();
	
	elementByName[name] = E;
	
	return E;
}

function handleProperty(E, data, P) {
	let T1 = elementByName[data.type];
	let S2 = data.type_arg;
	if (typeof S2 == "string") {
		S2 = [S2];
	}
	T2 = S2.map(s => elementByName[s]);

	var anyUnmapped = false;
	for (var i = 0; i < S2.length; ++i) {
		if (!T2[i]) {
			Session.Output("Unmapped: " + S2[i]);
			anyUnmapped = true;
			T2[i] = elementByName["UNKNOWN"];
		}
	}
	if (anyUnmapped) {
		// throw new Error("Unmapped types");
	}
	
    let atype = createPropertyType(T1, T2, P);
    
	A = E.Attributes.AddNew(
		data.name,
		atype.Name
	);
    A.ClassifierID = atype.ElementID;
	A.Update();
    
	return A;
}
 
function main() {
	Repository.EnableUIUpdates = false;
	Repository.EnableCache = true;	
	
	var P as EA.Package;
	var E as EA.Element;
	var A as EA.Attribute;
	var AT as EA.AttributeTag;
	
	visitPackage(Models.GetAt(0));
	
	for (let et of data.enumeration_properties) {
		deleteByName(et.name);
		
		let pp = et.package;
		if (!pp) {
			pp = "propertytypes"
		}
		
		Session.Output(pp + " " + et.name);
		P = packageByName[pp];
		
		E = P.Elements.AddNew(et.name, "enumeration");
		E.StereotypeEx += ",enumeration";
		E.Update();
		
		elementByName[et.name] = E;
		
		for (let vi = 0; vi < et.values.length; ++vi) {
			A = E.Attributes.AddNew(et.values[vi], "");
			if (A.StyleEx.indexOf("IsLiteral=") === -1) {
				A.StyleEx += ";IsLiteral=1";
			} else {
				A.StyleEx = A.StyleEx.replace("IsLiteral=0", "IsLiteral=1");
			}
			A.Update();
			AT = A.TaggedValues.AddNew("ExpressOrdering", vi);
			AT.Update();
			A.TaggedValues.Refresh();
		}
		
		E.Attributes.Refresh();
	}
	
	for (let cp of data.complex_properties) {
		deleteByName(cp.name);
		
		let pp = cp.package;
		if (!pp) {
			pp = "propertytypes"
		}
		
		Session.Output(pp + " " + cp.name);
		P = packageByName[pp];
		
		E = P.Elements.AddNew(cp.name, "Class");
		if (!E) {
			Session.Output(P.GetLastError());
			throw new Error("");
		}
		E.StereotypeEx += ",ComplexProperty";
		E.Update();
		
		elementByName[cp.name] = E;
		
		for (let vi = 0; vi < cp.properties.length; ++vi) {
			A = handleProperty(E, cp.properties[vi], P);			
			
			AT = A.TaggedValues.AddNew("ExpressOrdering", vi);
			AT.Update();
			A.TaggedValues.Refresh();
		}
		
		E.Attributes.Refresh();
	}
	
	for (let pset of data.property_sets) {
		deleteByName(pset.name);
		
		let pp = pset.package;
		Session.Output(pp + " " + pset.name);
		P = packageByName[pp];
		
		E = P.Elements.AddNew(pset.name, "Class");
		E.StereotypeEx += "," + pset.type;
		E.Update();
		
		for (let vi = 0; vi < pset.properties.length; ++vi) {
			try {
				A = handleProperty(E, pset.properties[vi], P);			
			} catch (error) {
				Session.Output("... on " + pset.name + "." + pset.properties[vi].name);
				continue;
			}
			
			AT = A.TaggedValues.AddNew("ExpressOrdering", vi);
			AT.Update();
			A.TaggedValues.Refresh();
		}
		
		E.Attributes.Refresh();
	}
	
	for (let qset of data.quantity_sets) {
		deleteByName(qset.name);
		
		let pp = qset.package;
		Session.Output(pp + " " + qset.name);
		P = packageByName[pp];
		
		E = P.Elements.AddNew(qset.name, "Class");
		E.StereotypeEx += ",QTO_TYPEDRIVENOVERRIDE";
		E.Update();
		
		for (let vi = 0; vi < qset.quantities.length; ++vi) {
			Session.Output(qset.quantities[vi].name + " " + qset.quantities[vi].type);
			A = E.Attributes.AddNew(qset.quantities[vi].name, qset.quantities[vi].type);
            A.ClassifierID = elementByName[qset.quantities[vi].type].ElementID;
			A.Update();
			
			AT = A.TaggedValues.AddNew("ExpressOrdering", vi);
			AT.Update();
			A.TaggedValues.Refresh();
		}
		
		E.Attributes.Refresh();
	}
	
	Repository.EnableUIUpdates = true;
	Repository.EnableCache = false;
	
	Repository.RefreshModelView(0);
}

data = /* output of dump_psets_to_json.py */

main();