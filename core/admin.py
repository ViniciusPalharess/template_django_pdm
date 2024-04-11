"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Acessorio, Categoria, Cor, Marca, User
from django.contrib import admin
from .models import Acessorio
from core import models




class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["Nacionalidade", "name"]
    fieldsets = (
        (None, {"fields": ("Nacionalidade", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "Nacionalidade",
                    "password1",
                    "password2",
                    "name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

@admin.register(Cor)
class corAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

@admin.register(Acessorio)
class AcessorioAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'cor', 'categoria')
    search_fields = ('categoria', 'cor__nome', 'categoria__descricao')
    list_filter = ('cor', 'categoria')
    ordering = ('categoria', 'cor', 'categoria')
    list_per_page = 25


class UserAdmin(UserAdmin):
    fields: tuple = ("first_name", "last_name", "foto")


from core.models import Compra

admin.site.register(Compra)
admin.site.register(User)
