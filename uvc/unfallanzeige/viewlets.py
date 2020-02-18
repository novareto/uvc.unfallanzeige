# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de

import grok
import uvcsite
from .uazwizard import UnfallanzeigeWizard 
from zope.interface import Interface


grok.templatedir('templates')


class UAZStepsProgressBar(grok.Viewlet):
    grok.context(Interface)
    grok.view(UnfallanzeigeWizard)
    grok.viewletmanager(uvcsite.browser.layout.slots.interfaces.IAboveContent)
    grok.order(10000)

    def update(self):
        self.progress = (
            (float(self.view.step + 1) / float(self.view.getMaximumStepId() + 1)) * 100)
