# Generated by Django 2.1.5 on 2019-02-06 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_post_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSetingFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлено')),
                ('post', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
            options={
                'verbose_name': 'Отправленный эмейл',
                'verbose_name_plural': 'Отправленные эмейлы',
            },
        ),
    ]