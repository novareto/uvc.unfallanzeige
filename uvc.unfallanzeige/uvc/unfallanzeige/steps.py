# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


import grok
import uvcsite
import megrok.z3cform.base as z3cform
import megrok.z3cform.wizard as z3cwizard 

from z3c.form.browser.radio import RadioFieldWidget
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IUnfallanzeigeWizard
from uvc.unfallanzeige.uazwizard import UnfallanzeigeWizard 


class Basic(z3cwizard.PageStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Basis Informationen'

    showCompleteButton = False

    fields = z3cform.Fields(IUnfallanzeige).select(
       'unfustdor', 'unfuname', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    fields['unfustdor'].widgetFactory = RadioFieldWidget


class Job(z3cwizard.PageStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'uadbru1', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    fields['unflar'].widgetFactory = RadioFieldWidget



class Person(z3cwizard.PageStep):
    grok.context(UnfallanzeigeWizard)
    label = form_name = u'weitere Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = z3cform.Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'ikstrnr', 'lkz', 'ikzplz', 
        'ikzort', 'prsgeb', 'prssta', 'unfbu', 'vehearbeitsv', 
        'vehebis', 'veheentgeltbis', 'unfefz', 'unfkka')

    fields['unfbu'].widgetFactory = RadioFieldWidget
    fields['vehearbeitsv'].widgetFactory = RadioFieldWidget

