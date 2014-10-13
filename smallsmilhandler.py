#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.etiquetas = [
            'root-layout', 'region', 'img', 'audio', 'textstream']
        self.atributos = {
            'root-layout': ["width", "height", "background-color"],
            'region': ["id", "top", "bottom", "left", "right"],
            'img': ["src", "region", "begin", "dur"],
            'audio': ["src", "begin", "dur"],
            'textstream': ["src", "region"]}

    def startElement(self, etiqueta, attrs):
        diccionario = {}
        if etiqueta in self.etiquetas:
            for atributo in self.atributos[etiqueta]:
                diccionario[atributo] = attrs.get(atributo, "")
            self.lista.append([etiqueta, diccionario])

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    print sHandler.get_tags()
