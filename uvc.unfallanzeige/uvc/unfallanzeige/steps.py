# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import zope.interface
import zope.component

from uvc.unfallanzeige import resources
from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder, IUnfallanzeige, IUnfallanzeigeWizard
from uvc.unfallanzeige.uazwizard import UnfallanzeigeWizard, Unfallanzeige 

from dolmen.forms import base
from zeam.form.base.markers import NO_VALUE
from zeam.form.base.errors import Error 


grok.templatedir('templates')

#
## Step1
#

class Basic(uvcsite.Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(10)
    label = u'Basis Informationen'
    ignoreContent = False


    fields = base.Fields(IUnfallanzeige).select(
       'unfustdor', 'unfuname', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    fields['unfustdor'].mode = "radio"

    def update(self):
        super(Basic, self).update()
        resources.step1.need()

    def validateStep(self, data, errors):
        if data.get('unfustdor') == 'In einer Zweigniederlassung':
            if data.get('unfuort') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Ort ausfüllen.', identifier='unfuort'))
            if data.get('unfustrasse') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Strasse ausfüllen.', identifier='unfustrasse'))
            if data.get('unfunr') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Nummer ausfüllen.', identifier='unfunr'))
            if data.get('unfuname') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Name ausfüllen.', identifier='unfuname'))
            if data.get('unfuplz') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Plz ausfüllen.', identifier='unfuplz'))
        return errors        

#
## Step2
#

class Job(uvcsite.Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(20)
    ignoreContent = False
    label = form_name = u'Angaben zur versicherten Person'

    fields = base.Fields(IUnfallanzeige).select(
        'uadbru1', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    fields['unflar'].mode = "radio"

    def update(self):
        super(Job, self).update()
        resources.step2.need()

    def validateStep(self, data, errors):
        if data.get('unflar') == 'ja':
            if data.get('unvlaraddr') == NO_VALUE:
                errors.append( Error(u'Bitte die Adresse der Firma ausfüllen.','unvlaraddr'))
        return errors

#
## Step3
#

class Person(uvcsite.Step):
    grok.context(IUnfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(30)
    ignoreContent = False
    label = form_name = u'weitere Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = base.Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'ikstr', 'iknr', 'lkz', 'ikzplz', 
        'ikzort', 'prsgeb', 'prssex', 'prssta', 'unfbu', 'vehearbeitsv', 
        'vehebis', 'veheentgeltbis', 'unfefz', 'unfkka')

    fields['unfbu'].mode = "radio"
    fields['prssex'].mode = "radio"
    fields['vehearbeitsv'].mode = "radio"

    def update(self):
        super(Person, self).update()
        resources.step3.need()

    def validateStep(self, data, errors):
        if data.get('unfbu') == "Ehegatte des Unternehmers":
            if data.get('vehearbeitsv') == NO_VALUE:
                errors.append(Error('Bitte hier eine Eingabe machen', identifier='vehearbeitsv'))
            if data.get('vehearbeitsv') == "Ja":
                if data.get('vehebis') == NO_VALUE:
                    errors.append(Error('Bitte hier eine Eingabe machen', identifier='vehebis'))
                if data.get('veheentgeltbis') == NO_VALUE:
                    errors.append(Error('Bitte hier eine Eingabe machen', identifier='veheentgeltbis'))
        return errors 

#
## Step4
#

class AccidentI(uvcsite.Step):
    grok.context(IUnfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(40)
    ignoreContent = False
    label = form_name = u'Informationen zum Unfall Teil I'

    fields = base.Fields(IUnfallanzeige).select(
        'unfdatum', 'unfzeit', 'unfort_detail', 'unfort',
        'unfhg1', 'unfhg2', 'unfkn1', 'unfkn2')

    fields['unfhg2'].mode = "radio"
    fields['unfkn2'].mode = "radio"

    def update(self):
        super(uvcsite.Step, self).update()
        resources.step4.need()

#
## Step5
#

class AccidentII(uvcsite.Step):
    grok.context(IUnfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(50)
    ignoreContent = False
    label = form_name = u'Informationen zum Unfall Teil II'

    handleApplyOnBack = True

    fields = base.Fields(IUnfallanzeige).select(
        'prstkz', 'unfae1', 'unfaedatum', 'unfaezeit', 'unfwa1', 
        'unfwax', 'uadbavon', 'uadbabis', 'diavkt', 'diaadv', 'unfeba', 'unfeba1')

    fields['prstkz'].mode = "radio"
    fields['unfae1'].mode = "radio"
    fields['unfwa1'].mode = "radio"
    fields['unfeba'].mode = "radio"

    def update(self):
        super(uvcsite.Step, self).update()
        resources.step5.need()

    def validateStep(self, data, errors):
        error = []
        if data.get('prstkz') == "nein":
            if data.get('unfae1') == NO_VALUE:
                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfae1',))
            else:
                if data.get('unfae1') == "ja, sofort":
                    if data.get('unfwa1') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfwa1'))
                    else:
                        if data.get('unfwa1') == "ja":
                            if data.get('unfwax') == NO_VALUE:
                                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfwax'))
                
                elif data.get('unfae1') == "ja, spaeter am":
                    if data.get('unfwa1') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfwa1'))
                    if data.get('unfaedatum') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfaedatum'))
                    if data.get('unfaezeit') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfaezeit'))
        if data.get('unfeba') == "Aerztliche Behandlung bei:":
            if data.get('unfeba1') == NO_VALUE:
                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='unfeba1'))
        return errors


#
## Step 6 
#

class BasicInformation(uvcsite.Step):
    grok.context(IUnfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(60)
    ignoreContent = False
    label = form_name = u'Allgemeine Informationen zum Unternehmen'

    fields = base.Fields(IUnfallanzeige).select('unfus3', 'unfus2')

#
## Step 7
#

class Finish(uvcsite.Step):
    grok.context(IUnfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(70)
    ignoreContent = False
    label = form_name = u'Versand und Druck der Unfallanzeige'
    fields = base.Fields(IUnfallanzeige).select('behandlung')

    fields['behandlung'].mode = "radio"


class Overview(grok.Viewlet):
    grok.view(UnfallanzeigeWizard)
    grok.viewletmanager(uvcsite.IExtraInfo)
    grok.context(IUnfallanzeige)

    @property
    def available(self):
        if int(self.view.step) == 6:
            return True
        return False
