import grok
from z3c.form import field
from megrok.z3cform.base import IGrokForm
from zope.i18n import translate
from zope.i18nmessageid import Message
from zope.security.proxy import removeSecurityProxy
from zope.component import getMultiAdapter
from zope.traversing.interfaces import ITraversable
from zope.publisher.interfaces.http import IHTTPRequest


class Errors(dict):
    
    def add(self, key, value, request):
        if isinstance(value, Message):
            value = translate(value, context=request)
        self[key] = value


class InlineValidation(grok.MultiAdapter):
    grok.provides(ITraversable)
    grok.name('validate')
    grok.adapts(IGrokForm, IHTTPRequest)

    def __init__(self, context, request):
        self.form = removeSecurityProxy(context)
        self.request = request

    def check(self):
        return True

    def update(self):
        self.form.update()
        self.form.updateWidgets()
        self.data, self.errors = self.form.extractData()

    def validate(self, fieldnames, fieldset=None):
        errors = Errors()
        if fieldset is not None:
            form = self.form.groups[fieldset]
        else:
            form = self.form
            
        for fieldname in fieldnames:
            for error in self.errors:
                if error.widget == form.widgets[fieldname]:
                    errors.add(fieldname, error.message, self.request)
                    break
        return errors

    def traverse(self, name, ignore):
        if not self.check() or not name:
            return ValueError
        self.update()
        return getMultiAdapter((self, self.request), name=name)


class Validators(grok.JSON):
    grok.context(InlineValidation)

    def fieldset(self, fieldset):
        """Valides a given fieldset
        """
        pass

    def field(self, fieldname, fieldset=None):
        wprefix = self.context.form.widgets.prefix
        fprefix = self.context.form.prefix

        remove = len(fprefix) + len(wprefix)
        prefixless = fieldname[remove:]
        errors = self.context.validate([prefixless, ])
        return errors
