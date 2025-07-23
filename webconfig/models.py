from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

class WebSetting(SingletonModel):
    title = models.CharField(_("Website Title"), max_length=200)
    meta_title = models.CharField(_("Meta Title"), max_length=70, help_text=_("Optimal length: 50-60 characters"))
    meta_description = models.CharField(_("Meta Description"), max_length=160, help_text=_("Optimal length: 150-160 characters"))
    logo = models.ImageField(_("Logo"), upload_to="webconfig/logos/")
    favicon = models.ImageField(_("Favicon"), upload_to="webconfig/favicons/")

    class Meta:
        verbose_name = _("Web Setting")
    def __str__(self): return self.title

class MyDocument(SingletonModel):
    cv_file = models.FileField(_("CV File"), upload_to="webconfig/documents/")

    class Meta:
        verbose_name = _("My Document")
    
    def __str__(self):
        return str(_("My CV Document"))

class SocialLink(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    icon = models.CharField(_("Icon"), max_length=50, help_text=_("e.g., 'fab fa-linkedin'"))
    url = models.URLField(_("URL"))
    
    class Meta:
        verbose_name = _("Social Link"); verbose_name_plural = _("Social Links"); ordering = ['title']
    def __str__(self): return self.title