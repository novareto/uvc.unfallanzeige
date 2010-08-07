# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import zope.interface
import zope.component

import megrok.z3cform.base as z3cform
import megrok.z3cform.wizard as z3cwizard 

from z3c.form.browser.radio import RadioFieldWidget

from uvc.unfallanzeige import resources
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IUnfallanzeigeWizard
from uvc.unfallanzeige.uazwizard import UnfallanzeigeWizard 


#
## Step1
#

class Basic(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Basis Informationen'

    showCompleteButton = False

    fields = z3cform.Fields(IUnfallanzeige).select(
       'unfustdor', 'unfuname', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    fields['unfustdor'].widgetFactory = RadioFieldWidget

    def update(self):
        super(uvcsite.BasicStep, self).update()
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
    #grok.view(Basic)

    def render(self):
        return "Daten des Unternehmens"


#
## Step2
#

class Job(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'uadbru1', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    fields['unflar'].widgetFactory = RadioFieldWidget

    def update(self):
        super(uvcsite.BasicStep, self).update()
        resources.step2.need()

    def validateStep(self, data):
        errors = []
        if data.get('unflar') == 'ja':
            if not data.get('unvlaraddr'):
                errors.append( ('unvlaraddr', u'Bitte die Adresse der Firma ausfüllen.') )
        return errors

#
## Step3
#

class Person(uvcsite.BasicStep):
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
        super(uvcsite.BasicStep, self).update()
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

#
## Step4
#

class AccidentI(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Informationen zum Unfall Teil I'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'unfdatum', 'unfzeit', 'unfort_detail', 'unfort',
        'unfhg1', 'unfhg2', 'unfkn1', 'unfkn2')

    fields['unfhg2'].widgetFactory = RadioFieldWidget
    fields['unfkn2'].widgetFactory = RadioFieldWidget

    def update(self):
        super(uvcsite.BasicStep, self).update()
        resources.step4.need()

#
## Step5
#

class AccidentII(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Informationen zum Unfall Teil II'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'prstkz', 'unfae1', 'unfaedatum', 'unfaezeit', 'unfwa1', 
        'unfwax', 'uadbavon', 'uadbabis', 'diavkt', 'diaadv', 'unfeba', 'unfeba1')

    fields['prstkz'].widgetFactory = RadioFieldWidget
    fields['unfae1'].widgetFactory = RadioFieldWidget
    fields['unfwa1'].widgetFactory = RadioFieldWidget
    fields['unfeba'].widgetFactory = RadioFieldWidget

    def update(self):
        super(uvcsite.BasicStep, self).update()
        resources.step5.need()

    def validateStep(self, data):
        error = []
        if data.get('prstkz') == "nein":
            if not data.get('unfae1'):
                error.append(('unfae1', 'Bitte machen Sie Angaben in diesem Feld.'))
            else:
                if data.get('unfae1') == "ja, sofort":
                    if not data.get('unfwa1'):
                        error.append(('unfwa1', 'Bitte machen Sie Angaben in diesem Feld.'))
                    else:
                        if data.get('unfwa1') == "ja":
                            if not data.get('unfwax'):
                                error.append(('unfwax', 'Bitte machen Sie Angaben in diesem Feld.'))
                
                elif data.get('unfae1') == "ja, spaeter am":
                    if not data.get('unfwa1'):
                        error.append(('unfwa1', 'Bitte machen Sie Angaben in diesem Feld.'))
                    if not data.get('unfaedatum'):
                        error.append(('unfaedatum', 'Bitte machen Sie Angaben in diesem Feld.'))
                    if not data.get('unfaezeit'):
                        error.append(('unfaezeit', 'Bitte machen Sie Angaben in diesem Feld.'))
        if data.get('unfeba') == "Name und Anschrift":
            if not data.get('unfeba1'):
                error.append(('unfeba1', 'Bitte machen Sie Angaben in diesem Feld.'))
        return error


#
## Step 6 
#

class BasicInformation(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Allgemeine Informationen zum Unternehmen'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select('unfus3', 'unfus2')


    def update(self):
        super(uvcsite.BasicStep, self).update()


#
## Step 7
#

class Finish(uvcsite.BasicStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Versand und Druck der Unfallanzeige'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select('behandlung')

    fields['behandlung'].widgetFactory = RadioFieldWidget

