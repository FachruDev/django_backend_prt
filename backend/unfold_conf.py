from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

UNFOLD = {
    "SITE_TITLE": "Admin Panel",
    "SITE_HEADER": "Project Prt",
    "SITE_SUBHEADER": "Backend admin",
    "SITE_URL": "/",
    "SITE_SYMBOL": "speed",
    
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": True,
    "SHOW_LANGUAGES": True,
    
    "SITE_DROPDOWN": [
        {
            "icon": "diamond",
            "title": _("My site link"),
            "link": "https://webptr.com",
        },
        {
            "icon": "diamond",
            "title": _("My site page"),
            "link": reverse_lazy("admin:index"),
        },
    ],

    "SIDEBAR": {
        "navigation": [
            {
                "title": _("Main Navigation"),
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("Article Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Articles"),
                        "link": reverse_lazy("admin:article_article_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "link": reverse_lazy("admin:article_articlecategory_changelist"),
                    },
                    {
                        "title": _("Tags"),
                        "link": reverse_lazy("admin:article_articletag_changelist"),
                    },
                ],
            },
            {
                "title": _("Web Configuration"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Web Settings"),
                        "link": reverse_lazy("admin:webconfig_websetting_changelist"),
                    },
                    {
                        "title": _("Social Link"),
                        "link": reverse_lazy("admin:webconfig_sociallink_changelist"),
                    },
                    {
                        "title": _("My Document"),
                        "link": reverse_lazy("admin:webconfig_mydocument_changelist"),
                    },
                ],
            },
            {
                "title": _("Contact"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Contact Form"),
                        "link": reverse_lazy("admin:contact_contactform_changelist"),
                    },
                    {
                        "title": _("Contact Information"),
                        "link": reverse_lazy("admin:contact_contactinformation_changelist"),
                    },
                ],
            },
        ],
    },
    
    "BORDER_RADIUS": "6px",
    "COLORS": {
        "base": {
            "50": "249, 250, 251",
            "100": "243, 244, 246",
            "200": "229, 231, 235",
            "300": "209, 213, 219",
            "400": "156, 163, 175",
            "500": "107, 114, 128",
            "600": "75, 85, 99",
            "700": "55, 65, 81",
            "800": "31, 41, 55",
            "900": "17, 24, 39",
            "950": "3, 7, 18",
        },
        "primary": {
            "50": "250, 245, 255",
            "100": "243, 232, 255",
            "200": "233, 213, 255",
            "300": "216, 180, 254",
            "400": "192, 132, 252",
            "500": "168, 85, 247",
            "600": "147, 51, 234",
            "700": "126, 34, 206",
            "800": "107, 33, 168",
            "900": "88, 28, 135",
            "950": "59, 7, 100",
        },
        "font": {
            "subtle-light": "var(--color-base-500)",  # text-base-500
            "subtle-dark": "var(--color-base-400)",  # text-base-400
            "default-light": "var(--color-base-600)",  # text-base-600
            "default-dark": "var(--color-base-300)",  # text-base-300
            "important-light": "var(--color-base-900)",  # text-base-900
            "important-dark": "var(--color-base-100)",  # text-base-100
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "id": "🇮🇩",
            },
        },
    },
}