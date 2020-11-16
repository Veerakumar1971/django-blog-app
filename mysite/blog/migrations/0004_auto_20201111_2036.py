# Generated by Django 3.1.3 on 2020-11-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_video_caption'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.AddField(
            model_name='post',
            name='clip',
            field=models.FileField(null=True, upload_to='videos/'),
        ),
    ]
