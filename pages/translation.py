from modeltranslation.translator import translator, TranslationOptions
from .models import (
    SectionHero,
    SectionAbout,
    SectionCertificate,
    SectionProject,
    SectionCallToAction,
    SectionHeaderExperience,
    SectionSkills,
    SectionArticle,
    SectionContact,
)


class SectionHeroTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionAboutTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')


class SectionCertificateTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionCallToActionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionHeaderExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionSkillsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


class SectionContactTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')


translator.register(SectionHero, SectionHeroTranslationOptions)
translator.register(SectionAbout, SectionAboutTranslationOptions)
translator.register(SectionCertificate, SectionCertificateTranslationOptions)
translator.register(SectionProject, SectionProjectTranslationOptions)
translator.register(SectionCallToAction, SectionCallToActionTranslationOptions)
translator.register(SectionHeaderExperience, SectionHeaderExperienceTranslationOptions)
translator.register(SectionSkills, SectionSkillsTranslationOptions)
translator.register(SectionArticle, SectionArticleTranslationOptions)
translator.register(SectionContact, SectionContactTranslationOptions)
