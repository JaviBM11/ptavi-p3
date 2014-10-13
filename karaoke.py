#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import os

Entrada = sys.argv

if __name__ == "__main__":
    try:
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(Entrada[1]))  
        Lista = sHandler.get_tags()
        for Elemento in Lista:
            Etiqueta = Elemento[0] + "\t"
            Atributos = ""
            for Atributo in Elemento[1].keys():
                recurso = Elemento[1][Atributo]
                if Atributo == "src" and Elemento[1][Atributo][0] == "h":
                    os.system("wget -q " + recurso)
                    recurso = Elemento[1][Atributo].split('/')
                    recurso = recurso[-1]   
                Atributos = Atributos + Atributo + '="' + recurso + '"' + '\t'
            print Etiqueta + Atributos
    except IndexError:
        print ("Usage: python karaoke.py file.smil")
