# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de

import time
import datetime
import grokcore.component as grok

from zope.interface import Interface
from zope.interface import Invalid
from zope.interface import implementer 

from uvcsite import IProductFolder, IContent
from zope.schema import TextLine, Choice, Text, Int
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.schema import ValidationError
from zope.component import queryUtility
from uvc.widgets.fields import OptionalChoice
from uvc.unfallanzeige import UvcUnfallanzeigeMessageFactory as _
from uvc.validation.validation import NotValidEingabeDatum, validateUhrzeit, validatePLZ


class FutureDatum(ValidationError):
    u""" Ihr eingegebenes Datum liegt in der Zukunft.
         Bitte überprüfen Sie ihre Eingabe.
    """


def validateFutureShortDatum(value):
    if value:
        try:
            time.strptime(value, "%m.%Y")
        except ValueError:
            raise NotValidEingabeDatum(value)
        vdatum = datetime.datetime.strptime(value, "%m.%Y")
        now = datetime.datetime.now()
        if vdatum > now:
            raise FutureDatum(value)
    return True


def validateFutureDatum(value):
    if value:
        try:
            time.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise NotValidEingabeDatum(value)
        vdatum = datetime.datetime.strptime(value, "%d.%m.%Y")
        now = datetime.datetime.now()
        if vdatum > now:
            raise FutureDatum(value)
    return True


class ArbeitEingestelltFields(Invalid):
    """Fehlerklasse"""


class IUnfallanzeigenFolder(IProductFolder):
    """Markerinterface"""


class IUnfallanzeigeWizard(Interface):
    """Markerinterface"""


class IPresentation(Interface):
    """ Marker Interface """


@implementer(IContextSourceBinder)
class DynVocab(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, context):
        vocab = queryUtility(
            IVocabularyFactory, name=self.name)
        if not vocab:
            return SimpleVocabulary([])
        return vocab(context)


@grok.provider(IContextSourceBinder)
def vocab_prssex(context):
    return SimpleVocabulary((
        SimpleTerm('maennlich', 'maennlich', u'männlich'),
        SimpleTerm('weiblich', 'weiblich', u'weiblich')
        ))


@grok.provider(IContextSourceBinder)
def vocab_unfbu(context):
    return SimpleVocabulary((
        SimpleTerm('Arbeitnehmer', 'Arbeitnehmer', u'Arbeitnehmer/-in'),
        SimpleTerm('Unternehmer', 'Unternehmer', u'Unternehmer/-in'),
        SimpleTerm('Gesellschafter/Geschaeftsfuehrer', 'Gesellschfter/Geschaeftsfuehrer', u'Gesellschafter/-in, Geschäftsführer/-in'),
        SimpleTerm('Ehegatte des Unternehmers', 'Ehegatte des Unternehmers', u'mit der Unternehmerin/dem Unternehmer verheiratet'),
        SimpleTerm('eingetragenen Lebenspartnerschaft', 'eingetragene Lebenspartnerschaft', u'mit der Unternehmerin/dem Unternehmer in eingetragener Lebenspartnerschaft lebend'),
        SimpleTerm('Mit dem Unternehmer verwandt', 'Mit dem Unternehmer verwandt', u'mit der Unternehmerin/dem Unternehmer verwandt'),
    ))



@grok.provider(IContextSourceBinder)
def vocab_unfhg2(context):
    return SimpleVocabulary((
        SimpleTerm('des Versicherten', 'des Versicherten', u'der versicherten Person'),
        SimpleTerm('einer anderen Person', 'einer anderen Person', u'anderer Personen'),
    ))


@grok.provider(IContextSourceBinder)
def vocab_unfortdetail(context):
    return SimpleVocabulary((
        SimpleTerm('Auf dem Betriebsgelaende', 'Auf dem Betriebsgelaende', u'Auf dem Betriebsgelände'),
        SimpleTerm('Auf dem Weg von oder zur Arbeit', 'Auf dem Weg von oder zur Arbeit', u'Auf dem Weg von oder zur Arbeit'),
        SimpleTerm('Auf dem Geschaeftsweg', 'Auf dem Geschaeftsweg', u'Auf dem Geschäftsweg'),
        SimpleTerm('Ausserhalb des Betriebsgelaendes', 'Ausserhalb des Betriebsgelaendes', u'Ausserhalb des Betriebsgeländes'),
        ))


@grok.provider(IContextSourceBinder)
def vocab_wiederaufnahme(context):
    return SimpleVocabulary((
        SimpleTerm('nein', 'nein', u'nein'),
        SimpleTerm('ja, sofort', 'ja, sofort', u'ja, sofort'),
        SimpleTerm('ja, spaeter am:', 'ja, spaeter am:', u'ja, später am:'),
        ))


@grok.provider(IContextSourceBinder)
def vocab_arzt(context):
    return SimpleVocabulary((
        SimpleTerm('Es ist keine aerztliche Behandlung erforderlich.',
                   'Es ist keine aerztliche Behandlung erforderlich.',
                   u'Es ist keine ärztliche Behandlung erforderlich.'),
        SimpleTerm('Aerztliche Behandlung bei:',
                   'Aerztliche Behandlung bei:',
                   u'Ärztliche Behandlung bei:',)
        ))


class IUnfallanzeige(IContent):

# Default Page

    unfustdor = Choice(
        title = u'Arbeitsstelle der versicherten Person',
        description = u"Wo ist die versicherte Person regelmäßig tätig?",
        values = (u'In dem vorher genannten Unternehmen', u'In einer Zweigniederlassung'),
        )

    unfuname = TextLine(
        title = u"Name der Zweigstelle",
        description = u"Bitte geben Sie hier den Namen der Zweigstelle an.",
        required = False,
        )

    unfustrasse = TextLine(
        title = u'Straße, ',
        description = u"Bitte geben Sie Straße",
        required = False,
        )

    unfunr = TextLine(
        title = u'Hausnummer',
        description = u'und die Hausnummer an.',
        required = False,
        )

    unfuplz = TextLine(
        title = u"PLZ, ",
        description = u"Bitte geben Sie die Postleitzahl",
        required = False,
        constraint = validatePLZ,
        )

    unfuort = TextLine(
        title = u"Ort",
        description = u'und den Ort an.',
        required = False,
        )

    anspname = TextLine(
        title = u"Name Ansprechpartner*in",
        description = u"",
        #description = u"Bitte geben Sie eine Ansprechperson an,",
        )

    anspfon = TextLine(
        title = u"und Telefonnummer",
        description = u"",
        #description = u"die wir bei Rückfragen schnell erreichen können.",
        )

# Page Two

    uadbru1 = OptionalChoice(
        title = u"Tätigkeit zum Unfallzeitpunkt",
        description = u"Die versicherte Person ist zum Unfallzeitpunkt beschäftigt als:",
        source=DynVocab("uvc.uadbru1"),
        )

    azubi = Choice(
        title = u'Auszubildende/-r',
        description=u'Befindet sich die versicherte Person in der Ausbildung?',
        required=True,
        values=['ja', 'nein'],
        default='nein',
        )

    uadst = TextLine(
        title = u"Beginn der Beschäftigung",
        description = u"Die versicherte Person ist beschäftigt seit: (Monat, Jahr)",
        constraint = validateFutureShortDatum,
        )

    unfute = OptionalChoice(
        title = u"Teil des Unternehmens",
        description = u"In welchem Teil des Unternehmens ist die versicherte Person ständig tätig?",
        source = DynVocab("uvc.unfute"),
        )

    unflar = Choice(
        title = u"Leiharbeitnehmer/-in",
        description = u"Ist die versicherte Person Leiharbeitnehmer/-in?",
        values = ('ja', 'nein'),
        )

    unvlaraddr = Text(
        title = u"Personaldienstleister",
        description = u"Bitte geben Sie Name und Anschrift des Personaldienstleisters bzw. Zeitarbeitsunternehmens an.",
        required = False,
        )

# Step 3

    prsname = TextLine(
        title = u"Name",
        description = u"Bitte geben Sie den Namen der versicherten Person an.",
        )

    prsvor = TextLine(
        title = u"Vorname",
        description = u"Bitte geben Sie den Vornamen der versicherten Person an.",
        )

    ikstr = TextLine(
        title = u"Straße",
        description = u"Bitte geben Sie die Straße und ",
        )

    iknr = TextLine(
        title = u"Hausnummer",
        description = u"die Hausnummer der versicherten Person an.",
        )

    lkz = OptionalChoice(
        title = u"Länderkennzeichen",
        description = u"Länderkennzeichen der versicherten Person",
        source = DynVocab(u'uvc.lkz'),
        )

    ikzplz = TextLine(
        title = u"PLZ",
        description = u"Bitte geben Sie die Postleitzahl und",
        #constraint = validatePLZ,
        )

    ikzort = TextLine(
        title = u"Ort",
        description = u"den Ort der versicherten Person an.",
        )

    prsgeb = TextLine(
        title = u"Geburtsdatum",
        description = u"Bitte geben Sie das Geburtstdatum der versicherten Person an (Tag, Monat, Jahr).",
        constraint = validateFutureDatum,
        )

    prssex = Choice(
        title = u"Geschlecht",
        description = u'Bitte wählen Sie das Geschlecht der versicherten Person aus.',
        source = vocab_prssex,
        )

    prssta = Choice(
        title = u"Staatsangehörigkeit",
        description = u'Bitte wählen Sie die Staatsangehörigkeit der versicherten Person aus.',
        source = DynVocab(u'uvc.sta'),
        )

    unfbu = Choice(
        title = u"Angaben zum Arbeitsverhältnis",
        description = u"Bitte wählen Sie aus, in welchem Arbeitsverhältnis die versicherte Person steht.",
        source = vocab_unfbu,
        )

    vehearbeitsv = Choice(
        title = u"Arbeitsvertrag",
        description = u'Besteht ein Arbeitsvertrag?',
        values = (u'Ja', u'Nein'),
        required = False,
        )

    vehebis = TextLine(
        title = u'Vertragsbeginn',
        description = u'Wann wurde der Arbeitsvertrag geschlossen (Tag, Monat, Jahr)?',
        required = False,
        constraint = validateFutureDatum,
        )

    veheentgeltbis = TextLine(
        title = u"Entgeltzahlung",
        description = u'Entgelt aus dem Arbeitsvertrag wurde gezahlt bis (Tag, Monat, Jahr):',
        required = False,
        constraint = validateFutureDatum,
        )

    unfefz = Int(
        title = u"Entgeltfortzahlung",
        description = u"Für wie viele Wochen besteht Anspuch auf Entgeltfortzahlung?",
        required = False,
        max=99,
        min=0,
        )

    unfkka = TextLine(
        title = u'Krankenkasse der versicherten Person',
        description = u'Bitte geben Sie den Namen und die Anschrift der Krankenkasse der versicherten Person an.',
        )

#Step4

    unfdatum = TextLine(
        title = u'Unfalldatum,',
        description = u'Bitte geben Sie das Unfalldatum (Tag, Monat, Jahr) und ',
        constraint = validateFutureDatum,
        )

    unfzeit = TextLine(
        title = u'Unfallzeit',
        description = u'den Unfallzeit (Stunde, Minute) an.',
        constraint = validateUhrzeit,
        )

    unfort_detail = Choice(
        title = u"Unfallort",
        description = u'Bitte wählen Sie aus, wo sich der Unfall ereignete.',
        source = vocab_unfortdetail,
        )

    unfort = Text(
        title = u"Angaben zum Unfallort",
        description = u'Bitte tragen Sie hier den Unfallort mit möglichst genauer Orts- und Straßenangabe und Postleitzahl ein.',
        )

    unfhg1= Text(
        title = u"Unfallhergang",
        description = u'Bitte schildern Sie möglichst detailliert, wie sich der Unfall ereignete.',
        )

    unfhg2= Choice(
        title = u"Angaben zum Unfall",
        description = u"Die Angaben beruhen auf den Schilderungen:",
        source = vocab_unfhg2,
        )

    unfkn1 = Text(
        title = u"Zeugen des Unfalls",
        description = u'Wer hat von dem Unfall zuerst Kenntnis genommen (Name und Anschrift der Zeugin/des Zeugen)?',
        required = False,
        )

    unfkn2 = Choice(
        title = u'Augenzeugin/Augenzeuge',
        description = u'War diese Person Augenzeugin/Augenzeuge?',
        values = ('ja', 'nein'),
        required = False,
        )

# Step 5

    prstkz = Choice(
        title = u"Tödlicher Unfall",
        default = 'nein',
        values = ('ja', 'nein'),
         )

    unfae1 = Choice(
        title = u"Unterbrechung der Arbeit",
        description = u'Hat die versicherte Person die Arbeit eingestellt?',
        source = vocab_wiederaufnahme,
        required = False,
        )

    unfaedatum = TextLine(
        title = u"Datum",
        description = u'Bitte geben Sie das Datum (Tag, Monat, Jahr) ',
        required = False,
        constraint = validateFutureDatum,
        )

    unfaezeit = TextLine(
        title = u"Uhrzeit",
        description = u'und die Uhrzeit (Stunde, Minute) an.',
        required = False,
        constraint = validateUhrzeit,
        )

    unfwa1 = Choice(
        title = u"Wiederaufnahme der Arbeit",
        description = u'Hat die versicherte Person die Arbeit wieder aufgenommen?',
        values = ('ja', 'nein'),
        required = False,
        )

    unfwax = TextLine(
        title = u"Datum der Wiederaufnahme",
        description = u'An welchem Tag wurde die Arbeit wieder aufgenommen (Tag, Monat, Jahr)?',
        required = False,
        constraint = validateFutureDatum,
        )

    uadbavon = TextLine(
        title = u'Arbeitszeitbeginn,',
        description = u'Um welche Uhrzeit beginnt und endet ',
        constraint = validateUhrzeit,
        )

    uadbabis = TextLine(
        title = u'Arbeitszeitende',
        description = u' die tägliche Arbeitszeit (Stunde, Minute)?',
        constraint = validateUhrzeit,
        )

    diavkt = TextLine(
        title = u"Verletzte Körperteile",
        description = u"Welche Körperteile sind verletzt?",
        )

    diaadv = TextLine(
        title = u"Art der Verletzung",
        description = u"Welche Art der Verletzung liegt vor?",
        )

    unfeba = Choice(
        title = u'Erstbehandlung der versicherten Person',
        description = u'War eine ärztliche Behandlung der versicherten Person erforderlich?',
        source = vocab_arzt,
        )

    unfeba1 = Text(
        title = u'Ärztliche Erstbehandlung',
        description = u'Bitte geben Sie den Namen und die Anschrift der Ärztin/des Arztes oder des Krankenhauses an.',
        required = False,
        )

#Step 6

    unfus3 = TextLine(
        title = u"Personal- bzw. Betriebsrat",
        description = u'Die folgende Person (Name, Vorname) des Personal- bzw. Betriebsrates wurde informiert:',
        required = False,
        )

    unfus2 = TextLine(
        title = u'Unternehmer/-in (Bevollmächtigte/-r)',
        description = u'Bitte geben Sie den Namen und Vornamen der Unternehmerin/des Unternehmers oder der Bevollmächtigten/des Bevollmächtigten an, der von dem Unfall in Kenntnis gesetzt wurde.',
        )

#Step 7

    behandlung = Choice(
        title = u"Weiteres Vorgehen",
        description = u"Unfallanzeige abschicken oder zur späteren Bearbeitung als Entwurf speichern.",
        values = ('Versand', 'Entwurf speichern'),
        )
