# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de

from fanstatic import Library, Resource

library = Library('uvc.unfallanzeige', 'static')

uazcss = Resource(library, 'uaz.css')
uazjs = Resource(library, 'uaz.js', bottom=True)

step1 = Resource(library, 'step1.js')
step2 = Resource(library, 'step2.js')
step3 = Resource(library, 'step3.js')
step4 = Resource(library, 'step4.js')
step5 = Resource(library, 'step5.js')
