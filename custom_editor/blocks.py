
import json

from django import forms

try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock

    wagtail_version = 1

except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock

    wagtail_version = 2

class CustomEditor(blocks.StructBlock):
    content = blocks.TextBlock(required=False)
    #RawHTMLBlock

    def get_form_context(self, value, prefix='', errors=None):
        context = super().get_form_context(value, prefix=prefix, errors=errors)
        context['suggested_first_names'] = ['John', 'Paul', 'George', 'Ringo']
        return context


    @property
    def media(self):
        return forms.Media(
            js=["https://cdn.quilljs.com/1.3.6/quill.js"],
            css={'all': ["https://cdn.quilljs.com/1.3.6/quill.snow.css"]}
        )

    class Meta:
        form_template = 'custom_editor/admin_blocks/template.html'
        template = 'custom_editor/template.html'
        #icon = "fa-globe"