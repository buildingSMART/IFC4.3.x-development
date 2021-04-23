import os
import sys
import glob

ifn, ofn = sys.argv[1:]

from xml.etree.ElementTree import Element, SubElement, tostring

for fn in glob.glob(os.path.join(ifn, "**", "*.md"), recursive=True):
    add = Element('add')
    top = SubElement(add, 'doc')

    title = SubElement(top, 'field')
    title.set('name','title')
    title.text = fn.split("/")[-1][:-3]

    title = SubElement(top, 'field')
    title.set('name','id')
    title.text = fn.split("/")[-1][:-3]

    body = SubElement(top, 'field')
    body.set('name', 'body')
    body.text = open(fn).read()
    
    with open(os.path.join(ofn, fn.split("/")[-1][:-3] + ".xml"), "wb") as ff:
        ff.write(tostring(add))

