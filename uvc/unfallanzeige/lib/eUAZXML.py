# -*- coding: utf-8 -*-

# @file: eUAZXML.py (bgv.unfallanzeige)
# @author: Team Elbe
# @date: 26.05.2011

# XML-Export der Unfalldaten (Dale)

# Grok Import
import grok

# UVCSite Import
import uvcsite
from uvc.unfallanzeige.interfaces import IUnfallanzeige

# Interne Imports
#from bgv.unfallanzeige.lib import helpers
#from bgv.schnittstellen.interfaces import IStammdaten
#from bgv.auth.interfaces import IPrincipalSparteVerkehr

# Sonstige Imports
import lxml.etree as etree
from time import strftime, localtime
#from elementtree.SimpleXMLWriter import XMLWriter
from io import StringIO


def create_uaz_xml(mgldata, unfdata, xmlfile, principal):
    '''
    XML-File fuer Dale erzeugen
    '''
    context = unfdata.context
    mitglied = mgldata.mnr
    adr = mgldata.getAdresse()

    io = StringIO()
    xml = XMLWriter(io, encoding='utf-8')
    bv = ''
    iknr = ''
    ikdav = '99999'

    ikuv = '120291319'

    date = strftime("%d.%m.%Y", localtime())
    time = strftime("%H:%M", localtime())
    uaz = xml.start("uaz_file")

    xml.start("mnr")
    xml.element("mnr_1", mitglied)
    xml.end("mnr")

    xml.start("unb")
    xml.element("unb_2", iknr)
    xml.element("unb_3", ikdav)
    xml.element("unb_4", date)
    xml.element("unb_5", '00:00')
    xml.element("unb_6", '1')
    xml.element("unb_9", '01')
    xml.end("unb")
    xml.start("unh")

    xml.element("unh_2", 'EUAZ:09:1:01:UV')
    xml.element("unh_3", ikuv)
    xml.end("unh")

    xml.start("uvt",)
    xml.element("uvt_1", bv)
    xml.element("uvt_2", ikuv)
    xml.element("uvt_3", date)
    uvt_4 = "%s.%s.20%s" % (context.unfdatum[0:2], context.unfdatum[3:5],
        context.unfdatum[8:11])
    xml.element("uvt_4", uvt_4)
    xml.element("uvt_5")
    xml.end("uvt")

    xml.start("vin")
    xml.element("vin_1", context.prsname[:30])
    xml.element("vin_2", context.prsvor[:30])
    vin_3 = context.prssta
    if vin_3 == '001':
        vin_3 = 'D'
    else:
        vin_3 = '099'
    xml.element("vin_3", vin_3)
    xml.element("vin_4", context.prssex[0])
    xml.element("vin_5", context.ikzplz[:6])
    xml.element("vin_6", context.ikzort[:30])
    vin_7 = "%s %s" % (context.ikstr, context.iknr)
    xml.element("vin_7", vin_7[:46])
    xml.element("vin_8",)

    if int(context.prsgeb[6:11]) > int(strftime("%Y", localtime())):
        vin_9 = "%s.%s.19%s" % (context.prsgeb[0:2], context.prsgeb[3:5],
            context.prsgeb[8:10])
    else:
        vin_9 = "%s.%s.%s" % (context.prsgeb[0:2], context.prsgeb[3:5],
            context.prsgeb[6:10])
    xml.element("vin_9", vin_9)

    xml.element("vin_10", '')
    xml.element("vin_11", '')
    xml.end("vin")

    xml.start("ufb")
    name1 = adr['untern_bez']
    name2 = adr['name1']
    name3 = adr['name2']

    stras = adr['strasse'] + adr['hausnr']

    plz = adr['plz']
    ort = adr['ort']
    ufb_1 = u'%s %s %s' % (unicode(name1), unicode(name2), unicode(name3))
    #ufb_1 = "MUSS NOCH GEMACHT WERDEN"
    xml.element("ufb_1", ufb_1[:200])
    xml.element("ufb_2", '')

    xml.element("ufb_3", plz)
    xml.element("ufb_4", ort[:30])
    xml.element("ufb_5", stras[:46])

    uadbru1 = context.uadbru1
    unfute = context.unfute

    ufb_6 = '%s %s' % (uadbru1[:15], unfute[:14])
    xml.element("ufb_6", ufb_6)
    ufb_7 = '01.%s' % context.uadst
    xml.element("ufb_7", ufb_7)
    xml.end("ufb")

    xml.start("eti")
    xml.element("eti_1", date)
    xml.element("eti_2", time)
    xml.end("eti")

    xml.start("ksd")
    xml.element("ksd_1", context.unfkka[:100])
    xml.element("ksd_5", '0')
    xml.element("ksd_2", '')
    xml.element("ksd_3", '')
    xml.element("ksd_4", '')
    xml.end("ksd")

    xml.start("ufd")
    xml.element("ufd_1", context.unfzeit)
    xml.element("ufd_2", context.uadbavon)
    xml.element("ufd_3", context.uadbabis)
    xml.end("ufd")

    xml.start("ebh")
    xml.element("ebh_1", '')

    if context.unfeba1:
        xml.element("ebh_2", context.unfeba1[:30])
    else:
        xml.element("ebh_2", '')
    xml.end("ebh")

    xml.start("dis")
    dis_1 = "%s %s" % (context.diavkt, context.diaadv)
    if context.prstkz == 'ja':
        dis_1 = u'tödlicher Unfall: %s' % dis_1
    xml.element("dis_1", dis_1[:100])
    xml.element("dis_4", '')
    xml.element("dis_3", '')
    xml.end("dis")

    xml.start("afb")
    if context.unfae1:
        eingestellt = context.unfae1
    else:
        eingestellt = ' '
    toedlich = context.prstkz
    if eingestellt == 'nein':
        afb_1 = '0'
        afb_4 = ''
    elif toedlich == 'ja':
        afb_1 = '1'
        afb_4 = ''
    else:
        afb_1 = '1'
    xml.element("afb_1", afb_1)

    if 'sofort' in eingestellt:
        afb_4 = uvt_4
    elif 'spaeter' in eingestellt:
        afb_4 = "%s.%s.20%s" % (context.unfaedatum[0:2],
            context.unfaedatum[3:5], context.unfaedatum[8:11])
    xml.element("afb_4", afb_4)

    arbeitsfaehig = context.unfwa1
    if arbeitsfaehig == 'nein' or arbeitsfaehig == None:
        afb_7 = ''
    else:
        afb_7 = "%s.%s.%s" % (context.unfwax[0:2], context.unfwax[3:5],
            context.unfwax[6:11])
    xml.element("afb_7", afb_7)
    xml.element("afb_8", '')
    xml.end("afb")

    xml.start("abs")
    xml.element("abs_1", context.unfus2[:81])
    xml.element("abs_2", '')
    xml.element("abs_3", '')
    xml.element("abs_4", 'Extranet')
    xml.element("abs_5", '')
    xml.element("abs_6", context.anspfon)
    xml.element("abs_7", context.anspname)
    xml.end("abs")

    xml.start("uaz")
    xml.element("uaz_1", context.unfhg1[:3000])
    uaz_2 = context.unfhg2
    if uaz_2 == 'des Versicherten':
        uaz_2 = '1'
    else:
        uaz_2 = '2'
    xml.element("uaz_2", uaz_2)
    xml.element("uaz_3", context.unfort[:200])

    if context.prstkz == 'ja':
        uaz_4 = '1'
    else:
        uaz_4 = '2'
    xml.element("uaz_4", uaz_4)
    xml.element("uaz_5", context.unfkn1)
    if context.unfkn2 == 'ja':
        uaz_6 = '1'
    else:
        uaz_6 = '2'
    xml.element("uaz_6", uaz_6)
    xml.element("uaz_7", context.unflar)

    xml.element("uaz_8", context.unfbu)
    xml.element("uaz_9", str(context.unfefz))
    xml.element("uaz_10", '')
    xml.end("uaz")

    xml.close(uaz)
    io.seek(0)

    filename = xmlfile
    f = open(filename, 'w')
    f.write(etree.tostring(etree.parse(io), pretty_print=True, encoding="ISO-8859-1", xml_declaration=True))
    f.close()
    return io
