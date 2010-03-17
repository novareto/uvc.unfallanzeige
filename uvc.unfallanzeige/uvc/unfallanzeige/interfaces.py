# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


from zope.schema import TextLine, Bool, Date, Choice, Text, Int
from zope.interface import Invalid, invariant

from uvcsite import IProductFolder, IContent


class IUnfallanzeigeFolder(IProductFolder):
    """Markerinterface"""


class IUnfallanzeige(IContent):

    unfustdor = Choice(
        title = u"Company of the Employee",
        description = u"Who does the Employee work",
        values = ('here', 'not here'),
        )

    unfustrasse = TextLine(
        title = u"Street",
        description = u"Street"
        )

    unfunr = Int(
        title = u"Number",
        description = u"Number"
        )

    unfuplz = TextLine(
        title = u"ZipCode",
        description = u"Zipcode"
        )

    unfuort = TextLine(
        title = u"Place",
        description = u"Place"
        )

    anspname = TextLine(
        title = u"Name",
        description = u"Name of a responsible Person",
        )

    anspfon = TextLine(
        title = u"Phone",
        description = u"Phone of a responsible Person",
        )


# Page Two

    uadbru = TextLine(
        title = u"Kind of work",
        description = u"What kind of work does the employee",
        )

    uadst = TextLine(
        title = u"since",
        description = u"Since when does he work on this job mm.YYYY",
        )

    unfute = TextLine(
        title = u"function",
        description = u"which function has the employee in the company",
        )

    unflar = Choice(
        title = u"parttimeworker",
        description = u"Is the employee a part time worker",
        values = ('yes', 'no'),
        )

    unvlaraddr = Text(
        title = u"Address",
        description = u"Address of the Part Time Company",
        )


