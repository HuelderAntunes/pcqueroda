# Generated by Django 3.0.7 on 2020-06-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='developer',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='publisher',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
