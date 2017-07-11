# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import tempfile
import uvcsite
import grok

from tempfile import TemporaryFile
from string   import replace
from time     import gmtime, strftime

from reportlab.pdfgen        import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units     import cm
from reportlab.lib.colors    import gray

from zope.i18n import translate
from zope.interface import implementer
from zope.component import adapter, getUtility
from zope.component import getMultiAdapter
from zope.publisher.interfaces import IRequest
from zope.dublincore.interfaces import IZopeDublinCore
from zope.schema.interfaces import IVocabularyFactory

from uvc.unfallanzeige.interfaces import IUnfallanzeige, IPresentation


def nN(value):
    if value == None:
        return ""
    return value


class Druck(grok.View):
    grok.context(IUnfallanzeige)
    grok.title(" ")
    grok.require('uvc.ViewContent')

    #uvcsite.sectionmenu(uvcsite.IDocumentActions, order=0, icon="/@@/uvc-icons/icon_pdf.gif")

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


    def createpdf(self, outputfilename):
        context = self.context
        request = self.request
        metadata = IZopeDublinCore(context)
        mitglied = ''.join(metadata.creators)
        filename = "/tmp/uaz_%s.pdf" %mitglied
        addr = ICompanyInfo(request.principal).getAddress()
        c = canvas.Canvas(filename,pagesize=A4)

        c.setAuthor("BG für Transport und Verkehrswirtschaft")
        c.setTitle("Unfallanzeige")
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        date = strftime("%d.%m.%Y", gmtime())
        date = metadata.modified.strftime("%d.%m.%Y")
        jahr = int(date[6:])

        if jahr > 2015:
          bv2={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Hamburg','name2':'Post-Logistik Telekommunikation','strasse':'Ottenser Hauptstraße 54','plzort':'22765 Hamburg'}
          bv3={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Hannover','name2':'Post-Logistik Telekommunikation','strasse':'Walderseestraße 5/6','plzort':'30163 Hannover'}
          bv4={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Berlin','name2':'Post-Logistik Telekommunikation','strasse':'Axel-Springer-Straße 52','plzort':'10969 Berlin'}
          bv5={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Dresden','name2':'Post-Logistik Telekommunikation','strasse':'Hofmühlenstraße 4','plzort':'01187 Dresden'}
          bv6={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Wuppertal','name2':'Post-Logistik Telekommunikation','strasse':'Aue 96','plzort':'42103 Wuppertal'}
          bv7={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung Wiesbaden','name2':'Post-Logistik Telekommunikation','strasse':'Wiesbadener Straße 70','plzort':'65197 Wiesbaden'}
          bv9={'name1':'Berufsgenossenschaft Verkehrswirtschaft','name3':'Bezirksverwaltung München','name2':'Post-Logistik Telekommunikation','strasse':'Deisenhofener Straße 74','plzort':'81539 München'}
        elif jahr > 2009:
          bv2={'name1':'Berufsgenossenschaft für','name3':'BV Hamburg','name2':'Transport und Verkehrswirtschaft','strasse':'Ottenser Hauptstraße 54','plzort':'22765 Hamburg'}
          bv3={'name1':'Berufsgenossenschaft für','name3':'BV Hannover','name2':'Transport und Verkehrswirtschaft','strasse':'Walderseestraße 5/6','plzort':'30163 Hannover'}
          bv4={'name1':'Berufsgenossenschaft für','name3':'BV Berlin','name2':'Transport und Verkehrswirtschaft','strasse':'Axel-Springer-Straße 52','plzort':'10969 Berlin'}
          bv5={'name1':'Berufsgenossenschaft für','name3':'BV Dresden','name2':'Transport und Verkehrswirtschaft','strasse':'Hofmühlenstraße 4','plzort':'01187 Dresden'}
          bv6={'name1':'Berufsgenossenschaft für','name3':'BV Wuppertal','name2':'Transport und Verkehrswirtschaft','strasse':'Aue 96','plzort':'42103 Wuppertal'}
          bv7={'name1':'Berufsgenossenschaft für','name3':'BV Wiesbaden','name2':'Transport und Verkehrswirtschaft','strasse':'Wiesbadener Straße 70','plzort':'65197 Wiesbaden'}
          bv9={'name1':'Berufsgenossenschaft für','name3':'BV München','name2':'Transport und Verkehrswirtschaft','strasse':'Deisenhofener Straße 74','plzort':'81539 München'}
        else:
          bv2={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Hamburg','name3':'','strasse':'Ottenser Hauptstrasse 54','plzort':'22765 Hamburg'}
          bv3={'name1':'Berufsgenossenschaft fr Fahrzeughaltungen','name2':'BV Hannover','name3':'','strasse':'Walderseestrasse 5/6','plzort':'30163 Hannover'}
          bv4={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Berlin','name3':'','strasse':'Axel-Springer-Strasse 52','plzort':'10969 Berlin'}
          bv5={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Dresden','name3':'','strasse':'Hofmühlenstrasse 4','plzort':'01187 Dresden'}
          bv6={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Wuppertal','name3':'','strasse':'Aue 96','plzort':'42103 Wuppertal'}
          bv7={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV Wiesbaden','name3':'','strasse':'Wiesbadener Strasse 70','plzort':'65197 Wiesbaden'}
          bv9={'name1':'Berufsgenossenschaft für Fahrzeughaltungen','name2':'BV München','name3':'','strasse':'Deisenhofener Strasse 74','plzort':'81539 München'}

        #Grauer Hintergrund
        c.setFillGray(0.85)
        c.rect(1.4*cm,0.3*cm,width=19.0*cm,height=29.1*cm,stroke=0,fill=1)
        #Weisse Rechtecke
        c.setLineWidth(0.5)
        c.setFillGray(1.0)
        c.rect(1.6*cm,27.6*cm,width=9.0*cm,height=1.6*cm,stroke=1,fill=1)
        c.rect(12.5*cm,27.6*cm,width=7.6*cm,height=1.6*cm,stroke=1,fill=1)
        c.rect(1.6*cm,22.5*cm,width=9.0*cm,height=4.5*cm,stroke=0,fill=1)
        c.rect(1.6*cm,2.8*cm,width=18.4*cm,height=18.8*cm,stroke=1,fill=1)
        c.rect(1.6*cm,0.7*cm,width=18.4*cm,height=1.9*cm,stroke=1,fill=1)

        # Senkrechte Linien bei der Unternehmensnummer
        x1=13.2
        x2=13.2
        y1=27.6
        y2=28.0
        for i in range(10):
            c.line(x1*cm,y1*cm,x2*cm,y2*cm)
            x1=x1+0.7
            x2=x2+0.7

        #Waagerechte Linien Felder 4-7
        lo = 21.6
        lm = 21.2
        y = lu = 20.8
        x1=1.6
        x2=20.0
        y1=15.5
        y2=15.5
        for i in range(3):
            c.line(x1*cm,y*cm,x2*cm,y*cm)
            y-=0.8

        #Waagerechte Linie unter Feld 10 und 11
        y -= 1.6
        c.line(x1*cm, y*cm, x2*cm, y*cm)

        #Waagerechte Linine unter Feld 12-16
        y -= 0.8
        for i in range(3):
            c.line(x1*cm, y*cm, x2*cm, y*cm)
            y -= 0.8


        #Waagerechte Linie unter Feld 17
        y -= 4
        c.line(x1*cm,y*cm,x2*cm,y*cm)

        #Waagerechte Linie unter Feld 18
        y -= 0.8
        c.line(x1*cm,y*cm,x2*cm,y*cm)

        #Waagerechte Linie unter Feld 20
        y -= 1.2
        c.line(x1*cm,y*cm,x2*cm,y*cm)

        #Waagerechte Linie unter Feld 21
        y -= 1.6
        c.line(x1*cm,y*cm,x2*cm,y*cm)

        #Waagerechte Linien unter Feld 22-27
        y -= 0.8
        for i in range(4):
            c.line(x1*cm,y*cm,x2*cm,y*cm)
            y -= 0.8

        #Linien in Feld 5
        c.line(13.7*cm,lo*cm,13.7*cm,lu*cm)
        c.setStrokeGray(0.5)
        c.line(16.5*cm,lm*cm,16.5*cm,lu*cm)
        c.line(17.5*cm,lm*cm,17.5*cm,lu*cm)

        x=16.0

        for i in range(3):
            c.line(x*cm,lo*cm,x*cm,lu*cm)
            x+=1.0

        x=18.5

        for i in range(3):
            c.line(x*cm,lm*cm,x*cm,lu*cm)
            x+=0.5

        #Linien in Feld 6
        x=10.5
        lo -= 0.8
        lm -= 0.8
        lu -= 0.8

        if hasattr(context, 'lkzbgv'):
            land = nN(context.lkzbgv)
            vocab = getUtility(IVocabularyFactory, name='uvc.sta')(None)
            try:
                term = vocab.getTerm(land)
                land = translate(term.title, 'uvc.unfallanzeige', target_language="de")
            except LookupError, e:
                print e
            
            if land != '':
                if land[0] == 'D' or land == '  ':
                    for i in range(4):
                        c.line(x*cm,lm*cm,x*cm,lu*cm)
                        x+=0.5
        else:
            for i in range(4):
                c.line(x*cm,lm*cm,x*cm,lu*cm)
                x+=0.5


        c.setStrokeGray(0.0)
        c.line(10.0*cm,lo*cm,10.0*cm,lu*cm)
        c.line(12.5*cm,lo*cm,12.5*cm,lu*cm)

        #Rechtecke in Feld 7
        lo -= 0.8
        lm -= 0.8
        lu -= 0.8

        c.rect(1.8*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(3.6*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linie abwaerts von Feld 8 bis 15
        c.line(6.5*cm,lo*cm,6.5*cm,(lu-4)*cm)

        #Rechtecke und Linien in Feld 9
        c.rect(17.3*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(18.5*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.line(17.1*cm,lo*cm,17.1*cm,lu*cm)

        #Rechtecke in Feld 10
        lo -= 0.8
        lm -= 0.8
        lu -= 0.4
        
        c.rect(1.8*cm,(lu-0.4)*cm,width=0.4*cm,height=0.4*cm)
        c.rect(3.6*cm,(lu-0.4)*cm,width=0.4*cm,height=0.4*cm)

        #Rechtecke in Feld 11
        c.rect(10.5*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(14.2*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        lu -= 0.8
        c.rect(14.7*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        lu -= 0.1
        c.rect(10.5*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        lu -= 0.5
        c.rect(14.7*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        lu -= 0.6
        c.rect(14.7*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linien in Feld 12
        lo -= 2.8
        lm -= 2.8
        lu -= 0.8
        c.line(3.6*cm,lo*cm,3.6*cm,lu*cm)
        c.line(4.6*cm,lo*cm,4.6*cm,lu*cm)

        c.setStrokeGray(0.5)
        c.line(4.1*cm,(lu+0.2)*cm,4.1*cm,lu*cm)

        #Rechtecke in Feld 14
        lo -= 0.4
        lm -= 0.4
        lu -= 0.8

        c.setStrokeGray(0.0)
        c.rect(1.8*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(3.6*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linien in Feld 15
        c.setStrokeGray(0.5)
        c.line(9.1*cm,lu*cm,9.1*cm,lo*cm)
        c.line(9.6*cm,lu*cm,9.6*cm,lm*cm)
        c.line(10.1*cm,lu*cm,10.1*cm,lo*cm)
        c.line(10.6*cm,lu*cm,10.6*cm,lm*cm)
        c.line(11.1*cm,lu*cm,11.1*cm,lo*cm)
        c.line(11.6*cm,lu*cm,11.6*cm,lm*cm)
        c.line(12.1*cm,lu*cm,12.1*cm,lm*cm)
        c.line(12.6*cm,lu*cm,12.6*cm,lm*cm)
        c.line(13.1*cm,lu*cm,13.1*cm,lo*cm)
        c.line(13.6*cm,lu*cm,13.6*cm,lm*cm)
        c.line(14.1*cm,lu*cm,14.1*cm,lo*cm)
        c.line(14.6*cm,lu*cm,14.6*cm,lm*cm)
        c.line(15.1*cm,lu*cm,15.1*cm,lo*cm)

        #Rechtecke in Feld 17
        lu -= 5.6

        c.setStrokeGray(0.0)
        c.rect(7.9*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(11.2*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linie in Feld 19
        lo -= 6.4
        lu -= 0.8
        c.line(10.7*cm,lo*cm,10.7*cm,lu*cm)

        #Rechtecke in Feld 20
        lu -= 1.2
        c.rect(15.1*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(16.6*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linien in Feld 22
        lu -= 1.6
        lm = lu + 0.4
        lh = lu + 0.8
        lo = lu + 1.6
        c.line(13.3*cm,lo*cm,13.3*cm,lu*cm)
        c.line(17.0*cm,lh*cm,17.0*cm,lu*cm)

        c.setStrokeGray(0.5)
        c.line(15.0*cm,lu*cm,15.0*cm,lh*cm)
        c.line(15.5*cm,lu*cm,15.5*cm,lm*cm)
        c.line(16.0*cm,lu*cm,16.0*cm,lh*cm)
        c.line(16.5*cm,lu*cm,16.5*cm,lm*cm)
        c.line(18.0*cm,lu*cm,18.0*cm,lh*cm)
        c.line(18.5*cm,lu*cm,18.5*cm,lm*cm)
        c.line(19.0*cm,lu*cm,19.0*cm,lh*cm)
        c.line(19.5*cm,lu*cm,19.5*cm,lm*cm)

        #Linien in Feld 24
        lo -= 1.6
        lu -= 0.8
        lm = lu + 0.4
        c.line(17.0*cm,lu*cm,17.0*cm,lo*cm)
        c.line(17.5*cm,lu*cm,17.5*cm,lm*cm)
        c.line(18.0*cm,lu*cm,18.0*cm,lo*cm)
        c.line(18.5*cm,lu*cm,18.5*cm,lm*cm)
        c.line(19.0*cm,lu*cm,19.0*cm,lm*cm)
        c.line(19.5*cm,lu*cm,19.5*cm,lm*cm)

        c.setStrokeGray(0.0)
        c.line(12.3*cm,lu*cm,12.3*cm,lo*cm)

        #Rechtecke und Linien in Feld 26
        lo -= 1.6
        lu -= 1.6
        lm = lu + 0.4
        c.rect(7.9*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(9.5*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(14.3*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        c.setStrokeGray(0.5)
        c.line(17.0*cm,lu*cm,17.0*cm,lo*cm)
        c.line(17.5*cm,lu*cm,17.5*cm,lm*cm)
        c.line(18.0*cm,lu*cm,18.0*cm,lo*cm)
        c.line(18.5*cm,lu*cm,18.5*cm,lm*cm)
        c.line(19.0*cm,lu*cm,19.0*cm,lo*cm)
        c.line(19.5*cm,lu*cm,19.5*cm,lm*cm)

        #Rechtecke und Linien in Feld 2i7
        lo -= 0.8
        lm -= 0.8
        lu -= 0.8
        c.line(16.0*cm,lu*cm,16.0*cm,lo*cm)
        c.line(16.5*cm,lu*cm,16.5*cm,lm*cm)
        c.line(17.0*cm,lu*cm,17.0*cm,lo*cm)
        c.line(17.5*cm,lu*cm,17.5*cm,lm*cm)
        c.line(18.0*cm,lu*cm,18.0*cm,lo*cm)
        c.line(18.5*cm,lu*cm,18.5*cm,lm*cm)
        c.line(19.0*cm,lu*cm,19.0*cm,lm*cm)
        c.line(19.5*cm,lu*cm,19.5*cm,lm*cm)

        c.setStrokeGray(0.0)
        c.rect(9.5*cm,lu*cm,width=0.4*cm,height=0.4*cm)
        c.rect(14.3*cm,lu*cm,width=0.4*cm,height=0.4*cm)

        #Linie in Feld 28
        c.line(1.7*cm,1.2*cm,19.9*cm,1.2*cm)

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
            c.drawString(2.1*cm,27.1*cm,"Empfänger/-in")
            c.setFont(schriftart,11)
            c.drawString(2.7*cm,25.8*cm,"An die zuständige")
            c.drawString(2.7*cm,25.3*cm,"Arbeitsschutzbehörde")
        elif flag == 'ps':
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,27.1*cm,"3")
            c.setFont(schriftart,7)
            c.drawString(2.1*cm,27.1*cm,"Empfänger/-in")
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
               bv=bv2
            c.setFont(schriftartfett,7)
            c.drawString(1.8*cm,27.1*cm,"3")
            c.setFont(schriftart,7)
            c.drawString(2.1*cm,27.1*cm, u"Empfänger/-in")
            c.setFont(schriftart,11)
            c.drawString(2.7*cm,25.8*cm,bv['name1'])
            c.drawString(2.7*cm,25.3*cm,bv['name2'])
            c.drawString(2.7*cm,24.8*cm,bv['name3'])
            c.drawString(2.7*cm,24.3*cm,bv['strasse'])
            c.setFont(schriftartfett,11)
            c.drawString(2.7*cm,23.3*cm,bv['plzort'])

        y = 21.3

        #Beschriftung Feld4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"4")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,y*cm,"Name, Vorname der versicherten Person")

        #Beschriftung Feld5
        c.setFont(schriftartfett,7)
        c.drawString(13.9*cm,y*cm,"5")
        c.setFont(schriftart,7)
        c.drawString(14.2*cm,y*cm,"Geburtsdatum")
        c.drawString(16.25*cm,y*cm,"Tag")
        c.drawString(17.15*cm,y*cm,"Monat")
        c.drawString(18.7*cm,y*cm,"Jahr")

        y -= 0.8

        #Beschriftung Feld6
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"6")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,y*cm,u"Straße, Hausnummer")
        c.drawString(10.1*cm,y*cm,"Postleitzahl")
        c.drawString(12.6*cm,y*cm,"Ort")

        y -= 0.8

        #Beschriftung Feld7
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"7")
        c.setFont(schriftart,7)
        c.drawString(2.1*cm,y*cm,"Geschlecht")
        c.drawString(2.3*cm,(y-0.4)*cm,u"Männlich")
        c.drawString(4.1*cm,(y-0.4)*cm,"Weiblich")

        #Beschriftung Feld8
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,y*cm,"8")
        c.setFont(schriftart,7)
        c.drawString(7.0*cm,y*cm,u"Staatsangehörigkeit")

        #Beschriftung Feld9
        c.setFont(schriftartfett,7)
        c.drawString(17.3*cm,y*cm,"9")
        c.setFont(schriftart,7)
        c.drawString(17.6*cm,y*cm,"Leiharbeitnehmer/-in")
        c.drawString(17.9*cm,(y-0.4)*cm,"Ja")
        c.drawString(19.0*cm,(y-0.4)*cm,"Nein")

        y -= 0.8

        #Beschriftung Feld10
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"10")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,"Auszubildende/-r")
        c.drawString(2.3*cm,(y-0.4)*cm,"Ja")
        c.drawString(4.1*cm,(y-0.4)*cm,"Nein")

        #Beschriftung Feld11
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,y*cm,"11")
        c.setFont(schriftart,7)


        c.drawString(7.1*cm,y*cm,"Die versicherte Person ist")
        c.drawString(11.0*cm,y*cm,"Unternehmer/-in")
        c.drawString(14.7*cm,y*cm,"mit der Unternehmerin/")
      
        y -= 0.3

        c.drawString(14.7*cm, y*cm,"dem Unternehmer:")

        y -= 0.5 

        c.drawString(11.0*cm,y*cm,u"Gesellschafter/-in")
        c.drawString(15.2*cm,y*cm,u"verheiratet")

        y -= 0.3
        c.drawString(11.0*cm,y*cm,u'Geschäftsführer/-in')

        y -= 0.1
        c.drawString(15.2*cm, y*cm, u'in eingetragener')
        y -= 0.3
        c.drawString(15.2*cm, y*cm, u'Lebenspartnerschaft lebend')
        y -= 0.5
        c.drawString(15.2*cm, y*cm, u'verwandt')

        y -= 0.4

        #Beschriftung Feld12
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"12")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,"Anspruch auf Entgeltfortzahlung")
        c.drawString(2.1*cm,(y-0.4)*cm,u"besteht für")
        c.drawString(4.8*cm,(y-0.4)*cm,"Wochen")

        #Beschriftung Feld13
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,y*cm,"13")
        c.setFont(schriftart,7)
        c.drawString(7.1*cm,y*cm,"Krankenkasse (Name, PLZ, Ort)")

        y -= 0.8

        #Beschriftung Feld14
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"14")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,u"Tödlicher Unfall")
        c.drawString(2.3*cm,(y-0.4)*cm,"Ja")
        c.drawString(4.1*cm,(y-0.4)*cm,"Nein")

        #Beschriftung Feld15
        c.setFont(schriftartfett,7)
        c.drawString(6.7*cm,y*cm,"15")
        c.setFont(schriftart,7)
        c.drawString(7.1*cm,y*cm,"Unfallzeitpunkt")
        c.drawString(9.4*cm,y*cm,"Tag")
        c.drawString(10.25*cm,y*cm,"Monat")
        c.drawString(11.85*cm,y*cm,"Jahr")
        c.drawString(13.2*cm,y*cm,"Stunde")
        c.drawString(14.25*cm,y*cm,"Minute")

        y -= 0.8

        #Beschriftung Feld16
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"16")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,u"Unfallort (genaue Orts- und Straßenangabe mit PLZ)")

        y -= 0.8

        #Beschriftung Feld17
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"17")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,u"Ausführliche Schilderung des Unfallhergangs")
        c.setFont(schriftart,6)
        c.drawString(7.4*cm,y*cm,u"(Verlauf, Bezeichnung des Betriebsteils, ggf. Beteiligung von Maschinen, Anlagen, Gefahrstoffen)")
        c.setFont(schriftart,7)

        y -= 4.4

        c.drawString(1.8*cm,y*cm,u"Die Angaben beruhen auf der Schilderung")
        c.drawString(8.4*cm,y*cm,u"der versicherten Person")
        c.drawString(11.7*cm,y*cm,u"anderer Personen")

        #Beschriftung Feld18
        y -= 0.4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"18")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,u"Verletzte Körperteile")

        #Beschriftung Feld19
        c.setFont(schriftartfett,7)
        c.drawString(10.9*cm,y*cm,"19")
        c.setFont(schriftart,7)
        c.drawString(11.3*cm,y*cm, u"Art der Verletzung")

        #Beschriftung Feld20
        y -= 0.8
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"20")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm, u"Wer hat von dem Unfall zuerst Kenntnis genommen ?")
        c.setFont(schriftart,6)
        c.drawString(8.2*cm,y*cm, u"(Name, Anschrift)")
        c.setFont(schriftart,7)
        c.drawString(15*cm,y*cm, u"War diese Person Augenzeugin/Augenzeuge")
        y -= 0.3
        c.drawString(15*cm,y*cm, u'des Unfalls?')
        y -= 0.5
        c.drawString(15.6*cm,y*cm, u"Ja")
        c.drawString(17.1*cm,y*cm, u"Nein")

        #Beschriftung Feld21
        y -= 0.4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"21")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm, u"Erstbehandlung:")
        c.drawString(2.2*cm,(y-0.3)*cm, u"Name und Anschrift der Ärztin/des Arztes oder des Krankenhauses")

        #Beschriftung Feld22
        c.setFont(schriftartfett,7)
        c.drawString(13.5*cm,y*cm,"22")
        c.setFont(schriftart,7)
        c.drawString(13.9*cm,y*cm, u"Beginn und Ende der Arbeitszeit")
        c.drawString(13.9*cm,(y-0.3)*cm, u"der versicherten Person")
        y -= 0.8
        c.drawString(15.1*cm,y*cm, u"Stunde")
        c.drawString(16.1*cm,y*cm, u"Minute")
        c.drawString(18.1*cm,y*cm, u"Stunde")
        c.drawString(19.1*cm,y*cm, u"Minute")
        y -= 0.4
        c.drawString(13.9*cm,y*cm, u"Beginn")
        c.drawString(17.2*cm,y*cm, u"Ende")

        #Beschriftung Feld23
        y -= 0.4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"23")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm, u"Zum Unfallzeitpunkt beschäftigt/tätig als")

        #Beschriftung Feld24
        c.setFont(schriftartfett,7)
        c.drawString(12.5*cm,y*cm,"24")
        c.setFont(schriftart,7)
        c.drawString(12.9*cm,y*cm, u"Seit wann bei dieser Tätigkeit ?")
        c.drawString(17.15*cm,y*cm,"Monat")
        c.drawString(18.7*cm,y*cm,"Jahr")

        #Beschriftung Feld25
        y -= 0.8
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"25")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm, u"In welchem Teil des Unternehmens ist die versicherte Person ständig tätig?")

        #Beschriftung Feld26
        y -= 0.8
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"26")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm, u"Hat die versicherte Person die Arbeit eingestellt?")
        c.drawString(17.25*cm,y*cm, u"Tag")
        c.drawString(18.15*cm,y*cm, u"Monat")
        c.drawString(19.1*cm,y*cm, u"Stunde")
        y -= 0.4
        c.drawString(8.5*cm,y*cm, u"Nein")
        c.drawString(10.1*cm,y*cm, u"Sofort")
        c.drawString(14.9*cm,y*cm, u"Später, am")

        #Beschriftung Feld27
        y -= 0.4
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"27")
        c.setFont(schriftart,7)
        c.drawString(2.2*cm,y*cm,"Hat die versicherte Person die Arbeit wieder aufgenommen ?")
        c.drawString(16.25*cm,y*cm,"Tag")
        c.drawString(17.15*cm,y*cm,"Monat")
        c.drawString(18.75*cm,y*cm,"Jahr")
        y -= 0.4
        c.drawString(10.1*cm,y*cm,"Nein")
        c.drawString(14.9*cm,y*cm,"Ja, am")

        #Beschriftung Feld28
        y -= 2.1
        c.setFont(schriftartfett,7)
        c.drawString(1.8*cm,y*cm,"28")
        c.setFont(schriftart,7)
        c.drawString(3.0*cm,y*cm,"Datum")
        c.drawString(5.1*cm,y*cm, u"Unternehmer/-in (Bevollmächtigte/-r)")
        c.drawString(10.3*cm,y*cm,"Betriebsrat (Personalrat)")
        c.drawString(14.65*cm,y*cm, u"Telefon-Nr. für Rückfragen")
        c.setFont(schriftartfett,12)
        c.drawString(7.0*cm,1.8*cm,u"versandt über Extranet")

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
        hsnr=addr['hausnr']
        if hsnr == None:
            hsnr = ' '

        name3=addr['name2']
        name3=unicode(name3)#.decode('utf-8')
        name2=addr['name1']
        name2=unicode(name2)#.decode('utf-8')
        name1=addr['untern_bez']
        name1=unicode(name1)#.decode('utf-8')

        c.setFont(schriftartfett,8)

        c.drawString(1.7*cm,27.7*cm,plz+' '+ort)
        c.setFont(schriftart,8)
        c.drawString(1.7*cm,28.0*cm,strasse+' '+hsnr)
        c.drawString(1.7*cm,28.3*cm,name2+' '+name3)
        if name1 != 'None':
            c.drawString(1.7*cm,28.6*cm,name1)
#
#   (2) Mitgliedsnummer
#
        x=12.7
        y=27.7
        c.setFont(schriftart,10)
        for i in mitglied:
            c.drawString(x*cm,y*cm,i)
            x=x+0.7
#
#   (3) Empfänger (Unfallversicherungsträger)
#
#   (4) Name, Vorname des Versicherten
#
        y = 20.9

        versname = nN(context.prsname) #getattr(uaz,'prsnam','')
        versvorname = nN(context.prsvor) #getattr(uaz,'prsvor','')
        c.drawString(1.7*cm,y*cm,versname+', '+versvorname)
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

            c.drawString(16.1*cm,y*cm,gebtag[0])
            c.drawString(16.6*cm,y*cm,gebtag[1])
            c.drawString(17.1*cm,y*cm,gebmonat[0])
            c.drawString(17.6*cm,y*cm,gebmonat[1])
            c.drawString(18.1*cm,y*cm,gebjahr[0])
            c.drawString(18.6*cm,y*cm,gebjahr[1])
            c.drawString(19.1*cm,y*cm,gebjahr[2])
            c.drawString(19.6*cm,y*cm,gebjahr[3])
#
#   (6) Strasse Hausnummer
#

        y -= 0.8

        plzort=nN(context.ikzplz) #grrc(v=getattr(uaz,'prsplzort',['','']),ret=['      .',''])
        aplz=nN(context.ikzplz)
        ort=nN(context.ikzort)
        #strhsnr=context.getIkstrnr() #grrc(v=getattr(uaz,'prsstrnr',['','']),ret=['',''])
        strasse=nN(context.ikstr)
        hausnummer=nN(context.iknr)
        c.drawString(12.6*cm,y*cm,ort)
        c.drawString(1.7*cm,y*cm,strasse+' '+hausnummer)
        if hasattr(context, 'lkzbgv'):
            if land != '':
                if land[0] == 'D':
                    c.drawString(10.1*cm,y*cm,aplz[0])
                    c.drawString(10.6*cm,y*cm,aplz[1])
                    c.drawString(11.1*cm,y*cm,aplz[2])
                    c.drawString(11.6*cm,y*cm,aplz[3])
                    c.drawString(12.1*cm,y*cm,aplz[4])
                elif land[0] != 'D' and land != '':
                    c.drawString(10.1*cm,y*cm,land[0]+'-'+aplz)
        else:
            if aplz:
                c.drawString(10.1*cm,y*cm,aplz[0])
                c.drawString(10.6*cm,y*cm,aplz[1])
                c.drawString(11.1*cm,y*cm,aplz[2])
                c.drawString(11.6*cm,y*cm,aplz[3])
                c.drawString(12.1*cm,y*cm,aplz[4])
#
#   (7) Geschlecht
#

        y -= 0.8

        c.setFont(schriftart,10)
        sex=nN(context.prssex)
        if sex == 'maennlich':
            c.drawString(1.9*cm,y*cm,'x')
        elif sex == 'weiblich':
            c.drawString(3.7*cm,y*cm,'x')
#
#   (8) Staatsangehörigkeitt
#
        staat = nN(context.prssta) #grrc(v=getattr(uaz,'prssta',['','']),ret=[' ',''])
        vocab = getUtility(IVocabularyFactory, name='uvc.sta')(None)
        try:
            term  = vocab.getTerm(staat)
            staat = translate(term.title, 'uvc.unfallanzeige', target_language="de")
        except LookupError, e:
            print e
        c.setFont(schriftart,10)
        c.drawString(6.6*cm,y*cm,staat)
#
#   (9) Leiharbeitnehmer
#
        c.setFont(schriftart,10)
        leiharbeit=nN(context.unflar) #getattr(uaz,'unflar','')
        if leiharbeit == 'ja':
            c.drawString(17.4*cm,y*cm,'x')
        elif leiharbeit == 'nein':
            c.drawString(18.6*cm,y*cm,'x')
#
#   (10) Auszubildender
#

        y -= 0.8

        c.setFont(schriftart,10)

        azubi = getattr(context, 'azubi', None) 
        if azubi:
            if azubi == 'ja':
                c.drawString(1.9*cm,y*cm,'x')
            elif azubi == 'nein':
                c.drawString(3.7*cm,y*cm,'x')
        else:
            azubi=nN(context.uadbru1)
            if azubi == 'Auszubildender':
                c.drawString(1.9*cm,y*cm,'x')
            elif azubi != 'Auszubildender':
                c.drawString(3.7*cm,y*cm,'x')
#
#   (11) Ist der Versicherte                
#
        c.setFont(schriftart,10)

        y0 = y + 0.4
        y1 = y - 0.5
        y2 = y - 0.4
        y3 = y - 1.0
        y4 = y - 1.6

        ist = ''
        ist=nN(context.unfbu) #getattr(uaz,'unfbu',[''])
        if ist == 'Unternehmer':
            c.drawString(10.6*cm,y0*cm,'x')
        elif ist == 'Ehegatte des Unternehmers':
            c.drawString(14.3*cm,y0*cm,'x')
            c.drawString(14.8*cm,y2*cm,'x')
        elif ist == 'eingetragenen Lebenspartnerschaft':
            c.drawString(14.3*cm,y0*cm,'x')
            c.drawString(14.8*cm,y3*cm,'x')
        elif ist == 'Kommanditist':
            c.drawString(10.6*cm, y4*cm, 'x')
        elif ist == 'mit dem Unternehmer verwandt':
            c.drawString(14.3*cm,y0*cm,'x')
            c.drawString(14.8*cm,y4*cm, 'x')
        elif ist == 'Gesellschafter / Geschaeftsfuehrer':
            c.drawString(10.6*cm,y1*cm,'x')
        else:
            pass
#
#    (12) Anspruch auf Entgeltfortzahlung
#

        y -= 2.4

        c.setFont(schriftart,10)
        entgelt=str(nN(context.unfefz)) # grrc(v=getattr(uaz,'unfefz',''),ret='  ')
        if len(entgelt) == 0:
            entgelt="  "
        if len(entgelt) == 1:
           c.drawString(4.2*cm,y*cm,entgelt[0])
        if len(entgelt) > 1:
           c.drawString(3.7*cm,y*cm,entgelt[0])
           c.drawString(4.2*cm,y*cm,entgelt[1])
#
#    (13) Krankenkasse des Versicherten
#
        c.setFont(schriftart,8)
        kk=nN(context.unfkka) #getattr(uaz,'unfkka','')
        c.drawString(6.7*cm,y*cm,kk)
#
#   (14) Tödlicher Unfall
#
 
        y -= 0.8
   
        c.setFont(schriftart,10)
        tod=nN(context.prstkz) #getattr(uaz,'prstkz','')
        if tod == 'ja':
            c.drawString(1.9*cm,y*cm,'x')
        elif tod == 'nein':
            c.drawString(3.7*cm,y*cm,'x')
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

                c.drawString(9.2*cm,y*cm,tag[0])
                c.drawString(9.7*cm,y*cm,tag[1])
                c.drawString(10.2*cm,y*cm,monat[0])
                c.drawString(10.7*cm,y*cm,monat[1])
                c.drawString(11.2*cm,y*cm,jahr[0])
                c.drawString(11.7*cm,y*cm,jahr[1])
                c.drawString(12.2*cm,y*cm,jahr[2])
                c.drawString(12.7*cm,y*cm,jahr[3])
                c.drawString(13.2*cm,y*cm,std[0])
                c.drawString(13.7*cm,y*cm,std[1])
                c.drawString(14.2*cm,y*cm,min[0])
                c.drawString(14.7*cm,y*cm,min[1])
#
#   (16) Unfallort
#

        y -= 0.8

        c.setFont(schriftart,10)
        uort=nN(context.unfort) #getattr(uaz,'unfuor','')
        uort = uort.replace('\r\n', ' ')
        uort = uort.replace('\r', ' ')
        uort = uort.replace('\n', ' ')
        uortlen = len(uort)
        if uortlen > 100:
            uortlen = 100
        c.drawString(1.7*cm,y*cm,uort[:uortlen])
#
#   (17) Ausführliche Schilderung des Unfalls
#

        y -= 0.8

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
        y1=y
        while len(hergang) > 0:
            if len(hergang) > n:
                if n > 0:
                    if hergang[n] == " ":
                        schilderung=hergang[0:n]
                        c.drawString(1.7*cm,y1*cm,schilderung)
                        hergang=hergang[(n+1):]
                        y1-=0.35
                        n=cpl
                    else:
                        n=n-1
                else:
                    schilderung1=hergang[0:cpl]
                    c.drawString(1.7*cm,y1*cm,schilderung1)
                    hergang=hergang[cpl:]
                    y1-=0.35
                    n=cpl
            else:
                c.drawString(1.7*cm,y1*cm,hergang)
                hergang=''
        else:
            pass
        c.setFont(schriftart,10)
        schilderungen=nN(context.unfhg2) #getattr(uaz,'unfhg2',[''])
        y -= 4
        if schilderungen == 'des Versicherten':
            c.drawString(8.0*cm,y*cm,'x')
        elif schilderungen == 'einer anderen Person':
            c.drawString(11.3*cm,y*cm,'x')
#
#   (18) Verletztes Körperteile
#
 
        y -= 0.8
 
        kteile=nN(context.diavkt) #getattr(uaz,'diavkt','')
        if len(kteile)>70:
            c.setFont(schriftart,7)
            kteile = kteile[:70] + ' ...'
        elif len(kteile)>50:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(1.7*cm,y*cm,kteile)
#
#   (19) Art der Verletzung
#
        vart=nN(context.diaadv) #getattr(uaz,'diaadv','')
        if len(vart)>50:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(10.8*cm,y*cm,vart)
#
#   (20) Wer hat von dem Unfall Kenntnis genommen?
#

        y -= 1.2

        wer=nN(context.unfkn1) #ngetattr(uaz,'unfkn1','')
        wer = wer.replace('\r\n', ' ')
        wer = wer.replace('\r', ' ')
        wer = wer.replace('\n', ' ')
        if len(wer)>60:
            c.setFont(schriftart,8)
        else:
            c.setFont(schriftart,10)
        c.drawString(1.7*cm,y*cm,wer)
        c.setFont(schriftart,10)
        augenzeuge=nN(context.unfkn2) #getattr(uaz,'unfkn2','')
        if augenzeuge == 'ja':
            c.drawString(15.2*cm,y*cm,'x')
        elif augenzeuge == 'nein':
            c.drawString(16.7*cm,y*cm,'x')
#
#   (21) Name und Anschrift des erstbehandelnden Arztes
#
#    c.setFont(schriftart,8)
#    arzt=getattr(uaz,'unfeba1','')
#    c.drawString(1.7*cm,6.55*cm,arzt.encode('latin-1'))

        y -= 1.2

        abehandlung=nN(context.unfeba)
        if abehandlung=='Es ist keine Aerztliche Behandlung erforderlich':
            c.drawString(1.7*cm,y*cm,u'keine ärztliche Behandlung erforderlich')

        c.setFont(schriftart,8)
        arzt=nN(context.unfeba1) #grrc(v=getattr(uaz,'unfeba1',''),ret=' ')
        arzt = arzt.replace('\r\n', ' ')
        arzt = arzt.replace('\r', ' ')
        arzt = arzt.replace('\n', ' ')
        n=75
        y1 = y
        y2 = y - 0.4
        # es duerfen nur zwei Zeilen gedruckt werden, ausserdem werden
        # Schmierzeichen entfernt
        while len(arzt) > 0:
            if len(arzt) > n:
                if n > 0:
                    if arzt[n] == " ":
                        notarzt=arzt[0:n]
                        if y1 > y2:
                            c.drawString(1.7*cm,y1*cm,notarzt)
                        arzt=arzt[(n+1):]
                        y1-=0.35
                        n=75
                    else:
                        n=n-1
                else:
                    notarzt1=arzt[0:75]
                    if y1 > y2:
                        c.drawString(1.7*cm,y1*cm,notarzt1)
                    arzt=arzt[75:]
                    y1-=0.35
                    n=75
            else:
                if y1 > y2:
                    c.drawString(1.7*cm,y1*cm,arzt)
                arzt=''
        else:
            pass
#
#   (22) Beginn und Ende der Arbeitszeit
#

        y -= 0.4

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

                c.drawString(15.1*cm,y*cm,std[0])
                c.drawString(15.6*cm,y*cm,std[1])
                c.drawString(16.1*cm,y*cm,min[0])
                c.drawString(16.6*cm,y*cm,min[1])

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

                c.drawString(18.1*cm,y*cm,std[0])
                c.drawString(18.6*cm,y*cm,std[1])
                c.drawString(19.1*cm,y*cm,min[0])
                c.drawString(19.6*cm,y*cm,min[1])
#
#   (23) Zum Unfallzeitpunkt beschäftigt alss
#

        y -= 0.8

        c.setFont(schriftart,10)

        taetig = ''
        taetig=nN(context.uadbru1) #grrc(v=getattr(uaz,'uadbru',['','']),ret=[' ',''])


        c.drawString(1.7*cm,y*cm,taetig)
#
#   (24) Seit wann bei dieser Tätigkeitt
#
        abeginn=nN(context.uadst)
        if abeginn!="":

            if abeginn.find('.')!=-1:
                abeginn=abeginn.split('.')
                ab_monat=abeginn[0]
                ab_jahr=abeginn[1]
                if len(ab_monat)==1:
                    ab_monat='0%s' %ab_monat

                c.drawString(17.1*cm,y*cm,ab_monat[0])
                c.drawString(17.6*cm,y*cm,ab_monat[1])
                c.drawString(18.1*cm,y*cm,ab_jahr[0])
                c.drawString(18.6*cm,y*cm,ab_jahr[1])
                c.drawString(19.1*cm,y*cm,ab_jahr[2])
                c.drawString(19.6*cm,y*cm,ab_jahr[3])
#
#   (25) In welchem Teil des Unternehmens
#

        y -= 0.8

        unter = ''
        unter=nN(context.unfute) #grrc(v=getattr(uaz,'unfute',['','']),ret=[' ',''])
        c.drawString(1.7*cm,y*cm,unter)
#
#   (26) Hat der Versicherte die Arbeit eingestellt?
#
        y -= 0.8
        einstell=nN(context.unfae1)
        #if einstell == 'nein':
        if einstell == 'nein'  and tod == 'nein':
            c.drawString(8.0*cm,y*cm,'x')
        #elif einstell == 'ja, sofort':
        elif einstell == 'ja, sofort'  and tod == 'nein':
            c.drawString(9.6*cm,y*cm,'x')
        #elif einstell == 'ja, spaeter am:':
        elif einstell == 'ja, spaeter am:'  and tod == 'nein':
            c.drawString(14.4*cm,y*cm,'x')

            tagmonat = context.unfaedatum
            stunde   = context.unfaezeit

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

            c.drawString(17.1*cm,y*cm,tag[0])
            c.drawString(17.6*cm,y*cm,tag[1])
            c.drawString(18.1*cm,y*cm,monat[0])
            c.drawString(18.6*cm,y*cm,monat[1])
            c.drawString(19.1*cm,y*cm,std[0])
            c.drawString(19.6*cm,y*cm,std[1])
#
#   (27) Hat der Versicherte die Arbeit wieder aufgenommen?

        y -= 0.8#
        aufnahme=nN(context.unfwa1)

        #if aufnahme == 'nein':
        if aufnahme == 'nein'  and tod == 'nein':
            c.drawString(9.6*cm,y*cm,'x')
        #elif aufnahme == 'ja':
        elif aufnahme == 'ja'  and tod == 'nein':
            c.drawString(14.4*cm,y*cm,'x')

            azeit=nN(context.unfwax)

            azeit=azeit.split('.')
            tag=azeit[0]
            monat=azeit[1]
            jahr=azeit[2]

            if len(tag)==1:
                tag='0%s' %tag
            if len(monat)==1:
                monat='0%s' %monat

            c.drawString(16.1*cm,y*cm,tag[0])
            c.drawString(16.6*cm,y*cm,tag[1])
            c.drawString(17.1*cm,y*cm,monat[0])
            c.drawString(17.6*cm,y*cm,monat[1])
            c.drawString(18.1*cm,y*cm,jahr[0])
            c.drawString(18.6*cm,y*cm,jahr[1])
            c.drawString(19.1*cm,y*cm,jahr[2])
            c.drawString(19.6*cm,y*cm,jahr[3])
#
#   (28) Datum Unterschrift
#
        y -= 1.6
        c.setFont(schriftart,8)
        c.drawString(2.8*cm,y*cm,date)
        unternehmer = nN(context.unfus2) #getattr(uaz,'unfus2','')
        personalrat = nN(context.unfus3) #getattr(uaz,'unfus3','')
        # anspartel1="%s,%s" %(anspartel[0],anspartel[1])
        anspar      = nN(context.anspname)
        tel         = nN(context.anspfon)

        c.drawString(4.8*cm,y*cm,unternehmer)
        c.drawString(10.0*cm,y*cm,personalrat)
        if len(tel)!=0:
            c.drawString(15.0*cm,y*cm,"Telefon:"+" "+tel)
            c.drawString(15.0*cm,(y+0.5)*cm,anspar)
        else:
            c.drawString(15.0*cm,y*cm,anspar)

        #Ende der Seite
        c.showPage()
#
#   Druck der Zusatzinformationen
#
        zweigstelle  = nN(context.unfustdor) #getattr(uaz,'unfustdor','')
        verleihfirma = nN(context.unflar) #getattr(uaz,'unflar','')

        ehegatte = ''
        if IPrincipalSparteVerkehr.providedBy(self.request.principal):
            ehegatte     = nN(context.unfbu) #getattr(uaz,'unfbu','')
        else:
            if hasattr(context, 'seeunfbu'):
                ehegatte     = nN(context.seeunfbu)

        if hasattr(context, 'maschine'):
            maschine = nN(context.maschine)
        else:
            maschine = None

        if 'Zweig' in zweigstelle  or  verleihfirma == 'ja'  or  ehegatte == 'Ehegatte des Unternehmers'  or ehegatte == 'eingetragene Lebenspartnerschaft' or  maschine == 'ja'  or  len(nextpage) > 1:

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
            c.drawString(1.8*cm,28.9*cm,"Name und Anschrift des Unternehmens")

            #Beschriftung Feld: Mitgliedsnummer
            c.setFont(schriftartfett,7)
            c.drawString(12.7*cm,28.9*cm, u"Unternehmensnummer des Unfallversicherungsträgers")

#	Name und Anschrift des Unternehmens
#
            plz=nN(addr['plz'])
            ort=nN(unicode(addr['ort']).decode('utf-8'))
            strasse=nN(unicode(addr['strasse']).decode('utf-8'))
            hsnr=nN(addr['hausnr'])
            name3=unicode(addr['name2'])#.decode('utf-8')
            name2=unicode(addr['name1'])#.decode('utf-8')
            name1=unicode(addr['untern_bez'])#.decode('utf-8')

            c.setFont(schriftartfett,8)

            c.drawString(1.7*cm,27.7*cm,plz+' '+ort)

            c.setFont(schriftart,8)
            c.drawString(1.7*cm,28.0*cm,strasse+' '+hsnr)
            c.drawString(1.7*cm,28.3*cm,name2+' '+name3)
            if name1 != 'None':
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
            c.drawString(1.7*cm,23.7*cm,"Name, Vorname der versicherten Person")

            #Name, Vorname des Versicherten
            versname=nN(context.prsname) #getattr(uaz,'prsnam','')
            versvorname=nN(context.prsvor) #getattr(uaz,'prsvor','')
            c.setFont(schriftart,10)
            if len(versvorname) > 0:
                c.drawString(1.7*cm,23.2*cm,versname+', '+versvorname)

            #Beschriftung Feld: Unfallzeitpunkt
            c.setFont(schriftartfett,10)
            c.drawString(14*cm,23.7*cm,"Unfallzeitpunkt")

            #Unfallzeitpunkt
            c.setFont(schriftart,10)
            uzeit=nN(context.unfzeit)

            if uzeit != '':
                datum  = nN(context.unfdatum)
                stunde = nN(context.unfzeit)

                datum = datum.split('.')
                tag   = datum[0]
                monat = datum[1]
                jahr  = datum[2]

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

                unfalltag  = '%s.%s.%s' %(tag,monat,jahr)
                unfallzeit = '%s:%s'    %(std,min)

                c.drawString(14*cm,23.2*cm,unfalltag)
                if len(stunde) > 1:
                    c.drawString(16*cm,23.2*cm,unfallzeit+" Uhr")
#
# Zweigstelle
#
            if 'Zweig' in zweigstelle:
                name    = nN(context.unfuname)
                strasse = nN(context.unfustrasse)
                nr      = nN(context.unfunr)
                plz     = nN(context.unfuplz)
                ort     = nN(context.unfuort)

                c.setFont(schriftartfett,10)
                c.drawString(1.8*cm,22*cm,"Angaben zur Zweigniederlassung")
                c.setFont(schriftart,10)
                c.drawString(1.8*cm,21.5*cm,"Name der Zweigniederlassung:")
                c.drawString(8*cm,21.5*cm,name)
                c.drawString(1.8*cm,21*cm,"Anschrift der Zweigniederlassung:")
                c.drawString(8*cm, 21*cm,   strasse+" "+nr)
                c.drawString(8*cm, 20.5*cm, plz+" "+ort)
#
# Leiharbeiter
#
            if  verleihfirma == 'ja':
                leihbetrieb=nN(context.unvlaraddr) #grrc(v=getattr(uaz,'unflfaddr',''),ret=' ')
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

#
#  Arbeitsverhaeltnis
#
            if ehegatte == 'Ehegatte des Unternehmers' or 'eingetragene Lebenspartnerschaft':
                c.setFont(schriftartfett,10)
                if ehegatte == 'Ehegatte des Unternehmers':
                    c.drawString(1.8*cm,15.5*cm,"Angaben zur Ehegattin/zum Ehegatten der Unternehmerin/des Unternehmers")
                if ehegatte == 'eingetragene Lebenspartnerschaft':
                    c.drawString(1.8*cm,15.5*cm,"Angaben zur eingetragenen Lebenspartnerschaft der Unternehmerin/des Unternehmers")
                vertrag = nN(context.vehearbeitsv) #getattr(uaz,'vehearbeitsv','')
                beginn  = nN(context.vehebis) #getattr(uaz,'vehebis','')
                #print "beginn", beginn
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

                entgelt=nN(context.veheentgeltbis) #getattr(uaz,'veheentgeltbis','')
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
                c.drawString(1.8*cm,15*cm,"Besteht ein Arbeitsvertrag?")
                c.drawString(8*cm,15*cm,vertrag)
                c.drawString(1.8*cm,14.5*cm,"Gegebenenfalls seit wann:")
                c.drawString(8*cm,14.5*cm,ehebeginn)
                c.drawString(1.8*cm,14*cm,"Entgelt wurde gezahlt bis:")
                c.drawString(8*cm,14*cm,entgeltende)
#
# Maschine
#
            if maschine == 'ja':
                art        = nN(context.art) #getattr(uaz,'mart','')
                hersteller = nN(context.hersteller) #getattr(uaz,'mhersteller','')
                typ        = nN(context.typ) #getattr(uaz,'mtyp','')
                baujahr    = nN(context.baujahr) #getattr(uaz,'mbaujahr','')

                c.setFont(schriftartfett,10)
                c.drawString(1.8*cm,13*cm,"Angaben zum Unfall an einer Maschine")
                c.setFont(schriftart,10)
                c.drawString(1.8*cm,12.5*cm,"Art der Maschine:")
                c.drawString(8*cm,12.5*cm,art)
                c.drawString(1.8*cm,12*cm,"Hersteller der Maschine:")
                c.drawString(8*cm,12*cm,hersteller)
                c.drawString(1.8*cm,11.5*cm,"Typ der Maschine:")
                c.drawString(8*cm,11.5*cm,typ)
                c.drawString(1.8*cm,11*cm,"Baujahr der Maschine:")
                c.drawString(8*cm,11*cm,baujahr)
#
# Unfallhergang: Fortsetzung
#
            c.setFont(schriftartfett,10)
            c.drawString(1.8*cm,10*cm,"Beschreibung des Unfallhergangs (Fortsetzung)")
            n=125
            cpl=125
            c.setFont(schriftart,8)
            y=9.5
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
        fp = open(filename, 'r')
        c = fp.read()
        fp.close()
        return c
