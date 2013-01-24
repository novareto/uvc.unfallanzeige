# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import grok
import zope.interface

from uvc.unfallanzeige.uazwizard import Unfallanzeige

from zope.app.homefolder.interfaces import IHomeFolder


class StartWizard(grok.View):
    grok.context(zope.interface.Interface)
    grok.title(u"Unfallanzeige")
    grok.baseclass()

    def update(self):
        """ Wir müssen zunächst eine Instanz der Unfallanzeige
            anlegen. Diese Instanz dient als Context für den
            Wizard.
        """
        hf = IHomeFolder(self.request.principal).homeFolder
        self.uaz = uaz = Unfallanzeige()
        hf['Unfallanzeigen'].add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'edit'))
