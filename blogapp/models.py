from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tags")

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
