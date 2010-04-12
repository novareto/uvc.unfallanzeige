# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 

import grok

from megrok import resource
from hurry.jquery import jquery
from uvcsite.resources import UVCResources



class UAZLibrary(resource.Library):
    resource.name('uazlib')
    grok.path('static')


uazjs = resource.ResourceInclusion(
    UAZLibrary, 'uaz.js', depends=[jquery])
