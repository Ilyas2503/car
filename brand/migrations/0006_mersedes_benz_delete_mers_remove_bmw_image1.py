# Generated by Django 4.0.5 on 2022-06-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0005_bmw_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mersedes_Benz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('value', models.FloatField()),
                ('color', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Мерс',
                'verbose_name_plural': 'Мерс',
            },
        ),
        migrations.DeleteModel(
            name='Mers',
        ),
        migrations.RemoveField(
            model_name='bmw',
            name='image1',
        ),
    ]
