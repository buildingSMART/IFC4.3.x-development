!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: remove_concept_parametrizations.js 
 */

function visitPackage(Fn, p) {
	var P as EA.Package;
	P = p;
	Session.Output("Package: " + P.Name);
	
	for (var i = P.Elements.Count - 1; i >= 0; --i) {
		var E as EA.Element;
		E = P.Elements.GetAt(i);
		Session.Output("Processing " + E.Name);
		if (Fn(P, E) == 'remove') {
			Session.Output("Removing " + E.Name);
			P.Elements.DeleteAt(i, true);
			P.Elements.Refresh();
		}
	}
	
	for (var i = P.Packages.Count - 1; i >= 0; --i) {
		var sub = P.Packages.GetAt(i);
		visitPackage(Fn, sub);
		
		if (Fn(sub) == 'remove') {
			Session.Output("Removing " + sub.Name);
			P.Packages.DeleteAt(i, true);
			P.Packages.Refresh();
		}
	}
}

function deleteConnector(con) {
	client = Repository.GetElementByID(con.ClientID);
	Session.Output("On: ", client.Name);
	for (let i = 0; i < client.Connectors.Count; i++) {
		Session.Output("Id: ", client.Connectors.GetAt(i).ConnectorID);
		if (client.Connectors.GetAt(i).ConnectorID == con.ConnectorID) {
			client.Connectors.Delete(i);
			client.Connectors.Refresh();
			client.Update();
			return;
		}
	}
	throw new Error("Not found");
}

function RemoveConceptParams(name) {
	function visitor(p, e) {
		var P as EA.Package;
		var E as EA.Element;
		P = p;
		E = e;
		
		if (P.Name == name) {
			if (E && E.AssociationClassConnectorID) {
				C = Repository.GetConnectorByID(E.AssociationClassConnectorID);
				deleteConnector(C);
				return 'remove';
			} else if (!E) {
				// remove package
				return 'remove';
			}
		}
	}
	return visitor;
}

function main()
{
	var P as EA.Package;
	P = Repository.Models.GetAt(0);
	
	visitPackage(RemoveConceptParams("ObjectTyping"), P);
}

main();
