from django.db import models
# from users.models import UserProfile
from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse





class Post(models.Model):
    #
    user = models.ForeignKey(User, blank=True, default=None,on_delete=models.CASCADE)
    name = models.CharField("Название",max_length=128,blank=True, null=True, default=None)
    header = models.CharField("Заголовок",max_length=128,blank=True, null=True, default=None)
    text = models.TextField("Текст",max_length=1280)
    read = models.BooleanField(default=False)
    sub = models.BooleanField(default=False)




    created = models.DateTimeField("Создан",auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обнавлено",auto_now_add=False, auto_now=True)









    def __str__(self):
        return " %s" % self.name

    class Meta:

        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Users(models.Model):


    user = models.ManyToManyField(User, blank=True,  default=None)
    post = models.ForeignKey(Post, blank=True, default=None,on_delete=models.CASCADE)



    def __str__(self):
        return " %s" % self.user

    class Meta:
        verbose_name = 'Подписки'
        verbose_name_plural = 'Подписки'