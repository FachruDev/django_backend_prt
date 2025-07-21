from modeltranslation.translator import register, TranslationOptions
from .models import ArticleTag, ArticleCategory, Article

@register(ArticleTag)
class ArticleTagTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(ArticleCategory)
class ArticleCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'content')