# Generated by Django 3.1.5 on 2022-02-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_remove_comment_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='first_name',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
