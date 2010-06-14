# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import z3c.wizard

import megrok.z3cform.wizard as z3cwizard 
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


class UnfallanzeigeWizard(z3cwizard.WizardForm):
    """ Wizard form."""
    grok.context(Unfallanzeige)

    label = u'Unfallanzeige'

    def setUpSteps(self):
        return [
            z3c.wizard.step.addStep(self, 'basic', weight=1),
            z3c.wizard.step.addStep(self, 'job', weight=2),
            z3c.wizard.step.addStep(self, 'person', weight=3),
            z3c.wizard.step.addStep(self, 'accidenti', weight=4),
            z3c.wizard.step.addStep(self, 'accidentii', weight=5),
            z3c.wizard.step.addStep(self, 'basicinformation', weight=6),
            z3c.wizard.step.addStep(self, 'finish', weight=7),
            ]


    def update(self):
        super(UnfallanzeigeWizard, self).update()
        uazjs.need()
        uazcss.need()

    def doFinish(self):
        print "FINISH"
