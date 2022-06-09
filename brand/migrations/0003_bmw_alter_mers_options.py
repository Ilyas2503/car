# Generated by Django 4.0.5 on 2022-06-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_alter_mers_options_mers_color_mers_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('value', models.FloatField()),
                ('color', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'BMW',
                'verbose_name_plural': 'BMW',
            },
        ),
        migrations.AlterModelOptions(
            name='mers',
            options={'verbose_name': 'Мерс', 'verbose_name_plural': 'Мерс'},
        ),
    ]
