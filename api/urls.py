from django.urls import path
from . import views

urlpatterns = [
    # API Overview
    path('', views.api_overview, name='api-overview'),
    
    # All Data Endpoint
    path('all-data/', views.all_data, name='all-data'),
    
    # Article URLs
    path('articles/', views.articles_list, name='articles-list'),
    path('articles/<int:pk>/', views.article_detail, name='article-detail'),
    path('article-categories/', views.article_categories_list, name='article-categories-list'),
    path('article-tags/', views.article_tags_list, name='article-tags-list'),
    
    # WebConfig URLs
    path('web-settings/', views.web_settings_detail, name='web-settings-detail'),
    path('my-documents/', views.my_documents_detail, name='my-documents-detail'),
    path('social-links/', views.social_links_list, name='social-links-list'),
    
    # Pages URLs
    path('pages/hero/', views.pages_hero_detail, name='pages-hero-detail'),
    path('pages/about/', views.pages_about_detail, name='pages-about-detail'),
    path('pages/certificate/', views.pages_certificate_detail, name='pages-certificate-detail'),
    path('pages/project/', views.pages_project_detail, name='pages-project-detail'),
    path('pages/call-to-action/', views.pages_call_to_action_detail, name='pages-call-to-action-detail'),
    path('pages/header-experience/', views.pages_header_experience_detail, name='pages-header-experience-detail'),
    path('pages/skills/', views.pages_skills_detail, name='pages-skills-detail'),
    path('pages/article/', views.pages_article_detail, name='pages-article-detail'),
    path('pages/contact/', views.pages_contact_detail, name='pages-contact-detail'),
    
    # Contact URLs
    path('contact/forms/', views.contact_forms_list, name='contact-forms-list'),
    path('contact/information/', views.contact_information_detail, name='contact-information-detail'),
    
    # Portfolio URLs
    path('portfolio/certificates/', views.certificates_list, name='certificates-list'),
    path('portfolio/project-categories/', views.project_categories_list, name='project-categories-list'),
    path('portfolio/projects/', views.projects_list, name='projects-list'),
    path('portfolio/project-images/', views.project_images_list, name='project-images-list'),
    path('portfolio/experiences/', views.experiences_list, name='experiences-list'),
    path('portfolio/achievement-experiences/', views.achievement_experiences_list, name='achievement-experiences-list'),
    path('portfolio/skills-categories/', views.skills_categories_list, name='skills-categories-list'),
    path('portfolio/skills/', views.skills_list, name='skills-list'),
]
