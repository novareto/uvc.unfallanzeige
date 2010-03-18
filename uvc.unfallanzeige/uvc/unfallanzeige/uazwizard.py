import grok

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


from zope.app.security.interfaces import IUnauthenticatedPrincipal
from zope.interface import Interface
from zope.traversing.browser import absoluteURL
from megrok.z3cform import wizard as z3cwizard
from z3c.wizard import wizard, step
from zope.schema.fieldproperty import FieldProperty


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


class Unfallanzeige(Content):
    """ContentType fuer das Lastschriftverfahren"""
    grok.implements(IUnfallanzeige)
    grok.name('unfallanzeige')

    unfustdor = FieldProperty(IUnfallanzeige['unfustdor'])
    unfustrasse = FieldProperty(IUnfallanzeige['unfustrasse'])
    unfunr = FieldProperty(IUnfallanzeige['unfunr'])
    unfuplz = FieldProperty(IUnfallanzeige['unfuplz'])
    unfuort = FieldProperty(IUnfallanzeige['unfuort'])
    anspname = FieldProperty(IUnfallanzeige['anspname'])
    anspfon = FieldProperty(IUnfallanzeige['anspfon'])
    uadbru = FieldProperty(IUnfallanzeige['uadbru'])
    uadst = FieldProperty(IUnfallanzeige['uadst'])
    unfute = FieldProperty(IUnfallanzeige['unfute'])
    unflar = FieldProperty(IUnfallanzeige['unflar'])
    unvlaraddr = FieldProperty(IUnfallanzeige['unvlaraddr'])

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

    fields = Fields(IUnfallanzeige).select(
       'unfustdor', 'unfustrasse', 'unfunr',
        'unfuplz', 'unfuort', 'anspname', 'anspfon')


class Job(z3cwizard.PageStep):
    grok.context(UazWizard)
    label = u'Basic Information'

    fields = Fields(IUnfallanzeige).select(
        'uadbru', 'uadst', 'unfute', 'unflar', 'unvlaraddr')

