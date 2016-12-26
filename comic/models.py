from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='comics', blank=True, null=True)

    def __str__(self):
        return self.title



class HeaderImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title    

        