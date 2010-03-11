# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 

import grok

from megrok import resource
from hurry.jquery import jquery

class UAZLibrary(resource.ResourceLibrary):
    resource.name('uazlib')
    grok.path('static')

    resource.resource('uaz.js', depends=[jquery,])
