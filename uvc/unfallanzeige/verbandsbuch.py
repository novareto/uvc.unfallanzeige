# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import grok
import uvcsite

from zope import interface
from zeam.form.base import Fields, action
from uvcsite.interfaces import IHomeFolder
from uvcsite.browser.forms import set_fields_data
from uvcsite.content.tables import MetaTypeColumn

from .interfaces import IUnfallanzeige, IUnfallanzeigenFolder
from .uazwizard import Unfallanzeige


class IVerbandbuchEintrag(interface.Interface):
    """ Marker Interface """


class MetaTypeColumn(MetaTypeColumn):
    grok.context(IUnfallanzeigenFolder)

    def renderCell(self, item):
        if IVerbandbuchEintrag.providedBy(item):
            return u"Eintrag im Verbandbuch"
        return item.meta_type


class MetaTypeColumn(MetaTypeColumn):
    grok.context(IHomeFolder)


class AddVerbandbuch(uvcsite.browser.Form):
    grok.context(IUnfallanzeigenFolder)
    label = title = "Verbandbuch"
    description = u"Bitte tragen Sie die fehlenden Werte ein"

    fields = Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'prsgeb', 'unfdatum', 'unfzeit',
        'diavkt', 'diaadv', 'unfhg1')

    @action('Eintrag speichern')
    def handle_save(self):
        data, errors = self.extractData()
        if errors:
            return
        uaz = Unfallanzeige()
        set_fields_data(IUnfallanzeige, uaz, data)
        interface.alsoProvides(uaz, IVerbandbuchEintrag)
        self.context.add(uaz)
        self.flash(u'Ihr Eintrag wurde erstellt')
        self.redirect(self.url(self.context))


class Edit(uvcsite.browser.Form):
    grok.context(IVerbandbuchEintrag)

    fields = Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'prsgeb', 'unfdatum',
        'unfzeit', 'diavkt', 'diaadv', 'unfhg1')
    ignoreContent = False

    @action('Speichern')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        set_fields_data(IUnfallanzeige, self.context, data)
        self.flash(u'Ihr Eintrag wurde erstellt')
        self.redirect(self.application_url())

    @action('Zu einer Unfallanzeige machen')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        interface.noLongerProvides(self.context, IVerbandbuchEintrag)
        self.flash(
            'Aus Ihrem Verbandbucheintrag wurde eine Unfallanzeige erstellt')
        self.redirect(self.url(self.context, 'edit'))
