# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import grok
import uvcsite

from zope.lifecycleevent import ObjectCreatedEvent
from uvc.unfallanzeige.resources import uazjs, uazcss
from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder, IUnfallanzeige


class Unfallanzeige(uvcsite.Content):
    """ContentType fuer das Lastschriftverfahren"""
    uvcsite.schema(IUnfallanzeige)
    grok.name('Unfallanzeige')
    grok.title('Unfallanzeige')

    title = u"Unfallanzeige"


class Unfallanzeigen(uvcsite.ProductFolder):
    """Container fuer die Speicherung der Lastschriftdokumente"""
    grok.implements(IUnfallanzeigenFolder)
    uvcsite.contenttype(Unfallanzeige)
    grok.title(u'Elektronische Unfallanzeigen')
    title = u"Unfallanzeigen"
    description = u"In diesem Ordner werden alle Elektronischen Unfallanzeigen gespeichert"


class Adder(grok.View):
    grok.context(IUnfallanzeigenFolder)
    grok.name('add')

    def update(self):
        self.uaz = uaz = Unfallanzeige()
        grok.notify(ObjectCreatedEvent(uaz))
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'edit'))


class UnfallanzeigeWizard(uvcsite.Wizard):
    """ Wizard form."""
    #grok.implements(IUnfallanzeige)
    grok.context(Unfallanzeige)
    grok.name('edit')
    grok.require('uvc.EditContent')

    label = u'Unfallanzeige'

    def update(self):
        super(UnfallanzeigeWizard, self).update()
        uazcss.need()
        uazjs.need()
