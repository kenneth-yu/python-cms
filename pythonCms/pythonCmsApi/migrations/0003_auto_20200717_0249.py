# Generated by Django 3.0.7 on 2020-07-17 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonCmsApi', '0002_auto_20200717_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='pageId',
            new_name='websiteId',
        ),
    ]
