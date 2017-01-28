from django.db import models
from django.utils import timezone


class Cast(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='cast', blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='issues', blank=True, null=True)
    issue_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comic(models.Model):
    MAX_PAGES_PER_ISSUE = 1000
    sort_number = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True )
    title = models.CharField(max_length=200, blank=True, null=True)
    issue = models.ForeignKey(Issue, blank=True, null=True)
    image = models.ImageField(upload_to='comics', blank=True, null=True)
    date_added = models.DateTimeField(
        help_text="Posted on: ",
        default = timezone.now, null=True, blank=True 
    )
    cast_members = models.ManyToManyField(Cast, related_name="comics", blank=True)

    class Meta:
        ordering = ['-sort_number', '-date_added']

    def __str__(self):
        return self.title

    @staticmethod
    def sortOrder(issue, page_number):
        return int(issue) * Comic.MAX_PAGES_PER_ISSUE + int(page_number)
        

    def save(self, *args, **kwargs):
        self.sort_number = self.issue * self.MAX_PAGES_PER_ISSUE + self.page_number
        super(Comic, self).save(*args, **kwargs) # Call the "real" save() method.


class HeaderImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title    

        