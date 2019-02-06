from django.db import models
from blog.models import *
class EmailSetingFact(models.Model):
    name=models.CharField(max_length=128,blank=True, null=True, default=None)
    email=models.EmailField()
    post=models.ForeignKey(Post,blank=True, null=True, default=None,on_delete=models.CASCADE)



    created = models.DateTimeField("Создан",auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обнавлено",auto_now_add=False, auto_now=True)




    def __str__(self):
        return " %s" % self.name

    class Meta:

        verbose_name = 'Отправленный эмейл'
        verbose_name_plural = 'Отправленные эмейлы'
