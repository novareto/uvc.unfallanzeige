# -*- coding: utf-8 -*-
# # Copyright (c) 2007-2018 NovaReto GmbH
# # cklinger@novareto.de

import grok
import uvcsite

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.ttfonts import TTFont
from uvc.unfallanzeige.interfaces import IUnfallanzeige
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.i18n import translate


class MockA(object):

    name1= u"KLAS"
    name2= u"KK"
    strasse = "kk"
    nr = "1"
    plz = "99999"
    ort = u"ORT"


class PDFPresentation(uvcsite.BasePDF):
    grok.context(IUnfallanzeige)
    grok.name('pdf')
    grok.title('unfallanzeige.pdf')

    def __init__(self, context, request):
        super(PDFPresentation, self).__init__(context, request)
        self.uaz = self.context
        #stammdaten = IStammdaten(self.request.principal)
        self.uaz.addr = MockA() #stammdaten.getAdresse()
        self.uaz.bv = MockA() #stammdaten.getHauptAdresse()
        print self.uaz.addr
        print self.uaz.bv
        #self.canvas = canvas.Canvas("/tmp/unfallanzeige.pdf")
        #self.canvas.setAuthor(u"novareto GmbH")
        #self.canvas.setTitle(u"Elektronische Unfallanzeige")

    def drawpdf(self, c):
        """zeichnet des UAZ-Formular"""

        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"

        ## Zeichnen von Linien:##

        # Dokumentrahmen:
        c.rect(2.5*cm, 1.8*cm, 17.2*cm, 25.4*cm)


        # Parallellinien oben wagerecht:
        x1=2.5*cm
        x2=19.7*cm
        y=20.3
        diff=0.8
        for i in range(4):
            c.line(x1, y*cm, x2, y*cm)
            y=y-diff


        #Trennstrich Z1 Spalten 2-4 durchgezogen:
        c.line(12.5*cm, 17.9*cm, 12.5*cm, 20.3*cm)


        #Feld Unternehmensnummer:
        c.line(12.2*cm, 25.5*cm, 19.7*cm, 25.5*cm)
        c.line(12.2*cm, 25.5*cm, 12.2*cm, 26.2*cm)


        #Feld Empfaenger/in:
        c.line(2.8*cm, 24*cm, 3.1*cm, 24*cm)
        c.line(2.8*cm, 20.8*cm, 2.8*cm, 20.5*cm)
        c.line(2.8*cm, 20.5*cm, 3.1*cm, 20.5*cm)
        c.line(2.8*cm, 23.7*cm, 2.8*cm, 24*cm)
        c.line(10.4*cm, 24*cm, 10.7*cm, 24*cm)
        c.line(10.7*cm, 23.7*cm, 10.7*cm, 24*cm)
        c.line(10.7*cm, 20.5*cm, 10.7*cm, 20.8*cm)
        c.line(10.4*cm, 20.5*cm, 10.7*cm, 20.5*cm)

        #Parallellinien unten wagerecht:
        x1=2.5*cm
        x2=19.7*cm
        y=6.6
        diff=0.8
        for i in range(5):
            c.line(x1, y*cm, x2, y*cm)
            y=y-diff

        #Trennstriche Tag/Monat/Jahr-durchgezogen:
        y1=19.5*cm
        y2=20.3*cm
        x=15
        diff=1.2
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        #Trennstriche Tag/Monat/Jahr halbdurchgezogen:
        y1=19.5*cm
        y2=19.8*cm
        x=15.6
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff
        c.line(15.6*cm, 19.5*cm, 15.6*cm, 19.8*cm)

        c.line(17.9*cm, 19.5*cm, 17.9*cm, 19.8*cm)
        y1=19.5*cm
        y2=19.8*cm
        x=17.9
        diff=0.6
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        #Trennstriche Z2 Durchgezogen:
        c.line(9.7*cm, 18.7*cm, 9.7*cm, 19.5*cm)

        #halbdurchgezogen:
        c.line(10.2*cm, 18.7*cm, 10.2*cm, 19.0*cm)
        y1=18.7*cm
        y2=19.0*cm
        x=10.2
        diff=0.6
        for i in range(4):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        #Allgemein Trennsrich Durchgezogen:
        c.line(7.9*cm, 14.6*cm, 7.9*cm, 15.6*cm)
        c.line(5.9*cm, 13.6*cm, 5.9*cm, 14.6*cm)
        c.line(12.9*cm, 13.6*cm, 12.9*cm, 14.6*cm)
        c.line(11.1*cm, 9.1*cm, 11.1*cm, 9.8*cm)
        c.line(12.7*cm, 6.6*cm, 12.7*cm, 7.9*cm)
        c.line(11.7*cm, 5.8*cm, 11.7*cm, 6.6*cm)
        c.line(7*cm, 13.6*cm, 7*cm, 14.2*cm)
        y1=13.6*cm
        y2=14.2*cm
        x=7
        diff=1.1
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff
        c.line(6.45*cm, 13.6*cm, 6.45*cm, 14*cm)
        y1=13.6*cm
        y2=14*cm
        x=6.45
        diff=1.1
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(10.5*cm, 13.6*cm, 10.5*cm, 14.2*cm)
        y1=13.6*cm
        y2=14.2*cm
        x=10.5
        diff=1.1
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(14*cm, 6.6*cm, 14*cm, 7.2*cm)
        y1=6.6*cm
        y2=7.2*cm
        x=14
        diff=1.2
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(17.4*cm, 6.6*cm, 17.4*cm, 7.2*cm)
        y1=6.6*cm
        y2=7.2*cm
        x=17.4
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(16.4*cm, 5.8*cm, 16.4*cm, 6.6*cm)
        y1=5.8*cm
        y2=6.6*cm
        x=16.4
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(16.2*cm, 4.2*cm, 16.2*cm, 5*cm)
        y1=4.2*cm
        y2=5*cm
        x=16.2
        diff=1.2
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(15*cm, 3.4*cm, 15*cm, 4.2*cm)
        y1=3.4*cm
        y2=4.2*cm
        x=15
        diff=1.2
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff


        #Halbdurchgezogen:
        c.line(8.7*cm, 13.6*cm, 8.7*cm, 14*cm)
        y1=13.6*cm
        y2=14*cm
        x=8.7
        diff=0.6
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(11.05*cm, 13.6*cm, 11.05*cm, 14*cm)
        y1=13.6*cm
        y2=14*cm
        x=11.05
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(14.6*cm, 6.6*cm, 14.6*cm, 7*cm)
        y1=6.6*cm
        y2=7*cm
        x=14.6
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(18*cm, 6.6*cm, 18*cm, 7*cm)
        y1=6.6*cm
        y2=7*cm
        x=18
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(17*cm, 5.8*cm, 17*cm, 6.2*cm)
        y1=5.8*cm
        y2=6.2*cm
        x=17
        diff=1.2
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(18.7*cm, 5.8*cm, 18.7*cm, 6.2*cm)
        y1=5.8*cm
        y2=6.2*cm
        x=18.7
        diff=0.5
        for i in range(2):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(16.8*cm, 4.2*cm, 16.8*cm, 4.6*cm)
        y1=4.2*cm
        y2=4.6*cm
        x=16.8
        diff=1.2
        for i in range(3):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff

        c.line(18.6*cm, 3.4*cm, 18.6*cm, 3.8*cm)
        c.line(15.6*cm, 3.4*cm, 15.6*cm, 3.8*cm)
        y1=3.4*cm
        y2=3.8*cm
        x=15.6
        diff=1.2
        for i in range(4):
            c.line(x*cm, y1, x*cm, y2)
            x=x+diff
        c.line(18.6*cm, 4.2*cm, 18.6*cm, 5*cm)

        #Trennstrich Z3-Spalte 5 durchgezogen:
        c.line(6.3*cm, 15.6*cm, 6.3*cm, 18.7*cm)

        #Allgemein wagerecht durgezogene Linien:
        c.line(2.5*cm, 15.6*cm, 19.7*cm, 15.6*cm)
        c.line(2.5*cm, 15.6*cm, 19.7*cm, 15.6*cm)
        c.line(2.5*cm, 14.6*cm, 19.7*cm, 14.6*cm)
        c.line(2.5*cm, 13.6*cm, 19.7*cm, 13.6*cm)
        c.line(2.5*cm, 9.8*cm, 19.7*cm, 9.8*cm)
        c.line(2.5*cm, 9.1*cm, 19.7*cm, 9.1*cm)
        c.line(2.5*cm, 7.9*cm, 19.7*cm, 7.9*cm)
        c.line(2.5*cm, 2.3*cm, 19.7*cm, 2.3*cm)

        #Checkboxen:
        c.rect(2.7*cm, 18*cm, 0.3*cm, 0.3*cm)
        c.rect(4.7*cm, 18*cm, 0.3*cm, 0.3*cm)
        c.rect(12.7*cm, 18*cm, 0.3*cm, 0.3*cm)
        c.rect(14.7*cm, 18*cm, 0.3*cm, 0.3*cm)
        c.rect(2.7*cm, 17.2*cm, 0.3*cm, 0.3*cm)
        c.rect(4.7*cm, 17.2*cm, 0.3*cm, 0.3*cm)
        c.rect(10.5*cm, 17.5*cm, 0.3*cm, 0.3*cm)
        c.rect(10.5*cm, 16.9*cm, 0.3*cm, 0.3*cm)
        c.rect(14.7*cm, 17.5*cm, 0.3*cm, 0.3*cm)
        c.rect(15.4*cm, 16.9*cm, 0.3*cm, 0.3*cm)
        c.rect(15.4*cm, 16.5*cm, 0.3*cm, 0.3*cm)
        c.rect(15.4*cm, 15.75*cm, 0.3*cm, 0.3*cm)
        c.rect(4.2*cm, 14.75*cm, 1.2*cm, 0.4*cm)
        c.line(4.8*cm, 14.75*cm, 4.8*cm, 15.15*cm)
        c.rect(2.7*cm, 13.85*cm, 0.3*cm, 0.3*cm)
        c.rect(4.7*cm, 13.85*cm, 0.3*cm, 0.3*cm)
        c.rect(8.8*cm, 9.9*cm, 0.3*cm, 0.3*cm)
        c.rect(12.4*cm, 9.9*cm, 0.3*cm, 0.3*cm)
        c.rect(13.9*cm, 8*cm, 0.3*cm, 0.3*cm)
        c.rect(16*cm, 8*cm, 0.3*cm, 0.3*cm)
        c.rect(13*cm, 4.6*cm, 0.3*cm, 0.3*cm)
        c.rect(11*cm, 4.6*cm, 0.3*cm, 0.3*cm)
        c.rect(13*cm, 3.8*cm, 0.3*cm, 0.3*cm)
        c.rect(11*cm, 3.8*cm, 0.3*cm, 0.3*cm)

        #Nummerierung:
        c.setFont(schriftartfett, 8)
        c.drawString(2.7*cm, 26.3*cm, '1')
        c.drawString(12.3*cm, 26.3*cm, '2')
        c.drawString(2.7*cm, 24.1*cm, '3')
        c.drawString(2.7*cm, 20*cm, '4')
        c.drawString(12.7*cm, 20*cm, '5')
        c.drawString(2.7*cm, 19.2*cm, '6')
        c.drawString(2.7*cm, 18.4*cm, '7')
        c.drawString(6.4*cm, 18.4*cm, '8')
        c.drawString(12.7*cm, 18.4*cm, '9')
        c.drawString(2.7*cm, 17.6*cm, '10')
        c.drawString(6.4*cm, 17.6*cm, '11')
        c.drawString(2.7*cm, 15.3*cm, '12')
        c.drawString(8*cm, 15.3*cm, '13')
        c.drawString(2.7*cm, 14.3*cm, '14')
        c.drawString(6*cm, 14.3*cm, '15')
        c.drawString(13*cm, 14.3*cm, '16')
        c.drawString(2.7*cm, 13.3*cm, '17')
        c.drawString(2.7*cm, 9.5*cm, '18')
        c.drawString(11.2*cm, 9.5*cm, '19')
        c.drawString(2.7*cm, 8.8*cm, '20')
        c.drawString(2.7*cm, 7.6*cm, '21')
        c.drawString(12.9*cm, 7.6*cm, '22')
        c.drawString(2.7*cm, 6.3*cm, '23')
        c.drawString(11.9*cm, 6.3*cm, '24')
        c.drawString(2.7*cm, 5.5*cm, '25')
        c.drawString(2.7*cm, 4.65*cm, '26')
        c.drawString(2.7*cm, 3.85*cm, '27')
        c.drawString(2.7*cm, 1.95*cm, '28')

        #Beschriftungen:
        c.setFont(schriftartfett, 16)
        c.drawString(12.3*cm, 26.6*cm, 'Eurostat-Meldung Beamte')
        c.setFont(schriftart, 8)
        c.drawString(2.9*cm, 26.3*cm, 'Name und Anschrift des Unternehmens')
        c.drawString(12.5*cm, 26.3*cm, u'Unternehmensnummer des Unfallversicherungsträgers')
        c.drawString(2.9*cm, 24.1*cm, u'Empfänger/-in')
        c.drawString(2.9*cm, 20*cm, 'Name, Vorname der versicherten Person')
        c.drawString(12.9*cm, 20*cm, 'Geburtsdatum')
        c.drawString(15.35*cm, 20*cm, 'Tag')
        c.drawString(16.4*cm, 20*cm, 'Monat')
        c.drawString(18.2*cm, 20*cm, 'Jahr')
        c.drawString(2.9*cm, 19.2*cm, u'Straße, Hausnummer')
        c.drawString(9.8*cm, 19.2*cm, 'Postleitzahl')
        c.drawString(12.7*cm, 19.2*cm, 'Ort')
        c.drawString(2.9*cm, 18.4*cm, u'Geschlecht')
        c.drawString(3.1*cm, 18.05*cm, u'Mänlich')
        c.drawString(5.1*cm, 18.05*cm, 'Weiblich')
        c.drawString(13.1*cm, 18.05*cm, 'Ja')
        c.drawString(15.1*cm, 18.05*cm, 'Nein')
        c.drawString(6.6*cm, 18.4*cm, u'Staatsangehörigkeit')
        c.drawString(12.9*cm, 18.4*cm, 'Leiharbeitnehmer/-in')
        c.drawString(3.1*cm, 17.6*cm, 'Auszubildende/-r')
        c.drawString(3.1*cm, 17.25*cm, 'Ja')
        c.drawString(5.1*cm, 17.25*cm, 'Nein')
        c.drawString(6.75*cm, 17.6*cm, 'Die versicherte Person ist')
        c.drawString(11.1*cm, 17.55*cm, 'Unternehmer/-in')
        c.drawString(15.2*cm, 17.6*cm, 'mit der Unternehmerin/')
        c.drawString(15.2*cm, 17.35*cm, u'dem Unternehmer:')
        c.drawString(11.1*cm, 16.95*cm, 'Gesellschafter/-in')
        c.drawString(11.1*cm, 16.65*cm, u'Geschäftsführer/-in')
        c.drawString(15.8*cm, 16.95*cm, 'verheiratet')
        c.drawString(15.8*cm, 16.55*cm, 'in eingetragener')
        c.drawString(15.8*cm, 16.21*cm, 'Lebenspartnerschaft lebend')
        c.drawString(15.8*cm, 15.85*cm, 'verwandt')
        c.drawString(3.1*cm, 15.3*cm, 'Anspruch auf Entgeltfortzahlung')
        c.drawString(2.7*cm, 14.85*cm, u'besteht für')
        c.drawString(5.5*cm, 14.85*cm, 'Wochen')
        c.drawString(8.4*cm, 15.3*cm, u'Krankenkasse (Name, PLZ, Ort)')
        c.drawString(3.1*cm, 14.3*cm, u'Tödlicher Unfall?')
        c.drawString(6.4*cm, 14.3*cm, u"Unfallzeitpunkt")
        c.drawString(13.4*cm, 14.3*cm, u"Unfallort")
        c.setFont(schriftart, 6)
        c.drawString(14.5*cm, 14.35*cm, u"(genaue Orts- und Straßenangabe mit PLZ)")
        c.setFont(schriftart, 8)
        c.drawString(3.1*cm, 13.95*cm, 'Ja')
        c.drawString(5.1*cm, 13.95*cm, 'Nein')
        c.drawString(6.2*cm, 14.05*cm, u"Tag")
        c.drawString(7.2*cm, 14.05*cm, u"Monat")
        c.drawString(9*cm, 14.05*cm, u"Jahr")
        c.drawString(10.6*cm, 14.05*cm, u"Stunde")
        c.drawString(11.8*cm, 14.05*cm, u"Minute")
        c.drawString(3.1*cm, 13.3*cm, u"Ausführliche Schilderung des Unfallhergangs")
        c.setFont(schriftart, 6)
        c.drawString(8.9*cm, 13.3*cm, u"(Verlauf, Bezeichnung des Betriebsteils, ggf. Beteiligung von Maschinen, Anlagen, Gefahrstoffen)")
        c.setFont(schriftart, 8)
        c.drawString(2.7*cm, 9.9*cm, u"Die Angaben beruhen auf der Schilderung")
        c.drawString(9.2*cm, 9.9*cm, u'der versicherten Person')
        c.drawString(12.9*cm, 9.9*cm, u'anderer Personen')
        c.drawString(3.1*cm, 9.5*cm, u'Verletzte Körperteile')
        c.drawString(11.6*cm, 9.5*cm, u'Art der Verletzung')
        c.drawString(3.1*cm, 8.8*cm, u'Wer hat von dem Unfall zuerst Kenntnis genommen?')
        c.setFont(schriftart, 6)
        c.drawString(9.8*cm, 8.8*cm, u'(Name, Anschrift)')
        c.setFont(schriftart, 8)
        c.drawString(13.9*cm, 8.8*cm, u'War diese Person Augenzeugin/Augenzeuge')
        c.drawString(13.9*cm, 8.5*cm, u'des Unfalls?')
        c.drawString(14.3*cm, 8.05*cm, 'Ja')
        c.drawString(16.42*cm, 8.05*cm, 'Nein')
        c.drawString(3.1*cm, 7.6*cm, 'Erstbehandlung')
        c.drawString(2.7*cm, 7.35*cm, 'Name und Anschrift der Ärztin/des Arztes oder des Krankenhauses')
        c.drawString(13.4*cm,7.6*cm, 'Beginn und Ende der Arbeitszeit')
        c.drawString(12.9*cm, 7.35*cm, 'der versicherten Person')
        c.drawString(12.9*cm, 6.7*cm, 'Beginn')
        c.drawString(14.15*cm, 7.05*cm, 'Stunde')
        c.drawString(15.35*cm, 7.05*cm, 'Minute')
        c.drawString(16.5*cm, 6.7*cm, 'Ende')
        c.drawString(17.55*cm, 7.05*cm, 'Stunde')
        c.drawString(18.75*cm, 7.05*cm, 'Minute')
        c.drawString(3.1*cm, 6.3*cm, u'Zum Unfallzeitpunkt beschäftigt/tätig als')
        c.drawString(12.25*cm, 6.3*cm, u'Seit wann bei dieser Tätigkeit?')
        c.drawString(16.6*cm, 6.3*cm, 'Monat')
        c.drawString(18.4*cm ,6.3*cm, 'Jahr')
        c.drawString(3.1*cm, 5.5*cm, u'In welchem Teil des Unternehmens ist die versicherte Person ständig tätig?')
        c.drawString(3.1*cm, 4.65*cm, u'Hat die versicherte Person die Arbeit eingestellt?')
        c.drawString(11.4*cm, 4.65*cm, 'Nein')
        c.drawString(13.4*cm, 4.65*cm, 'Sofort')
        c.drawString(14.65*cm, 4.65*cm, u'Später, am')
        c.drawString(16.55*cm, 4.65*cm, 'Tag')
        c.drawString(17.6*cm, 4.65*cm, 'Monat')
        c.drawString(18.75*cm, 4.65*cm, 'Stunde')
        c.drawString(3.1*cm, 3.85*cm, u'Hat die versicherte Person die Arbeit wieder aufgenommen?')
        c.drawString(11.4*cm, 3.85*cm, 'Nein')
        c.drawString(13.4*cm, 3.85*cm, u'Ja, am')
        c.drawString(15.35*cm, 3.9*cm, 'Tag')
        c.drawString(16.4*cm, 3.9*cm, 'Monat')
        c.drawString(18.4*cm, 3.9*cm, 'Jahr')
        c.drawString(3.2*cm, 1.95*cm, u'Datum')
        c.drawString(5*cm, 1.95*cm, u'Unternehmer/-in(Bevollmächtigte/-r)')
        c.drawString(11.2*cm, 1.95*cm, u'Betriebsrat(Personalrat)')
        c.drawString(15.4*cm, 1.95*cm, u'Telefon Nr. für Rückfragen')
        return c

    def kundetopdf(self, c, uaz):
        """schreibt das Mitgliedsunternehmen auf das PDF"""

        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"

        anschrift = "%s %s" %(uaz.unfustrasse, uaz.unfunr)

        c.setFont(schriftart, 9)
        c.drawString(3*cm, 25.9*cm, uaz.addr.name1) #uaz.unfuname)
        c.drawString(3*cm, 25.5*cm, uaz.addr.name2) #anschrift)
        c.drawString(3*cm, 25.1*cm, "%s %s" %(uaz.addr.strasse, uaz.addr.nr)) #uaz.unfuplz)
        c.drawString(3*cm, 24.7*cm, "%s %s" %(uaz.addr.plz, uaz.addr.ort)) #uaz.unfuort)
        c.setFont(schriftart, 12)
        #c.drawString(12.8*cm, 25.7*cm, uaz.addr.login)
        return c

    def uvtopdf(self, c, uaz):
        """schreibt den UV-Traeger auf das PDF"""

        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"

        c.setFont(schriftart, 12)
        c.drawString(3*cm, 23.3*cm, "uaz.bv.get('name1', '')")
        #c.drawString(3*cm, 22.8*cm, uaz.bv.get('name2', ''))
        c.drawString(3*cm, 22.3*cm, "uaz.bv.get('strasse', '')")
        c.drawString(3*cm, 21.8*cm, "%s %s" %('plz', 'ort'))
        return c

    def setcross(self, c, x, y):
        """setzt die Kreuze im PDF"""

        c.line(x*cm, y*cm, (x+0.3)*cm, (y+0.3)*cm)
        c.line(x*cm, (y+0.3)*cm, (x+0.3)*cm, y*cm)

        return c

    def datatopdf(self, c, uaz):

        schriftart = "Helvetica"
        # Formular beschriftung
        c.setFont(schriftart, 10)
        c.drawString(2.7*cm, 19.6*cm, uaz.prsname or '')
        c.drawString(4*cm, 19.6*cm, uaz.prsvor or '')

  
        # Formular beschriftung
        if uaz.prsgeb:
            geburtstag = uaz.prsgeb.split('.')[0]
            geburtsmonat = uaz.prsgeb.split('.')[1]
            geburtsjahr = uaz.prsgeb.split('.')[2]
            c.drawString(15.2*cm, 19.6*cm, geburtstag[0])
            c.drawString(15.8*cm, 19.6*cm, geburtstag[1])
            c.drawString(16.4*cm, 19.6*cm, geburtsmonat[0])
            c.drawString(17*cm, 19.6*cm, geburtsmonat[1])
            c.drawString(17.6*cm, 19.6*cm, geburtsjahr[0])
            c.drawString(18.1*cm, 19.6*cm, geburtsjahr[1])
            c.drawString(18.7*cm, 19.6*cm, geburtsjahr[2])
            c.drawString(19.3*cm, 19.6*cm, geburtsjahr[3])

        c.drawString(2.7*cm, 18.81*cm, uaz.ikstr or '')
        c.drawString(6.1*cm, 18.81*cm, uaz.iknr or '')
        if uaz.ikzplz:
            c.drawString(9.89*cm, 18.81*cm, uaz.ikzplz[0])
            c.drawString(10.4*cm, 18.81*cm, uaz.ikzplz[1])
            c.drawString(11*cm, 18.81*cm, uaz.ikzplz[2])
            c.drawString(11.6*cm, 18.81*cm, uaz.ikzplz[3])
            c.drawString(12.1*cm, 18.81*cm, uaz.ikzplz[4])
        c.drawString(12.8*cm, 18.81*cm, uaz.ikzort or '')

        staat = uaz.prssta or "999"
        vocab = getUtility(IVocabularyFactory, name='uvc.sta')(None)
        try:
            term  = vocab.getTerm(staat)
            staat = translate(term.title, 'uvc.unfallanzeige', target_language="de")
        except LookupError, e:
            print e

        c.drawString(6.6*cm, 18.05*cm, staat)
        if uaz.unfefz:
            c.drawString(4.45*cm, 14.8*cm, uaz.unfefz[0])
            c.drawString(5*cm, 14.8*cm, uaz.unfefz[1])

        c.drawString(8.3*cm, 14.85*cm, uaz.unfkka or '')

        if uaz.unfdatum:
            unfalltag = uaz.unfdatum.split('.')[0]
            unfallmonat = uaz.unfdatum.split('.')[1]
            unfalljahr = uaz.unfdatum.split('.')[2]
            unfallstunde = uaz.unfzeit.split(':')[0]
            unfallminute = uaz.unfzeit.split(':')[1]
            c.drawString(6.1*cm, 13.7*cm, unfalltag[0])
            c.drawString(6.6*cm, 13.7*cm, unfalltag[1])
            c.drawString(7.2*cm, 13.7*cm, unfallmonat[0])
            c.drawString(7.7*cm, 13.7*cm, unfallmonat[1])
            c.drawString(8.3*cm, 13.7*cm, unfalljahr[0])
            c.drawString(8.9*cm, 13.7*cm, unfalljahr[1])
            c.drawString(9.5*cm, 13.7*cm, unfalljahr[2])
            c.drawString(10*cm, 13.7*cm, unfalljahr[3])
            c.drawString(10.7*cm, 13.7*cm, unfallstunde[0])
            c.drawString(11.2*cm, 13.7*cm, unfallstunde[1])
            c.drawString(11.85*cm, 13.7*cm, unfallminute[0])
            c.drawString(12.4*cm, 13.7*cm, unfallminute[1])

        c.drawString(13.2*cm, 13.8*cm, uaz.unfort or '')

        c.drawString(2.7*cm, 9.15*cm, uaz.diavkt or '')
        c.drawString(11.5*cm, 9.15*cm, uaz.diaadv or '')
        c.drawString(2.7*cm, 8.2*cm, uaz.unfkn1 or '')
        c.drawString(2.7*cm, 6.7*cm, uaz.unfeba1 or '')
        if uaz.uadbavon:
            c.drawString(14.2*cm, 6.7*cm, uaz.uadbavon[0])
            c.drawString(14.8*cm, 6.7*cm, uaz.uadbavon[1])
            c.drawString(15.4*cm, 6.7*cm, uaz.uadbavon[3])
            c.drawString(16*cm, 6.7*cm, uaz.uadbavon[4])
        if uaz.uadbabis:
            c.drawString(17.6*cm, 6.7*cm, uaz.uadbabis[0])
            c.drawString(18.2*cm, 6.7*cm, uaz.uadbabis[1])
            c.drawString(18.8*cm, 6.7*cm, uaz.uadbabis[3])
            c.drawString(19.4*cm, 6.7*cm, uaz.uadbabis[4])

        c.drawString(2.7*cm, 5.9*cm, uaz.uadbru1 or '')
        if uaz.uadst:
            c.drawString(16.6*cm, 5.9*cm, uaz.uadst[0])
            c.drawString(17.2*cm, 5.9*cm, uaz.uadst[1])
            c.drawString(17.8*cm, 5.9*cm, uaz.uadst[3])
            c.drawString(18.35*cm, 5.9*cm, uaz.uadst[4])
            c.drawString(18.9*cm, 5.9*cm, uaz.uadst[5])
            c.drawString(19.45*cm, 5.9*cm, uaz.uadst[6])

        c.drawString(2.7*cm, 5.1*cm, uaz.unfute or '')
        c.drawString(3*cm, 2.4*cm, uaz.modtime.strftime('%d.%m.%Y'))
        c.drawString(5*cm, 2.4*cm, uaz.unfus2 or '')
        c.drawString(11.2*cm, 2.4*cm, uaz.unfus3 or '')
        c.drawString(15.4*cm, 2.8*cm, uaz.anspname or '')
        c.drawString(15.4*cm, 2.4*cm, uaz.anspfon or '')


        if uaz.prssex == 'maennlich':
            self.setcross(c,x=2.7,y=18)
        else:
            self.setcross(c,x=4.7,y=18)

        #if uaz.unflar == 'ja':
        #    self.setcross(c,x=12.7,y=18)
        #else:
        #   self.setcross(c,x=14.7,y=18)

        #if uaz.uadbru1 == 'Azubi':
        #    self.setcross(c,x=2.7,y=17.2)
        #else:
        #    self.setcross(c,x=4.7,y=17.2)

        if uaz.unfbu == 'Unternehmer':
            self.setcross(c,x=10.5,y=17.5)
        elif uaz.unfbu == 'Gesellschafter/Geschaeftsfuehrer':
            self.setcross(c,x=10.5,y=16.9)
        elif uaz.unfbu == 'Ehegatte des Unternehmers':
            self.setcross(c,x=14.7,y=17.5)
            self.setcross(c,x=15.4,y=16.9)
        elif uaz.unfbu == 'Mit dem Unternehmer verwandt':
            self.setcross(c,x=14.7,y=17.5)
            self.setcross(c,x=15.4,y=15.8)

        if uaz.prstkz == 'nein':
            self.setcross(c,x=4.7,y=13.85)
        else:
            self.setcross(c,x=2.7,y=13.85)

        #if uaz.unfhg2 == u'des Versicherten':
        #    self.setcross(c,x=8.8,y=9.9)
        #else:
        #    self.setcross(c,x=12.4,y=9.9)

        if uaz.unfkn2 == 'ja':
            self.setcross(c,x=13.9,y=8)
        elif uaz.unfkn2 == 'nein':
            self.setcross(c,x=16,y=8)

        if uaz.unfae1 == 'nein':
            self.setcross(c,x=11,y=4.6)
        elif uaz.unfae1 == 'ja, sofort':
            self.setcross(c,x=13,y=4.6)
        
        if uaz.unfaedatum:
            c.drawString(16.4*cm, 4.3*cm, uaz.unfaedatum[0])
            c.drawString(17.05*cm, 4.3*cm, uaz.unfaedatum[1])
            c.drawString(17.6*cm, 4.3*cm, uaz.unfaedatum[3])
            c.drawString(18.2*cm, 4.3*cm, uaz.unfaedatum[4])
            #c.drawString(18.8*cm, 4.3*cm, uaz.unfaezeit[0:1])
            #c.drawString(19.4*cm, 4.3*cm, uaz.unfaezeit[1:2])

        if uaz.unfwa1 == 'nein':
            self.setcross(c,x=11,y=3.8)
        if uaz.unfwa1 == 'ja':
            self.setcross(c,x=13,y=3.8)

        if uaz.unfwax:
            c.drawString(15.2*cm, 3.5*cm, uaz.unfwax[0])
            c.drawString(15.8*cm, 3.5*cm, uaz.unfwax[1])
            c.drawString(16.4*cm, 3.5*cm, uaz.unfwax[3])
            c.drawString(17*cm, 3.5*cm, uaz.unfwax[4])
            c.drawString(17.6*cm, 3.5*cm, uaz.unfwax[6])
            c.drawString(18.2*cm, 3.5*cm, uaz.unfwax[7])
            c.drawString(18.8*cm, 3.5*cm, uaz.unfwax[8])
            c.drawString(19.4*cm, 3.5*cm, uaz.unfwax[9])
        return c

    def texttozeilen(self, text):
        zeichen = 120
        textneu= text.split(' ')
        zeilen =[]
        zeile = ''
        for i in textneu:
            test = zeile + i
            if len(test) > zeichen:
                zeilen.append(zeile)
                zeile = ''
            elif len(test) == zeichen:
                zeile = zeile + ' ' + i
                zeilen.append(zeile)
                zeile = ''
            else:
                zeile = zeile + ' ' + i
        zeilen.append(zeile)
        return zeilen

    def hergangtopdf(self, c, zeilen):
        schriftart = "Helvetica"
        x=2.6
        y=12.9
        diff=0.3
        c.setFont(schriftart, 8)
        zz = len(zeilen)
        if zz > 9:
            zz = 9
        for i in range(zz):
            c.drawString(x*cm ,y*cm, zeilen[i])
            y=y-diff
        return c

    def createfolgeseite(self, c, folgeseite):
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        c.setFont(schriftartfett, 12)
        c.drawString(2.6*cm, 26.6*cm, u"Beschreibung des Unfallhergangs (Fortsetzung)")
        x=2.6
        y=25
        diff=0.3
        c.setFont(schriftart, 8)
        for i in folgeseite:
            c.drawString(x*cm, y*cm, i)
            y=y-diff
        return c

    def genpdf(self):
        c = self.c
        c = self.drawpdf(c)
        uaz = self.uaz
        c = self.kundetopdf(c, uaz)
        c = self.uvtopdf(c, uaz)
        c = self.datatopdf(c, uaz)
        zeilen = self.texttozeilen(uaz.unfhg1 or '')
        c = self.hergangtopdf(c, zeilen)
        folgeseite = []
        if len(zeilen) > 9:
            folgeseite = zeilen[9:]
        c.showPage()
        if folgeseite:
            self.createfolgeseite(c, folgeseite)
            c.showPage()
        return 

    def irender(self):
        pdf = self.genpdf()
        a = open(pdf._filename, 'rb').read()
        RESPONSE = self.request.response
        RESPONSE.setHeader('content-type', 'application/pdf')
        RESPONSE.setHeader('content-disposition', 'attachment; filename=unfallanzeige.pdf')
        return a
