from django.db import models
from django.utils import timezone
from django.conf import settings

def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s/%s.%s'%(instance.author.username, pid, extension)

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to= user_path, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'