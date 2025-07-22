from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from .models import Article, ArticleCategory, ArticleTag
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(ArticleTag)
class ArticleTagAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    tabs = True

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    tabs = True

@admin.register(Article)
class ArticleAdmin(TabbedTranslationAdmin, ModelAdmin):
    ordering_field = "weight"
    tabs = True
    list_display = ("title", "status", "category", "published_at")
    list_filter = ("status", "category", "tags")
    search_fields = ("title", "subtitle", "content")
    autocomplete_fields = ("category", "tags")
    readonly_fields = ("slug",)

    fieldsets = (
        (_("Content"), {
            "fields": (
                "title", "subtitle", "content",
                "category", "tags", "image",
                "status", "published_at",
            ),
        }),
        (_("SEO"), {
            "fields": (
                "slug", "meta_title", "meta_description",
                "featured_image_url", "featured_image_alt",
                "canonical_url", "structured_data",
            ),
            "classes": ("collapse",),
        }),
    )

    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget},  
        Article._meta.get_field("title"): {"widget": None},
        Article._meta.get_field("meta_title"): {"widget": WysiwygWidget},
        Article._meta.get_field("meta_description"): {"widget": WysiwygWidget},
        Article._meta.get_field("structured_data"): {"widget": WysiwygWidget},
    }
