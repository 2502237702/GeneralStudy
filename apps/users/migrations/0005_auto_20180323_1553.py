# Generated by Django 2.0.1 on 2018-03-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180321_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]