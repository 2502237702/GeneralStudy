# Generated by Django 2.0.1 on 2018-04-01 00:03

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_bannercourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('Beginner', '初级'), ('Medium', '中级'), ('Higher', '高级')], max_length=10, verbose_name='难度'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]