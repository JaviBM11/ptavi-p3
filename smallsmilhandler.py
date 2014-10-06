#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.dicrootlayout = {}
        self.dicregion = {}
        self.dicimg = {}
        self.dicaudio = {}
        self.dictextstream = {}
        self.lista = []
        self.etiquetas = ['root-layout', 'region']
        
    def startElement(self, etiqueta, attrs):
        diccionario = {}
        if etiqueta in self.etiquetas:
           for atributo in XXXXX(etiqueta):
                diccionario[atributo] = attrs.get(atributo, "")
           self.lista.append([name, diccionario]

        if etiqueta == 'root-layout':
            self.dicrootlayout['width'] = attrs.get('width', "")
            self.dicrootlayout['height'] = attrs.get('height', "")
            self.dicrootlayout['background-color'] = attrs.get('background-color', "")
            self.lista.append([etiqueta, self.dicrootlayout])
            
        elif etiqueta == 'region':
            self.dicregion['id'] = attrs.get('id', "")
            self.dicregion['top'] = attrs.get('top', "")
            self.dicregion['bottom'] = attrs.get('bottom', "")
            self.dicregion['left'] = attrs.get('left', "")
            self.dicregion['right'] = attrs.get('right', "")
            self.lista.append([etiqueta, self.dicregion])

        elif etiqueta == 'img':
            self.dicimg['src'] = attrs.get('src', "")
            self.dicimg['region'] = attrs.get('region', "")
            self.dicimg['begin'] = attrs.get('begin', "")
            self.dicimg['end'] = attrs.get('end', "")
            self.dicimg['dur'] = attrs.get('dur', "")
            self.lista.append([etiqueta, self.dicimg])

        elif etiqueta == 'audio':
            self.dicaudio['src'] = attrs.get('src', "")
            self.dicaudio['begin'] = attrs.get('begin', "")
            self.dicaudio['dur'] = attrs.get('dur', "")
            self.lista.append([etiqueta,self.dicaudio])

        elif etiqueta == 'textstream':
            self.dictextstream['src'] = attrs.get('src', "")
            self.dictextstream['region'] = attrs.get('region', "")
            self.lista.append([etiqueta, self.dictextstream])

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))  
    print sHandler.get_tags()
