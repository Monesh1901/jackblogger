# Generated by Django 2.1.5 on 2021-08-07 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='mail',
        ),
    ]
