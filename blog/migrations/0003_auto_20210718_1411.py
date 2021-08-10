# Generated by Django 3.2.5 on 2021-07-18 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_model_title_post_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_contents',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]