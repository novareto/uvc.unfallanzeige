# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 

import grok

from megrok import resource
from hurry.jquery import jquery
from uvcsite.resources import UVCResources

from uvc.widgets.resources import double


class UAZLibrary(resource.Library):
    resource.name('uazlib')
    grok.path('resourcen')

#CSS
uazcss = resource.ResourceInclusion(
    UAZLibrary, 'uaz.css')

#UAZ Javascript
uazjs = resource.ResourceInclusion(
    UAZLibrary, 'uaz.js', depends=[double])

#STEP Javascript
step1 = resource.ResourceInclusion(
    UAZLibrary, 'step1.js', depends=[double])

step2 = resource.ResourceInclusion(
    UAZLibrary, 'step2.js', depends=[double])

step3 = resource.ResourceInclusion(
    UAZLibrary, 'step3.js', depends=[double])

step4 = resource.ResourceInclusion(
    UAZLibrary, 'step4.js', depends=[double])

step5 = resource.ResourceInclusion(
    UAZLibrary, 'step5.js', depends=[double])
