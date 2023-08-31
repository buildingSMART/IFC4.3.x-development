import sys
import glob
from ifcopenshell.express import express_parser

schemas = glob.glob("../reference_schemas/*.exp")

try:
    n = int(sys.argv[1])
    from multiprocessing import Pool
    pool = Pool(processes=n)
    pool.map(express_parser.parse, schemas)
except:
    for fn in schemas:
        express_parser.parse(fn)
