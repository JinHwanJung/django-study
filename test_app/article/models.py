from django.db import models


class Article(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
