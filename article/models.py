from django.db import models
from django.utils.translation import gettext_lazy as _

# Seo model
class SEOModel(models.Model):
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, help_text=_("A user-friendly URL path."))
    meta_title = models.CharField(_("Meta Title"), max_length=70, blank=True)
    meta_description = models.CharField(_("Meta Description"), max_length=160, blank=True)
    featured_image_url = models.URLField(_("Featured Image URL"), blank=True)
    featured_image_alt = models.CharField(_("Featured Image Alt Text"), max_length=255, blank=True)
    canonical_url = models.URLField(_("Canonical URL"), blank=True)
    structured_data = models.JSONField(_("Structured Data (JSON-LD)"), null=True, blank=True)

    class Meta:
        abstract = True

# Article model
class ArticleTag(models.Model):
    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("Article Tag")
        verbose_name_plural = _("Article Tags")

    def __str__(self):
        return self.title

class ArticleCategory(models.Model):
    title = models.CharField(_("Title"), max_length=100)

    class Meta:
        verbose_name = _("Article Category")
        verbose_name_plural = _("Article Categories")

    def __str__(self):
        return self.title

class Article(SEOModel):
    class ArticleStatus(models.TextChoices):
        PUBLISHED = 'published', _('Published')
        DRAFT = 'draft', _('Draft')
        ARCHIVED = 'archived', _('Archived')

    title = models.CharField(_("Title"), max_length=200)
    subtitle = models.CharField(_("Subtitle"), max_length=255, blank=True)
    content = models.TextField(_("Content"))
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="articles")
    tags = models.ManyToManyField(ArticleTag, blank=True, related_name="articles")
    status = models.CharField(_("Status"), max_length=10, choices=ArticleStatus.choices, default=ArticleStatus.DRAFT)
    image = models.ImageField(_("Image"), upload_to="blog/articles/")
    published_at = models.DateTimeField(_("Published At"), null=True, blank=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ['-published_at']

    def __str__(self):
        return self.title