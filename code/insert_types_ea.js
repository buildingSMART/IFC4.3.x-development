!INC Local Scripts.EAConstants-JScript

/*
 * Script Name: insert_types_ea.js
 * Author: Thomas Krijnen <thomas@aecgeeks.com>
 */
 
packageByName = {};
elementsByPackages = {};
elementByName = {}

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

function main() {
	Repository.EnableUIUpdates = false;
	Repository.EnableCache = true;	
	
	var P as EA.Package;
	var E as EA.Element;
	var A as EA.Attribute;
	var AT as EA.AttributeTag;
	
	P = packageByName["IfcTunnelDomain"];

	visitPackage(Models.GetAt(0));
	
	for (let item of data) {

		if (item.enumeration_items) {
			E = P.Elements.AddNew(item.name, "enumeration");
			E.StereotypeEx += ",enumeration";
			E.Update();

			for (let vi = 0; vi < item.enumeration_items.length; ++vi) {
				A = E.Attributes.AddNew(item.enumeration_items[vi], "");
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
		} else if (item.select_list) {
			E = P.Elements.AddNew(item.name, "class");
			E.StereotypeEx += ",select";
			E.Update();
		} else if (item.attributes) {
			E = P.Elements.AddNew(item.name, "class");
			E.Update();	

			for (let vi = 0; vi < item.attributes.length; ++vi) {
				A = E.Attributes.AddNew(item.attributes[vi], "");
				A.Update();
				AT = A.TaggedValues.AddNew("ExpressOrdering", vi);
				AT.Update();
				A.TaggedValues.Refresh();
			}

			E.Attributes.Refresh();
		}

	}
	
	Repository.EnableUIUpdates = true;
	Repository.EnableCache = false;
	
	Repository.RefreshModelView(0);
}

data = [{"name": "IfcArchElement", "supertype": "IfcBuiltElement", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcArchElementTypeEnum"}], "is_abstract": false}, {"name": "IfcArchElementType", "supertype": "IfcBuiltElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcArchElementTypeEnum"}], "is_abstract": false}, {"name": "IfcArchElementTypeEnum", "enumeration_items": ["LINING", "NOTDEFINED", "SEGMENT", "USERDEFINED"]}, {"name": "IfcBoreholeType", "supertype": "IfcGeoScienceElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcBoreholeTypeEnum"}], "is_abstract": false}, {"name": "IfcBoreholeTypeEnum", "enumeration_items": ["COREDRILLING", "DESTRUCTIVEDRILLING", "NOTDEFINED", "TRIALPIT", "USERDEFINED"]}, {"name": "IfcComplementaryData", "supertype": "IfcProduct", "attributes": [], "is_abstract": true}, {"name": "IfcDatasetInformation", "supertype": "IfcDocumentInformation", "attributes": [{"name": "SchemaReference", "optional": true, "type_of_attribute": "IfcURIReference"}], "is_abstract": false}, {"name": "IfcDatasetReference", "supertype": "IfcExternalReference", "attributes": [{"name": "Description", "optional": true, "type_of_attribute": "IfcText"}, {"name": "ReferencedDataset", "optional": true, "type_of_attribute": "IfcDatasetInformation"}, {"name": "Filter", "optional": true, "type_of_attribute": "IfcText"}], "is_abstract": false}, {"name": "IfcDatasetSelect", "select_list": ["IfcDatasetInformation", "IfcDatasetReference"]}, {"name": "IfcEarthingElement", "supertype": "IfcFlowTerminal", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcEarthingElementTypeEnum"}], "is_abstract": false}, {"name": "IfcEarthingElementType", "supertype": "IfcFlowTerminalType", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcEarthingElementTypeEnum"}], "is_abstract": false}, {"name": "IfcEarthingElementTypeEnum", "enumeration_items": ["EARTHINGSTRIP", "FIXEDTERMINAL", "GROUNDINGMESH", "GROUNDINGPLATE", "GROUNDINGROD", "NOTDEFINED", "USERDEFINED"]}, {"name": "IfcEarthworksCut", "supertype": "IfcExcavation", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcEarthworksCutTypeEnum"}], "is_abstract": false}, {"name": "IfcExcavation", "supertype": "IfcFeatureElementSubtraction", "attributes": [], "is_abstract": true}, {"name": "IfcFillElement", "supertype": "IfcBuiltElement", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcFillElementTypeEnum"}], "is_abstract": false}, {"name": "IfcFillElementType", "supertype": "IfcBuiltElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcFillElementTypeEnum"}], "is_abstract": false}, {"name": "IfcFillElementTypeEnum", "enumeration_items": ["ANNULARGAPFILL", "INVERTFILL", "NOTDEFINED", "USERDEFINED"]}, {"name": "IfcGeoScienceElement", "supertype": "IfcElement", "attributes": [], "is_abstract": true}, {"name": "IfcGeoScienceElementType", "supertype": "IfcElementType", "attributes": [], "is_abstract": true}, {"name": "IfcGeoScienceFeature", "supertype": "IfcGeoScienceElement", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcGeoScienceFeatureTypeEnum"}], "is_abstract": false}, {"name": "IfcGeoScienceFeatureType", "supertype": "IfcGeoScienceElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcGeoScienceFeatureTypeEnum"}], "is_abstract": false}, {"name": "IfcGeoScienceFeatureTypeEnum", "enumeration_items": ["CONTACT", "DISCRETEDISCONTINUITY", "FAULT", "FLUIDBODY", "FOLD", "GEOLOGICUNIT", "GEOTECHNICALUNIT", "HAZARDAREA", "HYDROGEOUNIT", "NOTDEFINED", "PHYSICALPROPERTYDISTRIBUTION", "PIEZOMETRICWATERLEVEL", "USERDEFINED", "VOIDBODY"]}, {"name": "IfcGeoScienceModel", "supertype": "IfcGeoScienceElement", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcGeoScienceModelTypeEnum"}], "is_abstract": false}, {"name": "IfcGeoScienceModelType", "supertype": "IfcGeoScienceElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcGeoScienceModelTypeEnum"}], "is_abstract": false}, {"name": "IfcGeoScienceModelTypeEnum", "enumeration_items": ["GEOHAZARDMODEL", "GEOLOGYMODEL", "GEOTECHMODEL", "GEOTECHSYNTHESISMODEL", "HYDROGEOMODEL", "NOTDEFINED", "PHYSICALPROPERTYDISTIBUTIONMODEL", "USERDEFINED"]}, {"name": "IfcGeoScienceObservation", "supertype": "IfcObservation", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcGeoScienceObservationTypeEnum"}], "is_abstract": false}, {"name": "IfcGeoScienceObservationTypeEnum", "enumeration_items": ["BOREHOLELOG", "GEOPHYSICALSURVEYRESULT", "INSITUTESTRESULT", "LABTESTRESULT", "LOCALINFORMATION", "MAPPEDFEATURE", "NOTDEFINED", "USERDEFINED"]}, {"name": "IfcGroundReinforcementElement", "supertype": "IfcBuiltElement", "attributes": [{"name": "PredefinedType", "optional": true, "type_of_attribute": "IfcGroundReinforcementElementTypeEnum"}], "is_abstract": false}, {"name": "IfcGroundReinforcementElementType", "supertype": "IfcBuiltElementType", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcGroundReinforcementElementTypeEnum"}], "is_abstract": false}, {"name": "IfcGroundReinforcementElementTypeEnum", "enumeration_items": ["BAR", "BOLT", "FABRIC", "NOTDEFINED", "PILE", "PLATE", "TENDON", "TUBE", "USERDEFINED"]}, {"name": "IfcImprovedGround", "supertype": "IfcEarthworksElement", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcImprovedGroundTypeEnum"}], "is_abstract": false}, {"name": "IfcImprovedGroundTypeEnum", "enumeration_items": ["DEEPMIXED", "DYNAMICALLYCOMPACTED", "FROZEN", "GROUTED", "LATERALLYDRAINED", "NOTDEFINED", "REPLACED", "ROLLERCOMPACTED", "SURCHARGEPRELOADED", "USERDEFINED", "VERTICALLYDRAINED"]}, {"name": "IfcIntegerVoxelData", "supertype": "IfcVoxelData", "attributes": [{"name": "ValueData", "optional": false, "type_of_attribute": "<list [1:?] of <type IfcInteger: <integer>>>"}, {"name": "Unit", "optional": true, "type_of_attribute": "IfcUnit"}], "is_abstract": false}, {"name": "IfcLabelVoxelData", "supertype": "IfcVoxelData", "attributes": [{"name": "ValueData", "optional": false, "type_of_attribute": "<list [1:?] of <type IfcLabel: <string>>>"}], "is_abstract": false}, {"name": "IfcLinearZone", "supertype": "IfcLinearElement", "attributes": [], "is_abstract": true}, {"name": "IfcLogicalVoxelData", "supertype": "IfcVoxelData", "attributes": [{"name": "ValueData", "optional": false, "type_of_attribute": "<list [1:?] of <type IfcLogical: <logical>>>"}], "is_abstract": false}, {"name": "IfcObservation", "supertype": "IfcComplementaryData", "attributes": [], "is_abstract": false}, {"name": "IfcRealVoxelData", "supertype": "IfcVoxelData", "attributes": [{"name": "ValueData", "optional": false, "type_of_attribute": "<list [1:?] of <type IfcReal: <real>>>"}, {"name": "Unit", "optional": true, "type_of_attribute": "IfcUnit"}], "is_abstract": false}, {"name": "IfcRelAssociatesDataset", "supertype": "IfcRelAssociates", "attributes": [{"name": "RelatingDataset", "optional": false, "type_of_attribute": "IfcDatasetSelect"}], "is_abstract": false}, {"name": "IfcTunnel", "supertype": "IfcFacility", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcTunnelTypeEnum"}], "is_abstract": false}, {"name": "IfcTunnelPart", "supertype": "IfcFacilityPart", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcTunnelPartTypeEnum"}], "is_abstract": false}, {"name": "IfcTunnelPartTypeEnum", "enumeration_items": ["CROSSWAY", "NOTDEFINED", "PORTAL", "RINGSECTION", "TUNNELSECTION", "USERDEFINED"]}, {"name": "IfcTunnelTypeEnum", "enumeration_items": ["ACCESSTUNNEL", "BICYCLE", "BYPASS", "MAINTENANCE", "METRO", "NOTDEFINED", "PEDESTRIAN", "RAILWAY", "RAMP", "ROAD", "SHAFT", "UNDERGROUND_FACILITIES", "USERDEFINED", "UTILITIES"]}, {"name": "IfcTunnelTypicalSection", "supertype": "IfcLinearZone", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcTunnelTypicalSectionTypeEnum"}], "is_abstract": false}, {"name": "IfcTunnelTypicalSectionTypeEnum", "enumeration_items": ["EXCAVATIONSUPPORT", "GEOTECH", "NOTDEFINED", "RISK", "USERDEFINED"]}, {"name": "IfcUndergroundExcavation", "supertype": "IfcExcavation", "attributes": [{"name": "PredefinedType", "optional": false, "type_of_attribute": "IfcUndergroundExcavationTypeEnum"}], "is_abstract": false}, {"name": "IfcUndergroundExcavationTypeEnum", "enumeration_items": ["FACEEXCAVATION", "NOTDEFINED", "RADIALEXCAVATION", "USERDEFINED"]}, {"name": "IfcVectorVoxelData", "supertype": "IfcVoxelData", "attributes": [{"name": "ValueData", "optional": false, "type_of_attribute": "<list [1:?] of <entity IfcVector>>"}, {"name": "Unit", "optional": true, "type_of_attribute": "IfcUnit"}], "is_abstract": false}, {"name": "IfcVoxelData", "supertype": "IfcComplementaryData", "attributes": [{"name": "ValueType", "optional": true, "type_of_attribute": "IfcLabel"}], "is_abstract": true}, {"name": "IfcVoxelGrid", "supertype": "IfcSolidModel", "attributes": [{"name": "VoxelSizeX", "optional": false, "type_of_attribute": "IfcNonNegativeLengthMeasure"}, {"name": "VoxelSizeY", "optional": true, "type_of_attribute": "IfcNonNegativeLengthMeasure"}, {"name": "VoxelSizeZ", "optional": true, "type_of_attribute": "IfcNonNegativeLengthMeasure"}, {"name": "NumberOfVoxelsX", "optional": false, "type_of_attribute": "IfcPositiveInteger"}, {"name": "NumberOfVoxelsY", "optional": false, "type_of_attribute": "IfcPositiveInteger"}, {"name": "NumberOfVoxelsZ", "optional": false, "type_of_attribute": "IfcPositiveInteger"}, {"name": "Voxels", "optional": false, "type_of_attribute": "<array [1:?] of <type IfcBoolean: <boolean>>>"}], "is_abstract": false}]

main();
