import os

from markdown_it import MarkdownIt
from markdown_it.renderer import RendererHTML
from markdown_it.presets.default import make as make_default
from markdown_it.utils import AttrDict

options = AttrDict(make_default()['options'])

parser = MarkdownIt()
renderer = RendererHTML()

class markdown_attribute_parser:
    def __init__(self, data):
        self.lines = data.split("\n")
        tokens = parser.parse(data)
        renders = [renderer.render([t], options, {}) for t in tokens]
        tok_renders = [(t.type, s, t.as_dict().get('map'), t.tag) for t, s in zip(tokens, renders)]
        self.tok_renders_pairs = list(zip(tok_renders[:-1], tok_renders[1:]))
        
    def __iter__(self):
        try:
            attribute_heading_idx, tag = [(i,d[0][3]) for i,d in enumerate(self.tok_renders_pairs) if d[0][0] == 'heading_open' and d[1][1] == 'Attributes'][0]
        except IndexError as e:
            return
            
        try:
            next_same_level_heading = [i for i,d in enumerate(self.tok_renders_pairs) if i > attribute_heading_idx and d[0][0] == 'heading_open' and d[0][3] == tag][0]                           
        except IndexError as e:
            next_same_level_heading = 100000
        
        for heading_idx, name in [(i, d[1][1]) for i,d in enumerate(self.tok_renders_pairs) if d[0][0] == 'heading_open' and i > attribute_heading_idx and i < next_same_level_heading]:
        
            try:
                next_heading = [i for i,d in enumerate(self.tok_renders_pairs) if i > heading_idx and d[0][0] == 'heading_open'][0]                           
            except IndexError as e:
                next_heading = 100000

            try:            
                first_paragraph = [d for i, d in enumerate(self.tok_renders_pairs) if d[0][0] == 'paragraph_open' and i > heading_idx and i < next_heading][0]
            except IndexError as e:
                yield name, ''
                continue
            
            line_begin = first_paragraph[0][2][0]
            
            try:
                next_heading = [d for i,d in enumerate(self.tok_renders_pairs) if d[0][0] == 'heading_open' and i > heading_idx][0]
                line_end = next_heading[0][2][0]
            except IndexError as e:
                next_same_level_heading = 100000
                line_end = 100000
                
            definition = "\n".join(self.lines[line_begin:line_end])
            
            yield name, definition
