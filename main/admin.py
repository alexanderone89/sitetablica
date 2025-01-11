from django.contrib import admin, auth

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy

from .models import Post

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


admin.site.register(Post, PostAdmin)
admin.site.site_header = gettext_lazy('Админ панель')
admin.site.site_title = gettext_lazy('Админ панель')

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)