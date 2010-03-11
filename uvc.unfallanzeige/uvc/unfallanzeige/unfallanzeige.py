# -*- coding: utf-8 -*-
# Copyright (c) 2004-2009 novareto GmbH
# lwalther@novareto.de

import grok

from z3c.form import form
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from z3c.form.browser.radio import RadioFieldWidget 

from hurry.workflow.interfaces import IWorkflowInfo

from megrok.z3cform.base import PageAddForm, Fields

from uvcsite.interfaces import IMyHomeFolder, ISidebar
from uvcsite import ProductFolder, Content, schema, contenttype
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IUnfallanzeigeFolder
from zope.interface import Interface
from dolmen.menu import menu, menuentry, Entry
from uvc.layout.menus import SidebarMenu
from zope.traversing.browser import absoluteURL
from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zope.app.homefolder.interfaces import IHomeFolder
from uvc.unfallanzeige.resources import UAZLibrary


class UAZMenu(Entry):
    grok.context(Interface)
    grok.title('Unfallanzeige')
    menu(SidebarMenu)
    grok.order(30)

    @property
    def url(self):
        principal = self.request.principal
        if IUnauthenticatedPrincipal.providedBy(principal):
            return
        homeFolder = IHomeFolder(principal).homeFolder
        return absoluteURL(homeFolder, self.request) + '/unfallanzeigen/@@add'


class Unfallanzeige(Content):
    """ContentType fuer das Lastschriftverfahren"""
    grok.name('unfallanzeige')
    schema(IUnfallanzeige)


class UnfallanzeigenContainer(ProductFolder):
    """Container fuer die Speicherung der Lastschriftdokumente"""
    grok.implements(IUnfallanzeigeFolder)
    contenttype(Unfallanzeige)


class Add(PageAddForm):
    """Form für das Hinzufuegen neuer Dokumente im Dokumentcontainer"""
    grok.title('Unfallanzeige')
    grok.context(IUnfallanzeigeFolder)
    fields = Fields(IUnfallanzeige)
    fields['unfustdor'].widgetFactory = RadioFieldWidget 
    fields['unflar'].widgetFactory = RadioFieldWidget 
    grok.require('uvc.AddContent')
    label = u'Neues Unfallanzeige'
    description = u'Mit diesem Formular kann ein neues Dokument hinzugefuegt werden.'

    def create(self, data):
        content = self.context.getContentType()() #holen der Klasse und Instanzieren der Klasse
        form.applyChanges(self, content, data)
        return content

    def add(self, content):
        """
        """ 
        self.object = content 
        self.context.add(content)

    def nextURL(self):
        """
        """
        IWorkflowInfo(self.object).fireTransition('publish')
        self.flash(u'Ihr Dokument wurde gespeichert') 
        return self.url(self.context)

    def update(self):
        super(Add, self).update()
        UAZLibrary.need()


@grok.subscribe(IMyHomeFolder, grok.IObjectAddedEvent)
def addContainer(homefolder, event):
    """LastschriftContainer wird per Event im Homeordner angelegt.
       Der Event wird mit der ersten Anmeldung im Portal aufgerufen.
    """
    homefolder['unfallanzeigen'] = UnfallanzeigenContainer() 
