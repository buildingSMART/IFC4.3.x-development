import os
import re
import sys
import html
import json
import logging

from collections import defaultdict
from copy import deepcopy
from datetime import date

from xmi_document import xmi_document, missing_markdown
from nltk import PorterStemmer
from reversestem import unstem


logging.basicConfig(level=logging.INFO) # filename='app.log', filemode='w'

try:
    fn = sys.argv[1]
    try:
        output_dir = sys.argv[2]
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    logging.warning("Usage: python to_bsdd.py <schema.xml> <output_dir>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
xmi_doc.should_translate_pset_types = False
bfn = os.path.basename(fn)

ps = PorterStemmer()

CHAR_LIMIT = 50
HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(r'\s+')
# CHANGE_LOG_PATTERN = re.compile(r'\{\s*\.change\-\w+\s*\}.+', flags=re.DOTALL)
CURLY_BRACKET_PATTERN = re.compile('{.*?}.*') #also removes all text after curly brackets
FIGURE_PATTERN = re.compile('[^.,;]*(Figure|the figure)[^.,;]*') #removes the sentence when it mentiones a Figure.
LIST_PATTERN = re.compile('[^.,;]*:\s?') #removes the last sentence when it ends with a colon.

WORDS_TO_CATCH = sorted(['current','cost','of','switch','order','recovery','loading','barrier','predefined','reel','basin','fountain','packaged','nozzle','tube','plant',
                         'injection','assisted','element','vertically','vertical','turbine','heating','disassembly','button','component','security','deflector',
                         'cabinet','assembly','actuator','meter','sensor','object','detection','station','depth','controller','terminal','center','frame','electric',
                         'exchangers','wedge','gate','configured','plug','lubricated','parallel','slide','exchange','exchanger','change','outlet','server','plate','expansion',
                         'rail','solar','surcharge','excavation','combustion','draft','mechanical','constant','coil','cooled','cooler','evaporative','pavement','top',
                         'column','traffic','crossing','side','road','vehicle','island','gear','super','event','adiabatic','segment','marker','structure','ground',
                         'channel','pressure','shift','prevention','tray','provision','soil','preloaded','water','cold','hot','cable','domestic','power','generation',
                         'solid','waste','unit','carrier','duct','protection','disconnector','surfacing','breaker','wall','flow','curve','limiter','board','chamber',
                         'panel','acoustic','fire','inspection','transverse','rumble','strip','surface','maintenance','of','pier','system','fixed','hatch','transmission',
                         'network','machine','device','equipment','sound','stud','connector','marking','removal','space','agent','section','inventory','bill','schedule','rate',
                         'void','quantities','compacted','drained','tower','indirect','direct','media','intelligent','rigid','random','marine','compact','tensioner',
                         'operational','intermediate','storage','hooks','area','lift','lifting','forward','natural','radial','gravity','piston','relief','air','track', 'pair',
                         'switching','transition','off','bend','circular','derailer','tracked','roadway','plateau','retention','stock','double','twin','cage','seat',
                         'moving','soft','inlet','symbol','symbolic','toilet','dock','docking','parabolic','bending','transceiver','control','asset','furniture',
                         'contact','centre','motorized','motor','photocopier','generator','engine','point','access','asynchronous','synchronous','single','plaza','wheel','loops',
                         'drive','stop','rates','timer','leakage','time','dryer','framework','roof','induction','topping','alignment','curved','stair','elemented','scaffolding',
                         'electrical','chair','sofa','railway','entrance','secured','cover','manhole','flat','concave','convex','known','cylinder','horizontal','business','issues',
                         'elevated','work','platform','materials','handling','material','effects','health','safety','hazadrous','dust','scaffold','fall','fragile','shock',
                         'environmental','drowning','flooding','very','high','unintended','collapse','working','overhead','considerable','value','driven','defined','unknown',
                         'class','appliance','earth','protective','neutral','disposal','cradle','site','production','transport','repair','whole','lifecycle','siphon',
                         'urgent','procedure','emergency','offsite','very','office','sensors','volume','diffusers','variable','multiple','zone','conduit','temperature','powered',
                         'safety','light','warning','exit','blue','illumination','spark','gap','gas','filled','touch','screen','buttons','auto','transformer','divided','support',
                         'earthing','offload','break','glass','key','operated','manual','pull','cord','exhaust','damper','shell','pump','filter','conveyor','pumps','heat','heated',
                         'speed','fan','bypass','valve','dampers','wet','bulb','reset','exiting','folding','curtain','closed','circuit','dry','open','indicator','shunting','route',
                         'derail','departure','starting','signal','repeating','obstruction','hump','auxiliary','home','distant','block','blocking','approach','mesh','push',
                         'pushing', 'bidirectional','directional','right','left','damper','balancing','combination','earthquake','relay','interface','face','nail','loss',
                         'mounted','unidirectional','blast','damper','centrifugal','backward','inclined','vane','axial','propellor','diatomaceous','earth','reverse','osmosis',
                         'liquefied','petroleum','lightning','shaft','soak','slurry','collector','with','check','commercial','propane','butane','atmospheric','vacuum','wetted',
                         'function','complementary','circuit','fault','lower','inglimit','pulse','converter','running','average','upper','limit','lower','band','dimmer',
                         'position','frost','automatic','www','continuous','positioner','positioning','source','sink','profile','enumerated','content','extinguishing',
                         'photovoltaic','soils','between','central','reserve','shoulder','intersection','parking','passing','audiovisual','shape','co2','conduct','conductor',
                         'conductance','conductivity','obstacle','movement','moisture','radiation','radioactivity','rain','smoke','turnout','closure','wind','aggregates','aggregate',
                         'transporting','roofing','recording','stitch','wire','pair','router','tungsten','filament','gateway','selector','momentary','toggle','vertical','inline',
                         'submersible','sump','waterway','ship','lift','works','wheeled','grouted','indicators','mitigated','unmitigated','delivery','accessible','covering','interfaces',
                         'brightness','driver','sectional','rated','pairs','diameter','fans','supported','stations','carriers','transceivers','currents','classes','relays','curves',
                         'plates','corrugated','tracks','conductors','building','operator','owner','engineer','manager','field','construction','history','weather','station',
                         'consumption','photochemical','ozone','renewable','energy','resource','depletion','stratospheric','layer','destruction','reheat','reference','components',
                         'constraint','name','type','names','types','lrm','relative','window','dome','heavy','applicable','axis','placement','cooker','freestanding','heater','subgrade',
                         'inductor','packet','remote','radio','radioactive','above','dilation','winder','equidistant','switch','feed','pipe','pipes','rotary','hollow','humidity',
                         'concentration','identifier','level','cosine','helmert','sine','viennese','bloss','location','global','local','thickness','direction','fluorescent'], key=len)[::-1]

EXCLUDED_ENTITIES = ['IfcApplication','IfcOwnerHistory','IfcTable','IfcTableColumn','IfcTableRow','IfcChangeActionEnum','IfcGloballyUniqueId','IfcStateEnum','IfcShell','IfcAdvancedFace',
                     'IfcClosedShell','IfcConnectedFaceSet','IfcEdge','IfcEdgeCurve','IfcEdgeLoop','IfcFace','IfcFaceBound','IfcFaceOuterBound','IfcFaceSurface','IfcLoop','IfcOpenShell',
                     'IfcOrientedEdge','IfcPath','IfcPolyLoop','IfcSubedge','IfcTopologicalRepresentationItem','IfcVertex','IfcVertexLoop','IfcVertexPoint','IfcBoundaryNodeConditionWarping',
                     'IfcStructuralLoadConfiguration','IfcStructuralLoadOrResult','IfcStructuralLoadSingleDisplacement','IfcStructuralLoadSingleDisplacementDistortion',
                     'IfcStructuralLoadSingleForceWarping','IfcSurfaceReinforcementArea','IfcGeometricProjectionEnum','IfcGlobalOrLocalEnum','IfcWellKnownTextLiteral',
                     'IfcCoordinateOperation','IfcCoordinateReferenceSystem','IfcGeographicCRS','IfcGeometricRepresentationContext','IfcGeometricRepresentationSubContext','IfcMapConversion',
                     'IfcMapConversionScaled','IfcMaterialDefinitionRepresentation','IfcProductDefinitionShape','IfcProductRepresentation','IfcProjectedCRS','IfcRepresentation',
                     'IfcRepresentationContext','IfcRigidOperation','IfcShapeAspect','IfcShapeModel','IfcShapeRepresentation','IfcStyleModel','IfcStyledRepresentation','IfcTopologyRepresentation',
                     'IfcWellKnownText','IfcCurveInterpolationEnum','IfcExtendedProperties','IfcPreDefinedProperties','IfcProfileTypeEnum','IfcReinforcingBarRoleEnum','IfcReinforcingBarSurfaceEnum',
                     'IfcSectionTypeEnum','IfcArbitraryProfileDefWithVoids','IfcProfileProperties','IfcReinforcementBarProperties','IfcSectionProperties','IfcSectionReinforcementProperties',
                     'IfcLayeredItem','IfcLightDistributionCurveEnum','IfcLightEmissionSourceEnum','IfcLightDistributionData','IfcLightIntensityDistribution','IfcLightSourceAmbient',
                     'IfcLightSourceDirectional','IfcLightSourceGoniometric','IfcLightSourcePositional','IfcLightSourceSpot','IfcPresentationLayerAssignment','IfcPresentationLayerWithStyle',
                     'IfcBoxAlignment','IfcTextPath','IfcAnnotationFillArea','IfcPlanarBox','IfcPlanarExtent','IfcPresentationItem','IfcTextLiteral','IfcTextLiteralWithExtent','IfcBinary',
                     'IfcBoolean','IfcDerivedUnitEnum','IfcIdentifier','IfcInteger','IfcLabel','IfcLogical','IfcPHMeasure','IfcPositiveInteger','IfcReal','IfcSIPrefix','IfcSIUnitName','IfcText',
                     'IfcUnitEnum','IfcConversionBasedUnitWithOffset','IfcDerivedUnitElement','IfcDimensionalExponents','IfcUnitAssignment','IfcDirectionSenseEnum','IfcLayerSetDirectionEnum',
                     'IfcArcIndex','IfcAxis2Placement','IfcBSplineCurveForm','IfcBSplineSurfaceForm','IfcCurveOnSurface','IfcDimensionCount','IfcKnotType','IfcLineIndex',
                     'IfcPreferredSurfaceCurveRepresentation','IfcTransitionCode','IfcVectorOrDirection','IfcAxis1Placement','IfcAxis2Placement2D','IfcAxis2Placement3D','IfcAxis2PlacementLinear',
                     'IfcBSplineCurveWithKnots','IfcDirection','IfcBSplineSurface','IfcBSplineSurfaceWithKnots','IfcBoundedSurface','IfcClothoid','IfcCompositeCurveOnSurface',
                     'IfcCompositeCurveSegment','IfcConic','IfcCosineSpiral','IfcCurveBoundedPlane','IfcCurveBoundedSurface','IfcCurveSegment','IfcCylindricalSurface','IfcElementarySurface',
                     'IfcGeometricRepresentationItem','IfcMappedItem','IfcOffsetCurve2D','IfcOffsetCurve3D','IfcOffsetCurveByDistances','IfcPlacement','IfcPointByDistanceExpression',
                     'IfcPointOnSurface','IfcRationalBSplineCurveWithKnots','IfcRationalBSplineSurfaceWithKnots','IfcRectangularTrimmedSurface','IfcReparametrisedCompositeCurveSegment',
                     'IfcRepresentationItem','IfcRepresentationMap','IfcSecondOrderPolynomialSpiral','IfcSegment','IfcSeventhOrderPolynomialSpiral','IfcSineSpiral','IfcSphericalSurface',
                     'IfcSurfaceOfLinearExtrusion','IfcSurfaceOfRevolution','IfcSweptSurface','IfcThirdOrderPolynomialSpiral','IfcToroidalSurface','IfcBooleanOperand','IfcBooleanOperator',
                     'IfcAdvancedBrep','IfcAdvancedBrepWithVoids','IfcBlock','IfcBooleanClippingResult','IfcBooleanResult','IfcBoundingBox','IfcBoxedHalfSpace','IfcCsgPrimitive3D',
                     'IfcExtrudedAreaSolidTapered','IfcFaceBasedSurfaceModel','IfcFacetedBrep','IfcFacetedBrepWithVoids','IfcGeometricCurveSet','IfcGeometricSet','IfcIndexedPolygonalFace',
                     'IfcIndexedPolygonalFaceWithVoids','IfcManifoldSolidBrep','IfcPolygonalBoundedHalfSpace','IfcPolygonalFaceSet','IfcRectangularPyramid','IfcRevolvedAreaSolidTapered',
                     'IfcRightCircularCone','IfcRightCircularCylinder','IfcSectionedSolidHorizontal','IfcSectionedSpine','IfcSectionedSurface','IfcShellBasedSurfaceModel','IfcSolidModel',
                     'IfcSphere','IfcSweptDiskSolidPolygonal','IfcTessellatedFaceSet','IfcTessellatedItem','IfcTriangulatedFaceSet','IfcTriangulatedIrregularNetwork','IfcAlignmentCantSegmentTypeEnum',
                     'IfcAlignmentHorizontalSegmentTypeEnum','IfcAlignmentVerticalSegmentTypeEnum','IfcPointOrVertexPoint','IfcSolidOrShell','IfcSurfaceOrFaceSurface','IfcAlignmentCantSegment',
                     'IfcAlignmentHorizontalSegment','IfcAlignmentParameterSegment','IfcAlignmentVerticalSegment','IfcGridAxis','IfcGridPlacement','IfcLinearPlacement','IfcLocalPlacement',
                     'IfcObjectPlacement','IfcVirtualGridIntersection','IfcDocumentConfidentialityEnum','IfcLanguageId','IfcDocumentStatusEnum','IfcClassification','IfcDataOriginEnum','IfcDate',
                     'IfcDateTime','IfcDuration','IfcRecurrenceTypeEnum','IfcTaskDurationEnum','IfcTime','IfcTimeSeriesDataTypeEnum','IfcTimeStamp','IfcEventTime','IfcIrregularTimeSeries','IfcLagTime',
                     'IfcRecurrencePattern','IfcRegularTimeSeries','IfcResourceTime','IfcSchedulingTime','IfcTaskTime','IfcTaskTimeRecurring','IfcTimePeriod','IfcTimeSeries','IfcWorkTime',
                     'IfcArithmeticOperatorEnum','IfcBenchmarkEnum','IfcConstraintEnum','IfcLogicalOperatorEnum','IfcObjectiveEnum','IfcConstraint','IfcMetric','IfcObjective','IfcApproval',
                     'IfcAddressTypeEnum','IfcRoleEnum','IfcAddressTypeEnum','IfcRoleEnum','IfcActorRole','IfcAddress','IfcOrganization','IfcPerson','IfcPersonAndOrganization','IfcPostalAddress',
                     'IfcTelecomAddress','IfcCurve','IfcCircle','IfcEllipse','IfcLine','IfcPlane','IfcPoint','IfcPolyline','IfcSpiral','IfcSurface','IfcVector']

# ALLOW:  IfcRoot, IfcLightSource, IfcStructuralLoad, IfcStructuralLoadLinearForce, IfcStructuralLoadPlanarForce, IfcStructuralLoadSingleForce, IfcStructuralLoadStatic, IfcStructuralLoadTemperature

ALL_CAPS = ['ups','gprs','rs','am','gps','dc','tn','url','ac','co','co2','chp','id','led','oled','ole','gfa','tv','msc','ppm','iot','ocl','lrm','cgt','teu','tmp','std','gsm','cdma','lte','td','scdma',
            'wcdma','sc','mp','bm','ol','ep','ir','www','ip','ph','usb', 'ii', 'iii','url','uri','ssl','ffl','ty','tz','tx']

SMALL_CAPS = ['for','of','and','to','with','or','at']

SUBSTITUTIONS = {
    "Rel ": "Relation: ",
    "Qto_": "Quantity set: ",
    "Pset_": "Property set: ",
}

TYPE_TO_VALUES= {
    # 'boolean': ["TRUE","FALSE"],
    'logical': ["TRUE","FALSE","UNKNOWN"],
}

### shows the schema name if needed (e.g. IFC4X3_ADD2)
# schema_name = xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Package"][0].name.replace("exp", "").upper()
# schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
# schema_name = re.sub(r"_+", "_", schema_name)
# schema_name = schema_name.strip('_')


def yield_parents(node):
    """ Find all the parent elements if available """
    yield node
    if node.parentNode:
        yield from yield_parents(node.parentNode)


def get_path(xmi_node):
    """ Find the element's path in the XML tree """
    nodes = list(yield_parents(xmi_node.xml))

    def get_name(n):
        """ Find element's name in the XML """
        if n.attributes:
            v = n.attributes.get('name')
            if v: return v.value

    node_names = [get_name(n) for n in nodes]
    return node_names[::-1]

# included_packages = set(("IFC 4.2 schema (13.11.2019)", "Common Schema", "IFC Ports and Waterways", "IFC Road", "IFC Rail - PSM"))

# def skip_by_package(element):
#     return not (set(get_path(xmi_doc.by_id[element.idref])) & included_packages)


def reduce_description(s, trim=True):
    """ Remove all the unnecesarry characters, strip <html sections>, and trim the description to bare minimum. """
    try:
        s = html.unescape(s)
    except TypeError:
        # error when name contains link, for example: "https://github.com/buildingSMART/IFC4.3.x-development/edit/master/docs/schemas/core/IfcProductExtension/Types/IfcAlignmentTypeEnum.md#L0 has no content"
        s = ''
    if trim:
        # split and remove on keywords:        
        j = re.search(r'\$\$', s).start() if re.search(r'\$\$', s) else -1
        k = re.search(r'(Base|General) formula', s).start() if re.search(r'(Base|General) formula', s) else -1
        i = min([x for x in [s.find('NOTE'), s.find('DIAGRAM'), s.find('CHANGE'), s.find('IFC4'), s.find('HISTORY'), s.find('REFERENCE'), s.find('EXAMPLE'), s.find('DEPRECATION'), j, k, 1e5] if x >= 0])
        if i > 0 and i != 1e5:
            s = s[:i]
        elif i==0:
            # some descriptions start with History or Note. Don't want them.
            s = ""
    s = re.sub('[*]{2}', ' ', s)
    s = re.sub('\n', '; ', s)
    s = re.sub(':', ': ', s)
    s = re.sub(HTML_TAG_PATTERN, ' ', s)
    s = re.sub(CURLY_BRACKET_PATTERN, ' ', s)
    s = re.sub(r'SELF\\', '', s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(FIGURE_PATTERN, '', s)
    s = re.sub(LIST_PATTERN, '', s)
    s = re.sub(MULTIPLE_SPACE_PATTERN, ' ', s).strip()
    s = re.sub(r'(?<!\.)\.\.(?!\.)', '.', s).strip()
    # TODO too long description...
    # sx = re.sub('e.g.', "", re.sub('i.e.', "", re.sub('etc.', "", s9)))
    # if len(sx.split(".")) > 6:
    #     s9 = s9.split(sx.split(".")[6])[0] + "[IT WAS CUT HERE!]"
    return clean(s)


def caps_control(s):
    """ Turn special words to all caps or small caps using hard-coded lists.
    E.g. Usb -> USB, With -> with """
    s1 = s.split()
    if isinstance(s1, list):
        for part in s1:
            for a in ALL_CAPS:
                if part.lower() == a:
                    s = re.sub(part, a.upper(), s)
            for b in SMALL_CAPS:
                if part.lower() == b:
                    s = re.sub(part, b.lower(), s)
    return s


def split_at_word(w, s):
    """ Try spliting the string s with the word w. Return string s splited with whitespaces. """
    if w != '' and ((ps.stem(w) in s.lower()) or (w in s.lower())):
        # to_keep=False
        # for wtk in words_to_keep:
        #     if wtk in s.lower():
        #         to_keep=True
        # if not to_keep:
        if w in s.lower():
            s = re.sub(w, " "+w+" ", s.lower())
        else: 
            vs = unstem(ps.stem(w))
            if isinstance(vs, dict):
                # turn dict to flat list
                vsl = []
                for key, val in vs.items():
                    vsl.append(key)
                    if val:
                        for v in val:
                            vsl.append(v)
                vs = vsl
            if vs:
                vs.append(ps.stem(w))
                vs = sorted(vs, key=len)[::-1]
                for v in vs:
                    if v in s.lower():
                        s = re.sub(w, " "+w+" ", s.lower())
                        break
    if isinstance(s, list):
        s = " ".join(s)
    return s


def split_words(s):
    """ Split the phrase using the hard-coded list of words found in enumerations to split the ALLCAPS phrases into indivudual words. """
    found_words = []
    for w in WORDS_TO_CATCH:
        # skip if word is contained in previous words (e.g. EXCHANGE in EXCHANGER)
        previously_found = False
        for fw in found_words:
            if w in fw:
                previously_found = True
        if not previously_found:
            s2 = deepcopy(s)
            s2 = split_at_word(w, s2)
            if s2 != s:
                found_words.append(w)
                s = s2
    s = re.sub("_", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def to_str(s):
    """ Turn to string in case it finds a defaultdict or similar """
    if isinstance(s, str):
        return s
    elif isinstance(s, defaultdict):
        if len(dict(s)) == 0: 
            return ""
        else:
            logging.warning("Skipped the term, default dict: " + str(s))
            return ""
    elif isinstance(s, missing_markdown):
        logging.warning("Skipped the term, missing markdown in: " + str(s))
        return ""
    elif isinstance(s, dict):
        if not s:
            # value is an empty dictionary
            return ""
        else:
            logging.warning("Unempty dictionary passed as a value: " + s)
            return str(s)
    else:
        logging.warning("Skipped the term, unknown problem in: " + str(s))
        return ""


def quote(s):
    """ Add quotation around certain words. """
    return '"%s"' % to_str(s)


def annotate(s):
    """ Add double brackets [[...]] around certain words. """
    return re.sub(all_codes, lambda match: "[[%s]]" % match.group(0), to_str(s))


def normalise(s):
    """ format the text by spliting camelCase into separate words and replacing special prefixes."""
    s = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', to_str(s))
    for k,v in SUBSTITUTIONS.items():
        if k in s:
            s = re.sub(k,v,s)
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', s).strip()


def clean(s):
    """ format the text by removing unwanted characters."""    
    # remove all redundant characters (except those listed):
    cleaned = ''.join(['', c][c.isalnum() or c in ':.,()-+ —=;α°_/!?$%@<>\'"\\*'] for c in to_str(s))
    cleaned = re.sub('"',"'", cleaned)
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', cleaned).strip()
    

def generalization(pe):
    """ Finds a partent object if possible """
    try:
        P = xmi_doc.xmi.by_id[(pe|"generalization").general]
    except:
        P = None
    if P: 
        return generalization(P)
    else: 
        return pe


def need_brackets(s):
    """ Verify if that name should be annotated with brackets in other definitions.
      The criteria: minium 4 letters (skip 'ABC')."""
    if len(s) >= 4:
        return True
    else:
        return False
    # and at least 2 capital letters (skip 'Width' etc.).
    # if re.findall(r'\b(?:[a-zA-Z]*[A-Z]){2,}[a-zA-Z]*\b', s):
    #     return True
    

def list_ancestors(name, full_list, ancestor_list=[]):
    """ traverse the list of hierarchy to find all the parents of this object """
    try:
        ancestor = full_list[name]['Parent']
    except KeyError:
        logging.warning('The entity %s not found in the IFC.' % name)
    if ancestor:
        if ancestor in full_list:
            ancestor_list.append(ancestor)
            list_ancestors(ancestor, full_list, ancestor_list)
        else:
            logging.warning('Ancestor %s not found in the IFC.' % ancestor)
    return ancestor_list


def filter_concepts(di):
    """ Skip certain concepts to reduce amount of definitions in bSDD. """

    # children = defaultdict(list)    
    # for k, v in di.items():
    #     if v.get("Parent"):
    #         children[v.get("Parent")].append(k)

    def parents(k):
        yield k
        v = di.get(k)
        if v and v.get('Parent'):
            yield from parents(v.get('Parent'))
            
    # def child_or_self_has_psets(k):
    #     ps = di.get(k, {}).get("Psets")
    #     if ps:
    #         if set(ps.keys()) - {"Attributes"}:
    #             return True
    #     for c in children[k]:
    #         if child_or_self_has_psets(c):
    #             return True
    #     return False
        
    # def has_child(k):
    #     def has_child_(k2):
    #         if k2 == k: return True
    #         if not children[k2]: return False
    #         return any(has_child_(c) for c in children[k2])
    #     return has_child_

    def should_include(k, v):
        # PREVIOUSLY return ("IfcProduct" in parents(k)) or has_child("IfcProduct")(k) or child_or_self_has_psets(k) 
        # but decided to widen to also include all non-products that have psets, like IfcActor.
        # return ("IfcRoot" in parents(k)) or ("IfcMaterialDefinition" in parents(k)) or ("IfcProfileDef" in parents(k)) or child_or_self_has_psets(k)
        # Now skipping relations ('IfcRelAssociatesClassification'), types ('IfcWallType'), property definitions ('IfcPropertySingleValue'), Resources and some other abstract concepts. 
        result = False
        if not (k.startswith(('IfcRel','IfcProperty','IfcProperty','IfcQuantity','IfcConnection','IfcCartesian')) or k.endswith(('Relationship','Type','Definition','Usage','Property','Template','Resource','Select','Measure','Condition','ProfileDef','Value','Property','Quantity','Unit','Curve','Number','Reference','Information','Solid')) or any(x in parents(k) for x in ["IfcPropertyAbstraction","IfcConstraint","IfcRepresentationItem","IfcPresentationItem","IfcPresentationStyle","IfcPropertyDefinition","IfcTypeObject","IfcMaterialDefinition","IfcMaterialUsageDefinition"]) or any(z.endswith("Resource") for z in parents(k)) or (k in EXCLUDED_ENTITIES)):
            result = True
        # bypass for selected classes:
        elif k in ('IfcMaterial'): #,'IfcLightSource','IfcBoundingBox','IfcPoint','IfcCurve','IfcSegment','IfcDirection','IfcSurface','IfcVector'):
            result = True
        return result
    return {k: v for k, v in di.items() if should_include(k, v)}


def guid_by_id(id):
    """ add guid information (not the document ID, but IFC_DOC GUID) """
    try:
        guid = xmi_doc.guids[id]
    except KeyError:
        guid = ""
    return guid


def is_deprecated(elem):
    """ Check if the element is deprecated in that IFC version or not. """
    deprecated = False
    if elem.id in xmi_doc.deprecated:
        deprecated = True
    # some objects don't have deprecated status but their markdown says they are deprecated   
    try: 
        if "DEPRECAT" in elem.markdown:
            deprecated = True
    except (AttributeError, TypeError):
        pass
    return deprecated


def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    make_defaultdict = lambda: defaultdict(make_defaultdict)
    classes = defaultdict(make_defaultdict)
    

    def get_parent_of_pt(enum_type):
        enum_id = enum_type.idref
        type_refs = []
        for assoc in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
            try:
                c1, c2 = assoc/'ownedEnd'
            except ValueError as er:
                logging.error("Encountered exception `%s' on %s" % (er, assoc))
                continue
            assoc_type_refs = set(map(lambda c: (c|"type").idref, (c1, c2)))
            if enum_id in assoc_type_refs:
                other_idref = list(assoc_type_refs - {enum_id})[0]
                type_refs.append(xmi_doc.xmi.by_id[other_idref].name)
                
        # TODO filter this based on inheritance hierarchy
        type_refs_without_type = [s for s in type_refs if 'Type' not in s]
        
        return type_refs_without_type[0] if type_refs_without_type else None
    
  
    by_id = {}
    item_by_id = {}
    psets = [] # psets are deferred to the end so that all ids are resolved  
    entities = [] # same for entity attributes:
    enumerations = {} # predefined types are just normal enumerations
    pset_counts_by_stereo = defaultdict(int)
    
    ### extract all items from XML

    for item in xmi_doc:

        item_by_id[item.id] = item

        item.name = to_str(item.name)

        if not is_deprecated(item):
            if item.type in ("ENUM","PENUM"):
                enumerations[item.name] = item
            elif item.type == "PSET":
                psets.append(item)
                stereo = (item.node/"properties")[0].stereotype
                pset_counts_by_stereo[stereo] += 1
            elif item.type == "ENTITY":                
                by_id[item.id] = di = classes[item.name]
                st = item.meta.get('supertypes', [])
                if st:
                    di["Parent"] = to_str(st[0])
                di["Definition"] = reduce_description(to_str(item.markdown_definition), trim=True)
                # add human-readable name
                di["Name"] = caps_control(clean(normalise((item.name[3:] if item.name.lower().startswith('ifc') else item.name))).title())
                di["Guid"] = guid_by_id(item.id)
                entities.append(item)
                di["Package"] = to_str(item.package) # solely to split POT files
            # skipping: ('FUNCTION','SELECT','RULE','TYPE')

    ### process all found predefined types (entities) 

    for item in entities:

        if "IfcTypeObject" in xmi_doc.supertypes(item.id):
            continue
    
        predefined_type_attribute = [c for c in item.children if c.name == "PredefinedType"]
        if predefined_type_attribute:
            # NB this points to the EA extension node and not the packagedElement
            ptype = (predefined_type_attribute[0].node|"properties").type
            if ptype in enumerations:
                for c in enumerations[ptype].children:
                    if c.name not in ("USERDEFINED","NOTDEFINED"):
                        by_id[c.id] = di = classes[item.name + c.name]
                        di["Parent"] = to_str(item.name)
                        di["Definition"] = reduce_description(to_str(c.markdown), trim=True)
                        di["Description"] = "Technical note: Because this class is a 'Predefined Type' in IFC, meaning a specialisation of its parent class, in IFC it should be represented by the parent class, with all the relevant properties and attributes."
                        # add human-readable name, by identifying words in all-caps phrase (right now the words are hardcoded)
                        di["Name"] = caps_control(split_words(c.name).title())
                        di["Guid"] = guid_by_id(c.id)
                        di["Package"] = to_str(item.package) # solely to split POT files

    ### process all found property sets 

    for pset in psets:
        refs = set(pset.meta.get('refs') or [])
        
        for id in refs:
        
            if isinstance(id, tuple):
                # In case of TypeObject+PredefinedType appl
                # id = id[0]
                # what to do with typedrivenonly?
                # this option is disabled now
                assert False
                continue
            
            # find the relevant item (dictionary)
            di = by_id.get(id)
            if di is None:
                try:
                    log_attr_2 = xmi_doc.xmi.by_id[id].name
                    logging.warning("for %s entity %s not emitted" % (pset.name, log_attr_2))
                except KeyError:
                    log_attr_2 = id
                    logging.warning("id %s not found" % id)
                continue
            
            for a, (nm, (ty_ty_arg)) in zip(pset.children, pset.definition):

                if not is_deprecated(a):
                    if pset.stereotype == "QSET":
                        type_name = "real"
                        type_values = None
                        kind_name = 'Single'
                    else:
                        ty, ty_arg = ty_ty_arg
                        if ty == "PropertyEnumeratedValue":
                            type_name = list(ty_arg.values())[0]
                            enum_types_by_name = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                            enum_types_by_name += [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Enumeration"] if c.name == type_name]
                            type_values = [x.name for x in enum_types_by_name[0]/"ownedLiteral"]
                            kind_name = 'Single'
                        else:
                            type_name = list(ty_arg.values())[0]
                            pe_types = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                            pe_types += [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:DataType"] if c.name == type_name]                    
                            pe_type = pe_types[0]
                            root_generalization = generalization(pe_type)
                            type_name = root_generalization.name #.lower()
                            type_values = None
                            if ty == "PropertySingleValue":
                                kind_name = 'Single'
                            elif ty == "PropertyBoundedValue":
                                kind_name = 'Range'
                            elif ty == "PropertyReferenceValue":
                                kind_name = 'Complex'
                                di["Psets"][pset.name]["Properties"][a.name]["Description"] = "Technical note: this is a specific property from IFC that takes as its value a reference to %s. Read the IFC documentation for more information." % type_name
                            elif ty == "PropertyListValue":
                                kind_name = 'List'
                            elif ty == "PropertyTableValue":
                                kind_name = 'Complex'
                                di["Psets"][pset.name]["Properties"][a.name]["Description"] = "Technical note: this is a specific property from IFC that takes a table as its value. That table has two columns (lists), one with definitions and other for defined values. Read the IFC documentation for more information."
                            else:
                                logging.warning("%s.%s of type %s <%s> not mapped" % (pset.name, nm, ty, ",".join(map(lambda kv: "=".join(kv), ty_arg.items()))))
                                continue

                    di["Psets"][pset.name]["Definition"] = re.sub(r":\s*[A-Z]{2,}.*", '...', reduce_description(to_str(pset.markdown_definition), trim=True))
                    
                    di["Psets"][pset.name]["Properties"][a.name]["Type"] = type_name
                    di["Psets"][pset.name]["Properties"][a.name]["Name"] = caps_control(clean(split_words(normalise(a.name))).title())
                    # remove value explanation from the definition
                    di["Psets"][pset.name]["Properties"][a.name]["Definition"] = re.sub(r":\s*[A-Z]{2,}.*", '...', reduce_description(to_str(a.markdown), trim=True))
                    di["Psets"][pset.name]["Properties"][a.name]["Kind"] = kind_name
                    di["Psets"][pset.name]["Properties"][a.name]["Package"] = to_str(pset.package) # solely to split POT files

                    if type_values is None:
                        type_values = TYPE_TO_VALUES.get(type_name)
                    if type_values:
                        di["Psets"][pset.name]["Properties"][a.name]["Values"] = []
                        for tv in type_values:                       
                            # match the whole sentence containing the value, case insensitive
                            matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(a.markdown), flags=re.IGNORECASE)
                            if matches:
                                description = reduce_description(matches[0].strip())  #the whole sentence explaining the value
                            else:
                                description = caps_control(clean(normalise(split_words(tv))).title())  #the value but readable
                            di["Psets"][pset.name]["Properties"][a.name]["Values"].append({"Value": tv,"Description":description,"Package":to_str(pset.package)})

    ### process all found entities 

    for item in entities:

        item_name = item.name
        if item_name.endswith("Type"):
            item_name = item_name[:-4]
        di = classes[item_name]        
        
        for c in item.children:
                           
            c.name = reduce_description(c.name)

            if not is_deprecated(c):
                try:
                    node = c.node
                    if node.xml.tagName == "attribute":
                        node = xmi_doc.xmi.by_id[c.node.idref]
                        type_type = node|"type"
                        type_id = type_type.idref
                    else:
                        type_id = ([t for t in (node/"ownedEnd") if t.name == c.name][0]|"type").idref
                        type_type = xmi_doc.xmi.by_id[type_id]
                    type_item = item_by_id[type_id]
                except:
                    logging.warning("Not emitting %s.%s because of an error" % (item.name, c.name))
                    continue
                if c.name == "PredefinedType":
                    logging.warning("Not emitting %s.%s because it's the PredefinedType attribute" % (item.name, c.name))
                elif type_item.type == "ENTITY":
                    logging.warning("Not emitting %s.%s attribute because it's taking an ENTITY: %s" % (item.name, c.name, type_item.name))
                elif type_item.type == "SELECT":
                    logging.warning("Not emitting %s.%s attribute because it's taking a SELECT: %s" % (item.name, c.name, type_item.name))
                elif type_item.type == "TYPE":
                    
                    type_values = None
                    
                    if type_item.definition.super_verbatim:
                    
                        if not type_item.definition.super.lower().startswith("string"):                    
                            logging.warning("Not emitting %s.%s because it has a hardcoded express definition %s" % (item.name, c.name, type_item.definition.super))
                            continue
                        else:
                            type_name = "string"
                            
                    else:
                    
                        pattr = xmi_doc.xmi.by_id[c.node.idref]
                        ty_id = (pattr|"type").idref
                        ty_pe = xmi_doc.xmi.by_id[ty_id]
                        ty_gen = generalization(ty_pe)
                        type_name = ty_gen.name.lower()
                    
                    di["Psets"]["Attributes"]["Properties"][c.name]["Type"] = type_name
                    di["Psets"]["Attributes"]["Properties"][c.name]["Name"] = caps_control(clean(split_words(normalise(c.name))).title())
                    # remove value explanation from the definition
                    di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = re.sub(r":\s*[A-Z]{2,}.*", '...', reduce_description(to_str(c.markdown), trim=True))
                    di["Psets"]["Attributes"]["Properties"][c.name]["Package"] = to_str(item.package) # solely to split POT files
                    if type_values is None:
                        type_values = TYPE_TO_VALUES.get(type_name)
                    if type_values:
                        di["Psets"]["Attributes"]["Properties"][c.name]["Values"] = []
                        for tv in type_values:
                            # match the whole sentence containing the value, case insensitive
                            # matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(c.markdown), flags=re.IGNORECASE)
                            matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(c.markdown), flags=re.IGNORECASE)
                            if matches:
                                description = reduce_description(matches[0].strip())  #the whole sentence explaining the value
                            else:
                                description = caps_control(clean(normalise(split_words(tv))).title())  #the value but readable
                            di["Psets"]["Attributes"]["Properties"][c.name]["Values"].append({"Value": tv,"Description":description,"Package":to_str(item.package)})                           

                elif type_item.type == "ENUM":
                
                    type_name = type_item.name
                    type_values = type_item.definition.values
                    di["Psets"]["Attributes"]["Properties"][c.name]["Type"] = type_name
                    # remove value explanation from the definition
                    di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = re.sub(r":\s*[A-Z]{2,}.*", '...', reduce_description(to_str(c.markdown), trim=True))
                    di["Psets"]["Attributes"]["Properties"][c.name]["Values"] = []
                    di["Psets"]["Attributes"]["Properties"][c.name]["Package"] = to_str(item.package) # solely to split POT files
                    for tv in type_values:                   
                        # match the whole sentence containing the value, case insensitive
                        # matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(c.markdown), flags=re.IGNORECASE)
                        matches = re.findall(r"[^.;!,]*" + tv + r"[^.;!,]*", to_str(c.markdown), flags=re.IGNORECASE)
                        if matches:
                            description = reduce_description(matches[0].strip())  #the whole sentence explaining the value
                        else:
                            description = caps_control(clean(normalise(split_words(tv))).title())  #the value but readable
                        di["Psets"]["Attributes"]["Properties"][c.name]["Values"].append({"Value": tv,"Description":description,"Package":to_str(item.package)})
                else:
                    logging.warning("Not emitting %s.%s because it's a %s %s" % (item.name, c.name, type_item.name, type_item.type))
            
    for k, v in pset_counts_by_stereo.items():
        logging.info(k + ":", v)
        
    logging.info("TOTAL:", sum(pset_counts_by_stereo.values()))
            
    return classes

    
### Generate all the definitions:

all_concepts = filter_concepts(generate_definitions())


### iterate all the results to list all unique codes for translations

codes = set() #["USERDEFINED", "NOTDEFINED"]  # adding those two to be translatable values, as they occur in descriptions but will not be listed in bSDD.
for code, content in all_concepts.items(): 
    if need_brackets(code):
        codes.add(code)
    if content['Psets']:
        for pset_code, pset_content in content['Psets'].items():
            if need_brackets(pset_code):
                codes.add(pset_code)
            for prop_code, prop_content in pset_content['Properties'].items():
                if need_brackets(prop_code):
                    codes.add(prop_code)
                if prop_content['Values']:
                    for val in prop_content['Values']:
                        if need_brackets(val['Value']):
                            codes.add(val['Value'])

all_codes = re.compile("\\b(%s)\\b" % "|".join(sorted(codes, key=lambda s: -len(s))))


### iterate again to annotate all descriptions and restructure classes/properties/values:

classes = []
psets = []
props = []
props = []
to_translate = []
unique_props = set()
unique_psets = set()

for code, content in all_concepts.items(): 
    clas_def = annotate(content['Definition'])

    classes.append({
        'Code': code[0:CHAR_LIMIT],
        'Name': to_str(content['Name']) if to_str(content['Name']) else caps_control(clean(normalise((code[3:] if code.lower().startswith('ifc') else code))).title()),
        'Definition': clas_def,
        'ClassType': 'Class',
        'ClassProperties': []
    })

    if content['Guid']:
        classes[-1]['Uid'] = to_str(content['Guid'])
    if content['Parent']:
        classes[-1]['ParentClassCode'] = to_str(content['Parent'])
    if content['Description']:
        classes[-1]['Description'] = to_str(content['Description'])
        to_translate.append({"msgid":code[0:CHAR_LIMIT]+"_DESCRIPTION","msgstr":classes[-1]['Description'],"package":content['Package']})

    to_translate.append({"msgid":code[0:CHAR_LIMIT],"msgstr":classes[-1]['Name'],"package":content['Package']})
    to_translate.append({"msgid":code[0:CHAR_LIMIT]+"_DEFINITION","msgstr":clas_def,"package":content['Package']})

    # list all ancestors (skip enums (any code that has at least three consecutive capital letters), they don't need to inherit any properties) 
    if re.search(r"[A-Z]{3}", code):
        ancestors = []
    else:
        ancestors = [code]
        ancestors = list_ancestors(code, all_concepts, ancestors)

    unique_p_codes = set()

    # add properties (from this object and all its parents)
    for ancestor_name in ancestors:
        ancestor = all_concepts[ancestor_name]
        # if ancestor['Psets']:
        if ancestor['Psets']:
            for pset_code, pset_content in ancestor['Psets'].items():
                
                # add PSet as GroupOfProperties class:
                if not ((pset_code in unique_psets) or (pset_code == 'Attributes')):
                    unique_psets.add(pset_code)
                    psets.append({
                        'Code': pset_code[0:CHAR_LIMIT],
                        'Name': to_str(pset_content['Name']) if to_str(pset_content['Name']) else caps_control(clean(normalise(pset_code))).title(),
                        'Definition': annotate(pset_content['Definition']),
                        'ClassType': 'GroupOfProperties',
                        'ClassProperties': []
                    })
                    to_translate.append({"msgid":pset_code[0:CHAR_LIMIT],"msgstr":psets[-1]['Name'],"package":content['Package']})
                    to_translate.append({"msgid":pset_code[0:CHAR_LIMIT]+"_DEFINITION","msgstr":psets[-1]['Definition'],"package":content['Package']})
                
                # add ClassProperties
                for prop_code, prop_content in pset_content['Properties'].items():
                    prop_code = prop_code[0:CHAR_LIMIT]
                    name = to_str(prop_content['Name'])
                    if not name:
                        name = normalise(prop_code)
                    prop_def = annotate(prop_content['Definition'])
                    # property code must be unique for a given class and not longer than 50 characters
                    if len(prop_code)+len(pset_code) < 50: 
                        p_code = prop_code+"_from_"+re.sub('Pset_|Qto_','',pset_code)
                    # special treatment of 5 psets that result in duplicated codes:
                    elif prop_code in ("AdjustmentDesignation","IsCurrentTolerancePositiveOnly") and pset_code in ("Pset_ProtectiveDeviceTrippingUnitTimeAdjustment","Pset_ProtectiveDeviceTrippingUnitCurrentAdjustment","Pset_ProtectiveDeviceTrippingFunctionGCurve","Pset_ProtectiveDeviceTrippingFunctionICurve","Pset_ProtectiveDeviceTrippingFunctionICurve"):
                        p_code = prop_code+"_from_..."+''.join([c for c in pset_code if c.isupper()])
                    else:
                        # p_code = prop_code+"_"+pset_code[5:51-len(prop_code)]+"..."
                        p_code = prop_code+"_from_"+re.sub('Pset_|Qto_','',pset_code)[:int((41-len(prop_code))/2)]+"..."+re.sub('Pset_|Qto_','',pset_code)[len(re.sub('Pset_|Qto_','',pset_code))-int((41-len(prop_code))/2):]
                    classProp = {                   
                        "PropertyCode": prop_code[0:CHAR_LIMIT],
                        "Code": p_code[0:CHAR_LIMIT],
                        "PropertySet": pset_code[0:CHAR_LIMIT]
                        # Skip description and name as it should inherit from a Property.
                        # "Description": name + " – " + prop_def + ". IFC type: " + prop_content['Type'] + ". " + annotate(prop_content['Description']),
                        # "PropertyValueKind": prop_content['Type'],
                        }
                    
                    # 
                    if not p_code in unique_p_codes: 
                        classes[-1]['ClassProperties'].append(classProp)
                        unique_p_codes.add(p_code)
                    try:
                        if pset_code == psets[-1]['Code']:
                            if not any(classProp['PropertyCode'] == cp.get('PropertyCode')[0:CHAR_LIMIT] for cp in psets[-1]['ClassProperties']):
                                psets[-1]['ClassProperties'].append(classProp)
                    except IndexError:
                        pass
                    
                    # add to properties list, not just classProp
                    if not prop_code in unique_props:
                        unique_props.add(prop_code)

                        props.append({                   
                            "Code": prop_code[0:CHAR_LIMIT],
                            "Name": name,
                            "Definition": prop_def,
                            "PropertyValueKind": to_str(prop_content['Kind'])
                        })
                        to_translate.append({"msgid":prop_code[0:CHAR_LIMIT],"msgstr":name,"package":content['Package']})
                        to_translate.append({"msgid":prop_code[0:CHAR_LIMIT]+"_DEFINITION","msgstr":prop_def,"package":content['Package']})

                        if prop_content['Values'] and prop_content['Type'].lower() != "boolean":
                            allowed_values = []
                            for val in prop_content['Values']:
                                descr = annotate(val['Description'])
                                allowed_values.append({
                                    'Code': val['Value'][0:CHAR_LIMIT],
                                    'Value': val['Value'],
                                    'Description': descr
                                })
                                to_translate.append({"msgid":prop_code[0:CHAR_LIMIT]+"_"+val['Value'],"msgstr":descr,"package":content['Package']})
                            props[-1]['AllowedValues'] = allowed_values

                        if prop_content['Description']:
                            props[-1]['Description'] = annotate(prop_content['Description'])
                            to_translate.append({"msgid":prop_code[0:CHAR_LIMIT]+"_DESCRIPTION","msgstr":props[-1]['Description'],"package":content['Package']})

                        if prop_content['Type'].lower() == "string":
                            props[-1]['DataType'] = "String"
                        elif prop_content['Type'].lower() in ("real","number"):
                            props[-1]['DataType'] = "Real"
                        elif prop_content['Type'].lower() == "integer":
                            props[-1]['DataType'] = "Integer"
                        elif prop_content['Type'].lower() == "boolean":
                            props[-1]['DataType'] = "Boolean"
                        elif prop_content['Type'].startswith("PEnum_") or prop_content['Type'].endswith("Enum"):
                            # Assuming that all enums are text.
                            props[-1]['DataType'] = "String"
                        else:
                            logging.warning("Not sure what data type to apply to: '%s'." % prop_content['Type'])

classes.extend(psets)



### Generate IFC.json file:

bsdd_data = {
        'ModelVersion': '2.0',
        'OrganizationCode': 'buildingsmart',
        'DictionaryCode': 'ifc',
        'DictionaryName': 'IFC',
        'DictionaryVersion': '4.3',
        'LanguageIsoCode': 'EN',
        'LanguageOnly': False,
        'UseOwnUri': False,
        'License': 'CC BY-ND 4.0',
        'LicenseUrl': 'https://creativecommons.org/licenses/by-nd/4.0/legalcode',
        'MoreInfoUrl': 'https://ifc43-docs.standards.buildingsmart.org/',
        'QualityAssuranceProcedure': 'IFC is a standardized digital description of built environment created by buildingSMART International and its community members. For more information read ISO 16739 and IFC schema documentation.',
        'QualityAssuranceProcedureUrl': 'https://technical.buildingsmart.org/standards/ifc/',
        'ReleaseDate': date.today().strftime(r'%Y-%m-%d'),
        'Classes': classes,
        'Properties': props
    }

# with open(output_dir, 'w', encoding='utf-8') as f:
with open(os.path.join(output_dir, "IFC.json"), 'w', encoding='utf-8') as f :
    json.dump(bsdd_data, f, indent=4, default=lambda x: (getattr(x, 'to_json', None) or (lambda: vars(x)))(), ensure_ascii=False)
    logging.info("Saved JSON file.")

logging.info("Saved IFC.json file with %s classes and %s properties." % (len(classes), len(props)))

### Generate collection of .pot files in the "pot" folder:

class pot_file:

    def __init__(self, f):
        self.f = f
        now = date.today()
        print("""# Industry Foundation Classes IFC.
# Copyright (C) {year} buildingSMART
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: bsdd_support@buildingsmart.org\\n"
"POT-Creation-Date: {date} {time}\\n"
"X-Crowdin-SourceKey: msgstr\\n"
"Language-Team: buildingSMART community\\n"
""".format(year=now.strftime("%Y"), date=now.strftime(r"%Y-%m-%d"), time=now.strftime("%H:%M")), file=self.f)
        

    def __getattr__(self, k):
        return getattr(self.f, k)
        
class pot_dict(dict):

    def __missing__(self, key):
        if not os.path.exists(os.path.join(output_dir, "pot")):
            os.makedirs(os.path.join(output_dir, "pot"))
        if not key:
            key = "UNSPECIFIED_PACKAGE"
        v = self[key] = pot_file(open(os.path.join(output_dir, "pot", key + ".pot"), "w+", encoding="utf-8")) # add folder: "pot", 
        return v


po_files = pot_dict()       

# for i, (package, (ln, col), p, d) in enumerate(generate_definitions()):
i = 0
pos = set()
id_set = set()

for t in to_translate:
    if isinstance(t['package'], defaultdict):
        t['package'] = to_str(t['package'])
    if isinstance(t['msgstr'], defaultdict):
        t['msgstr'] = to_str(t['msgstr'])

    po_file = po_files[t['package']]

    if t['msgid'] and t['msgstr']:   # skip empty strings
        if not t['msgid'] in id_set:
            id_set.add(t['msgid'])
            print("msgid", quote(t['msgid']),  file=po_file)
            print("msgstr", quote(t['msgstr']),  file=po_file)
            print(file=po_file)
            pos.add(po_file)
            i += 1
        else:
            logging.warning("duplicated msgids '%s' in the pot file: %s." % (t['msgid'], po_file))

logging.info("Saved %s terms in %s POT files." % (i, len(pos)))
