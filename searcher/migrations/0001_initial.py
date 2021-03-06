# Generated by Django 3.0.7 on 2020-07-09 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('acronym', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='computers')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Notebook', 'Notebook'), ('Desktop', 'Desktop'), ('Apple', 'Apple'), ('Other', 'Other')], max_length=100)),
                ('manufacturer', models.CharField(blank=True, max_length=150, null=True)),
                ('affiliate_link', models.URLField()),
                ('price', models.FloatField()),
                ('graphics_level', models.IntegerField(choices=[(1, 'Lower Intel/GT/Vega'), (2, 'Medium Intel/GT/Vega'), (3, 'Higher Intel/GT/Vega'), (4, 'Lower Intel/GTX/Radeon'), (5, 'Intel/GTX/Radeon'), (6, 'Higher GTX/Radeon'), (5, 'Lower RTX/Radeon'), (6, 'Medium RTX/Radeon'), (7, 'Higher RTX/Radeon'), (8, 'Lower Titan/Radeon'), (9, 'Medium Titan/Radeon'), (10, 'Higher Titan/Radeon')])),
                ('processor_level', models.IntegerField(choices=[(1, 'Lower Pentium/Athlon'), (2, 'Higher Pentium/Athlon'), (3, 'Lower i3/Ryzen/FX'), (4, 'Higher i3/Ryzen/FX'), (5, 'Lower i5/Ryzen/FX'), (6, 'Higher i5/Ryzen/FX'), (7, 'Lower i7/Ryzen/FX'), (8, 'Higher i7/Ryzen/FX'), (9, 'Lower i9/Ryzen'), (10, 'Higher i9/Ryzen')])),
                ('memory_level', models.IntegerField(choices=[(1, '1GB'), (2, '2GB'), (3, '4GB'), (4, '6GB'), (5, '8GB'), (6, '12GB'), (7, '14GB'), (8, '16GB'), (9, '32GB'), (10, '64GB+')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('acronym', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='softwares')),
                ('sinopse', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('A', 'A'), ('AA', 'AA'), ('AAA', 'AAA')], max_length=3, null=True)),
                ('item_type', models.CharField(blank=True, choices=[('Game', 'Game'), ('Software', 'Software'), ('Other', 'Other')], max_length=30, null=True)),
                ('developer', models.CharField(blank=True, max_length=150, null=True)),
                ('publisher', models.CharField(blank=True, max_length=150, null=True)),
                ('website', models.CharField(blank=True, max_length=150, null=True)),
                ('min_graphics_level', models.IntegerField(choices=[(1, 'Lower Intel/GT/Vega'), (2, 'Medium Intel/GT/Vega'), (3, 'Higher Intel/GT/Vega'), (4, 'Lower Intel/GTX/Radeon'), (5, 'Intel/GTX/Radeon'), (6, 'Higher GTX/Radeon'), (5, 'Lower RTX/Radeon'), (6, 'Medium RTX/Radeon'), (7, 'Higher RTX/Radeon'), (8, 'Lower Titan/Radeon'), (9, 'Medium Titan/Radeon'), (10, 'Higher Titan/Radeon')])),
                ('min_processor_level', models.IntegerField(choices=[(1, 'Lower Pentium/Athlon'), (2, 'Higher Pentium/Athlon'), (3, 'Lower i3/Ryzen/FX'), (4, 'Higher i3/Ryzen/FX'), (5, 'Lower i5/Ryzen/FX'), (6, 'Higher i5/Ryzen/FX'), (7, 'Lower i7/Ryzen/FX'), (8, 'Higher i7/Ryzen/FX'), (9, 'Lower i9/Ryzen'), (10, 'Higher i9/Ryzen')])),
                ('min_memory_level', models.IntegerField(choices=[(1, '1GB'), (2, '2GB'), (3, '4GB'), (4, '6GB'), (5, '8GB'), (6, '12GB'), (7, '14GB'), (8, '16GB'), (9, '32GB'), (10, '64GB+')])),
                ('max_graphics_level', models.IntegerField(choices=[(1, 'Lower Intel/GT/Vega'), (2, 'Medium Intel/GT/Vega'), (3, 'Higher Intel/GT/Vega'), (4, 'Lower Intel/GTX/Radeon'), (5, 'Intel/GTX/Radeon'), (6, 'Higher GTX/Radeon'), (5, 'Lower RTX/Radeon'), (6, 'Medium RTX/Radeon'), (7, 'Higher RTX/Radeon'), (8, 'Lower Titan/Radeon'), (9, 'Medium Titan/Radeon'), (10, 'Higher Titan/Radeon')])),
                ('max_processor_level', models.IntegerField(choices=[(1, 'Lower Pentium/Athlon'), (2, 'Higher Pentium/Athlon'), (3, 'Lower i3/Ryzen/FX'), (4, 'Higher i3/Ryzen/FX'), (5, 'Lower i5/Ryzen/FX'), (6, 'Higher i5/Ryzen/FX'), (7, 'Lower i7/Ryzen/FX'), (8, 'Higher i7/Ryzen/FX'), (9, 'Lower i9/Ryzen'), (10, 'Higher i9/Ryzen')])),
                ('max_memory_level', models.IntegerField(choices=[(1, '1GB'), (2, '2GB'), (3, '4GB'), (4, '6GB'), (5, '8GB'), (6, '12GB'), (7, '14GB'), (8, '16GB'), (9, '32GB'), (10, '64GB+')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
