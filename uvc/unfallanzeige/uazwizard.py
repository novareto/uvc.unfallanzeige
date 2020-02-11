# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de


import grok
import uvcsite.content.components
import uvcsite.content.directive

from dolmen.forms.wizard import Wizard
from zope.lifecycleevent import ObjectCreatedEvent
from uvc.unfallanzeige.resources import uazjs, uazcss
from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder, IUnfallanzeige
from grok.components import ViewSupportMixin
from zeam.form.base import Actions
from dolmen.forms.wizard.actions import (PreviousAction, SaveAction,
     NextAction, HiddenSaveAction)


grok.templatedir('templates')


class Unfallanzeige(uvcsite.content.components.Content):
    """ContentType fuer das Lastschriftverfahren"""
    grok.name('Unfallanzeige')
    grok.title('Unfallanzeige')

    title = u"Unfallanzeige"
    schema = (IUnfallanzeige,)
    

class Unfallanzeigen(uvcsite.content.components.ProductFolder):
    """Container fuer die Speicherung der Unfallanzeige"""
    grok.implements(IUnfallanzeigenFolder)
    uvcsite.content.directive.contenttype(Unfallanzeige)
    grok.title(u'Elektronische Unfallanzeigen')

    title = u"Unfallanzeigen"
    #description = u"In diesem Ordner werden alle Elektronischen Unfallanzeigen gespeichert"
    description = u""


class Adder(grok.View):
    grok.context(IUnfallanzeigenFolder)
    grok.name('add')

    def update(self):
        self.uaz = uaz = Unfallanzeige()
        grok.notify(ObjectCreatedEvent(uaz))
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'edit'))


class UnfallanzeigeWizard(Wizard, ViewSupportMixin):
    """ Wizard form."""
    grok.context(Unfallanzeige)
    grok.name('edit')
    grok.require('uvc.EditContent')

    actions = Actions(
        PreviousAction(u"Zurück"),
        SaveAction(u"Speichern"),
        NextAction(u"Weiter"))

    label = u'Unfallanzeige'

    def update(self):
        super(UnfallanzeigeWizard, self).update()
        uazcss.need()
        uazjs.need()
