from rest_framework import serializers
from article.models import Article, ArticleCategory, ArticleTag
from webconfig.models import WebSetting, MyDocument, SocialLink
from pages.models import (
    SectionHero, SectionAbout, SectionCertificate, SectionProject,
    SectionCallToAction, SectionHeaderExperience, SectionSkills,
    SectionArticle, SectionContact
)
from contact.models import ContactForm, ContactInformation
from portfolio.models import (
    Certificate, ProjectCategory, Project, ImageProject,
    Experience, AchievementExperience, SkillsCategory, Skill
)


# Article Serializers
class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = '__all__'


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = ArticleCategorySerializer(read_only=True)
    tags = ArticleTagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'


# WebConfig Serializers
class WebSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSetting
        fields = '__all__'


class MyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDocument
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


# Pages Serializers
class SectionHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionHero
        fields = '__all__'


class SectionAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionAbout
        fields = '__all__'


class SectionCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCertificate
        fields = '__all__'


class SectionProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionProject
        fields = '__all__'


class SectionCallToActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCallToAction
        fields = '__all__'


class SectionHeaderExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionHeaderExperience
        fields = '__all__'


class SectionSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionSkills
        fields = '__all__'


class SectionArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionArticle
        fields = '__all__'


class SectionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionContact
        fields = '__all__'


# Contact Serializers
class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'


# Portfolio Serializers
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'


class ImageProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(read_only=True)
    images = ImageProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'


class AchievementExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementExperience
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    achievements = AchievementExperienceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Experience
        fields = '__all__'


class SkillsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsCategory
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    category = SkillsCategorySerializer(read_only=True)
    
    class Meta:
        model = Skill
        fields = '__all__' 