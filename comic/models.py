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
    last_page = models.IntegerField(blank=True, null=True)
    page_number = models.IntegerField(blank=True, null=True )
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

    def lastPage(last_page, page_number):
        comics = Comic.objects.all()
        for comic in comics: 
            if comic.last_page is None or comic.last_page < page_number:
                comic.last_page = page_number
                print('COMIC: ', comic.last_page)
                # comic.save()
        # if page_number > last_page: 
            # last_page = page_number
        # return last_page

    def save(self, *args, **kwargs):
        self.sort_number = Comic.sortOrder(self.page_number)
        self.last_page = Comic.lastPage(self.last_page, self.page_number)
        # print('SORT NUMBER: ', sort_number)
        super(Comic, self).save(*args, **kwargs) # Call the "real" save() method.


class HeaderImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title    

