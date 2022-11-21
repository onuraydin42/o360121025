from django.contrib import admin
from .models import Post
from .models import Personal
from .models import Professional
from .models import Business

class PersonelAdmin(admin.ModelAdmin):
    list_display = ("title","price","active_project","project_max","image","descripton","is_active","is_home")
    list_editable = ("is_active","is_home")
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("title","price","active_project","project_max","image","descripton","is_active","is_home")
    list_editable = ("is_active","is_home")
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("title","price","active_project","project_max","image","descripton","is_active","is_home")
    list_editable = ("is_active","is_home")

admin.site.register(Post)
admin.site.register(Personal, PersonelAdmin)
admin.site.register(Professional, ProfessionalAdmin)
admin.site.register(Business, BusinessAdmin)