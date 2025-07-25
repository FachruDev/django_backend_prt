from django.db import models
from solo.models import SingletonModel


class SectionHero(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Hero"


class SectionAbout(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    profile = models.ImageField(upload_to='about/profile/')

    def __str__(self):
        return "Section About"


class SectionCertificate(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Certificate"


class SectionProject(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Project"


class SectionCallToAction(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Call to Action"


class SectionHeaderExperience(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Header Experience"


class SectionSkills(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Skills"


class SectionArticle(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Article"


class SectionContact(SingletonModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)

    def __str__(self):
        return "Section Contact"
