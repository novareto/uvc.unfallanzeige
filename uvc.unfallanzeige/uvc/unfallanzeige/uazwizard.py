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

#from megrok import resource
#from hurry.jquery import jquery
#
#
#class z3cWizardLib(resource.Library):
#    resource.name('ajaxwizard')
#    grok.path('wizard')
#
#z3cWizard = resource.ResourceInclusion(
#    z3cWizardLib, 'z3c.js', depends=[jquery])
from z3c.wizard.interfaces import IStep

from megrok.z3cform.wizard import z3cWizard

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


class INewUnfallanzeige(IUnfallanzeige):
    pass


class Unfallanzeige(Content):
    """ContentType fuer das Lastschriftverfahren"""
    schema(INewUnfallanzeige)
    grok.name('unfallanzeige')


class StartWizard(grok.View):
    grok.implements(z3cwizard.IWizard)
    grok.context(IUnfallanzeigeFolder)

    def update(self):
        self.uaz = uaz = Unfallanzeige()
        self.context.add(uaz)

    def render(self):
        self.redirect(self.url(self.uaz, 'uazwizard'))


class UazWizard(z3cwizard.WizardForm):
    """ Wizard form."""
    grok.context(IUnfallanzeige)

    label = u'Unfallanzeige'

    def setUpSteps(self):
        return [
            step.addStep(self, 'basic', weight=1),
            step.addStep(self, 'job', weight=2),
            ]


class Basic(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = u'Basic Information'
    form_name = u'Basic Information'

    fields = Fields(IUnfallanzeige).select(
       'unfustdor', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')

    def update(self):
        z3cWizard.need()
        z3cwizard.PageStep.update(self)


class Job(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = u'Basic Information'
    form_name = u'Basic Information'

    fields = Fields(IUnfallanzeige).select(
        'uadbru', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

    def update(self):
        z3cWizard.need()
        z3cwizard.PageStep.update(self)


