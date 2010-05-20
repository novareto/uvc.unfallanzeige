# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import zope.interface
import zope.component

import megrok.z3cform.base as z3cform
import megrok.z3cform.wizard as z3cwizard 

from z3c.form.interfaces import IErrorViewSnippet
from z3c.form.browser.radio import RadioFieldWidget

from uvc.unfallanzeige import resources
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IUnfallanzeigeWizard
from uvc.unfallanzeige.uazwizard import UnfallanzeigeWizard 


class BasicStep(z3cwizard.PageStep):
    label = form_name = u""
    grok.baseclass()

    def extractData(self):
        data, errors = z3cwizard.PageStep.extractData(self)
        step_errors = []
        for field, message in self.validateStep(data):
            widget = self.widgets[field]
            error = zope.interface.Invalid(message)
            view = zope.component.getMultiAdapter(
                    (error, self.request, widget, widget.field,
                     self, self.context), IErrorViewSnippet)
            view.update()
            if not widget.error:
                widget.error = view
            step_errors.append(view)
        if step_errors:
            errors += tuple(step_errors)
        return data, errors    

    def validateStep(self, data):
        return []


#
## Step1
#

class Basic(BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Basis Informationen'

    showCompleteButton = False

    fields = z3cform.Fields(IUnfallanzeige).select(
       'unfustdor', 'unfuname', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    fields['unfustdor'].widgetFactory = RadioFieldWidget

    def update(self):
        super(BasicStep, self).update()
        resources.step1.need()

    def validateStep(self, data):
        errors = []
        if data.get('unfustdor') == 'In einer Zweigniederlassung':
            if not data.get('unfuort'):
                errors.append( ('unfuort', u'Bitte das Feld Ort ausfüllen.') )
            if not data.get('unfustrasse'):
                errors.append( ('unfustrasse', u'Bitte das Feld Strasse ausfüllen.') )
            if not data.get('unfunr'):
                errors.append( ('unfunr', u'Bitte das Feld Nummer ausfüllen.') )
            if not data.get('unfuname'):
                errors.append( ('unfuname', u'Bitte das Feld Name ausfüllen.') )
            if not data.get('unfuplz'):
                errors.append( ('unfuplz', u'Bitte das Feld Plz ausfüllen.') )
        return errors        


class Adress(grok.Viewlet):
    grok.viewletmanager(uvcsite.IExtraInfo)
    grok.context(IUnfallanzeige)
    grok.view(Basic)

    def render(self):
        return "ICH BINS DIE ADRESE"


#
## Step2
#

class Job(BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'uadbru1', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    fields['unflar'].widgetFactory = RadioFieldWidget

    def update(self):
        super(BasicStep, self).update()
        resources.step2.need()

#
## Step3
#
import pprint

class Person(BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'weitere Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'ikstr', 'iknr', 'lkz', 'ikzplz', 
        'ikzort', 'prsgeb', 'prssex', 'prssta', 'unfbu', 'vehearbeitsv', 
        'vehebis', 'veheentgeltbis', 'unfefz', 'unfkka')

    fields['unfbu'].widgetFactory = RadioFieldWidget
    fields['prssex'].widgetFactory = RadioFieldWidget
    fields['vehearbeitsv'].widgetFactory = RadioFieldWidget

    def update(self):
        super(BasicStep, self).update()
        resources.step3.need()

    def validateStep(self, data):
        error = []
        if data.get('unfbu') == "Ehegatte des Unternehmers":
            if not data.get('vehearbeitsv'):
                error.append(('vehearbeitsv', 'Bitte hier eine Eingabe machen'))
            if data.get('vehearbeitsv') == "Ja":
                if not data.get('vehebis'):
                    error.append(('vehebis', 'Bitte hier eine Eingabe machen'))
                if not data.get('veheentgeltbis'):
                    error.append(('veheentgeltbis', 'Bitte hier eine Eingabe machen'))
        return error 


class AccidentI(BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Informationen zum Unfall Teil I'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'unfdatum', 'unfzeit', 'unfort_detail', 'unfort',
        'unfhg1', 'unfhg2', 'unfkn1', 'unfkn2')

    fields['unfhg2'].widgetFactory = RadioFieldWidget
    fields['unfkn2'].widgetFactory = RadioFieldWidget

    def update(self):
        super(BasicStep, self).update()
        resources.step4.need()


class AccidentII(BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Informationen zum Unfall Teil II'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'prstkz', 'unfae1', 'unfaedatum', 'unfaezeit', 'unfwa1', 'unfwax')

    fields['prstkz'].widgetFactory = RadioFieldWidget
    fields['unfae1'].widgetFactory = RadioFieldWidget
    fields['unfwa1'].widgetFactory = RadioFieldWidget

    def update(self):
        super(BasicStep, self).update()
        resources.step5.need()
