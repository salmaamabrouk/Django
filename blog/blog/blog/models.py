from django.db import models
from django.contrib.auth.models import user

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date_published = models.DateField(auto_now = True)
    owner = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(user, on_delete = models.DO_NOTHING)
    post = models.OneToOneField(Post, on_delete = models.DO_NOTHING)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.post.title + " : " + self.body