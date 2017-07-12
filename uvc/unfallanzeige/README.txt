=======
Doctest
=======

uvc.unfallanzeige

:Test-Layer: functional

Setup
-----

Wir beginnen damit uns eine Beispiel uvcsite aufzubauen.

  >>> import zope.security
  >>> from zope.publisher.browser import TestRequest
  >>> from zope.component.hooks import getSite, setSite
  >>> from zope.pluggableauth.factories import Principal

  >>> request = TestRequest()
  >>> klaus = Principal('klaus', 'klaus', 'klaus')
  >>> request.setPrincipal(klaus)
  >>> zope.security.management.newInteraction(request)

  >>> root = getRootFolder()
  >>> from uvcsite.app import Uvcsite
  >>> root['extranet'] = app = Uvcsite()
  >>> setSite(root['extranet'])
  >>> app
  <uvcsite.app.Uvcsite object at 0...>


Product Registration

  >>> import uvcsite
  >>> import grok 
  >>> class UnfallanzeigeRegistration(uvcsite.ProductRegistration):
  ...     grok.name('Unfallanzeige')
  ...     grok.title('Unfallanzeige')
  ...     grok.description(u'Bitte klicken Sie hier um eine .')
  ...     grok.order(50)
  ...     uvcsite.productfolder('uvc.unfallanzeige.uazwizard.Unfallanzeigen')
  ...     icon = "fanstatic/guv.unfallanzeige/unfallanzeige.gif"
  ...     def action(self):
  ...         return "%sUnfallanzeigen/@@add" % (uvcsite.getHomeFolderUrl(self.request))
  >>> from grokcore.component.testing import grok_component
  >>> grok_component('UnfallanzeigeRegistration', UnfallanzeigeRegistration)
  True


Anlegen einer Unfallanzeige
---------------------------

  >>> import uvcsite
  >>> from zope import component

Für den Wizard brachen wir zuerst ein Object um auf diesem die steps auszufürhen
Zunächst holen wir uns den HomeFolder,

  >>> from zope.app.homefolder.interfaces import IHomeFolder
  >>> homeFolder = IHomeFolder(klaus).homeFolder
  >>> homeFolder
  <uvcsite.homefolder.homefolder.HomeFolder object at ...>

in diesem sollte ein ProductFolder 'unfallanzeigen' liegen,

  >>> unfallanzeigen = homeFolder.get('Unfallanzeigen')
  >>> unfallanzeigen 
  <uvc.unfallanzeige.uazwizard.Unfallanzeigen object at ...>

welcher noch keinen Inhalt hat,

  >>> len(unfallanzeigen)
  0

Hier vergewissern wir uns, dass das richtige Interface geladen wird.

  >>> from uvc.unfallanzeige.interfaces import IUnfallanzeigenFolder
  >>> IUnfallanzeigenFolder.providedBy(unfallanzeigen)
  True

Der View Start Wizard legt uns die Unfallanzeige an.

  >>> view = component.getMultiAdapter((unfallanzeigen, request), name=u"add")
  >>> view.update()

  >>> len(unfallanzeigen)
  1

  >>> unfallanzeige = unfallanzeigen.get('Unfallanzeige')
  >>> unfallanzeige
  <uvc.unfallanzeige.uazwizard.Unfallanzeige object at 0...>


Der Wizard
----------

Auf unserem unfallanzeige Object sollten wir nun den Wizard View ausführen können

  >>> wizard = component.getMultiAdapter((unfallanzeige, request), name=u"edit")
  >>> wizard
  <uvc.unfallanzeige.uazwizard.UnfallanzeigeWizard object at...>

Der Wizard sollte sieben Seiten haben
  >>> wizard.getMaximumStepId()
  6
  >>> len(wizard._getAvailableSubForms())
  7

  >>> step1, step2, step3, step4, step5, step6, step7 = wizard._getAvailableSubForms()

Step1
-----

Zunächst holen wir die Instanz des 1. Steps direkt vom Wizard.

  >>> step1
  <uvc.unfallanzeige.steps.Basic object at 0...>

Anschließend wird die updateForm Methode aufgerufen um den Wizard zu initialisieren

  >>> wizard.updateForm()

Vorbereiten des Requests...

  >>> request.method = "POST"
  >>> request.form = {
  ...    'form.action.weiter': 'Weiter', 
  ...    'form.field.step': '0', 
  ...    'form.basic.field.title': u'Unfallanzeige',
  ...    'form.basic.field.unfustdor': u'In einer Zweigniederlassung',
  ...    'form.basic.field.anspfon': u'09841 3644',
  ...    'form.basic.field.anspname': u'',
  ...    'form.basic.field.unfuort': u''
  ...    }

Ausführen/Absenden des Requests

  >>> pr = wizard.actions.process(wizard, request)

Gab es Fehler? Wie sehen die Daten aus.

  >>> values, errors = step1.extractData()

Es sollte einen Fehler geben für das Feld unfort da der Mitarbeiter in einer
Zweigniederlassung arbeitet

  >>> 'form.basic.field.unfuort' in errors.keys()
  True

Der Name des Ansprechpartners ist ein Pflichtfeld und soll ausgefüllt werden

  >>> 'form.basic.field.anspname' in errors.keys()
  True

  >>> step1.__extracted = None 
  >>> wizard.__extracted = None 

  >>> request.form = {
  ...    'form.action.weiter': 'Weiter', 
  ...    'form.field.step': '0', 
  ...    'form.basic.field.title': u'Unfallanzeige',
  ...    'form.basic.field.unfustdor': u'In einer Zweigniederlassung',
  ...    'form.basic.field.anspfon': u'09841 3644',
  ...    'form.basic.field.anspname': u'Christian Klinger',
  ...    'form.basic.field.unfuort': u''
  ...    }


Ausführen/Absenden des Requests

  >>> pr = wizard.actions.process(wizard, request)

Gab es Fehler? Wie sehen die Daten aus.

  >>> values, errors = step1.extractData()

  >>> 'form.basic.field.anspname' in errors.keys()
  False 


Cleanup
-------
  >>> zope.security.management.endInteraction()
