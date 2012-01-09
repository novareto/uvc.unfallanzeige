# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 

import grok

from js.jquery import jquery
from fanstatic import Library, Resource
from uvc.widgets.resources import double

library = Library('uvc.unfallanzeige', 'static')

uazcss = Resource(library, 'uaz.css')
uazjs = Resource(library, 'uaz.js', depends=[double])

step1 = Resource(library, 'step1.js', depends=[double])
step2 = Resource(library, 'step2.js', depends=[double])
step3 = Resource(library, 'step3.js', depends=[double])
step4 = Resource(library, 'step4.js', depends=[double])
step5 = Resource(library, 'step5.js', depends=[double])
