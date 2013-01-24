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
  >>> from zope.app.component.hooks import getSite, setSite
  >>> from zope.app.authentication.principalfolder import PrincipalInfo, Principal

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


Anlegen einer Unfallanzeige
---------------------------

  >>> import uvcsite
  >>> from zope import component
  >>> from zope.contentprovider.interfaces import IContentProvider

Für den Wizard brachen wir zuerst ein Object um auf diesem die steps auszufürhen
Zunächst holen wir uns den HomeFolder,

  >>> from zope.app.homefolder.interfaces import IHomeFolder
  >>> homeFolder = IHomeFolder(klaus).homeFolder
  >>> homeFolder
  <uvcsite.homefolder.homefolder.HomeFolder object at ...>

in diesem sollte ein ProductFolder 'unfallanzeigen' liegen,

  >>> unfallanzeigen = homeFolder.get('unfallanzeigen')
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

  >>> view = component.getMultiAdapter((unfallanzeigen, request), name=u"startwizard")
  >>> view.update()

  >>> len(unfallanzeigen)
  1

  >>> unfallanzeige = unfallanzeigen.get('Unfallanzeige')
  >>> unfallanzeige
  <uvc.unfallanzeige.uazwizard.Unfallanzeige object at 0...>


Der Wizard
----------

Auf unserem unfallanzeige Object sollten wir nun den Wizard View ausführen können

  >>> wizard = component.getMultiAdapter((unfallanzeige, request), name=u"unfallanzeigewizard")
  >>> wizard
  <UnfallanzeigeWizard 'unfallanzeigewizard'>

Der Wizard sollte sieben Seiten haben

  >>> len(wizard.steps)
  7

Step1
-----

Zunächst holen wir den Step direkt vom Wizard

  >>> step1 = wizard.steps[0]
  >>> step1
  <Basic 'basic'>



Cleanup
-------
  >>> zope.security.management.endInteraction()
