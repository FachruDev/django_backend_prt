from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Article, ArticleTag, ArticleCategory

@admin.register(ArticleTag)
class ArticleTagAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ('title',)

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(TabbedTranslationAdmin, ModelAdmin):
    search_fields = ('title',)

# Main Article Admin with advanced UX configuration
@admin.register(Article)
class ArticleAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'status', 'category', 'published_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content', 'subtitle')
    
    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget},
    }

    sidebar = [
        "status",
        "published_at",
        "image",
    ]

    fieldsets = (
        # Section 1 Main content
        (None, {
            "fields": (
                "title", 
                "subtitle", 
                "content",
            ),
        }),
        # Section 2 Relation
        ("Kategori & Tag", {
            "fields": (
                "category", 
                "tags",
            ),
        }),
        # Section 3 Seo
        ("Pengaturan SEO", {
            "classes": ("collapse",),
            "fields": (
                "slug",
                "meta_title",
                "meta_description",
                "featured_image_url",
                "featured_image_alt",
                "canonical_url",
                "structured_data",
            ),
        }),
    )

    # Auto slug from title
    prepopulated_fields = {
        "slug": ("title",),
    }
    
    filter_horizontal = ('tags',)