# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import grok
import zope.interface
import zope.component
import uvcsite.browser.layout.slots.interfaces

from dolmen.forms.wizard import WizardStep
from uvc.unfallanzeige import resources
from uvc.unfallanzeige.interfaces import IUnfallanzeige
from uvc.unfallanzeige.uazwizard import UnfallanzeigeWizard, Unfallanzeige

from zeam.form import base
from zeam.form.base.errors import Error
from zeam.form.base import NO_VALUE as NO_VALUEM
from grok.components import ViewSupportMixin


grok.templatedir('templates')

#
## Step1
#

NO_VALUE = ""


class Step(WizardStep, ViewSupportMixin):
    grok.baseclass()
    
    def __init__(self, *args):
        WizardStep.__init__(self, *args)
        self.macros = zope.component.getMultiAdapter(
            (self.context, self.request), name='fieldmacros').template.macros

    def validateStep(self, fields, data):
        return

    def validateData(self, fields, data):
        errors = super(Step, self).validateData(fields, data)
        self.validateStep(data, errors)
        return errors


class Basic(Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(10)

    available = False

    label = u'Basis-Informationen'
    ignoreContent = False

    fields = base.Fields(IUnfallanzeige).select(
        'title', 'unfustdor', 'unfuname', 'unfustrasse',
        'unfunr', 'unfuplz', 'unfuort', 'anspname', 'anspfon',
    )

    fields['unfustdor'].mode = "radio"

    def data(self):
        return "jinx"

    def updateWidgets(self):
        super(Basic, self).updateWidgets()
        resources.step1.need()

    def validateStep(self, data, errors):
        if data.get('unfustdor') == 'In einer Zweigniederlassung':
            if data.get('unfuort') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Ort ausfüllen.', identifier='form.basic.field.unfuort'))
            if data.get('unfustrasse') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Strasse ausfüllen.', identifier='form.basic.field.unfustrasse'))
            if data.get('unfunr') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Nummer ausfüllen.', identifier='form.basic.field.unfunr'))
            if data.get('unfuname') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Name ausfüllen.', identifier='form.basic.field.unfuname'))
            if data.get('unfuplz') == NO_VALUE:
                errors.append(Error(u'Bitte das Feld Plz ausfüllen.', identifier='form.basic.field.unfuplz'))
        return errors

#
## Step2
#


class Job(Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(20)

    ignoreContent = False
    label = form_name = u'Angaben zur versicherten Person'

    fields = base.Fields(IUnfallanzeige).select(
        'uadbru1', 'azubi', 'uadst', 'unfute', 'unflar', 'unvlaraddr')


    fields['unflar'].mode = "radio"
    fields['azubi'].mode = "radio"

    def updateWidgets(self):
        super(Job, self).updateWidgets()
        resources.step2.need()

    def validateStep(self, data, errors):
        if data.get('unflar') == 'ja':
            if data.get('unvlaraddr') == NO_VALUE:
                errors.append(Error(u'Bitte die Adresse der Firma ausfüllen.', 'form.job.field.unvlaraddr'))
        return errors

#
## Step3
#


class Person(Step):
    grok.context(Unfallanzeige)
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

    def updateWidgets(self):
        super(Person, self).updateWidgets()
        resources.step3.need()

    def validateStep(self, data, errors):
        if data.get('lkz') == 'D':
            if data.get('ikzplz') is not NO_VALUEM:
                if len(data.get('ikzplz', '')) != 5:
                    errors.append((Error(u'Ihre Postleitzahl muss aus fünf Zahlen bestehen.', identifier='form.person.field.ikzplz')))
        if data.get('unfbu') == "Ehegatte des Unternehmers" or data.get('unfbu') == "eingetragenen Lebenspartnerschaft":
            if data.get('vehearbeitsv') == NO_VALUEM:
                errors.append(Error('Bitte hier eine Eingabe machen', identifier='form.person.field.vehearbeitsv'))
            if data.get('vehearbeitsv') == "Ja":
                if data.get('vehebis') == "":
                    errors.append(Error('Bitte hier eine Eingabe machen', identifier='form.person.field.vehebis'))
                if data.get('veheentgeltbis') == "":
                    errors.append(Error('Bitte hier eine Eingabe machen', identifier='form.person.field.veheentgeltbis'))
        return errors

#
## Step4
#


class AccidentI(Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(40)
    ignoreContent = False
    label = form_name = u'Informationen zum Unfall Teil I'

    fields = base.Fields(IUnfallanzeige).select(
        'unfdatum', 'unfzeit', 'unfort_detail', 'unfort',
        'unfhg1', 'unfhg2', 'unfkn1', 'unfkn2')

    fields['unfhg2'].mode = "radio"
    fields['unfkn2'].mode = "radio"

    def updateWidgets(self):
        super(Step, self).updateWidgets()
        resources.step4.need()

#
## Step5
#


class AccidentII(Step):
    grok.context(Unfallanzeige)
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

    def updateWidgets(self):
        super(Step, self).updateWidgets()
        resources.step5.need()

    def validateStep(self, data, errors):
        if data.get('prstkz') == "nein":
            if data.get('unfae1') == NO_VALUEM:
                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfae1',))
            else:
                if data.get('unfae1') == "ja, sofort":
                    if data.get('unfwa1') == NO_VALUEM:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfwa1'))
                    else:
                        if data.get('unfwa1') == "ja":
                            if data.get('unfwax') == NO_VALUE:
                                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfwax'))

                elif data.get('unfae1') == "ja, spaeter am:":
                    if data.get('unfwa1') == NO_VALUEM:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfwa1'))
                    if data.get('unfwa1') == "ja":
                        if data.get('unfwax') == NO_VALUE:
                            errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfwax'))
                    if data.get('unfaedatum') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfaedatum'))
                    if data.get('unfaezeit') == NO_VALUE:
                        errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfaezeit'))
        if data.get('unfeba') == "Aerztliche Behandlung bei:":
            if data.get('unfeba1') == NO_VALUE:
                errors.append(Error('Bitte machen Sie Angaben in diesem Feld.', identifier='form.accidentii.field.unfeba1'))
        return errors


#
## Step 6
#


class BasicInformation(Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(60)
    ignoreContent = False
    label = form_name = u'Allgemeine Informationen zum Unternehmen'

    fields = base.Fields(IUnfallanzeige).select('unfus3', 'unfus2')

#
## Step 7
#


class Finish(Step):
    grok.context(Unfallanzeige)
    grok.view(UnfallanzeigeWizard)
    grok.order(70)
    ignoreContent = False
    label = form_name = u'Versand und Druck der Unfallanzeige'
    fields = base.Fields(IUnfallanzeige).select('behandlung')
    fields['behandlung'].mode = "radio"



class Overview(grok.Viewlet):
    grok.view(Finish)
    grok.viewletmanager(uvcsite.browser.layout.slots.interfaces.IExtraInfo)
    grok.context(IUnfallanzeige)

#    def available(self):
#        if int(self.view.step) + 1 == len(self.view.allSubforms):
#            return True
#        return False


    def getTitle(self, term, vocab_name):
        vocab = zope.component.getUtility(
            zope.schema.interfaces.IVocabularyFactory, vocab_name)(None)
#        return vocab.getTrem(term).title
        try:
            return vocab.getTerm(term).title
        except:
            return term
