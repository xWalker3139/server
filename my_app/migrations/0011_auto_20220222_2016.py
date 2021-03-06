# Generated by Django 3.1.5 on 2022-02-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_auto_20220222_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_name',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, null=True)),
                ('last_name', models.CharField(max_length=264, null=True)),
                ('comment', models.TextField(max_length=10000, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.post')),
            ],
        ),
    ]
