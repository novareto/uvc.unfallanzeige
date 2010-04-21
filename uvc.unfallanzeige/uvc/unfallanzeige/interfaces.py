# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


from uvcsite import IProductFolder, IContent
from zope.interface import Invalid, invariant
from zope.schema import TextLine, Bool, Date, Choice, Text, Int
from fields import OptionalChoice


class IUnfallanzeigeFolder(IProductFolder):
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

    uadbru = OptionalChoice(
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


