from django.db import models


class Article(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
