# Generated by Django 3.2.5 on 2021-07-14 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_post_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
