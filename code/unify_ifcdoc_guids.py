import sys
import glob
import ifcopenshell.guid
from xml.dom.minidom import parse

fns = glob.glob(f"{sys.argv[1]}/**/*.xml", recursive=True)
for fn in fns:
    try:
        parse(fn)
    except:
        import traceback
        traceback.print_exc()
        breakpoint()
doms = list(map(parse, fns))

for fn, d in zip(fns, doms):
  uid = d.childNodes[0].attributes['UniqueId'].value
  if len(uid) == 22:
    hex = ifcopenshell.guid.split(ifcopenshell.guid.expand(uid))[1:-1].lower()
    d.childNodes[0].setAttribute('UniqueId', hex)
    open(fn, "wb").write(d.toxml(encoding='utf-8').replace(b"?>", b"?>\r\n"))
