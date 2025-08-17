from modeltranslation.translator import register, TranslationOptions
from .models import WebSetting, MyDocument

@register(WebSetting)
class WebSettingTranslationOptions(TranslationOptions):
    fields = ('title', 'meta_title', 'meta_description')

@register(MyDocument)
class MyDocumentTranslationOptions(TranslationOptions):
    fields = ('cv_file',)