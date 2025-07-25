from django.contrib import admin
from django.shortcuts import redirect
from unfold.admin import ModelAdmin
from .models import WebSetting, MyDocument, SocialLink
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(WebSetting)
class WebSettingAdmin(ModelAdmin, TabbedTranslationAdmin):
    def changelist_view(self, request, extra_context=None):
        return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/1/change/')

    def has_add_permission(self, request):
        return False 

@admin.register(MyDocument)
class MyDocumentAdmin(ModelAdmin, TabbedTranslationAdmin):
    def changelist_view(self, request, extra_context=None):
        return redirect(f'/admin/{self.model._meta.app_label}/{self.model._meta.model_name}/1/change/')

    def has_add_permission(self, request):
        return False

@admin.register(SocialLink)
class SocialLinkAdmin(ModelAdmin):
    list_display = ("title", "icon", "url")
    search_fields = ("title", "icon", "url")
