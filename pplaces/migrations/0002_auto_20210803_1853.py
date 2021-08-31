# Generated by Django 3.2.6 on 2021-08-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pplaces', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priorityplacesref',
            name='PriorityPlaceNameFrench',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Priority Place (Fr)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='GeneralLocationDescriptonEnglish',
            field=models.TextField(blank=True, null=True, verbose_name='General Location (En)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='GeneralLocationDescriptonFrench',
            field=models.TextField(blank=True, null=True, verbose_name='General Location (Fr)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectPurposeDescriptonEnglish',
            field=models.TextField(blank=True, null=True, verbose_name='Description (En)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectPurposeDescriptonFrench',
            field=models.TextField(blank=True, null=True, verbose_name='Description (Fr)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ProjectTitleFrench',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title (Fr)'),
        ),
        migrations.AlterField(
            model_name='projectlocation',
            name='ProjectLocationGeneralDescriptonEnglish',
            field=models.TextField(blank=True, null=True, verbose_name='Description (En)'),
        ),
        migrations.AlterField(
            model_name='projectlocation',
            name='ProjectLocationGeneralDescriptonFrench',
            field=models.TextField(blank=True, null=True, verbose_name='Description (Fr)'),
        ),
        migrations.AlterField(
            model_name='projectlocation',
            name='ProjectLocationNameFrench',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name (Fr)'),
        ),
        migrations.AlterField(
            model_name='projectlocation',
            name='ProjectLocationShapeFileSource',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Source'),
        ),
    ]