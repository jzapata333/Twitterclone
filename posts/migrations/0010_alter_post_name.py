# Generated by Django 3.2.6 on 2021-09-09 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=20, verbose_name='Name'),
        ),
    ]
