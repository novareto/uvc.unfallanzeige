
# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import grok
import PyPDF2
import uvcsite

from os import path
from datetime import datetime
from zope.i18n import translate
from reportlab.lib.units import mm
from zope.component import getUtility

#from kuvb.skin.layout import IGuvLayer
#from kuvb.auth.interfaces import IStammdaten
from zope.schema.interfaces import IVocabularyFactory
from zope.dublincore.interfaces import IZopeDublinCore
from uvc.unfallanzeige.interfaces import IUnfallanzeige

from reportlab.platypus import Paragraph 
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

styles = getSampleStyleSheet()
styleN = styles['Normal']


class Presentation(uvcsite.WatermarkPDF):
    grok.title("Unfallanzeige Download")
    grok.context(IUnfallanzeige)
    grok.name('pdf_neu')
#    grok.layer(IGuvLayer)

    def watermark(self):
        pdf = "%s/U1000_siguv.pdf" % path.dirname(__file__)
        wm = PyPDF2.PdfFileReader(pdf)
        orig = PyPDF2.PdfFileReader(self.base_file)
        wm_p1 = wm.getPage(0)
        output = PyPDF2.PdfFileWriter()
        wm_p1.mergePage(orig.getPage(0))
        output.addPage(wm_p1)
        if orig.numPages == 2:
            output.addPage(orig.getPage(1))
        output.write(self.base_file)

    @property
    def filename(self):
        return "Unfallanzeige.pdf"

    def P(self, x, y, s):
        self.c.drawString(x*mm, y*mm, unicode(s))

    def genpdf(self):
        c = self.c
        context = self.context
        metadata = IZopeDublinCore(context)
        mitglied = ''.join(metadata.creators)
        mitglied = mitglied[:9]
        stammdaten = None
        #stammdaten = IStammdaten(self.request.principal)
        #addr = stammdaten.getAdresse()
        c.setAuthor("Gesetzliche Unfallversicherung")
        c.setTitle("Unfallanzeige")
        schriftart = "Helvetica"
        schriftartfett = "Helvetica-Bold"
        # ADR UAZTRAEGER
        c.setFont(schriftartfett, 8)
        #bv = stammdaten.getHauptAdresse()
        self.P(28, 237, u"Unfallversicherungsträger")
        self.P(28, 234, u"UV-Träger Name2")
        self.P(28, 231, u"UV-Träger Name3" )
        self.P(28, 228, "Strasse Hausnummer")
        self.P(28, 224, u"PLZ Ort")


        # 1 Name und Anschrift
        self.P(28, 261, "Novareto")
        self.P(28, 258, "GmbH")
        self.P(28, 255, u"Geschäftsprozess im Netz ")
        self.P(28, 252, u"Karolinenstr. 17")
        self.P(28, 249, u"90763 Fürth")

        # 2 Mitgliedsnummer
        self.P(130, 260, "10014877")

        # 4 Name des Versicherten
        c.setFont(schriftart, 10)
        self.P(28, 197, "%s %s" % (
            context.prsname or '', context.prsvor or ''))

        # 5 Geburtsdatum
        self.P(140.1, 197, context.prsgeb)

        # 6 Adresse
        self.P(28, 189, "%s, %s" % (context.ikstr or '', context.iknr or ''))
        self.P(111, 189, context.ikzplz)
        self.P(140, 189, context.ikzort)

        # 7 Geschlecht
        sex = context.prssex or ''
        if sex == "maennlich":
            self.P(25, 180, 'X')
        elif sex == "weiblich":
            self.P(44, 180, 'X')
        elif sex == "divers":
            self.P(64, 180, 'X')
        elif sex == "keine Angabe":
            self.P(78.8, 180, 'X')

        # 8 Staatsangehörigkeit
        staat = context.prssta
        vocab = getUtility(IVocabularyFactory, name='uvc.sta')(None)
        try:
            term = vocab.getTerm(staat)
            staat = translate(
                term.title,
                'uvc.unfallanzeige',
                target_language="de")
        except StandardError:
            pass
        self.P(111, 180, staat)

        # 9 Leiharbeitnehmer
        if context.unflar == "ja":
            self.P(139.6, 180, 'X')
        elif context.unflar == "nein":
            self.P(159.6, 180, 'X')

        # 10 Auszubildender
        azubi = context.uadbru1
        if azubi == 'Auszubildender':
            self.P(46, 172.5, 'X')
        else:
            self.P(25, 172.5, 'X')

        # 11 Ist der Versicherte

        ist = context.unfbu
        if ist == "Unternehmer":
            self.P(105.5, 176, 'X')
        elif ist == "Gesellschafter/Geschaeftsfuehrer":
            self.P(105.5, 172, 'X')
        elif ist == "Ehegatte des Unternehmers":
            self.P(146.5, 176, 'X')
            self.P(154, 169, 'X')
            self.P(149, 177, 'X')
        elif ist == "in eingetragener Lebenspartnerschaft lebend":
            self.P(146.5, 176, 'X')
            self.P(150.5, 172, 'X')
        elif ist == "Mit dem Unternehmer verwandt":
            self.P(146.5, 176, 'X')
            self.P(150.5, 165, 'X')

        # 12 Anspruch auf Entgeltfortzahlung
        entgelt = str(context.unfefz) or ''
        if entgelt:
            self.P(43, 156.6, entgelt)

        # 13 Krankenkasse
        self.P(82, 156, context.unfkka or '')

        # 14 Tödlicher Unfall
        if context.prstkz == 'ja':
            self.P(44.7, 147, 'X')
        elif context.prstkz == 'nein':
            self.P(25, 147, 'X')

        # 15 Unfzeit Unfdatum
        unfzeit = context.unfzeit or '         '
        unfdatum = context.unfdatum or '      '

        self.P(63, 147, "%s / %s" %(unfdatum, unfzeit))
        
        # Tel Versicherter
        self.P(140, 147, getattr(context, 'prstel', ''))

        # 16 Unfallort
        self.P(25, 139, context.unfort or '')

        if context.unfort_detail == "Homeoffice":
            self.P(179.8, 138, 'X')
        else:
            self.P(159.6, 138, 'X')

        # 17 Unfallhergang
        P = Paragraph((context.unfhg1), styleN)
        w, h = P.wrap(480, 280)
        P.drawOn(self.c, 75, 310)
        if context.unfhg2 == 'des Versicherten':
            self.P(91.8, 103, 'X')
        elif context.unfhg2 == 'eine andere Person':
            self.P(135.8, 103, 'X')

        ge = getattr(context, 'unfge', 'nein')
        if ge == "ja":
            self.P(162.3, 99, 'X')
        else:
            self.P(135.8, 99, 'X')

        # 18 V Körperteile
        self.P(25, 91, context.diavkt or '')

        # 19 Dianose
        self.P(115, 91, context.diaadv or '')

        # 20 Kenntnis des Unfallas
        self.P(25, 82, context.unfkn1 or '')
        if context.unfkn2 == 'ja':
            self.P(144.9, 82, 'X')
        elif context.unfkn2 == 'nein':
            self.P(124.9, 82, 'X')

        # 21 Erstbehandelnder Arzt
        print(context.unfeba)
        if context.unfeba == 'Es ist keine aerztliche Behandlung erforderlich.': 
            self.P(25, 71, u'keine ärztliche Behandlung erforderlich')
        else:
            c.setFont(schriftart, 8)
            self.P(25, 71, context.unfeba1.replace('\r\n', ' ').replace('\n', ' '))
            c.setFont(schriftart, 10)

        # 22 Arbeitszeit
        beginn = context.uadbavon or '     '
        ende = context.uadbabis or '     '
        self.P(136, 70.5, beginn)

        self.P(177, 70.5, ende)

        # 23 Unfallzeitpunkt beschäftigt als
        beruf = context.uadbru1
        self.P(25, 62, beruf)

        # 24 Seit wann in dieser Tätigkeit

        wann = context.uadst or '       '
        self.P(128, 62, wann)

        # 25 WAS
        self.P(25, 54, context.unfute)

        # 26 Arbeit eingestellt
        einstell = context.unfae1
        if einstell == 'nein':
            self.P(81, 46, 'X')
        elif einstell == 'ja, sofort':
            self.P(97, 46, 'X')
        elif einstell == 'ja, spaeter am:':
            self.P(115, 46, 'X')
            datum = context.unfaedatum or '        '
            zeit = context.unfaezeit or '     '
            self.P(135, 46, datum)
            self.P(174.5, 46, zeit)

        # 27 Arbeit wieder aufgenommen
        aufnahme = context.unfwa1


        if aufnahme == "nein":
            self.P(81, 38, 'X')
        elif aufnahme == "ja":
            self.P(97, 38, 'X')
            wax = context.unfwax or '          '
            self.P(115, 39, wax)

        # Ansprechpartner
        c.setFont(schriftart, 9)
        self.P(25, 27, context.modtime.strftime('%d.%m.%Y'))
        self.P(49, 27, context.unfus2)
        self.P(111, 27, context.unfus3)
        self.P(155, 27, "%s %s" % (
            context.anspname or '', context.anspfon or ''))
        self.P(67, 27, u"versandt via Extranet")
        self.c.showPage()
