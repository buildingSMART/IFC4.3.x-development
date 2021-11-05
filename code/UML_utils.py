import os
import subprocess 
import json
import sys

class tex_ulm_object():
    def __init__(self,texfilename):
        self.data = {}
        self.tex_file = open(texfilename+".tex", "x")
        self.tex_file_name = texfilename 
        self.tex_content = r''' \documentclass{article}
                                \usepackage{tikz-uml}
                                \usetikzlibrary{positioning}
                                \begin{document}
                                \hoffset=-1in
                                \voffset=-1in
                                \setbox0\hbox{\begin{tabular}{cccc} 
                                \begin{tikzpicture} '''

        self.tex_meta = set()



    def get_data(self,entity_name,schema):
        # Get data
        data = {}
        for d in schema:
            if d['IFCtype'] == 'ENTITY':
                if d['name'] == entity_name:
                    data['attributes'] = d['attributes']
                    data['subtypes'] = d['subtypes']
                    data['supertypes'] = d['supertypes']
                    data['is_abstract'] = d['is_abstract']
            
            if d['IFCtype'] == 'ENUM':
                if d['name'] == entity_name:
                    data['name'] = d['name']
                    data['values'] = d['values']

            if d['IFCtype'] == 'TYPE':
                if d['name'] == entity_name:
                    data['super'] = d['super']
                    data['name'] = d['name']
                    
                   


        return data
    
    def make_connection(self,source,target,connection_type="assoc",stereo="vec"):
        if connection_type == 'aggreg':
            tex_content = r''' \umluniaggreg[arg2=a, mult2=1, pos2=0.9]{%s}{%s}'''%(source,target)
        if connection_type == 'assoc':
            tex_content = r''' \umluniassoc[geometry=-|, arg1=x, mult1=1, pos1=1.9, arg2=y, mult2=*, pos2=0.2,stereo=%s,pos stereo=1.4]{%s}{%s} '''%(stereo,source,target)
        if connection_type == 'uni':
            tex_content = r''' \umlunicompo[arg=z, mult=1..*, pos=0.8, angle1=-90, angle2=-140, loopsize=2cm]{%s}{%s}'''%(source,target)
        
        self.tex_content += tex_content


    def write_type_class(self,type_name,schema,xpos=2,ypos=2,make_connections=True):
        if ' ' in type_name:
            type_name = type_name.split(' ')
            type_name = type_name[-1]
            type_name = type_name[:-1]
        

        # Build content
        if type_name not in self.tex_meta:
            tex_content = r''' \umlsimpleclass[x=%s,y=%s,type=typedef]{%s}'''%(xpos,ypos,type_name)
            self.tex_content += tex_content
            self.tex_meta.add(type_name)

        if make_connections:
            x=5
            y=7
           # Get data
            data = self.get_data(type_name,schema)
            supertype = data['super']
            self.write_type_class(supertype,schema,make_connections=False,xpos=x,ypos=y)
            self.make_connection(type_name,supertype)


        

    def write_enum_class(self,enum_name,schema,xpos=2,ypos=2):
        # Get data
        if ' ' in enum_name:
            enum_name = enum_name.split(' ')
            enum_name = enum_name[-1][:-1]
        
        data = self.get_data(enum_name,schema)
        
        values = data['values']


        # Build content
        attribute_content = ""
        i = 0
        for value in values:
            value = value.replace('_',' ')
            if i != len(values) - 1:
                attribute_content += value + r'\\'
            else:
                attribute_content += value
            i += 1
        
        print('X',xpos,'\n')
        print('Y',ypos,'\n')
        print('enum_name',enum_name,'\n')
        print('ac',attribute_content,'\n')

        
        tex_content = r''' \umlclass[x=%s, y=%s, width=15ex, anchor=north,type=enum]{%s}{%s}{} '''%(xpos,ypos,enum_name,attribute_content)
        self.tex_content += tex_content
        self.tex_meta.add(enum_name)



    def write_class(self,entity_name,schema,make_connections=True,xpos=2,ypos=2,relativepos=None,previous_class=None):

        # Resister class name
        # self.tex_meta[entity_name] = []

        # Get data
        data = self.get_data(entity_name,schema)
        attributes = data['attributes'] 
        subtypes = data['subtypes'] 
        supertypes = data['supertypes'] 
        is_abstract = data['is_abstract']

        # Determine tex properties
        # xpos = 2
        # ypos = 2
        anchor = 'north'
        other_properties =[]

        # Register tex class     
        entity_dict = {}
        entity_dict['type'] = 'ENTITY'
        entity_dict['classname'] = entity_name
        entity_dict['x'] = xpos
        entity_dict['y'] = ypos
        
        # Build content
        # todo: derived attributes!
        attribute_content = ""
        i = 0
        y = 5
        x = 5
        for attribute in attributes:
            y += 5
            x += 5
 

            if 'Enum' in attribute:
                self.write_enum_class(attribute,schema,xpos=x,ypos=y)
                
            else: 
                self.write_type_class(attribute,schema,make_connections=False,xpos=x,ypos=y)
                


            if i != len(attributes) - 1:
                attribute_content += attribute + r'\\'
            else:
                attribute_content += attribute 
            i += 1


        if is_abstract:
            if relativepos!=None:
                command = "right="+str(relativepos)+"cm of "+previous_class+".north"
                tex_content = r''' \umlclass[%s, width=15ex, anchor=north,type=abstract]{%s}{%s}{} '''%(command,entity_name,attribute_content)
            else:
                tex_content = r''' \umlclass[x=%s, y=%s, width=15ex, anchor=north,type=abstract]{%s}{%s}{} '''%(xpos,ypos,entity_name,attribute_content)

        
        else:
            if relativepos!=None:
                command = "right="+str(relativepos)+"cm of "+previous_class+".north"
                tex_content = r''' \umlclass[%s, width=15ex, anchor=north]{%s}{%s}{} '''%(command,entity_name,attribute_content)
            else:
                tex_content = r''' \umlclass[x=%s, y=%s, width=15ex, anchor=north]{%s}{%s}{} '''%(xpos,ypos,entity_name,attribute_content)


        self.tex_content += tex_content
        self.tex_meta.add(entity_name)

        if make_connections:
            # Children classes
            y = -4
            x = -15
            
            j = 0
            prev_class = subtypes[j]
            for supertype in supertypes:
                j += 1
                # y -= 5
                # x += 5 
                if j != 1:
                    prev_class = supertypes[j-2]
                    self.write_class(supertype,schema,make_connections=False,relativepos=5,previous_class=prev_class)
                else:
                    self.write_class(supertype,schema,make_connections=False,xpos=x,ypos=y)


                self.make_connection(entity_name,supertype)
                

            # Parent class
            y = 8
            #x = -3
            
            for subtype in subtypes:
                
                self.write_class(subtype,schema,make_connections=False,xpos=x,ypos=y)

                self.make_connection(subtype,entity_name)
                
            for attribute in attributes:
                attribute = attribute.split(' ')
                stereo = attribute[0]
                attribute = attribute[-1][:-1]
                
                self.make_connection(entity_name,attribute,stereo=stereo)




                 
    def generate_pdf(self):
        self.tex_content += r''' \end{tikzpicture} 
                                 \end{tabular}}
                                 \pdfpageheight=\dimexpr\ht0+\dp0\relax
                                 \pdfpagewidth=\wd0
                                 \shipout\box0
                                 \stop
                                 \end{document}'''
                                
        self.tex_file.write(self.tex_content)
        self.tex_file.close()
        subprocess.call(['pdflatex',self.tex_file_name+'.tex'])
    


######TEST######

# print(sys.argv[1])

name_tex_file = sys.argv[1]

with open('ifcschema2.json', 'r') as fp:
    data_schema = json.load(fp)
    


tex_object = tex_ulm_object(name_tex_file)

tex_object.write_class('IfcWindow',data_schema)
#tex_object.write_enum_class('IfcWindowTypePartitioningEnum',data_schema)
#tex_object.write_type_class('IfcLuminousFluxMeasure',data_schema)
tex_object.generate_pdf()




