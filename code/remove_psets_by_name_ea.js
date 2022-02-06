const elementByName = {};
const packageByElementName = {};

function deleteElement(e) {
    var E as EA.Element;
    E = e;
    var P as EA.Package;
    P = packageByElementName[E.Name];
    for (var i = 0; i < P.Elements.Count; ++i) {
        if (P.Elements.GetAt(i).ElementID == E.ElementID) {
            P.Elements.DeleteAt(i, false);
        }
    }
    P.Elements.Refresh();
}

function visitPackage(p) {
    var P as EA.Package;
    P = p;
    for (var i = 0; i < P.Elements.Count; ++i) {
        var E = P.Elements.GetAt(i);
        if (elementByName[E.Name]) {
            throw new Error();
        }
        elementByName[E.Name] = E;
        packageByElementName[E.Name] = P;
    }
    for (var i = 0; i < P.Packages.Count; ++i) {
        var sub = P.Packages.GetAt(i);
        visitPackage(sub);
    }
}

function removePropertyAssociationsClasses(e, ty) {
    var E as EA.Element;
    E = e;
    let n = 0;
    for (var i = E.Connectors.Count -1; i >= 0; --i) {
        var con as EA.Connector;
        con = E.Connectors.GetAt(i);
        if (con.AssociationClass) {
            Session.Output(con.AssociationClass.Name);
            if (packageByElementName[con.AssociationClass.Name].Name == "PropertySetsforObjects") {
                deleteElement(con.AssociationClass);
                E.Connectors.DeleteAt(i, false);
            }
        }
    }
    E.Connectors.Refresh();
    return n;
}

function main()
{
    visitPackage(Models.GetAt(0));
    elementsToDelete.forEach(e => {
        let E = elementByName[e];
        Session.Output(e);
        if (!E) {
            return;
        }
        Session.Output(E.Name);
        removePropertyAssociationsClasses(E);
        deleteElement(E);
    });
}

const elementsToDelete = [];

main();