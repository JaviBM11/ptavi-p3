#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler

Entrada = sys.argv

if __name__ == "__main__":
    try:
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(Entrada[1]))  
        Lista = sHandler.get_tags()
        for Elemento in Lista:
            Etiqueta = Elemento[0] + "/"
            Atributos = ""
            for Atributo in Elemento[1].keys():
                Atributos = Atributos + Atributo + '="' + Elemento[1][Atributo] + '"' + '/'
            print Etiqueta + Atributos
    except IndexError:
        print ("Usage: python karaoke.py file.smil")
