# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


from uvcsite import IProductFolder, IContent
from zope.interface import Invalid, invariant
from zope.schema import TextLine, Bool, Date, Choice, Text, Int
from z3c.wizard.interfaces import IWizard
from uvc.widgets.fields import OptionalChoice


class IUnfallanzeigenFolder(IProductFolder):
    """Markerinterface"""


class IUnfallanzeigeWizard(IWizard):
    """Markerinterface"""


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
        alternative=True,
        description = (u"Die versicherte Person ist zum "
                       u"Unfallzeitpunkt beschäftigt als"),
        values = ('Drucker', 'Bildhauer'),
        )

    uadst = TextLine(
        title = u"Im Unternehmen seit:",
        description = u"und in dieser Tätigkeit seit: Datum (mm.jjjj)",
        )

    unfute = TextLine(
        title = u"Tätig als",
        description = u"In welchem Teil des Unternehmens ist der Versicherte ständig tätig?",
        )

    unflar = Choice(
        title = u"Leiharbeitsfirma",
        description = u"Ist die versicherte Person Leiharbeitnehmer?",
        values = ('ja', 'nein'),
        )

    unvlaraddr = Text(
        title = u"Address",
        description = u"Address of the Part Time Company",
        )


    prsname = TextLine(
        title = u"Name",
        description = u"Name des Versicherten",
        )

    prsvor = TextLine(
        title = u"Vorname",
        description = u"Vorname des Versicherten",
        )

    ikstrnr = TextLine(
        title = u"Anschrift des Versicherten",
        description = u"Strasse, Hausnummer",
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

    prssta = TextLine(
        title = u"Staatsangehörigkeit",
        description = u"Staatsangehörigkeit",
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
        )

    vehebis = TextLine(
        title = u"Ehegattenarbeitsvertrag (Vertragsbeginn)",
        description = u"Ehegattenarbeitsvertrag (Vertragsbeginn)",
        )

    veheentgeltbis = TextLine(
        title = u"Entgelt gezahlt bis",
        description = u"Entgelt bezahlt bis",
        )

    unfefz = TextLine(
        title = u"Entgeltfortzahlung bis",
        description = u"Entgeltfortzahlung bis",
        )

    unfkka = TextLine(
        title = u"Anschrift der Krankenkasse",
        description = u"Anschrift der Krankenkasse",
        )

     
     

     

     

 
