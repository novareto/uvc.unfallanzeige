# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de

import grok
import uvcsite

from zope import interface
from uvcsite.interfaces import IMyHomeFolder

from .uazwizard import Unfallanzeige
from dolmen.forms.base.utils import set_fields_data
from .interfaces import IUnfallanzeige, IUnfallanzeigenFolder
from uvcsite.content.tables import MetaTypeColumn


class IVerbandbuchEintrag(interface.Interface):
    """ Marker Interface """


class MetaTypeColumn(MetaTypeColumn):
    grok.context(IUnfallanzeigenFolder)

    def renderCell(self, item):
        #import pdb; pdb.set_trace()
        if IVerbandbuchEintrag.providedBy(item):
            return u"Eintrag im Verbandbuch"
        return item.meta_type


class MetaTypeColumn(MetaTypeColumn):
    grok.context(IMyHomeFolder)


class AddVerbandbuch(uvcsite.Form):
    grok.context(IUnfallanzeigenFolder)
    label = title = "Verbandbuch"
    description = u"Bitte tragen Sie die fehlenden Werte ein"

    fields = uvcsite.Fields(IUnfallanzeige).select('prsname', 'prsvor', 'prsgeb', 'unfdatum', 'unfzeit', 'diavkt', 'diaadv', 'unfhg1')

    #def update(self):
    #    import pdb; pdb.set_trace()

    @uvcsite.action('Eintrag speichern')
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
    fields = uvcsite.Fields(IUnfallanzeige).select('prsname', 'prsvor', 'prsgeb', 'unfdatum', 'unfzeit', 'diavkt', 'diaadv', 'unfhg1')
    ignoreContent = False

    @uvcsite.action('Speichern')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        set_fields_data(IUnfallanzeige, self.context, data)
        self.flash(u'Ihr Eintrag wurde erstellt')
        self.redirect(self.application_url())

    @uvcsite.action('Zu einer Unfallanzeige machen')
    def handle_update(self):
        data, errors = self.extractData()
        if errors:
            return
        interface.noLongerProvides(self.context, IVerbandbuchEintrag)
        self.flash(u'Aus Ihrem Verbandbucheintrag wurde eine Unfallanzeige erstellt')
        self.redirect(self.url(self.context, 'edit'))
