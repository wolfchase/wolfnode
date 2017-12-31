from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']


class Post(models.Model):
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    content = models.TextField(blank=True)
    publish_date = models.DateField()
    edit_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['publish_date']
