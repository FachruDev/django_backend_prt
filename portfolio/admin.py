from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    Certificate, ProjectCategory, Project, ImageProject,
    Experience, AchievementExperience, SkillsCategory, Skill
)
from unfold.contrib.forms.widgets import WysiwygWidget
from modeltranslation.admin import TabbedTranslationAdmin

class ImageProjectInline(admin.TabularInline):
    model = ImageProject
    extra = 1
    fields = ('image', 'featured_image_url', 'featured_image_alt')

class AchievementExperienceInline(admin.TabularInline):
    model = AchievementExperience
    extra = 1
    fields = ('description',)
    formfield_overrides = {
        AchievementExperience.description.field: {'widget': WysiwygWidget},
    }

@admin.register(Certificate)
class CertificateAdmin(ModelAdmin):
    list_display = ('title', 'issuedby', 'issuedon', 'valid_until')
    list_filter = ('issuedby', 'issuedon', 'valid_until')
    search_fields = ('title', 'subtitle', 'issuedby', 'credential_id')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'issuedby', 'issuedon', 'valid_until', 'credential_id')
        }),
        ('Files', {
            'fields': ('certificate_image', 'pdf_certificate'),
            'classes': ('collapse',)
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Sertifikat', 'fields': ['title', 'subtitle', 'issuedby', 'issuedon', 'valid_until', 'credential_id']},
            {'title': 'File Sertifikat', 'fields': ['certificate_image', 'pdf_certificate'], 'collapsible': True},
        ],
    }

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Informasi Kategori', 'fields': ['title']},
        ],
    }

@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'subtitle', 'category', 'issued_on', 'role')
    list_filter = ('category', 'issued_on')
    search_fields = ('title', 'subtitle', 'description', 'role')
    list_per_page = 25
    inlines = [ImageProjectInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'issued_on', 'role', 'category')
        }),
    )

    formfield_overrides = {
        Project.description.field: {'widget': WysiwygWidget},
    }

    unfold = {
        'list_display_links': ('title',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Proyek', 'fields': ['title', 'subtitle', 'description', 'issued_on', 'role', 'category']},
        ],
    }

@admin.register(ImageProject)
class ImageProjectAdmin(ModelAdmin):
    list_display = ('project', 'featured_image_alt')
    list_filter = ('project',)
    search_fields = ('project__title', 'featured_image_alt', 'featured_image_url')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('project', 'image', 'featured_image_url', 'featured_image_alt')
        }),
    )

    unfold = {
        'list_display_links': ('project',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Gambar', 'fields': ['project', 'image', 'featured_image_url', 'featured_image_alt']},
        ],
    }

@admin.register(Experience)
class ExperienceAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('title', 'company', 'work_on', 'company_location')
    list_filter = ('company',)
    search_fields = ('title', 'role', 'company', 'work_on', 'company_location')
    list_per_page = 25
    inlines = [AchievementExperienceInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'role', 'company', 'work_on', 'company_location')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Pengalaman', 'fields': ['title', 'role', 'company', 'work_on', 'company_location']},
        ],
    }

@admin.register(AchievementExperience)
class AchievementExperienceAdmin(TabbedTranslationAdmin, ModelAdmin):
    list_display = ('experience', 'description')
    list_filter = ('experience',)
    search_fields = ('experience__title', 'description')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('experience', 'description')
        }),
    )

    formfield_overrides = {
        AchievementExperience.description.field: {'widget': WysiwygWidget},
    }

    unfold = {
        'list_display_links': ('experience',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Pencapaian', 'fields': ['experience', 'description']},
        ],
    }

@admin.register(SkillsCategory)
class SkillsCategoryAdmin(ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title', 'icon')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'icon')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Informasi Kategori Skill', 'fields': ['title', 'icon']},
        ],
    }

@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('title', 'category', 'status', 'percentage')
    list_filter = ('category', 'status')
    search_fields = ('title', 'category__title', 'status')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'percentage', 'status', 'icon', 'category', 'projects', 'certificates')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Skill', 'fields': ['title', 'percentage', 'status', 'icon', 'category', 'projects', 'certificates']},
        ],
    }