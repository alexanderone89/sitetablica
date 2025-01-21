from django.contrib import admin, auth

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy

from .models import Post, Settings, Servise, Socials


class MyAdminSite(admin.AdminSite):
    site_title = gettext_lazy('111111111111')

    # Text to put in each page's <h1> (and above login form).
    site_header = gettext_lazy('222222222222')

    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('333333333333333')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "image", "title", "enabled")

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width: 200px">')

class SettingsAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_logo", "preview_background"]
    list_display = ("theme", "nick", "description", "logo", "background", "enabled")

    def save_model(self, request, obj, form, change):
        Settings.objects.filter(enabled=True).update(enabled=not obj.enabled)
        obj.save()

    def preview_logo(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 200px">')

    def preview_background(self, obj):
        return mark_safe(f'<img src="{obj.background.url}" style="max-width: 200px">')


class ServiseAdmin(admin.ModelAdmin):
    list_display = ("title","description","price","enabled")

class SocialsAdmin(admin.ModelAdmin):
    readonly_fields = ["preview_logo"]
    list_display = ("preview_logo2", "title","url_account", "enabled")

    def preview_logo(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 200px">')

    def preview_logo2(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="max-width: 20px">')


admin.site.register(Post, PostAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(Servise, ServiseAdmin)
admin.site.register(Socials, SocialsAdmin)

admin.site.site_header = gettext_lazy('Админ панель')
admin.site.site_title = gettext_lazy('Админ панель')

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)