# Generated by Django 3.2.5 on 2021-07-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/thumbnails'),
        ),
    ]
