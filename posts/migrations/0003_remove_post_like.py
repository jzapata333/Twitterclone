# Generated by Django 3.2.6 on 2021-09-02 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
