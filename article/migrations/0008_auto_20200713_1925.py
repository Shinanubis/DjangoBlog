# Generated by Django 2.2.12 on 2020-07-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200713_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='article/static/img/cover'),
        ),
    ]
