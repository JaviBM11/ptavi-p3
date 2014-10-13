#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import os


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self):
        self.Entrada = sys.argv
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(self.Entrada[1]))
        self.Lista = sHandler.get_tags()

    def __str__(self):
        listastr = ""
        for Elemento in self.Lista:
            Etiqueta = Elemento[0] + "\t"
            Atributos = ""
            for Atributo in Elemento[1].keys():
                if Elemento[1][Atributo] != "":
                    recurso = Elemento[1][Atributo]
                    Atributos = Atributos + Atributo
                    Atributos += '="' + recurso + '"' + '\t'
            listastr += Etiqueta + Atributos + '\n'
        return listastr

    def do_local(self):
        for Elemento in self.Lista:
            Etiqueta = Elemento[0] + "\t"
            for Atributo in Elemento[1].keys():
                if Elemento[1][Atributo] != "":
                    recurso = Elemento[1][Atributo]
                    if Atributo == "src" and Elemento[1][Atributo][0] == "h":
                        os.system("wget -q " + recurso)
                        recurso = Elemento[1][Atributo].split('/')
                        Elemento[1][Atributo] = recurso[-1]

if __name__ == "__main__":

    if len(sys.argv) == 2:
        Karaoke = KaraokeLocal()
        print Karaoke.__str__()
        Karaoke.do_local()
        print Karaoke.__str__()
    else:
        sys.exit('Usage: python karaoke.py file.smil')
