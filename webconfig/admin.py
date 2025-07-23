from django.contrib import admin
from unfold.admin import ModelAdmin
from solo.admin import SingletonModelAdmin
from .models import WebSetting, MyDocument, SocialLink
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(WebSetting)
class WebSettingAdmin(SingletonModelAdmin, ModelAdmin, TabbedTranslationAdmin):
    
    pass

@admin.register(MyDocument)
class MyDocumentAdmin(SingletonModelAdmin, ModelAdmin, TabbedTranslationAdmin):
    pass

@admin.register(SocialLink) 
class SocialLinkAdmin(ModelAdmin):
    list_display = ("title", "icon", "url")
    search_fields = ("title", "icon", "url")