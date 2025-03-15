from django.contrib import admin
from .models import PersonalInfo, Skill, Experience, Contact, SocialMedia

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'order')
    list_editable = ('order',)  # Sıralamayı liste görünümünde düzenlenebilir yap
    ordering = ('order',)  # Varsayılan sıralama

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current',)

# Education admin kaydı kaldırıldı

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon', 'order')
    list_editable = ('order',)
    ordering = ('order',)