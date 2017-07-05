# -*- coding: utf-8 -*-

import grok
import uvcsite
import zope.security.management
import zope.security.interfaces
import zope.publisher.interfaces

from zope.interface import Interface
from zope.component import getMultiAdapter, queryMultiAdapter
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from uvc.unfallanzeige import UvcUnfallanzeigeMessageFactory as _


def vocabulary(*terms):
    """ """
    return SimpleVocabulary([SimpleTerm(value, token, title) for value, token, title in terms])


def vocabulary_list(terms):
    return SimpleVocabulary([SimpleTerm(value, token, title) for value, token, title in terms])


class IMultiSource(Interface):
    pass


class DefaultUadbru1Sources(grok.MultiAdapter):
    grok.provides(IMultiSource)
    grok.adapts(Interface, zope.publisher.interfaces.IRequest)
    grok.name('uvc.uadbru1')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, context):
        return vocabulary(('Hausmeister', 'Hausmeister', 'Hausmeister'),
                          ('Drucker', 'Drucker', 'Druker'),
                          ('Bildhauer', 'Bildhauer', 'Bildhauer'))


class DefaultUnfuteSources(grok.MultiAdapter):
    grok.provides(IMultiSource)
    grok.adapts(Interface, zope.publisher.interfaces.IRequest)
    grok.name(u'uvc.unfute')

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self, context):
        return vocabulary(('Verwaltung', 'Verwaltung', 'Verwaltung'),
                          ('Druckerei', 'Druckerei', 'Druckerei'),
                          ('Schreinerei', 'Schreinerei', 'Schreinerei'))



class DefaultLkzSources(grok.MultiAdapter):
    grok.provides(IMultiSource)
    grok.adapts(Interface, zope.publisher.interfaces.IRequest)
    grok.name(u'uvc.lkz')

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self, context):
        return vocabulary(
                  ('D', 'Deutschland', _(u'label_lkz_Deutschland')),
                  ('A', 'Oesterreich', _(u'label_lkz_Oesterreich')),
                  ('AAA', 'unbekannt', _(u'label_lkz_unbekannt')),
                  ('ADN', 'Jemen', _(u'label_lkz_Jemen')),
                  ('AFG', 'Afghanistan', _(u'label_lkz_Afghanistan')),
                  ('AGO', 'Angola', _(u'label_lkz_Angola')),
                  ('AL', 'Albanien', _(u'label_lkz_Albanien')),
                  ('AND', 'Andorra', _(u'label_lkz_Andorra')),
                  ('ANT', 'Antigua', _(u'label_lkz_Antigua')),
                  ('AUS', 'Australien', _(u'label_lkz_Australien')),
                  ('B', 'Belgien', _(u'label_lkz_Belgien')),
                  ('BD', 'Bangla', _(u'label_lkz_Bangla')),
                  ('BDS', 'Barbados', _(u'label_lkz_Barbados')),
                  ('BG', 'Bulgarien', _(u'label_lkz_Bulgarien')),
                  ('BH', 'Belize', _(u'label_lkz_Belize')),
                  ('BHT', 'Bhutan', _(u'label_lkz_Bhutan')),
                  ('BIO', 'Malediven', _(u'label_lkz_Malediven')),
                  ('BOL', 'Bolivien', _(u'label_lkz_Bolivien')),
                  ('BOS', 'Bosnien-Herzegowina', _(u'label_lkz_Bosnien-Herzegowina')),
                  ('BR', 'Brasilien', _(u'label_lkz_Brasilien')),
                  ('BRN', 'Bahrein', _(u'label_lkz_Bahrein')),
                  ('BRU', 'Brunai', _(u'label_lkz_Brunai')),
                  ('BS', 'Bahamas', _(u'label_lkz_Bahamas')),
                  ('BUR', 'Birma', _(u'label_lkz_Birma')),
                  ('BY', 'Weissrussland', _(u'label_lkz_Weissrussland')),
                  ('C', 'Kuba', _(u'label_lkz_Kuba')),
                  ('CAM', 'Kamerun', _(u'label_lkz_Kamerun')),
                  ('CDN', 'Kanada', _(u'label_lkz_Kanada')),
                  ('CH', 'Schweiz', _(u'label_lkz_Schweiz')),
                  ('CHD', 'Tschad', _(u'label_lkz_Tschad')),
                  ('CI', 'Elfenbeinkueste', _(u'label_lkz_Elfenbeinkueste')),
                  ('CL', 'Sri', _(u'label_lkz_Sri')),
                  ('CO', 'Kolumbien', _(u'label_lkz_Kolumbien')),
                  ('CR', 'Costa', _(u'label_lkz_Costa')),
                  ('CY', 'Zypern', _(u'label_lkz_Zypern')),
                  ('CZ', 'Tschechische', _(u'label_lkz_Tschechische')),
                  ('DCM', 'Dominikanische', _(u'label_lkz_Dominikanische')),
                  ('DK', 'Daenemark', _(u'label_lkz_Daenemark')),
                  ('DY', 'Benin', _(u'label_lkz_Benin')),
                  ('DZ', 'Algerien', _(u'label_lkz_Algerien')),
                  ('E', 'Spanien', _(u'label_lkz_Spanien')),
                  ('EAK', 'Kenia', _(u'label_lkz_Kenia')),
                  ('EAT', 'Tansania', _(u'label_lkz_Tansania')),
                  ('EAU', 'Uganda', _(u'label_lkz_Uganda')),
                  ('EAZ', 'Sansibar', _(u'label_lkz_Sansibar')),
                  ('EC', 'Ecuador', _(u'label_lkz_Ecuador')),
                  ('ES', 'El', _(u'label_lkz_El')),
                  ('ET', 'Aegypten', _(u'label_lkz_Aegypten')),
                  ('ETH', 'Aethiopien', _(u'label_lkz_Aethiopien')),
                  ('EW', 'Estland', _(u'label_lkz_Estland')),
                  ('F', 'Frankreich', _(u'label_lkz_Frankreich')),
                  ('FAL', 'Falklandinseln', _(u'label_lkz_Falklandinseln')),
                  ('FIN', 'Finnland', _(u'label_lkz_Finnland')),
                  ('FJI', 'Fidshi', _(u'label_lkz_Fidshi')),
                  ('FL', 'Liechtenstein', _(u'label_lkz_Liechtenstein')),
                  ('FR', 'Faroeer', _(u'label_lkz_Faroeer')),
                  ('FSM', 'Mikronesien,', _(u'label_lkz_Mikronesien,')),
                  ('GAB', 'Gabun', _(u'label_lkz_Gabun')),
                  ('GB', 'Grossbritannien', _(u'label_lkz_Grossbritannien')),
                  ('GBA', 'Alderney', _(u'label_lkz_Alderney')),
                  ('GBG', 'Guernsey', _(u'label_lkz_Guernsey')),
                  ('GBJ', 'Jersey', _(u'label_lkz_Jersey')),
                  ('GBM', 'Insel', _(u'label_lkz_Insel')),
                  ('GBZ', 'Gibraltar', _(u'label_lkz_Gibraltar')),
                  ('GCA', 'Guatemala', _(u'label_lkz_Guatemala')),
                  ('GEO', 'Georgien', _(u'label_lkz_Georgien')),
                  ('GH', 'Ghana', _(u'label_lkz_Ghana')),
                  ('GR', 'Griechenland', _(u'label_lkz_Griechenland')),
                  ('GUY', 'Guyana', _(u'label_lkz_Guyana')),
                  ('H', 'Ungarn', _(u'label_lkz_Ungarn')),
                  ('HCA', 'Honduras', _(u'label_lkz_Honduras')),
                  ('HK', 'Hongkong', _(u'label_lkz_Hongkong')),
                  ('HR', 'Kroatien', _(u'label_lkz_Kroatien')),
                  ('HV', 'Burkina', _(u'label_lkz_Burkina')),
                  ('I', 'Italien', _(u'label_lkz_Italien')),
                  ('IL', 'Israel', _(u'label_lkz_Israel')),
                  ('IND', 'Indien', _(u'label_lkz_Indien')),
                  ('IR', 'Iran', _(u'label_lkz_Iran')),
                  ('IRL', 'Irland', _(u'label_lkz_Irland')),
                  ('IRQ', 'Iraq', _(u'label_lkz_Iraq')),
                  ('IS', 'Island', _(u'label_lkz_Island')),
                  ('J', 'Japan', _(u'label_lkz_Japan')),
                  ('JA', 'Jamaika', _(u'label_lkz_Jamaika')),
                  ('JOR', 'Jordanien', _(u'label_lkz_Jordanien')),
                  ('K', 'Kambodscha', _(u'label_lkz_Kambodscha')),
                  ('KAS', 'Kasachstan', _(u'label_lkz_Kasachstan')),
                  ('KIS', 'Kirgisistan', _(u'label_lkz_Kirgisistan')),
                  ('KWT', 'Kuweit', _(u'label_lkz_Kuweit')),
                  ('L', 'Luxemburg', _(u'label_lkz_Luxemburg')),
                  ('LAO', 'Laos', _(u'label_lkz_Laos')),
                  ('LAR', 'Libyen', _(u'label_lkz_Libyen')),
                  ('LB', 'Liberia', _(u'label_lkz_Liberia')),
                  ('LS', 'Lesotho', _(u'label_lkz_Lesotho')),
                  ('LT', 'Litauen', _(u'label_lkz_Litauen')),
                  ('LV', 'Lettland', _(u'label_lkz_Lettland')),
                  ('M', 'Malta', _(u'label_lkz_Malta')),
                  ('MA', 'Marokko', _(u'label_lkz_Marokko')),
                  ('MAK', 'Makedonien', _(u'label_lkz_Makedonien')),
                  ('MAL', 'Malaysia', _(u'label_lkz_Malaysia')),
                  ('MAO', 'Oman', _(u'label_lkz_Oman')),
                  ('MC', 'Monaco', _(u'label_lkz_Monaco')),
                  ('MEX', 'Mexiko', _(u'label_lkz_Mexiko')),
                  ('MNE', 'Montenegro', _(u'label_lkz_Montenegro')),
                  ('MOL', 'Moldawien', _(u'label_lkz_Moldawien')),
                  ('MOZ', 'Mozambik', _(u'label_lkz_Mozambik')),
                  ('MS', 'Mauritius', _(u'label_lkz_Mauritius')),
                  ('MW', 'Malawi', _(u'label_lkz_Malawi')),
                  ('N', 'Norwegen', _(u'label_lkz_Norwegen')),
                  ('NA', 'Curacao', _(u'label_lkz_Curacao')),
                  ('NAU', 'Nauru', _(u'label_lkz_Nauru')),
                  ('NEP', 'Nepal', _(u'label_lkz_Nepal')),
                  ('NIC', 'Nicaragua', _(u'label_lkz_Nicaragua')),
                  ('NL', 'Niederlande', _(u'label_lkz_Niederlande')),
                  ('NZ', 'Neuseeland', _(u'label_lkz_Neuseeland')),
                  ('O', 'Neue', _(u'label_lkz_Neue')),
                  ('P', 'Portugal', _(u'label_lkz_Portugal')),
                  ('PA', 'Panama', _(u'label_lkz_Panama')),
                  ('PAK', 'Pakistan', _(u'label_lkz_Pakistan')),
                  ('PE', 'Peru', _(u'label_lkz_Peru')),
                  ('PL', 'Polen', _(u'label_lkz_Polen')),
                  ('PNG', 'Papua-Neuguinea', _(u'label_lkz_Papua-Neuguinea')),
                  ('PY', 'Paraguay', _(u'label_lkz_Paraguay')),
                  ('QAT', 'Katar', _(u'label_lkz_Katar')),
                  ('RA', 'Argentinien', _(u'label_lkz_Argentinien')),
                  ('RB', 'Botswana', _(u'label_lkz_Botswana')),
                  ('RC', 'Taiwan', _(u'label_lkz_Taiwan')),
                  ('RCA', 'Zentralafrikanische', _(u'label_lkz_Zentralafrikanische')),
                  ('RCB', 'Kongo', _(u'label_lkz_Kongo')),
                  ('RCH', 'Chile', _(u'label_lkz_Chile')),
                  ('RG', 'Guinea', _(u'label_lkz_Guinea')),
                  ('RH', 'Haiti', _(u'label_lkz_Haiti')),
                  ('RI', 'Indonesien', _(u'label_lkz_Indonesien')),
                  ('RIM', 'Mauretanien', _(u'label_lkz_Mauretanien')),
                  ('RL', 'Libanon', _(u'label_lkz_Libanon')),
                  ('RM', 'Madagaskar', _(u'label_lkz_Madagaskar')),
                  ('RMM', 'Mali', _(u'label_lkz_Mali')),
                  ('RN', 'Niger', _(u'label_lkz_Niger')),
                  ('RO', 'Rumaenien', _(u'label_lkz_Rumaenien')),
                  ('ROK', 'Korea', _(u'label_lkz_Korea')),
                  ('ROU', 'Uruguay', _(u'label_lkz_Uruguay')),
                  ('RP', 'Philippinen', _(u'label_lkz_Philippinen')),
                  ('RSM', 'San', _(u'label_lkz_San')),
                  ('RU', 'Burundi', _(u'label_lkz_Burundi')),
                  ('RUS', 'Russland', _(u'label_lkz_Russland')),
                  ('RWA', 'Ruanda', _(u'label_lkz_Ruanda')),
                  ('S', 'Schweden', _(u'label_lkz_Schweden')),
                  ('SAU', 'Saudi-Arabien', _(u'label_lkz_Saudi-Arabien')),
                  ('SCN', 'St.', _(u'label_lkz_St.')),
                  ('SD', 'Swasiland', _(u'label_lkz_Swasiland')),
                  ('SGP', 'Singapur', _(u'label_lkz_Singapur')),
                  ('SK', 'Slowakische', _(u'label_lkz_Slowakische')),
                  ('SLO', 'Slowenien', _(u'label_lkz_Slowenien')),
                  ('SME', 'Surinam', _(u'label_lkz_Surinam')),
                  ('SN', 'Senegal', _(u'label_lkz_Senegal')),
                  ('SOL', 'Salomonen', _(u'label_lkz_Salomonen')),
                  ('SP', 'Somalia', _(u'label_lkz_Somalia')),
                  ('SRB', 'Serbien', _(u'label_lkz_Serbien')),
                  ('STP', 'Sao', _(u'label_lkz_Sao')),
                  ('SUD', 'Sudan', _(u'label_lkz_Sudan')),
                  ('SWA', 'Namibia', _(u'label_lkz_Namibia')),
                  ('SY', 'Seychellen', _(u'label_lkz_Seychellen')),
                  ('SYR', 'Syrien', _(u'label_lkz_Syrien')),
                  ('T', 'Thailand', _(u'label_lkz_Thailand')),
                  ('TAD', 'Tadschikistan', _(u'label_lkz_Tadschikistan')),
                  ('TG', 'Togo', _(u'label_lkz_Togo')),
                  ('TJ', 'China', _(u'label_lkz_China')),
                  ('TMN', 'Turkmenistan', _(u'label_lkz_Turkmenistan')),
                  ('TN', 'Tunesien', _(u'label_lkz_Tunesien')),
                  ('TR', 'Tuerkei', _(u'label_lkz_Tuerkei')),
                  ('TT', 'Trinidad', _(u'label_lkz_Trinidad')),
                  ('UA', 'Ukraine', _(u'label_lkz_Ukraine')),
                  ('UAE', 'Vereinigte UAE', _(u'label_lkz_Vereinigte')),
                  ('USA', 'Vereinigte USA', _(u'label_lkz_VereinigteStaaten')),
                  ('USB', 'Usbekistan', _(u'label_lkz_Usbekistan')),
                  ('V', 'Vatikanstadt', _(u'label_lkz_Vatikanstadt')),
                  ('VN', 'Vietnam', _(u'label_lkz_Vietnam')),
                  ('W', '(alte', _(u'label_lkz_(alte')),
                  ('WAG', 'Gambia', _(u'label_lkz_Gambia')),
                  ('WAL', 'Sierra', _(u'label_lkz_Sierra')),
                  ('WAN', 'Nigeria', _(u'label_lkz_Nigeria')),
                  ('WD', 'Dominica Wd', _(u'label_lkz_Dominica')),
                  ('WG', 'Grenada', _(u'label_lkz_Grenada')),
                  ('WL', 'St. Wl', _(u'label_lkz_St.')),
                  ('WO', 'Dominica wo', _(u'label_lkz_Dominica')),
                  ('WS', 'Samoa', _(u'label_lkz_Samoa')),
                  ('WV', 'St. WV', _(u'label_lkz_St.')),
                  ('YU', 'Jugoslawien', _(u'label_lkz_Jugoslawien')),
                  ('YV', 'Venezuela', _(u'label_lkz_Venezuela')),
                  ('Z', 'Sambia', _(u'label_lkz_Sambia')),
                  ('ZA', 'Suedafrika', _(u'label_lkz_Suedafrika')),
                  ('ZRE', 'Zaire', _(u'label_lkz_Zaire')),
                  ('ZW', 'Simbabwe', _(u'label_lkz_Simbabwe')),
            )


class DefaultStaSources(grok.MultiAdapter):
    grok.provides(IMultiSource)
    grok.adapts(Interface, zope.publisher.interfaces.IRequest)
    grok.name(u'uvc.sta')

    def __init__(self, context, request):
        self.context = context
        self.request = request
    
    def __call__(self, context):
        return vocabulary_list((
                          ('001','Deutschland',_(u'label_deutschland')),
                          ('050','Aegypten',_(u'label_aegypten')),
                          ('051','Algerien',_(u'label_algerien')),
                          ('010','Albanien',_(u'label_albanien')),
                          ('031','Armenien',_(u'label_armenien')),
                          ('060','Argentinen',_(u'label_argentinien')),
                          ('0311','Aserbaidschan',_(u'label_aserbaidschan')),
                          ('089','Australien',_(u'label_australien')),
                          ('011','Belgien',_(u'label_belgien')),
                          ('0312','Belarus',_(u'label_belarus')),
                          ('039','Bosnien',_(u'label_bosnien')),
                          ('069','Bolivien',_(u'label_bolivien')),
                          ('061','Brasilien',_(u'label_brasilien')),
                          ('012','Bulgarien',_(u'label_bulgarien')),
                          ('062','Chile',_(u'label_chile')),
                          ('070','China',_(u'label_china')),
                          ('013','Daenemark',_(u'label_daenemark')),
                          ('0362','Estland',_(u'label_estland')),
                          ('014','Finnland',_(u'label_finnland')),
                          ('015','Frankreich',_(u'label_frankreich')),
                          ('0313','Georgien',_(u'label_georgien')),
                          ('052','Ghana',_(u'label_ghana')),
                          ('016','Griechenland',_(u'label_griechenland')),
                          ('017','Grossbritannien und Nordirland',_(u'label_grossbritannien')),
                          ('071','Indien',_(u'label_indien')),
                          ('072','Indonesien',_(u'label_indonesien')),
                          ('078','Iran',_(u'label_iran')),
                          ('018','Irland',_(u'label_irland')),
                          ('073','Irak',_(u'label_irak')),
                          ('074','Israel',_(u'label_israel')),
                          ('019','Island',_(u'label_island')),
                          ('020','Italien',_(u'label_italien')),
                          ('075','Japan',_(u'label_japan')),
                          ('076','Jordanien',_(u'label_jordanien')),
                          ('063','Kanada',_(u'label_kanada')),
                          ('0314','Kasachstan',_(u'label_kasachstan')),
                          ('0315','Kirgisistan',_(u'label_kirgisistan')),
                          ('040','Kroatien',_(u'label_kroatien')),
                          ('036','Lettland',_(u'label_lettland')),
                          ('0361','Litauen',_(u'label_litauen')),
                          ('022','Luxemburg',_(u'label_luxemburg')),
                          ('037','Malta',_(u'label_malta')),
                          ('053','Marokko',_(u'label_marokko')),
                          ('041','Mazedonien',_(u'label_mazedonien')),
                          ('064','Mexiko',_(u'label_mexiko')),
                          ('0316','Moldawien',_(u'label_moldawien')),
                          ('023','Niederlande',_(u'label_niederlande')),
                          ('054','Nigeria',_(u'label_nigeria')),
                          ('024','Norwegen',_(u'label_norwegen')),
                          ('025','Oesterreich',_(u'label_oesterreich')),
                          ('077','Pakistan',_(u'label_pakistan')),
                          ('065','Peru',_(u'label_peru')),
                          ('026','Polen',_(u'label_polen')),
                          ('027','Portugal',_(u'label_portugal')),
                          ('028','Rumaenien',_(u'label_rumaenien')),
                          ('0317','Russland',_(u'label_russland')),
                          ('029','Schweden',_(u'label_schweden')),
                          ('030','Schweiz',_(u'label_schweiz')),
                          ('042','Serbien',_(u'label_serbien')),
                          ('043','Slowenien',_(u'label_slowenien')),
                          ('0331','Slowakei',_(u'label_slowakei')),
                          ('032','Spanien',_(u'label_spanien')),
                          ('055','Suedafrika',_(u'label_suedafrika')),
                          ('079','Syrien',_(u'label_syrien')),
                          ('0318','Tadschikistan',_(u'label_tadschikistan')),
                          ('033','Tschechien',_(u'label_tschechien')),
                          ('056','Tunesien',_(u'label_tunesien')),
                          ('034','Tuerkei',_(u'label_tuerkei')),
                          ('0319','Turkmenistan',_(u'label_turkmenistan')),
                          ('03110','Ukraine',_(u'label_ukraine')),
                          ('035','Ungarn',_(u'label_ungarn')),
                          ('066','USA',_(u'label_usa')),
                          ('03111','Usbekistan',_(u'label_usbekistan')),
                          ('038','Zypern',_(u'label_zypern')),
                          ('0999','Sonstige','Sonstige'),
                         ))


class MultiSource(grok.GlobalUtility):
    grok.implements(IVocabularyFactory)
    grok.baseclass()

    def __call__(self, context):
        name = grok.name.bind().get(self)
        request = uvcsite.getRequest()
        vocabulary = queryMultiAdapter((context, request), name=name)
        if vocabulary is not None:
            return vocabulary(context)
        raise NotImplementedError(
            "MultiSource couldn't find a vocabulary %r" % name)


class Uadbru1Sources(MultiSource):
    grok.name('uvc.uadbru1')


class UnfuteSources(MultiSource):
    grok.name(u'uvc.unfute')


class LkzSources(MultiSource):
    grok.name(u'uvc.lkz')


class StaSources(MultiSource):
    grok.name(u'uvc.sta')
