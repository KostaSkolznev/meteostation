# Generated by Django 4.0.5 on 2022-10-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precipitation', models.CharField(max_length=25)),
                ('cloud_cover', models.CharField(max_length=25)),
                ('cloud_img', models.CharField(max_length=25)),
            ],
        ),
    ]