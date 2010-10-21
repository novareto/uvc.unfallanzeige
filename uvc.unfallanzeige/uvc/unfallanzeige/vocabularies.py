
import grok
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from uvc.unfallanzeige import UvcUnfallanzeigeMessageFactory as _


def vocabulary(*terms):
    """ """
    return SimpleVocabulary([SimpleTerm(value, token, title) for value, token, title in terms])


class Uadbru1Sources(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.name(u'uvc.uadbru1')
    
    def __call__(self, context):
        return vocabulary(('Hausmeister', 'Hausmeister', 'Hausmeister'),
                          ('Drucker', 'Drucker', 'Druker'),
                          ('Bildhauer', 'Bildhauer', 'Bildhauer'))
        

class UnfuteSources(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.name(u'uvc.unfute')
    
    def __call__(self, context):
        return vocabulary(('Verwaltung', 'Verwaltung', 'Verwaltung')
                          ('Druckerei', 'Druckerei', 'Druckerei')
                          ('Schreinerei', 'Schreinerei', 'Schreinerei'))


class StaSources(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.name(u'uvc.sta')

    def __call__(self, context):
        return vocabulary((
                          ('001', 'Deutschland',_(u'label_deutschland')),
                          ('010','Albanien',_(u'label_albanien')),
                          ('011','Belgien',_(u'label_belgien')),
                          ('012','Bulgarien',_(u'label_bulgarien')),
                          ('013','Daenemark',_(u'label_daenemark')),
                          ('014','Finnland',_(u'label_finnland')),
                          ('015','Frankreich',_(u'label_frankreich')),
                          ('016','Griechenland',_(u'label_griechenland')),
                          ('017','Grossbritannien und Nordirland',_(u'label_grossbritannien')),
                          ('018','Irland',_(u'label_irland')),
                          ('019','Island',_(u'label_island')),
                          ('020','Italien',_(u'label_italien')),
                          ('022','Luxemburg',_(u'label_luxemburg')),
                          ('023','Niederlande',_(u'label_niederlande')),
                          ('024','Norwegen',_(u'label_norwegen')),
                          ('025','Oesterreich',_(u'label_oesterreich')),
                          ('026','Polen',_(u'label_polen')),
                          ('027','Portugal',_(u'label_portugal')),
                          ('028','Rumaenien',_(u'label_rumaenien')),
                          ('029','Schweden',_(u'label_schweden')),
                          ('030','Schweiz',_(u'label_schweiz')),
                          ('031','Armenien',_(u'label_armenien')),
                          ('031','Aserbaidschan',_(u'label_aserbaidschan')),
                          ('031','Belarus',_(u'label_belarus')),
                          ('031','Georgien',_(u'label_georgien')),
                          ('031','Kasachstan',_(u'label_kasachstan')),
                          ('031','Kirgisistan',_(u'label_kirgisistan')),
                          ('031','Moldawien',_(u'label_moldawien')),
                          ('031','Russland',_(u'label_russland')),
                          ('031','Tadschikistan',_(u'label_tadschikistan')),
                          ('031','Turkmenistan',_(u'label_turkmenistan')),
                          ('031','Ukraine',_(u'label_ukraine')),
                          ('031','Usbekistan',_(u'label_usbekistan')),
                          ('032','Spanien',_(u'label_spanien')),
                          ('033','Tschechien',_(u'label_tschechien')),
                          ('033','Slowakei',_(u'label_slowakei')),
                          ('034','Tuerkei',_(u'label_tuerkei')),
                          ('035','Ungarn',_(u'label_ungarn')),
                          ('036','Lettland',_(u'label_lettland')),
                          ('036','Litauen',_(u'label_litauen')),
                          ('036','Estland',_(u'label_estland')),
                          ('037','Malta',_(u'label_malta')),
                          ('038','Zypern',_(u'label_zypern')),
                          ('039','Bosnien',_(u'label_bosnien')),
                          ('040','Kroatien',_(u'label_kroatien')),
                          ('041','Mazedonien',_(u'label_mazedonien')),
                          ('042','Serbien',_(u'label_serbien')),
                          ('043','Slowenien',_(u'label_slowenien')),
                          ('050','Aegypten',_(u'label_aegypten')),
                          ('051','Algerien',_(u'label_algerien')),
                          ('052','Ghana',_(u'label_ghana')),
                          ('053','Marokko',_(u'label_marokko')),
                          ('054','Nigeria',_(u'label_nigeria')),
                          ('055','Suedafrika',_(u'label_suedafrika')),
                          ('056','Tunesien',_(u'label_tunesien')),
                          ('060','Argentinen',_(u'label_argentinien')),
                          ('061','Brasilien',_(u'label_brasilien')),
                          ('062','Chile',_(u'label_chile')),
                          ('063','Kanada',_(u'label_kanada')),
                          ('064','Mexiko',_(u'label_mexiko')),
                          ('065','Peru',_(u'label_peru')),
                          ('066','USA',_(u'label_usa')),
                          ('070','China',_(u'label_china')),
                          ('071','Indien',_(u'label_indien')),
                          ('072','Indonesien',_(u'label_indonesien')),
                          ('073','Irak',_(u'label_irak')),
                          ('074','Israel',_(u'label_israel')),
                          ('075','Japan',_(u'label_japan')),
                          ('076','Jordanien',_(u'label_jordanien')),
                          ('077','Pakistan',_(u'label_pakistan')),
                          ('078','Iran',_(u'label_iran')),
                          ('089','Australien',_(u'label_australien')),
                          ('099', 'sonstiges',_(u'label_sonstiges')),
                          ))
