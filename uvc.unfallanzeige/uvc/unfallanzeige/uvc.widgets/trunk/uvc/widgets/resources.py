from megrok.resource import ResourceInclusion, Library, path, name
from hurry.jqueryui import jqueryui
from hurry.tinymce import tinymce

class FancyWidgetsLibrary(Library):
    path('jslibrary')
    name('fancywidgets')


DatePicker = ResourceInclusion(FancyWidgetsLibrary, 'datepicker.js', depends=[jqueryui])

TinyMCE = ResourceInclusion(FancyWidgetsLibrary, 'tinymce.js', depends=[tinymce])
