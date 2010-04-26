import grok
from megrok.pagetemplate import PageTemplate, view
from dolmen.menu import menu, menuentry, Entry
from hurry.workflow.interfaces import IWorkflowInfo
from megrok.z3cform.base import PageAddForm, Fields
from uvc.layout.menus import SidebarMenu
from uvc.unfallanzeige.interfaces import IUnfallanzeige, IUnfallanzeigeFolder
from uvcsite import ProductFolder, Content, schema, contenttype
from uvcsite.interfaces import IMyHomeFolder, ISidebar
from z3c.form import form, group
from z3c.form.browser.radio import RadioFieldWidget
from zope.app.homefolder.interfaces import IHomeFolder
from uvc.layout.layout import IUVCLayer

from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zope.interface import Interface
from zope.traversing.browser import absoluteURL
from megrok.z3cform import wizard as z3cwizard
from z3c.wizard import wizard, step
from zope.schema.fieldproperty import FieldProperty

from z3c.wizard.interfaces import IStep
from megrok.z3cform.wizard import z3cWizard

from resources import uazjs, uazcss

### Content

class Unfallanzeige(Content):
    """ContentType fuer das Lastschriftverfahren"""
    schema(IUnfallanzeige)
    grok.name('unfallanzeige')


class UnfallanzeigenContainer(ProductFolder):
    """Container fuer die Speicherung der Lastschriftdokumente"""
    grok.implements(IUnfallanzeigeFolder)
    contenttype(Unfallanzeige)


### MenuStuff

class UAZMenuWizard(Entry):
    grok.context(Interface)
    grok.title('Unfallanzeige Wizard')
    menu(SidebarMenu)
    grok.order(30)

    @property
    def url(self):
        principal = self.request.principal
        if IUnauthenticatedPrincipal.providedBy(principal):
            return
        homeFolder = IHomeFolder(principal).homeFolder
        return absoluteURL(homeFolder, self.request) + '/unfallanzeigen/startwizard'


class StartWizard(grok.View):
    grok.implements(z3cwizard.IWizard)
    grok.context(IUnfallanzeigeFolder)

    def update(self):
        self.uaz = uaz = Unfallanzeige()
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'uazwizard'))


### Wizard

class UazWizard(z3cwizard.WizardForm):
    """ Wizard form."""
    grok.context(IUnfallanzeige)

    label = u'Unfallanzeige'

    def setUpSteps(self):
        return [
            step.addStep(self, 'basic', weight=1),
            step.addStep(self, 'job', weight=2),
            step.addStep(self, 'person', weight=3),
            ]


### Steps

class Basic(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = forn_name = u'Basis Informationen'

    showCompleteButton = False

    fields = Fields(IUnfallanzeige).select(
       'unfustdor', 'unfuname', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    fields['unfustdor'].widgetFactory = RadioFieldWidget


    def update(self):
        uazcss.need()
        uazjs.need()
        z3cwizard.PageStep.update(self)


class Job(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = form_name = u'Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = Fields(IUnfallanzeige).select(
        'uadbru1', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    fields['unflar'].widgetFactory = RadioFieldWidget

    def update(self):
        uazjs.need()
        uazcss.need()
        z3cwizard.PageStep.update(self)


class Person(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = form_name = u'weitere Angaben zur versicherten Person'

    handleApplyOnBack = True

    fields = Fields(IUnfallanzeige).select(
        'prsname', 'prsvor', 'ikstrnr', 'lkz', 'ikzplz', 
        'ikzort', 'prsgeb', 'prssta', 'unfbu', 'vehearbeitsv', 
        'vehebis', 'veheentgeltbis', 'unfefz', 'unfkka')

    fields['unfbu'].widgetFactory = RadioFieldWidget
    fields['vehearbeitsv'].widgetFactory = RadioFieldWidget

    def update(self):
        uazjs.need()
        uazcss.need()
        z3cwizard.PageStep.update(self)



@grok.subscribe(IMyHomeFolder, grok.IObjectAddedEvent)
def addContainer(homefolder, event):
    """LastschriftContainer wird per Event im Homeordner angelegt.
       Der Event wird mit der ersten Anmeldung im Portal aufgerufen.
    """
    homefolder['unfallanzeigen'] = UnfallanzeigenContainer() 
