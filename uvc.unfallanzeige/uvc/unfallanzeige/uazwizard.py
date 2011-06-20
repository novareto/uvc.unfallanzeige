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
    grok.name('Unfallanzeige')
    grok.title('Unfallanzeige')

    title = u"Unfallanzeige"


class Unfallanzeigen(uvcsite.ProductFolder):
    """Container fuer die Speicherung der Lastschriftdokumente"""
    grok.implements(IUnfallanzeigenFolder)
    uvcsite.contenttype(Unfallanzeige)


class Adder(grok.View):
    grok.context(IUnfallanzeigenFolder)
    grok.name('add')
    
    def update(self):
        self.uaz = uaz = Unfallanzeige()
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'edit'))



class UnfallanzeigeWizard(uvcsite.Wizard):
    """ Wizard form."""
    grok.implements(IUnfallanzeige)
    grok.context(Unfallanzeige)
    grok.name('edit')


    label = u'Unfallanzeige'

    def update(self):
        super(UnfallanzeigeWizard, self).update()
        uazjs.need()
        uazcss.need()
