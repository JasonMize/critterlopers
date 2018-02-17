from django.db import models
from django.utils import timezone
from pprint import pprint

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
    last_page = models.IntegerField(default=1)
    title = models.CharField(max_length=200, blank=True, null=True)
    issue = models.ForeignKey(Issue, blank=True, null=True, on_delete=models.DO_NOTHING)
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
    def sortOrder(page_number):
        # TODO: ADD ISSUE 3 LOGIC WHEN WE GET THERE
        if int(page_number) < 33:
            issue_num = 1
        else:
            issue_num = 2
        # print('ISSUE NUM: ', issue_num)
        order = issue_num * Comic.MAX_PAGES_PER_ISSUE + int(page_number) 
        # print ('SORT ORDER: ', order)
        return order

    def save(self, *args, **kwargs):
        self.sort_number = Comic.sortOrder(self.page_number)
        super(Comic, self).save(*args, **kwargs) # Call the "real" save() method.



class ComicManager(models.Model):
    last_page = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = ("Comic Manager")

    def __str__(self):
        return str(self.last_page)

    def save(self, *args, **kwargs):
        super(ComicManager, self).save(*args, **kwargs)
        # TODO - automate this so that anytime a comic is saved it checks last page status and runs here
        # update all Comic instances to have this last page
        comics = Comic.objects.all()
        for comic in comics:
            if comic.last_page < self.last_page:
                comic.last_page = self.last_page
                comic.save()



class HeaderImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    class Meta: 
        verbose_name_plural = ('Header Images')

    def __str__(self):
        return self.title

