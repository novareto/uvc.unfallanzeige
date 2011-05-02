# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de

import time
import grokcore.component as grok

from zope.interface import Interface
from uvcsite import IProductFolder, IContent
from zope.schema import TextLine, Choice, Text, Int
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.component import queryUtility
from uvc.widgets.fields import OptionalChoice
from uvc.unfallanzeige import UvcUnfallanzeigeMessageFactory as _
from uvc.validation.validation import NotValidEingabeDatum, validateDatum, validateUhrzeit


def validateShortDatum(value):
    """ """
    try:
        time.strptime(value, "%m.%Y")
    except ValueError:
        raise NotValidEingabeDatum(value)
    return True


class IUnfallanzeigenFolder(IProductFolder):
    """Markerinterface"""


class IUnfallanzeigeWizard(Interface):
    """Markerinterface"""


class IPresentation(Interface):
    """ Marker Interface """


class DynVocab(object):
    grok.implements(IContextSourceBinder)

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
        SimpleTerm('Arbeitnehmer', 'Arbeitnehmer', u'Arbeitnehmer'),
        SimpleTerm('Gesellschafter/Geschaeftsfuehrer', 'Gesellschfter/Geschaeftsfuehrer', u'Gesellschafter/Geschäftsführer'),
        SimpleTerm('Unternehmer', 'Unternehmer', u'Unternehmer'),
        SimpleTerm('Mit dem Unternehmer verwandt', 'Mit dem Unternehmer verwandt', u'Mit dem Unternehmer verwandt'),
        SimpleTerm('Ehegatte des Unternehmers', 'Ehegatte des Unternehmers', u'Ehegatte des Unternehmers'),
    ))


@grok.provider(IContextSourceBinder) 
def vocab_unfortdetail(context):
    return SimpleVocabulary((
        SimpleTerm('Auf dem Betriebsgelaende', 'Auf dem Betriebsgelaende', u'Auf dem Betriebsgelände'),
        SimpleTerm('Auf dem Weg von oder zur Arbeit', 'Auf dem Weg von oder zur Arbeit', u'Auf dem Weg von oder zur Arbeit'),
        SimpleTerm('Auf dem Geschaeftsweg', 'Auf dem Geschaeftsweg', u'Auf dem Geschäftsweg'),
        SimpleTerm('Ausserhalb des Betriebsgelaendes', 'Ausserhalb des Betriebsgelaendes', u'Ausserhalb des Betriebsgeländes'),
        ))


class IUnfallanzeige(IContent):

# Default Page

    unfustdor = Choice(
        title = _(u"Arbeitsstelle des Versicherten"),
        description = _(u"Wo ist die versicherte Person regelmaessig taetig?"),
        values = (u'In dem vorher genannten Unternehmen', 'In einer Zweigniederlassung'),
        )

    unfuname = TextLine(
        title = _(u"Name der Zweigstelle"),
        description = _(u"Bitte geben Sie hier den Namen der Zweigstelle an."),
        required = False,
        )

    unfustrasse = TextLine(
        title = _(u"Strasse"),
        description = _(u"Bitte geben Sie Strasse"),
        required = False,
        )

    unfunr = TextLine(
        title = _(u"Hs.-Nr."),
        description = _(u"Hausnummer der Zweigstelle an."),
        required = False,
        )

    unfuplz = TextLine(
        title = _(u"PLZ"),
        description = _(u"Bitte geben Sie Postleitzahl"),
        required = False,
        )

    unfuort = TextLine(
        title = _(u"Ort"),
        description = _(u"Ort der Zweigstelle an."),
        required = False,
        )

    anspname = TextLine(
        title = _(u"Ansprechpartner"),
        description = _(u"Bitte geben Sie einen Ansprechpartner an, den wir bei Rueckfragen schnell erreichen koennen"),
        )

    anspfon = TextLine(
        title = _(u"Telefon"),
        description = _(u"vergessen Sie dabei bitte nicht die Telefonnummer."),
        )


# Page Two

    uadbru1 = OptionalChoice(
        title = _(u"Taetigkeit zum Unfallzeitpunkt"),
        description = _(u"Die versicherte Person ist zum Unfallzeitpunkt beschaeftigt als:"),
        source=DynVocab("uvc.uadbru1"),
        )

    uadst = TextLine(
        title = _(u"Beginn der Beschaeftigung"),
        description = _(u"Der Versicherte ist beschaeftigt seit: (mm.jjjj)"),
        constraint = validateShortDatum,
        )

    unfute = OptionalChoice(
        title = _(u"Teil des Unternehmens"),
        description = _(u"In welchem Teil des Unternehmens ist der Versicherte staendig taetig?"),
        source = DynVocab("uvc.unfute"),
        )

    unflar = Choice(
        title = _(u"Leiharbeitnehmer"),
        description = _(u"Ist die versicherte Person Leiharbeitnehmer?"),
        values = ('ja', 'nein'),
        )

    unvlaraddr = Text(
        title = _(u"Personaldienstleister"),
        description = _(u"Bitte geben Sie Name und Anschrift des Personaldienstleisters bzw. Zeitarbeitsunternehmens an."),
        required = False,
        )

# Step 3

    prsname = TextLine(
        title = _(u"Name"),
        description = _(u"Name des Versicherten"),
        )

    prsvor = TextLine(
        title = _(u"Vorname"),
        description = _(u"Vorname des Versicherten"),
        )

    ikstr = TextLine(
        title = _(u"Anschrift (Strasse"),
        description = _(u"Bitte geben Sie Strasse"),
        )

    iknr = TextLine(
        title = _(u"Hs.-Nr.)"),
        description = _(u"Hausnummer des Versicherten an."),
        )

    lkz = Choice(
        title = _(u"Laenderkennzeichen"),
        description = _(u"Laenderkennzeichen des Versicherten"),
        values = (u'Deutschland', u'Polen'),
        )

    ikzplz = TextLine(
        title = _(u"PLZ"),
        description = _(u"Bitte geben Sie Postleitzahl"),
        )

    ikzort = TextLine(
        title = _(u"Ort"),
        description = _(u"Ort des Versicherten an."),
        )

    prsgeb = TextLine(
        title = _(u"Geburtsdatum"),
        description = _(u"Geburtsdatum des Versicherten (tt.mm.jjjj)"),
        constraint = validateDatum,
        )

    prssex = Choice(
        title = _(u"Geschlecht"),
        description = _(u"Geschlecht des Versicherten"),
        source = vocab_prssex,
        )

    prssta = Choice(
        title = _(u"Staatsangehoerigkeit"),
        description = _(u"Staatsangehoerigkeit des Versicherten"),
        source = DynVocab(u'uvc.sta'),
        )

    unfbu = Choice(
        title = _(u"Angaben zum Arbeitsverhaeltnis"),
        description = _(u"Bitte waehlen Sie aus, in welchem Arbeitsverhaeltnis der Versicherte steht."),
        source = vocab_unfbu,
        )

    vehearbeitsv = Choice(
        title = _(u"Ehegattenarbeitsvertrag"),
        description = _(u"Besteht ein Ehegattenarbeitsvertrag?"),
        values = (u'Ja', u'Nein'),
        required = False,
        )

    vehebis = TextLine(
        title = _(u"Ehegattenarbeitsvertrag (Vertragsbeginn)"),
        description = _(u"Wann wurde der Ehegattenarbeitsvertrag geschlossen (tt.mm.jjjj)"),
        required = False,
        constraint = validateDatum,
        )

    veheentgeltbis = TextLine(
        title = _(u"Entgeltzahlung"),
        description = _(u"Entgelt aus dem Ehegattenarbeitsvertrag wurde gezahlt bis (tt.mm.jjjj):"),
        required = False,
        constraint = validateDatum,
        )

    unfefz = Int(
        title = _(u"Entgeltfortzahlung"),
        description = _(u"Fuer wie viele Wochen besteht Anspuch auf Entgeltfortzahlung?"),
        required = False,
        max=99,
        min=0,
        )

    unfkka = TextLine(
        title = _(u"Krankenkasse des Versicherten"),
        description = _(u"Name und Anschrift der Krankenkasse des Versicherten."),
        )

#Step4

    unfdatum = TextLine(
        title = _(u"Unfallzeitpunkt (Datum"),
        description = _(u"Bitte geben Sie das Unfallatum (tt.mm.jjjj)"),
        constraint = validateDatum,
        )

    unfzeit = TextLine(
        title = _(u"Zeit)"),
        description = _(u"den Zeitpunkt (hh:mm) des Unfalls an."),
        constraint = validateUhrzeit,
        )

    unfort_detail = Choice(
        title = _(u"Unfallort"),
        description = _(u"Bitte waehlen Sie aus wo sich der Unfall ereignete."),
        source = vocab_unfortdetail,
        )

    unfort = Text(
        title = _(u"Angaben zum Unfallort"),
        description = _(u"Bitte geben Sie den Unfallort moeglichst genau an (genaue Orts- und Strassenangabe mit Postleitzahl)."),
        )

    unfhg1= Text(
        title = _(u"Unfallhergang"),
        description = _(u"Bitte schildern sie moeglichst detailliert wie sich der Unfall ereignete"),
        )

    unfhg2= Choice(
        title = _(u"Angaben zum Unfall"),
        description = _(u"Die Angaben beruhen auf den Schilderungen:"),
        values = ('des Versicherten', 'einer anderen Person'),
        )

    unfkn1 = Text(
        title = _(u"Zeugen des Unfalls"),
        description = _(u"Wer hat von dem Unfall zuerst Kenntnis genommen (Name und Anschrift des Zeugen)"),
        required = False,
        )

    unfkn2 = Choice(
        title = _(u"Augenzeuge"),
        description = _(u"War diese Person Augenzeuge?"),
        values = ('ja', 'nein'),
        required = False,
        )

# Step 5     

    prstkz = Choice(
        title = _(u"Toedlicher Unfall"),
        description = u"Handelt es sich um einen toedlichen Unfall?",
        values = ('ja', 'nein'),
         )

    unfae1 = Choice(
        title = _(u"Unterbrechung der Arbeit"),
        description = _(u"Hat der Versicherte die Arbeit eingestellt?"),
        values = ('nein', 'ja, sofort', 'ja, spaeter am:'),
        required = False,
        )

    unfaedatum = TextLine(
        title = _(u"Datum"),
        description = _(u"Bitte geben Sie Datum (tt.mm.jjjj)"),
        required = False,
        constraint = validateDatum,
        )

    unfaezeit = TextLine(
        title = _(u"Uhrzeit"),
        description = _(u"Uhrzeit (hh:mm) an."),
        required = False,
        constraint = validateUhrzeit,
        )
     
    unfwa1 = Choice(
        title = _(u"Wiederaufnahme der Arbeit"),
        description = _(u"Hat der Versicherte die Arbeit wieder aufgenommen?"),
        values = ('ja', 'nein'),
        required = False,
        )

    unfwax = TextLine(
        title = _(u"Datum der Wiederaufnahme"),
        description = _(u"An welchem Tag wurde die Arbeit wieder aufgenommen (tt.mm.jjjj)?"),
        required = False,
        constraint = validateDatum,
        )

    uadbavon = TextLine(
        title = _(u"Arbeitszeit (Beginn"),
        description = _(u"Die taegliche Arbeitszeit beginnt um Uhrzeit (hh:mm)"),
        constraint = validateUhrzeit,
        )

    uadbabis = TextLine(
        title = _(u"Ende)"),
        description = _(u"endet um Uhrzeit (hh:mm)."),
        constraint = validateUhrzeit,
        )
     
    diavkt = TextLine(
        title = _(u"Verletzte Koerperteile"),
        description = _(u"Welche Koerperteile sind verletzt?"),
        )

    diaadv = TextLine(
        title = _(u"Art der Verletzung"),
        description = _(u"Welche Art der Verletzung liegt vor?"),
        )

    unfeba = Choice(
        title = _(u"Erstbehandlung des Versicherten"),
        description = _(u"War eine aerztliche Erstbehandlung des Versicherten erforderlich?"),
        values = ("Es ist keine aerztliche Behandlung erforderlich.", "Aerztliche Behandlung bei:"),
        )

    unfeba1 = Text(
        title = _(u"Erstbehandelnder Arzt"),
        description = _(u"Bitte geben Sie Name und Anschrift des erstbehandelnden Arztes an."),
        required = False,
        )

#Step 6

    unfus3 = TextLine(
        title = _(u"Personal- bzw. Betriebsrat"),
        description = _(u"Die folgende Person des Personal- bzw Betriebsrates wurde informiert: (Vorname, Name)"),
        )

    unfus2 = TextLine(
        title = _(u"Unternehmer / Bevollmaechtigter"),
        description = _(u"Vorname, Name des Unternehmens bzw. des Bevollmaechtigten"),
        )

#Step 7

    behandlung = Choice(
        title = _(u"Weiteres Vorgehen"),
        description = _(u"Bitte waehlen Sie aus, wie Sie weiter vorgehen moechten."),
        values = ('Druck', 'Versand', 'Druck & Versand')
        )

