# -*- coding: utf-8 -*-

from zope.schema import Choice
from zope.interface import Interface, directlyProvides


class IAlternativeChoice(Interface):
    pass


class OptionalChoice(Choice):
    """A choice field with the option to add an alternative value
    """
    def __init__(self, values=None, vocabulary=None,
                 source=None, alternative=False, **kw):
        Choice.__init__(self, values, vocabulary, source, **kw)
        self.alternative = alternative
        if alternative is True:
            directlyProvides(self, IAlternativeChoice)

    def _validate(self, value):

        #import pdb
        #pdb.set_trace()
        
        # Pass all validations during initialization
        if self._init_field:
            return
        
        #super(OptionalChoice, self)._validate(value)
        if not self.alternative:
            vocabulary = self.vocabulary
            if vocabulary is None:
                vr = getVocabularyRegistry()
                try:
                    vocabulary = vr.get(None, self.vocabularyName)
                except VocabularyRegistryError:
                    raise ValueError("Can't validate value without vocabulary")
                if value not in vocabulary:
                    raise ConstraintNotSatisfied(value)
