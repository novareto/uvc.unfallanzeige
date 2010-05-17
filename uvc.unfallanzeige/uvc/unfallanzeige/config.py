# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import zope.interface

import uvc.unfallanzeige
import megrok.z3cform.wizard
from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder
from uvc.unfallanzeige.uazwizard import Unfallanzeige



class UAZMenuWizard(uvcsite.Entry):
    grok.context(zope.interface.Interface)
    grok.title('Unfallanzeige Wizard')
    uvcsite.menu(uvcsite.GlobalMenu)
    grok.order(30)

    @property
    def url(self):
        adapter = uvcsite.IGetHomeFolderUrl(self.request)
        return adapter.getURL() + 'unfallanzeigen/startwizard'


class StartWizard(grok.View):
    grok.implements(megrok.z3cform.wizard.IWizard)
    grok.context(IUnfallanzeigenFolder)

    def update(self):
        self.uaz = uaz = Unfallanzeige()
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'unfallanzeigewizard'))


