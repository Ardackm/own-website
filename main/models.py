from django.db import models

class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    location = models.CharField(max_length=200, help_text="Örn: İstanbul, Türkiye")
    social_media = models.ManyToManyField('SocialMedia', blank=True)
    
    def __str__(self):
        return self.full_name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    icon = models.CharField(max_length=50, help_text="Font Awesome class name", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # Sıralama için eklendi
    
    class Meta:
        ordering = ['order']  # Varsayılan sıralama
    
    def __str__(self):
        return self.name

# Removed entire Project class

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.position} at {self.company}"

# Education model kaldırıldı

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Font Awesome class name (örn: fab fa-github)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Social Media Links'

    def __str__(self):
        return self.name