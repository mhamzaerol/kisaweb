# Generated by Django 3.0 on 2020-09-11 07:59

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kisa_text', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=80)),
                ('phnum_eng', phone_field.models.PhoneField(max_length=31)),
                ('phnum_kor', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=20)),
                ('fb_link', models.URLField()),
                ('insta_link', models.URLField()),
                ('yt_link', models.URLField()),
            ],
        ),
    ]
