# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite

from uvc.unfallanzeige.resources import uazjs, uazcss
from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder, IUnfallanzeige, IUnfallanzeigeWizard


class Unfallanzeige(uvcsite.Content):
    """ContentType fuer das Lastschriftverfahren"""
    uvcsite.schema(IUnfallanzeige)
    grok.name('unfallanzeige')


class Unfallanzeigen(uvcsite.ProductFolder):
    """Container fuer die Speicherung der Lastschriftdokumente"""
    grok.implements(IUnfallanzeigenFolder)
    uvcsite.contenttype(Unfallanzeige)


class UnfallanzeigeWizard(uvcsite.Wizard):
    """ Wizard form."""
    grok.implements(IUnfallanzeige)
    grok.context(Unfallanzeige)

    label = u'Unfallanzeige'

    def update(self):
        super(UnfallanzeigeWizard, self).update()
        uazjs.need()
        uazcss.need()
