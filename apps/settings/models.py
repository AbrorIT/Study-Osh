from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class About(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "о нас"

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_image")
    image = models.ImageField(upload_to = "about_image/")


    class Meta:
        verbose_name = "Фото о нас"
        verbose_name_plural = "Фото о нас"