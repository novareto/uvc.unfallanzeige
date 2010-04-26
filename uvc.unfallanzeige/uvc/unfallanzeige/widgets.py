# -*- coding: utf-8 -*-

import grok
import megrok.z3cform.base as z3cform
import zope.schema
import zope.component

from zope.interface import Interface, implements
from zope.component import getMultiAdapter
from zope.traversing.browser.absoluteurl import absoluteURL
import zope.component
import zope.interface
import zope.schema
import zope.schema.interfaces
from zope.i18n import translate
from uvc.unfallanzeige.resources import optchoice

from z3c.form import interfaces
from z3c.form.converter import SequenceDataConverter
from z3c.form.i18n import MessageFactory as _
from z3c.form.browser import widget
from z3c.form.browser import select
from z3c.form.interfaces import ISelectWidget
from fields import IAlternativeChoice


class INonExclusiveSelect(ISelectWidget):
    """A widget that renders a choice as a select box with
    the possibility to input something else.
    """


class NonExclusiveSelect(select.SelectWidget):
    """A widget for a named file object
    """
    klass = u'alternative-choice-widget'
    implements(INonExclusiveSelect)

    def extract(self, default=interfaces.NO_VALUE):
        """See z3c.form.interfaces.IWidget."""
        #print "EXTRACT", self.name
        #import pdb; pdb.set_trace()
        if (self.name not in self.request and
            self.name+'-empty-marker' in self.request):
            return []
        value = self.request.get(self.name, default)
        if value != default:
            if not isinstance(value, (tuple, list)):
                value = (value,)
            # do some kind of validation, at least only use existing values
            for token in value:
                if token == self.noValueToken:
                    continue
                try:
                    self.terms.getTermByToken(token)
                except LookupError:
                    return value
        return value

    def update(self):
        """See z3c.form.interfaces.IWidget."""
        optchoice.need()
        super(select.SelectWidget, self).update()
        anothervalue = True
        
        widget.addFieldClass(self)
        self.items = []
        if (not self.required or self.prompt) and self.multiple is None:
            message = self.noValueMessage
            if self.prompt:
                message = self.promptMessage
            self.items.append({
                'id': self.id + '-novalue',
                'value': self.noValueToken,
                'content': message,
                'selected': self.value == []
                })

        for count, term in enumerate(self.terms):
            selected = self.isSelected(term)
            id = '%s-%i' % (self.id, count)
            content = term.token
            if self.value and content == self.value:
                anothervalue = False
            if zope.schema.interfaces.ITitledTokenizedTerm.providedBy(term):
                content = translate(
                    term.title, context=self.request, default=term.title)
            self.items.append(
                {'id':id, 'value':term.token, 'content':content,
                 'selected':selected})

        if self.value and anothervalue is True:
            count += 1
            self.items.append(
                {'id': '%s-%i' % (self.id, count),
                 'value':self.value,
                 'content':self.value,
                 'selected': True})


class AltChoiceWidgetInput(z3cform.WidgetTemplate):
    grok.context(Interface)
    grok.layer(z3cform.IFormLayer)
    grok.template('templates/input.pt')
    z3cform.directives.field(IAlternativeChoice)
    z3cform.directives.widget(INonExclusiveSelect)
    z3cform.directives.mode(z3cform.INPUT_MODE)


@grok.adapter(IAlternativeChoice, z3cform.IFormLayer)
@grok.implementer(z3cform.IFieldWidget)
def FileFieldWidget(field, request):
    """IFieldWidget factory for FileWidget."""
    return z3cform.FieldWidget(field, NonExclusiveSelect(request))


class SequenceDataConverter(grok.MultiAdapter, SequenceDataConverter):
    """Basic data converter for ISequenceWidget."""
    grok.adapts(IAlternativeChoice, INonExclusiveSelect)

    def toWidgetValue(self, value):
        """Convert from Python bool to HTML representation."""
        widget = self.widget
        # if the value is the missing value, then an empty list is produced.
        if value is self.field.missing_value:
            return []
        return [value]

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        widget = self.widget
        if not len(value) or value[0] == widget.noValueToken:
            return self.field.missing_value
        return value[0]
