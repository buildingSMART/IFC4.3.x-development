import glob
from express_diff import express_parser

for fn in glob.glob("../reference_schemas/*.exp"):
    express_parser.parse(fn)
