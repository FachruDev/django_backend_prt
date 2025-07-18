from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from parler.models import TranslatableModel, TranslatedFields

# For Web Setting
class WebSetting(SingletonModel, TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Website Title"), max_length=200),
        meta_title=models.CharField(_("Meta Title"), max_length=70, help_text=_("Optimal length: 50-60 characters")),
        meta_description=models.CharField(_("Meta Description"), max_length=160, help_text=_("Optimal length: 150-160 characters"))
    )
    logo = models.ImageField(_("Logo"), upload_to="configuration/logos/")
    favicon = models.ImageField(_("Favicon"), upload_to="configuration/favicons/")

    class Meta:
        verbose_name = _("Web Setting")
        verbose_name_plural = _("Web Settings")

    def __str__(self):
        return self.title

# For My Document
class MyDocument(SingletonModel, TranslatableModel):
    translations = TranslatedFields(
        cv_file=models.FileField(_("CV File"), upload_to="configuration/documents/")
    )

    class Meta:
        verbose_name = _("My Document")
        verbose_name_plural = _("My Documents")

    def __str__(self):
        return _("My CV Document")

# For Social Link
class SocialLink(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    icon = models.CharField(_("Icon"), max_length=50, help_text=_("e.g., 'fab fa-linkedin', 'fab fa-github' from Font Awesome"))
    url = models.URLField(_("URL"))

    class Meta:
        verbose_name = _("Social Link")
        verbose_name_plural = _("Social Links")
        ordering = ['title']

    def __str__(self):
        return self.title