# Generated by Django 4.2.2 on 2023-06-27 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_remove_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date_time',
            field=models.DateTimeField(auto_now_add=True, default='2023-06-27 02:42:52.868671+00:00'),
            preserve_default=False,
        ),
    ]
