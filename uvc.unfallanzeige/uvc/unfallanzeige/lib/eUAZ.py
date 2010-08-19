# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from time import gmtime, strftime
from reportlab.lib.colors import gray
from zope.interface import implementer
from zope.component import adapter
from zope.publisher.interfaces import IRequest
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IPresentation
from tempfile import TemporaryFile
from string import replace


def nN(value):
    if value == None:
        return ""
    return value


bv2={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Hamburg','name3':'','strasse':'Ottenser Hauptstrasse 54','plzort':'22765 Hamburg'}
bv3={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Hannnover','name3':'','strasse':'Walderseestrasse 5/6','plzort':'30163 Hannover'}
bv4={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Berlin','name3':'','strasse':'Axel-Springer-Strasse 52','plzort':'10969 Berlin'}
bv5={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Dresden','name3':'','strasse':'Hofmühlenstrasse 4','plzort':'01187 Dresden'}
bv6={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Wuppertal','name3':'','strasse':'Aue 96','plzort':'42103 Wuppertal'}
bv7={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Wiesbaden','name3':'','strasse':'Wiesbadener Strasse 70','plzort':'65197 Wiesbaden'}
bv9={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV München','name3':'','strasse':'Deisenhofener Strasse 74','plzort':'81539 München'}



import tempfile
import uvcsite
import grok
from zope.component import getMultiAdapter
from zope.dublincore.interfaces import IZopeDublinCore
from zope.publisher.interfaces import IRequest
from uvcsite.api.interfaces import ICompanyInfo, ICompanyAddress

class Druck(grok.View):
    grok.context(IUnfallanzeige)
    grok.title(" ")
    uvcsite.sectionmenu(uvcsite.IDocumentActions, order=0, icon="@@/uvc-icons/icon_pdf.gif")

    def render(self):
        RESPONSE = self.request.response
        RESPONSE.setHeader('content-type', 'application/pdf')
        RESPONSE.setHeader('content-disposition', 'attachment; filename=unfallanzeige.pdf')
        return getMultiAdapter((self.context, self.request), IPresentation).createpdf()


class Presentation(grok.MultiAdapter):
    grok.adapts(IUnfallanzeige, IRequest)
    grok.implements(IPresentation)

    def __init__(self, context, request):
        self.context = context
        self.request = request


    def createpdf(self):
        context = self.context
        request = self.request
        metadata = IZopeDublinCore(context)
        mitglied = ''.join(metadata.creators)
        filename = "/tmp/uaz_%s.pdf" %mitglied
        addr = ICompanyInfo(request.principal).getAddress()
        c = canvas.Canvas(filename,pagesize=A4)

        c.setAuthor("BG fÃ¼r Fahrzeughaltungen")
        c.setTitle("Unfallanzeige")
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        date = strftime("%d.%m.%Y",gmtime())
        date = metadata.modified.strftime("%d.%m.%Y")
        #Grauer Hintergrund
        c.setFillGray(0.85)
        c.rect(1.4*cm,0.5*cm,width=19.0*cm,height=28.9*cm,stroke=0,fill=1)
        #Weisse Rechtecke
        c.setLineWidth(0.5)
        c.setFillGray(1.0)
        c.rect(1.6*cm,27.6*cm,width=9.0*cm,height=1.6*cm,stroke=1,fill=1)
        c.rect(12.5*cm,27.6*cm,width=7.6*cm,height=1.6*cm,stroke=1,fill=1)
        c.rect(1.6*cm,22.5*cm,width=9.0*cm,height=4.5*cm,stroke=0,fill=1)
        c.rect(1.6*cm,3.0*cm,width=18.4*cm,height=18.6*cm,stroke=1,fill=1)
        c.rect(1.6*cm,0.9*cm,width=18.4*cm,height=1.9*cm,stroke=1,fill=1)

        x1=13.2
        x2=13.2
        y1=27.6
        y2=28.0
        for i in range(10):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            x1=x1+0.7
            x2=x2+0.7
        #Waagerechte Linien Felder 4-17
        x1=1.6
        x2=20.0
        y1=15.5
        y2=15.5
        for i in range(7):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            y1=y1+0.85
            y2=y2+0.85

        #Waagerechte Linien Felder 18-21 und 23-27
        x1=1.6
        x2=20.
        y1=7.7
        y2=7.7

        for i in range(3):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            y1=y1+0.85
            y2=y2+0.85

        x1=1.6
        x2=20.0
        y1=3.9
        y2=3.9

        for i in range(4):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            y1=y1+0.85
            y2=y2+0.85

        #Linien in Feld 5
        c.line(13.7*cm,20.6*cm,13.7*cm,21.6*cm)
        c.setStrokeGray(0.5)
        c.line(16.5*cm,20.6*cm,16.5*cm,21.1*cm)
        c.line(17.5*cm,20.6*cm,17.5*cm,21.1*cm)

        x1=16.0
        x2=16.0
        y1=20.6
        y2=21.6

        for i in range(3):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            x1=x1+1.0
            x2=x2+1.0

        x1=18.5
        x2=18.5
        y1=20.6
        y2=21.1

        for i in range(3):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            x1=x1+0.5
            x2=x2+0.5

        #Linien in Feld 6
        x1=10.5
        x2=10.5
        y1=19.75
        y2=20.2
        land=context.lkz #grrc(v=getattr(uaz,'lkz',''),ret='  ')
        if land == 'D' or land == '  ':
            for i in range(4):
                c.line(x1*cm,y1*cm,x2*cm,y2*cm)
                x1=x1+0.5
                x2=x2+0.5

        c.setStrokeGray(0.0)
        c.line(10.0*cm,19.75*cm,10.0*cm,20.6*cm)
        c.line(12.5*cm,19.75*cm,12.5*cm,20.6*cm)

        #Rechtecke in Feld 7
        c.rect(1.8*cm,18.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(3.6*cm,18.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linie abwaerts von Feld 8 bis 15
        c.line(6.5*cm,16.35*cm,6.5*cm,19.75*cm)

        #Rechtecke und Linien in Feld 9
        c.rect(17.3*cm,18.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(18.5*cm,18.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.line(17.1*cm,18.9*cm,17.1*cm,19.75*cm)

        #Rechtecke in Feld 10
        c.rect(1.8*cm,18.05*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(3.6*cm,18.05*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linien in Feld 11
        c.line(9.4*cm,18.05*cm,9.4*cm,18.9*cm)
        c.line(9.8*cm,18.05*cm,9.8*cm,18.9*cm)
        c.line(9.4*cm,18.45*cm,9.8*cm,18.45*cm)
        c.line(14.1*cm,18.05*cm,14.1*cm,18.9*cm)
        c.line(14.5*cm,18.05*cm,14.5*cm,18.9*cm)
        c.line(14.1*cm,18.45*cm,14.5*cm,18.45*cm)

        #Linien in Feld 12
        c.line(3.6*cm,17.2*cm,3.6*cm,17.7*cm)
        c.line(4.6*cm,17.2*cm,4.6*cm,17.7*cm)

        c.setStrokeGray(0.5)
        c.line(4.1*cm,17.2*cm,4.1*cm,17.5*cm)

        #Rechtecke in Feld 14
        c.setStrokeGray(0.0)
        c.rect(1.8*cm,16.35*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(3.6*cm,16.35*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linien in Feld 15
        c.setStrokeGray(0.5)
        c.line(9.1*cm,16.35*cm,9.1*cm,17.2*cm)
        c.line(9.6*cm,16.35*cm,9.6*cm,16.75*cm)
        c.line(10.1*cm,16.35*cm,10.1*cm,17.2*cm)
        c.line(10.6*cm,16.35*cm,10.6*cm,16.75*cm)
        c.line(11.1*cm,16.35*cm,11.1*cm,17.2*cm)
        c.line(11.6*cm,16.35*cm,11.6*cm,16.75*cm)
        c.line(12.1*cm,16.35*cm,12.1*cm,16.75*cm)
        c.line(12.6*cm,16.35*cm,12.6*cm,16.75*cm)
        c.line(13.1*cm,16.35*cm,13.1*cm,17.2*cm)
        c.line(13.6*cm,16.35*cm,13.6*cm,16.75*cm)
        c.line(14.1*cm,16.35*cm,14.1*cm,17.2*cm)
        c.line(14.6*cm,16.35*cm,14.6*cm,16.75*cm)
        c.line(15.1*cm,16.35*cm,15.1*cm,17.2*cm)

        #Rechtecke in Feld 17
        c.setStrokeGray(0.0)
        c.rect(7.9*cm,9.4*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(10.7*cm,9.4*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linie in Feld 19
        c.line(10.7*cm,8.55*cm,10.7*cm,9.4*cm)

        #Rechtecke in Feld 20
        c.rect(15.7*cm,7.7*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(17.2*cm,7.7*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linien in Feld 22
        c.line(13.3*cm,6.45*cm,13.3*cm,7.7*cm)
        c.line(17.0*cm,6.45*cm,17.0*cm,7.25*cm)

        c.setStrokeGray(0.5)
        c.line(15.0*cm,6.45*cm,15.0*cm,7.25*cm)
        c.line(15.5*cm,6.45*cm,15.5*cm,6.85*cm)
        c.line(16.0*cm,6.45*cm,16.0*cm,7.25*cm)
        c.line(16.5*cm,6.45*cm,16.5*cm,6.85*cm)
        c.line(18.0*cm,6.45*cm,18.0*cm,7.25*cm)
        c.line(18.5*cm,6.45*cm,18.5*cm,6.85*cm)
        c.line(19.0*cm,6.45*cm,19.0*cm,7.25*cm)
        c.line(19.5*cm,6.45*cm,19.5*cm,6.85*cm)

        #Linien in Feld 24
        c.line(17.0*cm,5.6*cm,17.0*cm,6.45*cm)
        c.line(17.5*cm,5.6*cm,17.5*cm,6.0*cm)
        c.line(18.0*cm,5.6*cm,18.0*cm,6.45*cm)
        c.line(18.5*cm,5.6*cm,18.5*cm,6.0*cm)
        c.line(19.0*cm,5.6*cm,19.0*cm,6.0*cm)
        c.line(19.5*cm,5.6*cm,19.5*cm,6.0*cm)

        c.setStrokeGray(0.0)
        c.line(12.3*cm,5.6*cm,12.3*cm,6.45*cm)

        #Rechtecke und Linien in Feld 26
        c.rect(7.9*cm,3.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(9.5*cm,3.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(14.3*cm,3.9*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        c.setStrokeGray(0.5)
        c.line(17.5*cm,3.9*cm,17.5*cm,4.3*cm)
        c.line(18.5*cm,3.9*cm,18.5*cm,4.3*cm)
        c.line(19.0*cm,3.9*cm,19.0*cm,4.75*cm)
        c.line(19.5*cm,3.9*cm,19.5*cm,4.3*cm)

        #Rechtecke und Linien in Feld 27
        c.line(16.0*cm,3.0*cm,16.0*cm,3.9*cm)
        c.line(16.5*cm,3.0*cm,16.5*cm,3.5*cm)
        c.line(17.0*cm,3.0*cm,17.0*cm,4.75*cm)
        c.line(17.5*cm,3.0*cm,17.5*cm,3.5*cm)
        c.line(18.0*cm,3.0*cm,18.0*cm,4.75*cm)
        c.line(18.5*cm,3.0*cm,18.5*cm,3.5*cm)
        c.line(19.0*cm,3.0*cm,19.0*cm,3.5*cm)
        c.line(19.5*cm,3.0*cm,19.5*cm,3.5*cm)

        c.setStrokeGray(0.0)
        c.rect(9.5*cm,3.0*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)
        c.rect(14.3*cm,3.0*cm,width=0.4*cm,height=0.4*cm,stroke=1,fill=1)

        #Linie in Feld 28
        c.line(1.7*cm,1.4*cm,19.9*cm,1.4*cm)

        #Feldbeschriftungen
        c.setFillGray(0.0)

        #Formulartitel
        c.setFont(schriftartfett,18)
        c.drawString(12.5*cm,24.5*cm,"U N F A L L A N Z E I G E")

        #Beschriftung Feld1
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,28.9*cm,"1")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,28.9*cm,"Name und Anschrift des Unternehmens")

        #Beschriftung Feld2
        c.setFont(schriftartfett,7)
        c.drawString(12.7*cm,28.9*cm,"2")
        c.setFont(schriftart,7)
        c.drawString(13.0*cm,28.9*cm, u"Unternehmensnummer des Unfallversicherungsträgers")

       #Beschriftung Feld3
        flag = "nix"
        if flag == 'as':
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,27.1*cm,"3")
            c.setFont(schriftart,7)
            c.drawString(2.1*cm,27.1*cm,"Empfänger")
            c.setFont(schriftart,11)
            c.drawString(2.7*cm,25.8*cm,"An die zuständige")
            c.drawString(2.7*cm,25.3*cm,"Arbeitsschutzbehörde")
        elif flag == 'ps':
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,27.1*cm,"3")
            c.setFont(schriftart,7)
            c.drawString(2.1*cm,27.1*cm,"Empfänger")
            c.setFont(schriftart,11)
            c.drawString(2.7*cm,25.8*cm,"An den")
            c.drawString(2.7*cm,25.3*cm,"Betriebsrat")
        else:
            bv=self.request.principal.id[1]
            if bv == '1':
                bv=bv1
            elif bv == '2':
                bv=bv2
            elif bv == '3':
                bv=bv3
            elif bv == '4':
                bv=bv4
            elif bv == '5':
                bv=bv5
            elif bv == '6':
                bv=bv6
            elif bv == '7':
                bv=bv7
            elif bv == '9':
                bv=bv9
            else:
                bv=bv3
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,27.1*cm,"3")
            c.setFont(schriftart,7)
            c.drawString(2.1*cm,27.1*cm, u"Empfänger (Unfallversicherungsträger)")
            c.setFont(schriftart,11)
            c.drawString(2.7*cm,25.8*cm,bv['name1'])
            c.drawString(2.7*cm,25.3*cm,bv['name2'])
            c.drawString(2.7*cm,24.8*cm,bv['name3'])
            c.drawString(2.7*cm,24.3*cm,bv['strasse'])
            c.setFont(schriftartfett,11)
            c.drawString(2.7*cm,23.3*cm,bv['plzort'])

        #Beschriftung Feld4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,21.3*cm,"4")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,21.3*cm,"Name, Vorname des Versicherten")

        #Beschriftung Feld5
        c.setFont(schriftartfett,7)
        c.drawString(13.9*cm,21.3*cm,"5")
        c.setFont(schriftart,7)
        c.drawString(14.2*cm,21.3*cm,"Geburtsdatum")
        c.drawString(16.25*cm,21.3*cm,"Tag")
        c.drawString(17.15*cm,21.3*cm,"Monat")
        c.drawString(18.7*cm,21.3*cm,"Jahr")

        #Beschriftung Feld6
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,20.3*cm,"6")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,20.3*cm,u"Straße, Hausnummer")
        c.drawString(10.1*cm,20.3*cm,"Postleitzahl")
        c.drawString(12.6*cm,20.3*cm,"Ort")

        #Beschriftung Feld7
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,19.45*cm,"7")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,19.45*cm,"Geschlecht")
        c.drawString(2.3*cm,19.0*cm,u"männlich")
        c.drawString(4.1*cm,19.0*cm,"weiblich")

        #Beschriftung Feld8
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,19.45*cm,"8")
        c.setFont(schriftart,7)
        c.drawString(7.0*cm,19.45*cm,u"Staatsangehörigkeit")

        #Beschriftung Feld9
        c.setFont(schriftartfett,7)
        c.drawString(17.3*cm,19.45*cm,"9")
        c.setFont(schriftart,7)
        c.drawString(17.6*cm,19.45*cm,"Leiharbeitnehmer")
        c.drawString(17.9*cm,19.0*cm,"ja")
        c.drawString(19.0*cm,19.0*cm,"nein")

        #Beschriftung Feld10
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,18.6*cm,"10")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,18.6*cm,"Auszubildender")
        c.drawString(2.3*cm,18.2*cm,"ja")
        c.drawString(4.1*cm,18.2*cm,"nein")

        #Beschriftung Feld11
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,18.6*cm,"11")
        c.setFont(schriftart,7)
        c.drawString(7.1*cm,18.6*cm,"Ist der Versicherte")
        c.drawString(10.0*cm,18.55*cm,"Unternehmer")
        c.drawString(10.0*cm,18.15*cm,"mit dem Unternehmer verwandt")
        c.drawString(14.7*cm,18.55*cm,"Ehegatte des Unternehmers")
        c.drawString(14.7*cm,18.15*cm,u"Gesellschafter/Geschäftsführer")

        #Beschriftung Feld12
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,17.75*cm,"12")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,17.75*cm,"Anspruch auf Entgeltfortzahlung")
        c.drawString(2.1*cm,17.3*cm,u"besteht für")
        c.drawString(4.8*cm,17.3*cm,"Wochen")

        #Beschriftung Feld13
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,17.75*cm,"13")
        c.setFont(schriftart,7)
        c.drawString(7.1*cm,17.75*cm,"Krankenkasse des Versicherten (Name, PLZ, Ort)")

        #Beschriftung Feld14
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,16.9*cm,"14")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,16.9*cm,u"Tödlicher Unfall")
        c.drawString(2.3*cm,16.45*cm,"ja")
        c.drawString(4.1*cm,16.45*cm,"nein")

        #Beschriftung Feld15
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,16.9*cm,"15")
        c.setFont(schriftart,7)
        c.drawString(7.1*cm,16.9*cm,"Unfallzeitpunkt")
        c.drawString(9.4*cm,16.9*cm,"Tag")
        c.drawString(10.25*cm,16.9*cm,"Monat")
        c.drawString(11.85*cm,16.9*cm,"Jahr")
        c.drawString(13.2*cm,16.9*cm,"Stunde")
        c.drawString(14.25*cm,16.9*cm,"Minute")

        #Beschriftung Feld16
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,16.05*cm,"16")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,16.05*cm,u"Unfallort (genaue Orts- und Straßenangabe mit PLZ)")

        #Beschriftung Feld17
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,15.2*cm,"17")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,15.2*cm,u"Ausführliche Schilderung des Unfallhergangs")
        c.setFont(schriftart,6)
        c.drawString(7.4*cm,15.2*cm,u"(Verlauf, Bezeichnung des Betriebsteils, ggf. Beteiligung von Maschinen, Anlagen, Gefahrstoffen)")
        c.setFont(schriftart,7)
        c.drawString(1.8*cm,9.55*cm,u"Die Angaben beruhen auf der Schilderung")
        c.drawString(8.4*cm,9.55*cm,u"des Versicherten")
        c.drawString(11.2*cm,9.55*cm,u"anderer Personen")

        #Beschriftung Feld18
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,9.1*cm,"18")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,9.1*cm,u"Verletzte Körperteile")

        #Beschriftung Feld19
        c.setFont(schriftartfett,7)
        c.drawString(10.9*cm,9.1*cm,"19")
        c.setFont(schriftart,7)
        c.drawString(11.3*cm,9.1*cm, u"Art der Verletzung")

        #Beschriftung Feld20
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,8.25*cm,"20")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,8.25*cm, u"Wer hat von dem Unfall zuerst Kenntnis genommen ?")
        c.setFont(schriftart,6)
        c.drawString(8.2*cm,8.25*cm, u"(Name, Anschrift des Zeugen)")
        c.setFont(schriftart,7)
        c.drawString(15.7*cm,8.25*cm, u"War diese Person Augenzeuge ?")
        c.drawString(16.2*cm,7.8*cm, u"ja")
        c.drawString(17.7*cm,7.8*cm, u"nein")

        #Beschriftung Feld21
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,7.4*cm,"21")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,7.4*cm, u"Name und Anschrift des erstbehandelnden Arztes/Krankenhauses")

        #Beschriftung Feld22
        c.setFont(schriftartfett,7)
        c.drawString(13.5*cm,7.4*cm,"22")
        c.setFont(schriftart,7)
        c.drawString(13.9*cm,7.4*cm, u"Beginn und Ende der Arbeitszeit des Versicherten")
        c.drawString(13.9*cm,6.7*cm, u"Beginn")
        c.drawString(15.1*cm,7.0*cm, u"Stunde")
        c.drawString(16.1*cm,7.0*cm, u"Minute")
        c.drawString(17.2*cm,6.7*cm, u"Ende")
        c.drawString(18.1*cm,7.0*cm, u"Stunde")
        c.drawString(19.1*cm,7.0*cm, u"Minute")

        #Beschriftung Feld23
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,6.15*cm,"23")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,6.15*cm, u"Zum Unfallzeitpunkt beschäftigt/tätig als")

        #Beschriftung Feld24
        c.setFont(schriftartfett,7)
        c.drawString(12.5*cm,6.15*cm,"24")
        c.setFont(schriftart,7)
        c.drawString(12.9*cm,6.15*cm, u"Seit wann bei dieser Tätigkeit ?")
        c.drawString(17.15*cm,6.15*cm,"Monat")
        c.drawString(18.7*cm,6.15*cm,"Jahr")

        #Beschriftung Feld25
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,5.3*cm,"25")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,5.3*cm, u"In welchem Teil des Unternehmens ist der Versicherte ständig tätig ?")

        #Beschriftung Feld26
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,4.45*cm,"26")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,4.45*cm, u"Hat der Versicherte die Arbeit eingestellt ?")
        c.drawString(8.5*cm,4.0*cm, u"nein")
        c.drawString(10.1*cm,4.0*cm, u"sofort")
        c.drawString(14.9*cm,4.0*cm, u"später, am")
        c.drawString(17.25*cm,4.45*cm, u"Tag")
        c.drawString(18.15*cm,4.45*cm, u"Monat")
        c.drawString(19.1*cm,4.45*cm, u"Stunde")

        #Beschriftung Feld27
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,3.6*cm,"27")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,3.6*cm,"Hat der Versicherte die Arbeit wieder aufgenommen ?")
        c.drawString(10.1*cm,3.1*cm,"nein")
        c.drawString(14.9*cm,3.1*cm,"ja, am")
        c.drawString(16.25*cm,3.6*cm,"Tag")
        c.drawString(17.15*cm,3.6*cm,"Monat")
        c.drawString(18.75*cm,3.6*cm,"Jahr")

        #Beschriftung Feld28
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,1.1*cm,"28")
        c.setFont(schriftart,7)
        c.drawString(3.0*cm,1.1*cm,"Datum")
        c.drawString(5.1*cm,1.1*cm, u"Unternehmer/Bevollmächtigter")
        c.drawString(10.3*cm,1.1*cm,"Betriebsrat (Personalrat)")
        c.drawString(14.65*cm,1.1*cm, u"Telefon-Nr. für Rückfragen (Ansprechpartner)")
        c.setFont(schriftartfett,12)
        c.drawString(7.0*cm,2.15*cm,u"versandt über Extranet")

#   Variablen enfügen
#
#   (1) Name und Anschrift des Unternehmens
#
        plz=addr['plz']
        if plz == None:
            plz = ' '
        ort=unicode(addr['ort']).decode('utf-8')
        if ort == None:
            ort = ' '
        ort=unicode(ort)
        strasse=unicode(addr['strasse']).decode('utf-8')
        if strasse == None:
            strasse = ' '
        strasse=unicode(strasse)
        hsnr=addr['nr']
        if hsnr == None:
            hsnr = ' '

        name3=addr['name3']
        name3=unicode(name3).decode('utf-8')
        name2=addr['name2']
        name2=unicode(name2).decode('utf-8')
        name1=addr['name1']
        name1=unicode(name1).decode('utf-8')

        c.setFont(schriftartfett,8)
        c.drawString(1.7*cm,27.7*cm,plz+' '+ort)
        c.setFont(schriftart,8)
        c.drawString(1.7*cm,28.0*cm,strasse+' '+hsnr)
        #import pdb; pdb.set_trace()
        c.drawString(1.7*cm,28.3*cm,name2+' '+name3)
        c.drawString(1.7*cm,28.6*cm,name1)
#
#   (2) Mitgliedsnummer
#
        x=12.7
        y=27.7
        c.setFont(schriftart,10)
        print mitglied
        for i in mitglied:
            c.drawString(x*cm,y*cm,i)
            x=x+0.7
#
#   (3) Empfänger (Unfallversicherungsträger)
#
#   (4) Name, Vorname des Versicherten
#
        versname = nN(context.prsname) #getattr(uaz,'prsnam','')
        versvorname = nN(context.prsvor) #getattr(uaz,'prsvor','')
        c.setFont(schriftart,10)
        c.drawString(1.7*cm,20.7*cm,versname+', '+versvorname)
#
#   (5) Geburtsdatum
#
        gebdatum=nN(context.prsgeb) #getattr(uaz,'prsgeb','')
        if  len(gebdatum) != 0:
            gebdatum=gebdatum.split('.')
            gebtag=gebdatum[0]
            gebmonat=gebdatum[1]
            gebjahr=gebdatum[2]
            
            if len(gebtag)==1:
                gebtag='0%s' %gebtag
            if len(gebmonat)==1:
                gebmonat='0%s' %gebmonat

            c.setFont(schriftart,10)
            c.drawString(16.1*cm,20.7*cm,gebtag[0])
            c.drawString(16.6*cm,20.7*cm,gebtag[1])
            c.drawString(17.1*cm,20.7*cm,gebmonat[0])
            c.drawString(17.6*cm,20.7*cm,gebmonat[1])
            c.drawString(18.1*cm,20.7*cm,gebjahr[0])
            c.drawString(18.6*cm,20.7*cm,gebjahr[1])
            c.drawString(19.1*cm,20.7*cm,gebjahr[2])
            c.drawString(19.6*cm,20.7*cm,gebjahr[3])
#
#   (6) Strasse Hausnummer
#
        plzort=nN(context.ikzplz) #grrc(v=getattr(uaz,'prsplzort',['','']),ret=['      .',''])
        aplz=nN(context.ikzplz)
        ort=nN(context.ikzort)
        #strhsnr=context.getIkstrnr() #grrc(v=getattr(uaz,'prsstrnr',['','']),ret=['',''])
        strasse=nN(context.ikstr)
        hausnummer=nN(context.iknr)
        c.setFont(schriftart,10)
        c.drawString(12.6*cm,19.85*cm,ort)
        c.drawString(1.7*cm,19.85*cm,strasse+' '+hausnummer)
        if land == 'D':
            c.drawString(10.1*cm,19.85*cm,aplz[0])   
            c.drawString(10.6*cm,19.85*cm,aplz[1])
            c.drawString(11.1*cm,19.85*cm,aplz[2])
            c.drawString(11.6*cm,19.85*cm,aplz[3])
            c.drawString(12.1*cm,19.85*cm,aplz[4])
        elif land != 'D' and land != None:
            c.setFont(schriftart,10)
            c.drawString(10.1*cm,19.85*cm,land+'-'+aplz)
#
#   (7) Geschlecht
#
        c.setFont(schriftart,10)
        sex=nN(context.prssex)
        if sex == '1':
            c.drawString(1.9*cm,19.0*cm,'x')
        elif sex == '2':
            c.drawString(3.7*cm,19.0*cm,'x')
#
#   (8) Staatsangehörigkeitt
#
        staat=nN(context.prssta) #grrc(v=getattr(uaz,'prssta',['','']),ret=[' ',''])
        c.setFont(schriftart,10)
        c.drawString(6.6*cm,19.0*cm,staat)
#
#   (9) Leiharbeitnehmer
#
        c.setFont(schriftart,10)
        leiharbeit=nN(context.unflar) #getattr(uaz,'unflar','')
        if leiharbeit == 'ja':
            c.drawString(17.4*cm,19.0*cm,'x')
        elif leiharbeit == 'nein':
            c.drawString(18.6*cm,19.0*cm,'x')
#
#   (10) Auszubildender 
#
        c.setFont(schriftart,10)   
        azubi=nN(context.uadbru1)
#    azubi=getattr(uaz,'uadbru',['',''])
        if azubi == 'Auszubildender':
            c.drawString(1.9*cm,18.15*cm,'x')
        elif azubi != 'Auszubildender':
            c.drawString(3.7*cm,18.15*cm,'x')
#
#   (11) Ist der Versicherte
#
        c.setFont(schriftart,10)
        ist=nN(context.unfbu) #getattr(uaz,'unfbu',[''])
        if ist == 'Unternehmer':
            c.drawString(9.5*cm,18.55*cm,'x')
        elif ist == 'Mit dem Unternehmer verwand':
            c.drawString(9.5*cm,18.15*cm,'x')
        elif ist == 'Gesellschafter':
            c.drawString(14.2*cm,18.15*cm,'x')
        elif ist == 'Ehegatte des Unternehmers':
            c.drawString(14.2*cm,18.55*cm,'x')
        else:
            pass
#
#    (12) Anspruch auf Entgeltfortzahlung
#
        c.setFont(schriftart,10)
        entgelt=nN(context.unfefz) # grrc(v=getattr(uaz,'unfefz',''),ret='  ')
        if len(entgelt) == 0:
            entgelt="  "
        c.drawString(3.7*cm,17.3*cm,entgelt[0])
        if len(entgelt) > 1:
           c.drawString(4.2*cm,17.3*cm,entgelt[1])
#
#    (13) Krankenkasse des Versicherten
# 
        c.setFont(schriftart,8)
        kk=nN(context.unfkka) #getattr(uaz,'unfkka','')
        c.drawString(6.7*cm,17.3*cm,kk)
#
#   (14) Tödlicher Unfall
#
        c.setFont(schriftart,10)
        tod=nN(context.prstkz) #getattr(uaz,'prstkz','')
        if tod == 'ja':
            c.drawString(1.9*cm,16.45*cm,'x')
        elif tod == 'nein':
            c.drawString(3.7*cm,16.45*cm,'x')
#
#   (15) Unfallzeitpunkt
#
        c.setFont(schriftart,10)
        uzeit=nN(context.unfzeit)
        
        if uzeit != '':

            datum=nN(context.unfdatum)
            stunde=nN(context.unfzeit)

            datum=datum.split('.')
            tag=datum[0]
            monat=datum[1]
            jahr=datum[2]

            if len(tag)==1:
                tag='0%s' %tag
            if len(monat)==1:
                monat='0%s' %monat
            if len(jahr)==1:
                jahr='0%s' %jahr

            if stunde.find(':') != -1:
                stunde=stunde.split(':')
                if len(stunde[0])==1:
                    std='0%s' %stunde[0]
                else:
                    std=stunde[0]
                if len(stunde[1])==1:
                    min='0%s' %stunde[1]
                else:
                    min=stunde[1]

                c.drawString(9.2*cm,16.45*cm,tag[0])
                c.drawString(9.7*cm,16.45*cm,tag[1])
                c.drawString(10.2*cm,16.45*cm,monat[0])
                c.drawString(10.7*cm,16.45*cm,monat[1])
                c.drawString(11.2*cm,16.45*cm,jahr[0])
                c.drawString(11.7*cm,16.45*cm,jahr[1])
                c.drawString(12.2*cm,16.45*cm,jahr[2])
                c.drawString(12.7*cm,16.45*cm,jahr[3])
                c.drawString(13.2*cm,16.45*cm,std[0])
                c.drawString(13.7*cm,16.45*cm,std[1])
                c.drawString(14.2*cm,16.45*cm,min[0])
                c.drawString(14.7*cm,16.45*cm,min[1])
#
#   (16) Unfallort
#
        c.setFont(schriftart,10)
        uort=nN(context.unfort) #getattr(uaz,'unfuor','')
        c.drawString(1.7*cm,15.6*cm,uort)
#
#   (17) Ausführliche Schilderung des Unfalls
#
        ubericht=nN(context.unfhg1)
        #Entfernung von evtl. Zeilenumbruechen aus dem Text
        ubericht=ubericht.replace('\r\n',' ')
        ubericht=ubericht.replace('\r',' ')
        ubericht=ubericht.replace('\n',' ')
        #weg=getattr(uaz,'unfweg','')
        uweg="XXX"
#    c.setFont(schriftartfett,10)
#    c.drawString(1.7*cm,14.6*cm,"Der Unfall ereignete sich:"+" "+uweg.encode('latin-1'))
        c.setFont(schriftart,10)
        cutstring=ubericht[:3000]
        cut=1500
        if len(cutstring)>1500:
           while len(cutstring) > 0:
                if cutstring[cut]== " ":
                    hergang=cutstring[0:cut]
                    nextpage=cutstring[(cut+1):]
                    break
                #harte Trennung nach 100 Zeichen ohne Leerzeichen
                elif cut==1400:
                    hergang=cutstring[0:cut]
                    nextpage=cutstring[(cut+1):]
                    break
                else:
                    cut=cut-1
           else:
                pass
        else:
            hergang=cutstring
            nextpage=" "
        if len(hergang)>1000:
            n=125
            cpl=125
            c.setFont(schriftart,8)
        else:
            n=105
            cpl=105
            c.setFont(schriftart,10)
        y=14.6
        while len(hergang) > 0:
            if len(hergang) > n:
                if n > 0:
                    if hergang[n] == " ":
                        schilderung=hergang[0:n]
                        c.drawString(1.7*cm,y*cm,schilderung)
                        hergang=hergang[(n+1):]
                        y=y-0.35
                        n=cpl
                    else:
                        n=n-1
                else:
                    schilderung1=hergang[0:cpl]
                    c.drawString(1.7*cm,y*cm,schilderung1)
                    hergang=hergang[cpl:]
                    y=y-0.35
                    n=cpl
            else:
                c.drawString(1.7*cm,y*cm,hergang)
                hergang=''
        else:
            pass
        c.setFont(schriftart,10)
        schilderungen=nN(context.unfhg2) #getattr(uaz,'unfhg2',[''])
        if schilderungen == 'des Versicherten':
            c.drawString(8.0*cm,9.5*cm,'x')
        elif schilderungen == 'anderer Person':
            c.drawString(10.8*cm,9.5*cm,'x')
#
#   (18) Verletztes Körperteile
#
        kteile=nN(context.diavkt) #getattr(uaz,'diavkt','')
        if len(kteile)>50:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(1.7*cm,8.65*cm,kteile)
#
#   (19) Art der Verletzung
#
        vart=nN(context.diaadv) #getattr(uaz,'diaadv','')
        if len(vart)>50:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(10.8*cm,8.65*cm,vart)
#
#   (20) Wer hat von dem Unfall Kenntnis genommen?
#
        wer=nN(context.unfkn1) #ngetattr(uaz,'unfkn1','')
        if len(wer)>60:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(1.7*cm,7.8*cm,wer)
        c.setFont(schriftart,10)
        augenzeuge=nN(context.unfkn2) #getattr(uaz,'unfkn2','')
        if augenzeuge == 'ja':
            c.drawString(15.8*cm,7.8*cm,'x')
        elif augenzeuge == 'nein':
            c.drawString(17.3*cm,7.8*cm,'x')
#
#   (21) Name und Anschrift des erstbehandelnden Arztes
#
#    c.setFont(schriftart,8)
#    arzt=getattr(uaz,'unfeba1','')
#    c.drawString(1.7*cm,6.55*cm,arzt.encode('latin-1'))

        abehandlung=nN(context.unfeba)
        if abehandlung=='Es ist keine Aerztliche Behandlung erforderlich':
            c.drawString(1.7*cm,6.95*cm,u'keine ärztliche Behandlung erforderlich')

        c.setFont(schriftart,8)
        arzt=nN(context.unfeba1) #grrc(v=getattr(uaz,'unfeba1',''),ret=' ')
        n=75
        y=6.95
        while len(arzt) > 0:
            if len(arzt) > n:
                if n > 0:
                    if arzt[n] == " ":
                        notarzt=arzt[0:n]
                        c.drawString(1.7*cm,y*cm,notarzt)
                        arzt=arzt[(n+1):]
                        y=y-0.35
                        n=75
                    else:
                        n=n-1
                else:
                    notarzt1=arzt[0:75]
                    c.drawString(1.7*cm,y*cm,notarzt1)
                    arzt=arzt[75:]
                    y=y-0.35
                    n=75
            else:
                c.drawString(1.7*cm,y*cm,arzt)
                arzt=''
        else:
            pass
#
#   (22) Beginn und Ende der Arbeitszeit
#
        c.setFont(schriftart,10)  
        zeit=""
        if zeit != ['','']:
            
            beginn=nN(context.uadbavon)
            ende=nN(context.uadbabis)
                
            if beginn.find(':')!=-1:
                beginn=beginn.split(':')
                if len(beginn[0])==1:
                    std='0%s' %beginn[0]
                else:
                    std=beginn[0]
                if len(beginn[1])==1:
                    min='0%s' %beginn[1]
                else:
                    min=beginn[1]
        
                c.drawString(15.1*cm,6.55*cm,std[0])
                c.drawString(15.6*cm,6.55*cm,std[1])
                c.drawString(16.1*cm,6.55*cm,min[0])
                c.drawString(16.6*cm,6.55*cm,min[1])

            if ende.find(':')!=-1:
                ende=ende.split(':')
                if len(ende[0])==1:
                    std='0%s' %ende[0]
                else:
                    std=ende[0]
                if len(ende[1])==1:
                    min='0%s' %ende[1]
                else:
                    min=ende[1]

                c.drawString(18.1*cm,6.55*cm,std[0])
                c.drawString(18.6*cm,6.55*cm,std[1])
                c.drawString(19.1*cm,6.55*cm,min[0])
                c.drawString(19.6*cm,6.55*cm,min[1])
#
#   (23) Zum Unfallzeitpunkt beschäftigt alss
#
        c.setFont(schriftart,10)   
        taetig=nN(context.uadbru1) #grrc(v=getattr(uaz,'uadbru',['','']),ret=[' ',''])
        c.drawString(1.7*cm,5.7*cm,taetig)
#
#   (24) Seit wann bei dieser Tätigkeitt
#
        c.setFont(schriftart,10)
        abeginn=nN(context.uadst)
        if abeginn!="":
            
            if abeginn.find('.')!=-1:
                abeginn=abeginn.split('.')
                ab_monat=abeginn[0]
                ab_jahr=abeginn[1]
                if len(ab_monat)==1:
                    ab_monat='0%s' %ab_monat 
            
                c.drawString(17.1*cm,5.7*cm,ab_monat[0])
                c.drawString(17.6*cm,5.7*cm,ab_monat[1])
                c.drawString(18.1*cm,5.7*cm,ab_jahr[0])
                c.drawString(18.6*cm,5.7*cm,ab_jahr[1])
                c.drawString(19.1*cm,5.7*cm,ab_jahr[2])
                c.drawString(19.6*cm,5.7*cm,ab_jahr[3])
#
#   (25) In welchem Teil des Unternehmens
#
        c.setFont(schriftart,10)
        unter=nN(context.unfute) #grrc(v=getattr(uaz,'unfute',['','']),ret=[' ',''])
#    unter=getattr(uaz,'unfute',['',''])
        c.drawString(1.7*cm,4.85*cm,unter)
#
#   (26) Hat der Versicherte die Arbeit eingestellt?
#
        c.setFont(schriftart,10)
        einstell=nN(context.unfae1)
        if einstell == 'nein':
            c.drawString(8.0*cm,4.0*cm,'x')
        elif einstell == 'sofort':
            c.drawString(9.6*cm,4.0*cm,'x')
        elif einstell == 'Spaeter am':
            c.drawString(14.4*cm,4.0*cm,'x')
            edat=nN(context.unfaex)
            
            tagmonat=edat[0]
            stunde=edat[1]

            tagmonat=tagmonat.split('.')
            tag=tagmonat[0]
            monat=tagmonat[1]
            
            if len(tag)==1:
                tag='0%s' %tag
            if len(monat)==1:
                monat='0%s' %monat        

            stunde=stunde.split(':')
            if len(stunde[0])==1:
                std='0%s' %stunde[0]
            else:
                std=stunde[0]

            c.drawString(17.1*cm,4.0*cm,tag[0])
            c.drawString(17.6*cm,4.0*cm,tag[1])
            c.drawString(18.1*cm,4.0*cm,monat[0])
            c.drawString(18.6*cm,4.0*cm,monat[1])
            c.drawString(19.1*cm,4.0*cm,std[0])
            c.drawString(19.6*cm,4.0*cm,std[1])
#
#   (27) Hat der Versicherte die Arbeit wieder aufgenommen?
#
        c.setFont(schriftart,10)
        aufnahme=nN(context.unfwa1)
        if aufnahme == 'nein':
            c.drawString(9.6*cm,3.1*cm,'x')
        elif aufnahme == 'ja':
            c.drawString(14.4*cm,3.1*cm,'x')

            azeit=nN(context.unfwax)
            import pdb; pdb.set_trace() 

            azeit=azeit.split('.')
            tag=azeit[0]
            monat=azeit[1]
            jahr=azeit[2]

            if len(tag)==1:
                tag='0%s' %tag
            if len(monat)==1:
                monat='0%s' %monat

            c.drawString(16.1*cm,3.1*cm,tag[0])
            c.drawString(16.6*cm,3.1*cm,tag[1])
            c.drawString(17.1*cm,3.1*cm,monat[0])
            c.drawString(17.6*cm,3.1*cm,monat[1])
            c.drawString(18.1*cm,3.1*cm,jahr[0])
            c.drawString(18.6*cm,3.1*cm,jahr[1])
            c.drawString(19.1*cm,3.1*cm,jahr[2])
            c.drawString(19.6*cm,3.1*cm,jahr[3])
#
#   (28) Datum Unterschrift
#
        c.setFont(schriftart,8)
        c.drawString(2.8*cm,1.5*cm,date)
        unternehmer=nN(context.unfus2) #getattr(uaz,'unfus2','')
        personalrat=nN(context.unfus3) #getattr(uaz,'unfus3','')
#    anspartel1="%s,%s" %(anspartel[0],anspartel[1])
        anspar=nN(context.anspname)
        tel=nN(context.anspfon) 
        c.drawString(4.8*cm,1.5*cm,unternehmer)
        c.drawString(10.0*cm,1.5*cm,personalrat)
        if len(tel)!=0:
            c.drawString(15.0*cm,1.5*cm,"Telefon:"+" "+tel)
            c.drawString(15.0*cm,2.0*cm,anspar)
        else:
            c.drawString(15.0*cm,1.5*cm,anspar)

        #Ende der Seite
        c.showPage()
#
#   Druck der Zusatzinformationen
#
        zweigstelle=nN(context.unfustdor) #getattr(uaz,'unfustdor','')
        verleihfirma=nN(context.unflar) #getattr(uaz,'unflar','')
        ehegatte=nN(context.unfbu) #getattr(uaz,'unfbu','')

#    print zweigstelle
#    print verleihfirma
#    print ehegatte
#    print masch
#    a=len(nextpage)
#    print a


        masch = "nein"
        if zweigstelle=='Zweigstelle' or verleihfirma=='ja' or ehegatte=='Ehegatte des Unternehmers' or masch=='ja' or len(nextpage) > 1:


            #Grauer Hintergrund
            c.setFillGray(0.85)
            c.rect(1.4*cm,0.5*cm,width=19.0*cm,height=28.9*cm,stroke=0,fill=1)

            #Weisse Rechtecke
            c.setLineWidth(0.5)
            c.setFillGray(1.0)
            c.rect(1.6*cm,27.6*cm,width=9.0*cm,height=1.6*cm,stroke=1,fill=1)
            c.rect(12.5*cm,27.6*cm,width=7.6*cm,height=1.6*cm,stroke=1,fill=1)
            c.rect(1.6*cm,3.0*cm,width=18.4*cm,height=19.6*cm,stroke=1,fill=1)
            c.rect(1.6*cm,22.8*cm,width=18.4*cm,height=1.6*cm,stroke=1,fill=1)

            #Linien Mitgliedsnummer
            x1=13.2
            x2=13.2
            y1=27.6
            y2=28.0

            for i in range(10):
                c.line(x1*cm,y1*cm,x2*cm,y2*cm)
                x1=x1+0.7
                x2=x2+0.7

            #Titel fuer Seite2 des Formulars
            c.setFillGray(0.0)
            c.setFont(schriftartfett,18)
            c.drawString(3.5*cm,25.7*cm,"Zusatzinformationen zur U N F A L L A N Z E I G E")

            #Beschriftung Feld: Name und Anschrift des Unternehmens
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,28.9*cm,"Name und Anschrift des Unternehmers")

            #Beschriftung Feld: Mitgliedsnummer
            c.setFont(schriftartfett,7)
            c.drawString(12.7*cm,28.9*cm, u"Unternehmensnummer des Unfallversicherungsträgers")

#	Name und Anschrift des Unternehmens
#
            print addr
            plz=addr['P_PLZ']
            if plz == None:
                    plz = ' '
            ort=unicode(addr['P_ORT']).decode('utf-8')
            if ort == None:
                    ort = ' '
            strasse=unicode(addr['P_STRASSE']).decode('utf-8')
            if strasse == None:
                    strasse = ' '
            hsnr=addr['P_HAUSNR']
            if hsnr == None:
                    hsnr = ' '
            name3=unicode(addr['P_NAME-3']).decode('utf-8')
            name2=unicode(addr['P_NAME-2']).decode('utf-8')
            name1=unicode(addr['P_NAME-1']).decode('utf-8')
            c.setFont(schriftartfett,8)
            c.drawString(1.7*cm,27.7*cm,plz+' '+ort)
            c.setFont(schriftart,8)
            c.drawString(1.7*cm,28.0*cm,strasse+' '+hsnr)
            c.drawString(1.7*cm,28.3*cm,name2+' '+name3)
            c.drawString(1.7*cm,28.6*cm,name1)
#
#   	Mitgliedsnummer
#
            x=12.7
            y=27.7
            c.setFont(schriftart,10)
            for i in mitglied:
                    c.drawString(x*cm,y*cm,i)
                    x=x+0.7
            c.setFont(schriftartfett,10)
            c.drawString(1.7*cm,23.7*cm,"Name, Vorname des Versicherten")

            #Name, Vorname des Versicherten
            #
            versname=nN(context.prsnam) #getattr(uaz,'prsnam','')
            versvorname=nN(context.prsvor) #getattr(uaz,'prsvor','')
            c.setFont(schriftart,10)
            if len(versvorname) > 0:
                c.drawString(1.7*cm,23.2*cm,versname+', '+versvorname)

            #Beschriftung Feld: Unfallzeitpunkt
            c.setFont(schriftartfett,10)
            c.drawString(14*cm,23.7*cm,"Unfallzeitpunkt")

            #Unfallzeitpunkt
            #
            c.setFont(schriftart,10)
            uzeit=nN(context.unfzeit)

            if uzeit != ['','']:

                tag=uzeit[0]
                tag=tag.split('.')
                if len(tag[0])==1:
                    day='0%s' %tag[0]
                else:
                    day=tag[0]
                if len(tag[1])==1:
                    month='0%s' %tag[1]
                else:
                    month=tag[1]
                year=tag[2]
                unfalltag='%s.%s.%s' %(day,month,year)

                stunde=uzeit[1]
                stunde=stunde.split(':')
                if len(stunde[0])==1:
                    hour='0%s' %stunde[0]
                else:
                    hour=stunde[0]
                if len(stunde[1])==1:
                    minute='0%s' %stunde[1]
                else:
                    minute=stunde[1]
                unfallzeit='%s:%s' %(hour,minute)

                c.drawString(14*cm,23.2*cm,unfalltag)
                if len(stunde) > 1:
                    c.drawString(16*cm,23.2*cm,unfallzeit+" Uhr")

            addrzweigstelle1=nN(context.unfustrasse) #grrc(v=getattr(uaz,'unfustrasse',['','']),ret=['',''])
            name=addrzweigstelle1[0]
            strasse=addrzweigstelle1[1]
            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,22*cm,"Angaben zur Zweigniederlassung")
            c.setFont(schriftart,10) 
            c.drawString(1.8*cm,21.5*cm,"Name der Zweigniederlassung:")
            c.drawString(8*cm,21.5*cm,name)
            c.drawString(1.8*cm,21*cm,"Anschrift der Zweigniederlassung:")
            c.drawString(8*cm,21*cm,strasse)
            #addrzweigstelle2=nN(context.unfuplzort() #grrc(v=getattr(uaz,'unfuplzort',['','']),ret=['',''])
            plz=nN(context.unfuplz)
            ort=nN(context.unfuort)
            c.drawString(8*cm,20.5*cm,plz+" "+ort)

            leihbetrieb=nN(context.unflaraddr) #grrc(v=getattr(uaz,'unflfaddr',''),ret=' ')
            leihe=[]
            if str(leihbetrieb).find('\r\n') != -1:
                leihe=leihbetrieb.split('\r\n')
            else:
                leihe.append(leihbetrieb)

            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,19.5*cm,"Angaben zur Verleihfirma")
            c.setFont(schriftart,10) 
            c.drawString(1.8*cm,19*cm,"Name und Anschrift:")

            n=60
            y=19
            for leihfirma in leihe:
              leihfirma=leihfirma[:200]
              while len(leihfirma) > 0:
                if len(leihfirma) > n:
                    if n > 0:
                        if leihfirma[n] == " ":
                            pagentur=leihfirma[0:n]
                            c.drawString(8*cm,y*cm,pagentur)
                            leihfirma=leihfirma[(n+1):]
                            y=y-0.5
                            n=60
                        else:
                            n=n-1
                    else:
                        pagentur1=leihfirma[0:60]
                        c.drawString(8*cm,y*cm,pagentur1)
                        leihfirma=leihfirma[60:]
                        y=y-0.5
                        n=60
                else:
                    c.drawString(8*cm,y*cm,leihfirma)
                    leihfirma=''
                    y=y-0.5
              else:
                pass

            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,15.5*cm,"Angaben zum Ehegatten des Unternehmers")
            vertrag=nN(context.getVehearbeitsv()) #getattr(uaz,'vehearbeitsv','')
            beginn=nN(context.getVehebis()) #getattr(uaz,'vehebis','')
            print "beginn", beginn
            if beginn != "":
                beginn=beginn.split('.')
                if len(beginn[0])==1:
                    day='0%s' %beginn[0]
                else:
                    day=beginn[0]
                if len(beginn[1])==1:
                    month='0%s' %beginn[1]
                else:
                    month=beginn[1]
                year=beginn[2]
                ehebeginn='%s.%s.%s' %(day,month,year)
            else:
                ehebeginn=' '

            entgelt=nN(context.getVeheentgeltbis()) #getattr(uaz,'veheentgeltbis','')
            if entgelt != '':
                entgelt=entgelt.split('.')
                if len(entgelt[0])==1:
                    day='0%s' %entgelt[0]
                else:
                    day=entgelt[0]
                if len(entgelt[1])==1:
                    month='0%s' %entgelt[1]
                else:
                    month=entgelt[1]
                year=entgelt[2]
                entgeltende='%s.%s.%s' %(day,month,year)
            else:
                entgeltende=""

            c.setFont(schriftart,10)
            c.drawString(1.8*cm,15*cm,"Besteht ein Ehegattenarbeitsvertrag?")
            c.drawString(8*cm,15*cm,vertrag)
            c.drawString(1.8*cm,14.5*cm,"Gegebenenfalls seit wann:")
            c.drawString(8*cm,14.5*cm,ehebeginn)
            c.drawString(1.8*cm,14*cm,"Entgelt wurde gezahlt bis:")
            c.drawString(8*cm,14*cm,entgeltende)

            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,13*cm,"Angaben zum Unfall an einer Maschine")
            #art=nN(context.getMart() #getattr(uaz,'mart','')
            #hersteller=nN(context.getMhersteller() #getattr(uaz,'mhersteller','')
            #typ=nN(context.getMtyp() #getattr(uaz,'mtyp','')
            #baujahr=nN(context.getMbaujahr() #getattr(uaz,'mbaujahr','')
            c.setFont(schriftart,10)
            c.drawString(1.8*cm,12.5*cm,"Art der Maschine:")
            #c.drawString(8*cm,12.5*cm,art)
            c.drawString(1.8*cm,12*cm,"Hersteller der Maschine:")
            #c.drawString(8*cm,12*cm,hersteller)
            c.drawString(1.8*cm,11.5*cm,"Typ der Maschine:")
            #c.drawString(8*cm,11.5*cm,typ)
            c.drawString(1.8*cm,11*cm,"Baujahr der Maschine:")
            #c.drawString(8*cm,11*cm,baujahr)

            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,10*cm,"Beschreibung des Unfallhergangs (Fortsetzung)")
            n=125
            cpl=125
            c.setFont(schriftart,8)
            y=9.5
            print nextpage
            if nextpage:
                while len(nextpage) > 0:
                    if len(nextpage) > n:
                        if n > 0:
                            if nextpage[n] == " ":
                                schilderung=nextpage[0:n]
                                c.drawString(1.8*cm,y*cm,schilderung)
                                nextpage=nextpage[(n+1):]
                                y=y-0.35
                                n=cpl
                            else:
                                n=n-1
                        else:
                            schilderung1=nextpage[0:cpl]
                            c.drawString(1.8*cm,y*cm,schilderung1)
                            nextpage=nextpage[cpl:]
                            y=y-0.35
                            n=cpl
                    else:
                        c.drawString(1.8*cm,y*cm,nextpage)
                        nextpage=''
                else:
                    pass

            

            c.showPage()

        else:
            pass


        #Ende des Formulars
        c.save()
        fp = open(filename,'r')
        c = fp.read()
        fp.close()
        return c

