# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import grok
import uvcsite

from zope import interface

from .uazwizard import Unfallanzeige
from dolmen.forms.base.utils import set_fields_data
from .interfaces import IUnfallanzeige, IUnfallanzeigenFolder
from uvcsite.content.tables import MetaTypeColumn


class IVerbandbuchEintrag(interface.Interface):
    """ Marker Interface """


class MetaTypeColumn(MetaTypeColumn):
    grok.context(IUnfallanzeigenFolder)

    def renderCell(self, item):
        if IVerbandbuchEintrag.providedBy(item):
            return u"Eintrag im Verbandbuch"
        return item.meta_type


class AddVerbandsbuch(uvcsite.Form):
    grok.context(IUnfallanzeigenFolder)

    fields = uvcsite.Fields(IUnfallanzeige).select('prsname', 'prsvor', 'prsgeb', 'unfdatum', 'unfzeit', 'unfhg1')

    @uvcsite.action('Ins Versandbuch eintragen.')
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


class Edit(uvcsite.Form):
    grok.context(IVerbandbuchEintrag)
    fields = uvcsite.Fields(IUnfallanzeige).select('prsname', 'prsvor', 'prsgeb', 'unfdatum', 'unfzeit', 'unfhg1')
    ignoreContent = False

    @uvcsite.action('Bearbeiten')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        set_fields_data(IUnfallanzeige, self.context, data)
        self.flash(u'Ihr Eintrag wurde erstellt')
        self.redirect(self.url(self.context))

    @uvcsite.action('Zu einer Unfallanzeige machen')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        interface.noLongerProvides(self.context, IVerbandbuchEintrag)
        self.flash(u'Aus Ihrem Verbandsbucheintrag wurde eine Unfallanzeige erstellt')
        self.redirect(self.url(self.context, 'edit'))
