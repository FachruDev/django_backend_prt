from modeltranslation.translator import register, TranslationOptions
from .models import (
    Certificate,
    ProjectCategory,
    Project,
    Experience,
    AchievementExperience
)

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')

@register(ProjectCategory)
class ProjectCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'work_on') 

@register(AchievementExperience)
class AchievementExperienceTranslationOptions(TranslationOptions):
    fields = ('description',)