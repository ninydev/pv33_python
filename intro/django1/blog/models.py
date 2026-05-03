from django.db import models
from django.conf import settings  # Правильный способ сослаться на кастомного юзера


def post_thumbnail_upload_to(instance, filename):
    """Upload function that places thumbnails into a folder named by the Post id.

    If the instance has no pk yet (not saved), return a temporary path. The
    Post.save override below will handle saving the file to the final folder
    once the instance has an id.
    """
    if instance.pk:
        return f'post_thumbnails/{instance.pk}/{filename}'
    return f'post_thumbnails/temp/{filename}'


class Post(models.Model):
    # ForeignKey - это связь "Один ко многим". У поста один автор, но у автора много постов.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to=post_thumbnail_upload_to, blank=True, null=True)

    # ManyToMany - "Многие ко многим". Один юзер лайкает много постов, у поста много лайков.
    # blank=True означает, что пост может существовать и без лайков.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title  # Так пост будет красиво называться в админке

    # Метод-помощник для быстрого подсчета лайков
    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        """Ensure that uploaded thumbnail is stored under a folder with the post id.

        If the instance is new and a thumbnail was provided, we first save the
        instance without the file to get a primary key, then attach the file and
        save again so the callable upload_to can use the instance.pk in the path.
        """
        # If new object (no pk) and there's a thumbnail file provided, do two-step save
        if not self.pk and self.thumbnail:
            thumb = self.thumbnail
            # Temporarily clear the file to get a pk
            self.thumbnail = None
            super().save(*args, **kwargs)
            # Re-assign the file and save again so upload_to sees the pk
            self.thumbnail = thumb
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class Comment(models.Model):
    # Комментарий жестко привязан и к посту, и к автору
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"