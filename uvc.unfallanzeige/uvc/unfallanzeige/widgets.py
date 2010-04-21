# -*- coding: utf-8 -*-

import grok
import megrok.z3cform.base as z3cform

from zope.interface import Interface, implements
from zope.component import getMultiAdapter
from zope.traversing.browser.absoluteurl import absoluteURL
import zope.component
import zope.interface
import zope.schema
import zope.schema.interfaces
from zope.i18n import translate

from z3c.form import interfaces
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

    def update(self):
        """See z3c.form.interfaces.IWidget."""        
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
