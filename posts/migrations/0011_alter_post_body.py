# Generated by Django 3.2.6 on 2021-09-09 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, db_index=True, max_length=280, null=True, verbose_name='Body'),
        ),
    ]
