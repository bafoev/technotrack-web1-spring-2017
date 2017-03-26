# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Category(models.Model):
    blog = models.ManyToManyField('Blog', related_name='blogs')
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Категория #{id}: {name}'.format(id=self.id, name=self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-created_at',)


class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField('Category', related_name='categories')
    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Блог #{id}: {title}'.format(id=self.id, title=self.title)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('-created_at',)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog')

    title = models.CharField(max_length=255)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Пост #{id}: {title}'.format(id=self.id, title=self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey(Post, related_name='likes')

    def __str__(self):
        return 'Лайк #{id}: от "{author}" к посту "{post}"'.format(id=self.id, author=self.author, post=self.post)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ('-created_at',)
