from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ContactForm, ContactInformation
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse

@admin.register(ContactForm)
class ContactFormAdmin(ModelAdmin):
    list_display = ('email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('email', 'subject', 'message')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    unfold = {
        'list_display_links': ('email', 'subject'),
        'list_filter_position': 'sidebar',
        'form_layout': [
            {'title': 'Informasi Pesan', 'fields': ['email', 'subject', 'message']},
            {'title': 'Metadata', 'fields': ['created_at'], 'collapsible': True},
        ],
    }

@admin.register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    list_display = ('email_address', 'phone', 'location')
    search_fields = ('email_address', 'phone', 'location')
    list_per_page = 25

    fieldsets = (
        (None, {
            'fields': ('email_address', 'phone', 'location')
        }),
    )

    unfold = {
        'list_display_links': ('email_address',),
        'form_layout': [
            {'title': 'Informasi Kontak', 'fields': ['email_address', 'phone', 'location']},
        ],
    }

    def has_add_permission(self, request):
        return not ContactInformation.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        if ContactInformation.objects.exists():
            obj = ContactInformation.objects.first()
            return HttpResponseRedirect(
                reverse('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), args=[obj.pk])
            )
        return super().changelist_view(request, extra_context)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if ContactInformation.objects.exists():
            return qs.filter(pk=ContactInformation.objects.first().pk)
        return qs

    def save_model(self, request, obj, form, change):
        if not ContactInformation.objects.exists() or obj == ContactInformation.objects.first():
            super().save_model(request, obj, form, change)
        else:
            raise PermissionDenied("Only one ContactInformation instance is allowed.")