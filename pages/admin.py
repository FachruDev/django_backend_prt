from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import (
    SectionHero, SectionAbout, SectionCertificate, SectionProject,
    SectionCallToAction, SectionHeaderExperience, SectionSkills,
    SectionArticle, SectionContact
)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(SectionHero)
class SectionHeroAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Hero Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionAbout)
class SectionAboutAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle', 'description')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle', 'description', 'profile')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'About Content', 'fields': ['title', 'subtitle', 'description', 'profile']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionCertificate)
class SectionCertificateAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Certificate Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionProject)
class SectionProjectAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Project Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionCallToAction)
class SectionCallToActionAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Call to Action Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionHeaderExperience)
class SectionHeaderExperienceAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Header Experience Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionSkills)
class SectionSkillsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Skills Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionArticle)
class SectionArticleAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Article Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")

@admin.register(SectionContact)
class SectionContactAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('title', 'subtitle')
        }),
    )

    unfold = {
        'list_display_links': ('title',),
        'form_layout': [
            {'title': 'Contact Content', 'fields': ['title', 'subtitle']},
        ],
    }

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if self.model.objects.exists():
            obj = self.model.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.model.objects.exists():
            return qs.filter(pk=self.model.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not self.model.objects.exists() or obj == self.model.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one instance is allowed.")