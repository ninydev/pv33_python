from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings  # Правильный способ сослаться на кастомного юзера


class Post(models.Model):
    # ForeignKey - это связь "Один ко многим". У поста один автор, но у автора много постов.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ManyToMany - "Многие ко многим". Один юзер лайкает много постов, у поста много лайков.
    # blank=True означает, что пост может существовать и без лайков.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title  # Так пост будет красиво называться в админке

    # Метод-помощник для быстрого подсчета лайков
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    # Комментарий жестко привязан и к посту, и к автору
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.post.title}"