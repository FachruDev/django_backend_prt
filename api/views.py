from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

# Import models
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

# Import serializers
from .serializers import (
    ArticleSerializer, ArticleCategorySerializer, ArticleTagSerializer,
    WebSettingSerializer, MyDocumentSerializer, SocialLinkSerializer,
    SectionHeroSerializer, SectionAboutSerializer, SectionCertificateSerializer,
    SectionProjectSerializer, SectionCallToActionSerializer, SectionHeaderExperienceSerializer,
    SectionSkillsSerializer, SectionArticleSerializer, SectionContactSerializer,
    ContactFormSerializer, ContactInformationSerializer,
    CertificateSerializer, ProjectCategorySerializer, ProjectSerializer,
    ImageProjectSerializer, ExperienceSerializer, AchievementExperienceSerializer,
    SkillsCategorySerializer, SkillSerializer
)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    """
    Overview of all available API endpoints
    """
    api_urls = {
        'All Data': '/api/all-data/',
        'Articles': '/api/articles/',
        'Article Categories': '/api/article-categories/',
        'Article Tags': '/api/article-tags/',
        'Web Settings': '/api/web-settings/',
        'My Documents': '/api/my-documents/',
        'Social Links': '/api/social-links/',
        'Pages Sections': {
            'Hero': '/api/pages/hero/',
            'About': '/api/pages/about/',
            'Certificate': '/api/pages/certificate/',
            'Project': '/api/pages/project/',
            'Call to Action': '/api/pages/call-to-action/',
            'Header Experience': '/api/pages/header-experience/',
            'Skills': '/api/pages/skills/',
            'Article': '/api/pages/article/',
            'Contact': '/api/pages/contact/',
        },
        'Contact': {
            'Forms': '/api/contact/forms/',
            'Information': '/api/contact/information/',
        },
        'Portfolio': {
            'Certificates': '/api/portfolio/certificates/',
            'Project Categories': '/api/portfolio/project-categories/',
            'Projects': '/api/portfolio/projects/',
            'Project Images': '/api/portfolio/project-images/',
            'Experiences': '/api/portfolio/experiences/',
            'Achievement Experiences': '/api/portfolio/achievement-experiences/',
            'Skills Categories': '/api/portfolio/skills-categories/',
            'Skills': '/api/portfolio/skills/',
        }
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([AllowAny])
def all_data(request):
    """
    Get all data from all apps in a single response
    """
    try:
        # Articles
        articles = Article.objects.filter(status='published')
        articles_data = ArticleSerializer(articles, many=True).data
        
        article_categories = ArticleCategory.objects.all()
        article_categories_data = ArticleCategorySerializer(article_categories, many=True).data
        
        article_tags = ArticleTag.objects.all()
        article_tags_data = ArticleTagSerializer(article_tags, many=True).data
        
        # WebConfig
        web_settings = WebSetting.objects.first()
        web_settings_data = WebSettingSerializer(web_settings).data if web_settings else None
        
        my_documents = MyDocument.objects.first()
        my_documents_data = MyDocumentSerializer(my_documents).data if my_documents else None
        
        social_links = SocialLink.objects.all()
        social_links_data = SocialLinkSerializer(social_links, many=True).data
        
        # Pages
        pages_data = {}
        try:
            pages_data['hero'] = SectionHeroSerializer(SectionHero.objects.first()).data
        except:
            pages_data['hero'] = None
            
        try:
            pages_data['about'] = SectionAboutSerializer(SectionAbout.objects.first()).data
        except:
            pages_data['about'] = None
            
        try:
            pages_data['certificate'] = SectionCertificateSerializer(SectionCertificate.objects.first()).data
        except:
            pages_data['certificate'] = None
            
        try:
            pages_data['project'] = SectionProjectSerializer(SectionProject.objects.first()).data
        except:
            pages_data['project'] = None
            
        try:
            pages_data['call_to_action'] = SectionCallToActionSerializer(SectionCallToAction.objects.first()).data
        except:
            pages_data['call_to_action'] = None
            
        try:
            pages_data['header_experience'] = SectionHeaderExperienceSerializer(SectionHeaderExperience.objects.first()).data
        except:
            pages_data['header_experience'] = None
            
        try:
            pages_data['skills'] = SectionSkillsSerializer(SectionSkills.objects.first()).data
        except:
            pages_data['skills'] = None
            
        try:
            pages_data['article'] = SectionArticleSerializer(SectionArticle.objects.first()).data
        except:
            pages_data['article'] = None
            
        try:
            pages_data['contact'] = SectionContactSerializer(SectionContact.objects.first()).data
        except:
            pages_data['contact'] = None
        
        # Contact
        contact_forms = ContactForm.objects.all()
        contact_forms_data = ContactFormSerializer(contact_forms, many=True).data
        
        contact_information = ContactInformation.objects.first()
        contact_information_data = ContactInformationSerializer(contact_information).data if contact_information else None
        
        # Portfolio
        certificates = Certificate.objects.all()
        certificates_data = CertificateSerializer(certificates, many=True).data
        
        project_categories = ProjectCategory.objects.all()
        project_categories_data = ProjectCategorySerializer(project_categories, many=True).data
        
        projects = Project.objects.all()
        projects_data = ProjectSerializer(projects, many=True).data
        
        project_images = ImageProject.objects.all()
        project_images_data = ImageProjectSerializer(project_images, many=True).data
        
        experiences = Experience.objects.all()
        experiences_data = ExperienceSerializer(experiences, many=True).data
        
        achievement_experiences = AchievementExperience.objects.all()
        achievement_experiences_data = AchievementExperienceSerializer(achievement_experiences, many=True).data
        
        skills_categories = SkillsCategory.objects.all()
        skills_categories_data = SkillsCategorySerializer(skills_categories, many=True).data
        
        skills = Skill.objects.all()
        skills_data = SkillSerializer(skills, many=True).data
        
        # Compile all data
        all_data = {
            'articles': {
                'articles': articles_data,
                'categories': article_categories_data,
                'tags': article_tags_data,
            },
            'webconfig': {
                'settings': web_settings_data,
                'documents': my_documents_data,
                'social_links': social_links_data,
            },
            'pages': pages_data,
            'contact': {
                'forms': contact_forms_data,
                'information': contact_information_data,
            },
            'portfolio': {
                'certificates': certificates_data,
                'project_categories': project_categories_data,
                'projects': projects_data,
                'project_images': project_images_data,
                'experiences': experiences_data,
                'achievement_experiences': achievement_experiences_data,
                'skills_categories': skills_categories_data,
                'skills': skills_data,
            }
        }
        
        return Response({
            'status': 'success',
            'message': 'All data retrieved successfully',
            'data': all_data
        })
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Article Views
@api_view(['GET'])
@permission_classes([AllowAny])
def articles_list(request):
    """Get all published articles"""
    articles = Article.objects.filter(status='published')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def article_detail(request, pk):
    """Get specific article by ID"""
    article = get_object_or_404(Article, pk=pk, status='published')
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def article_categories_list(request):
    """Get all article categories"""
    categories = ArticleCategory.objects.all()
    serializer = ArticleCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def article_tags_list(request):
    """Get all article tags"""
    tags = ArticleTag.objects.all()
    serializer = ArticleTagSerializer(tags, many=True)
    return Response(serializer.data)


# WebConfig Views
@api_view(['GET'])
@permission_classes([AllowAny])
def web_settings_detail(request):
    """Get web settings"""
    settings = WebSetting.objects.first()
    if settings:
        serializer = WebSettingSerializer(settings)
        return Response(serializer.data)
    return Response({'message': 'No web settings found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def my_documents_detail(request):
    """Get my documents"""
    documents = MyDocument.objects.first()
    if documents:
        serializer = MyDocumentSerializer(documents)
        return Response(serializer.data)
    return Response({'message': 'No documents found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def social_links_list(request):
    """Get all social links"""
    links = SocialLink.objects.all()
    serializer = SocialLinkSerializer(links, many=True)
    return Response(serializer.data)


# Pages Views
@api_view(['GET'])
@permission_classes([AllowAny])
def pages_hero_detail(request):
    """Get hero section"""
    hero = SectionHero.objects.first()
    if hero:
        serializer = SectionHeroSerializer(hero)
        return Response(serializer.data)
    return Response({'message': 'No hero section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_about_detail(request):
    """Get about section"""
    about = SectionAbout.objects.first()
    if about:
        serializer = SectionAboutSerializer(about)
        return Response(serializer.data)
    return Response({'message': 'No about section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_certificate_detail(request):
    """Get certificate section"""
    certificate = SectionCertificate.objects.first()
    if certificate:
        serializer = SectionCertificateSerializer(certificate)
        return Response(serializer.data)
    return Response({'message': 'No certificate section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_project_detail(request):
    """Get project section"""
    project = SectionProject.objects.first()
    if project:
        serializer = SectionProjectSerializer(project)
        return Response(serializer.data)
    return Response({'message': 'No project section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_call_to_action_detail(request):
    """Get call to action section"""
    cta = SectionCallToAction.objects.first()
    if cta:
        serializer = SectionCallToActionSerializer(cta)
        return Response(serializer.data)
    return Response({'message': 'No call to action section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_header_experience_detail(request):
    """Get header experience section"""
    header_exp = SectionHeaderExperience.objects.first()
    if header_exp:
        serializer = SectionHeaderExperienceSerializer(header_exp)
        return Response(serializer.data)
    return Response({'message': 'No header experience section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_skills_detail(request):
    """Get skills section"""
    skills = SectionSkills.objects.first()
    if skills:
        serializer = SectionSkillsSerializer(skills)
        return Response(serializer.data)
    return Response({'message': 'No skills section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_article_detail(request):
    """Get article section"""
    article = SectionArticle.objects.first()
    if article:
        serializer = SectionArticleSerializer(article)
        return Response(serializer.data)
    return Response({'message': 'No article section found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny])
def pages_contact_detail(request):
    """Get contact section"""
    contact = SectionContact.objects.first()
    if contact:
        serializer = SectionContactSerializer(contact)
        return Response(serializer.data)
    return Response({'message': 'No contact section found'}, status=status.HTTP_404_NOT_FOUND)


# Contact Views
@api_view(['GET'])
@permission_classes([AllowAny])
def contact_forms_list(request):
    """Get all contact forms"""
    forms = ContactForm.objects.all()
    serializer = ContactFormSerializer(forms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def contact_information_detail(request):
    """Get contact information"""
    info = ContactInformation.objects.first()
    if info:
        serializer = ContactInformationSerializer(info)
        return Response(serializer.data)
    return Response({'message': 'No contact information found'}, status=status.HTTP_404_NOT_FOUND)


# Portfolio Views
@api_view(['GET'])
@permission_classes([AllowAny])
def certificates_list(request):
    """Get all certificates"""
    certificates = Certificate.objects.all()
    serializer = CertificateSerializer(certificates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def project_categories_list(request):
    """Get all project categories"""
    categories = ProjectCategory.objects.all()
    serializer = ProjectCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def projects_list(request):
    """Get all projects"""
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def project_images_list(request):
    """Get all project images"""
    images = ImageProject.objects.all()
    serializer = ImageProjectSerializer(images, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def experiences_list(request):
    """Get all experiences"""
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def achievement_experiences_list(request):
    """Get all achievement experiences"""
    achievements = AchievementExperience.objects.all()
    serializer = AchievementExperienceSerializer(achievements, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def skills_categories_list(request):
    """Get all skills categories"""
    categories = SkillsCategory.objects.all()
    serializer = SkillsCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def skills_list(request):
    """Get all skills"""
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)
