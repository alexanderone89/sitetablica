from django import forms
from django.contrib import admin, auth

# Register your models here.
from django.contrib import admin


from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy

from .models import Post, Settings, Servise, Socials, MyColorField, Colors


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "image", "title", "enabled")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width: 200px">')


class SettingsAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_logo", "preview_background"]
    list_display = ("theme", "nick", "description", "logo", "background", "enabled")
    formfield_overrides = {
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
    }

    def save_model(self, request, obj, form, change):
        Settings.objects.filter(enabled=True).update(enabled=not obj.enabled)
        obj.save()

    def preview_logo(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 200px">')

    def preview_background(self, obj):
        return mark_safe(f'<img src="{obj.background.url}" style="max-width: 200px">')

    # def color1_field(self, obj):
    #     return mark_safe(f'<input value = "#3399FF80" >')


class ServiseAdmin(admin.ModelAdmin):
    list_display = ("title","description","price","enabled")


class SocialsAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_logo"]
    list_display = ("preview_logo2", "title","url_account", "enabled")

    def preview_logo(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 200px">')

    def preview_logo2(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 20px">')

class ColorsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},
        MyColorField: {'widget': forms.TextInput(attrs={'type': 'color', 'style': 'width: 50px; height: 50px;'})},

    }




admin.site.site_header = gettext_lazy('Админ панель')
admin.site.site_title = gettext_lazy('Админ панель')

admin.site.register(Post, PostAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Servise, ServiseAdmin)
admin.site.register(Socials, SocialsAdmin)
admin.site.register(Colors, ColorsAdmin)


admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)