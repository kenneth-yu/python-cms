# Generated by Django 3.0.7 on 2020-07-17 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pythonCmsApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name_plural': 'user models'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='components',
        ),
        migrations.RemoveField(
            model_name='website',
            name='pages',
        ),
        migrations.AddField(
            model_name='component',
            name='pageId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pythonCmsApi.Page'),
        ),
        migrations.AddField(
            model_name='page',
            name='pageId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pythonCmsApi.Website'),
        ),
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='ownerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pythonCmsApi.UserModel'),
        ),
        migrations.AlterField(
            model_name='component',
            name='content',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='fieldName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='testing',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
