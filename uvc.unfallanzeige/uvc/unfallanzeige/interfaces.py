# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de

from zope.interface import Interface
from uvcsite import IProductFolder, IContent
from zope.schema import TextLine, Choice, Text, Int
from z3c.wizard.interfaces import IWizard
from uvc.widgets.fields import OptionalChoice


class IUnfallanzeigenFolder(IProductFolder):
    """Markerinterface"""


class IUnfallanzeigeWizard(IWizard):
    """Markerinterface"""

class IPresentation(Interface):
    """ Marker Interface """

class IUnfallanzeige(IContent):

    unfustdor = Choice(
        title = u"Arbeitsstelle",
        description = u"Die Versicherte Person ist regelmäßig tätig",
        values = (u'In dem vorher genannten Unternehmen', 'In einer Zweigniederlassung'),
        )

    unfuname = TextLine(
        title = u"Name",
        description = u"Name der Zweigstelle",
        required = False,
        )

    unfustrasse = TextLine(
        title = u"Strasse",
        description = u"Strasse",
        required = False,
        )

    unfunr = Int(
        title = u"Nr.",
        description = u"Hausnummer",
        required = False,
        )

    unfuplz = TextLine(
        title = u"Postleitzahl",
        description = u"Postleitzahl",
        required = False,
        )

    unfuort = TextLine(
        title = u"Ort",
        description = u"Ort",
        required = False,
        )

    anspname = TextLine(
        title = u"Ansprechpartner",
        description = u"Ansprechpartner",
        )

    anspfon = TextLine(
        title = u"Telefon",
        description = u"Telefon",
        )


# Page Two

    uadbru1 = OptionalChoice(
        title = u"Position",
        description = (u"Die versicherte Person ist zum "
                       u"Unfallzeitpunkt beschäftigt als"),
        alternative=True,
        values = ('Drucker', 'Bildhauer'),
        )

    uadst = TextLine(
        title = u"Im Unternehmen seit:",
        description = u"und in dieser Tätigkeit seit: Datum (mm.jjjj)",
        )

    unfute = OptionalChoice(
        title = u"Tätig als",
        description = u"In welchem Teil des Unternehmens ist der Versicherte ständig tätig?",
        alternative=True,
        values = ('Verwaltung', 'Druckerei', 'Schreinerei')
        )

    unflar = Choice(
        title = u"Leiharbeitsfirma",
        description = u"Ist die versicherte Person Leiharbeitnehmer?",
        values = ('ja', 'nein'),
        )

    unvlaraddr = Text(
        title = u"Address",
        description = u"Address of the Part Time Company",
        required = False,
        )

# Step 3

    prsname = TextLine(
        title = u"Name",
        description = u"Name des Versicherten",
        )

    prsvor = TextLine(
        title = u"Vorname",
        description = u"Vorname des Versicherten",
        )

    ikstr = TextLine(
        title = u"Anschrift des Versicherten",
        description = u"Strasse",
        )

    iknr = TextLine(
        title = u"",
        description = u"Nr",
        )

    lkz = Choice(
        title = u"Länderkennzeichen",
        description = u"Länderkennzeichen",
        values = (u'Deutschland', u'Polen'),
        )

    ikzplz = TextLine(
        title = u"Postleitzahl",
        description = u"Postleitzahl",
        )

    ikzort = TextLine(
        title = u"Ort",
        description = u"Ort",
        )

    prsgeb = TextLine(
        title = u"Geburtsdatum des Versicherten",
        description = u"Geburtsdatum (tt.mm.jjjj)",
        )

    prssex = Choice(
        title = u"Geschlecht",
        description = u"Geschlecht",
        values = [u'maennlich', 'weiblich']
        )

    prssta = Choice(
        title = u"Staatsangehörigkeit",
        description = u"Staatsangehörigkeit",
        values = ['Albanien', 'Belgien', 'Deutschland', 'Schweiz']
        )

    unfbu = Choice(
        title = u"Angaben zum Arbeitsverhältnis",
        description = u"Angaben zum Arbeitsverhältnis",
        values = (u'Arbeitnehmer', u'Ehegatte des Unternehmers', u'...')
        )

    vehearbeitsv = Choice(
        title = u"Ehegattenarbeitsvertrag",
        description = u"Ehegattenarbeitsvertrag",
        values = (u'Ja', u'Nein'),
        required = False,
        )

    vehebis = TextLine(
        title = u"Ehegattenarbeitsvertrag (Vertragsbeginn)",
        description = u"Seit wann (tt.mm.jjjj)",
        required = False,
        )

    veheentgeltbis = TextLine(
        title = u"Entgelt gezahlt bis",
        description = u"Entgelt wurde bezahlt bis (tt.mm.jjjj)",
        required = False,
        )

    unfefz = TextLine(
        title = u"Entgeltfortzahlung bis",
        description = u"Für wie viele Wochen besteht Anspuch auf Entgeltfortzahlung?",
        required = False,
        )

    unfkka = TextLine(
        title = u"Anschrift der Krankenkasse",
        description = u"Anschrift der Krankenkasse",
        )

#Step4

    unfdatum = TextLine(
        title = u"Unfallzeitpunkt",
        description = u"Datum",
        )

    unfzeit = TextLine(
        title = u"Unfallzeitpunkt",
        description = u"Zeit",
        )

    unfort_detail = Choice(
        title = u"Unfallort",
        description = u"Bitte geben Sie an wo sich der Unfall ereignete:",
        values = ('Im Betriebsgelaende', 'Arbeitsweg'),
        )

    unfort = TextLine(
        title = u"Unfallort",
        description = u"Unfallort (genaue Orts- und Strassenangabe mit Postleitzahl)",
        )

    unfhg1= Text(
        title = u"Unfallhergang",
        description = u"Bitte schildern sie ausführlich wie sich der Unfall ereignete",
        )

    unfhg2= Choice(
        title = u"Zeugen",
        description = u"Die Angaben beruhen auf den Schilderungen:",
        values = ('Des Verunfallten', 'eines Zeugen'),
        )

    unfkn1 = TextLine(
        title = u"Erstkontakt",
        description = u"Wer hat von dem Unfall zuerst Kenntnis genommen (Name und Anschrift des Zeugen)",
        required = False,
        )

    unfkn2 = Choice(
        title = u"Augenzeuge",
        description = u"War diese Person Augenzeuge",
        values = ('ja', 'nein'),
        )

# Step 5     

    prstkz = Choice(
        title = u"Tödlicher Unfall",
        description = u"Handelt es sich um einen toedlichen Unfall?",
        values = ('ja', 'nein'),
         )

    unfae1 = Choice(
        title = u"Fortsetzung der Arbeit",
        description = u"Hat der Versicherte die Arbeit eingestellt?",
        values = ('nein', 'ja, sofort', 'ja, spaeter am'),
        required = False,
        )

    unfaedatum = TextLine(
        title = u"wann",
        description = u"Bitte Datum (tt.mm.jjjj)",
        required = False,
        )

    unfaezeit = TextLine(
        title = u"",
        description = u"und Uhrzeit (hh:mm)",
        required = False,
        )
     
    unfwa1 = Choice(
        title = u"Wieder Aufgenommen",
        description = u"Hat der Versicherte die Arbeit wieder aufgenommen?",
        values = ('ja', 'nein'),
        required = False,
        )

    unfwax = TextLine(
        title = u"Wieder aufegnommen",
        description = u"Wenn ja: aufgenommen am Datum (tt.mm.jjjj)",
        required = False,
        )

    uadbavon = TextLine(
        title = u"Arbeitszeit Beginn",
        description = u"Die Arbeitszeit beginnt um Uhrzeit (hh:mm)",
        )

    uadbabis = TextLine(
        title = u"Ende",
        description = u"und endet um Uhrzeit (hh:mm)",
        )
     
    diavkt = TextLine(
        title = u"Verletzte Körperteile",
        description = u"Welche Körperteile sind verletzt?",
        )

    diaadv = TextLine(
        title = u"Art der Verletzung",
        description = u"Welche Art der Verletzung liegt vor",
        )

    unfeba = Choice(
        title = u"Name des erstbehandelnden Arztes",
        description = u"Wie lauten Name und Anschrift des erstbehandelnden Arztes / Krankenhauses?",
        values = ("Es ist keine Aerztliche Behandlung erforderlich", "Name und Anschrift"),
        )

    unfeba1 = TextLine(
        title = u"Erstbehandelnder Artz (Name und Anschrift)",
        description = u"Name und Anschrift",
        required = False,
        )

#Step 6

    unfus3 = TextLine(
        title = u"Personal- bzw. Betriebsrat",
        description = u"Die folgende Person des Personal- bzw Betriebsrates wurde informiert"
                      u"(bitte Name und Vorname eintragen)",
        )

    unfus2 = TextLine(
        title = u"Unternehmer / Bevollmaechtigter",
        description = u"Name, Vorname des Unternehmens / des Bevollmaechtigten",
        )

#Step 7

    behandlung = Choice(
        title = u"Weiteres Vorgehen",
        description = u"Wie möchten Sie weiter vorgehen.",
        values = ('Druck', 'Versand', 'Druck & Versand')
        )

     

     
     
     
     
