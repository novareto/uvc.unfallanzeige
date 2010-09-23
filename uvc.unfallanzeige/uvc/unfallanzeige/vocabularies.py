
import grok
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def vocabulary(terms):
    """ """
    return SimpleVocabulary([SimpleTerm(title, title, title) for title in terms])


class Uadbru1Sources(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.name(u'uvc.uadbru1')
    
    def __call__(self, context):
        return vocabulary(('Hausmeister', 'Drucker', 'Bildhauer'))
        

class UnfuteSources(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.name(u'uvc.unfute')
    
    def __call__(self, context):
        return vocabulary(('Verwaltung', 'Druckerei', 'Schreinerei'))
