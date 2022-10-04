from django.contrib import admin 
from apps.settings.models import Setting, About, AboutImage

# Register your models here.

admin.site.register(Setting)
admin.site.register(About)
admin.site.register(AboutImage)