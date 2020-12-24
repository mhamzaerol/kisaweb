# Generated by Django 3.0 on 2020-11-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_candidate_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='embed_video_ratio',
            field=models.CharField(choices=[('21by9', '21by9'), ('16by9', '16by9'), ('4by3', '4by3'), ('1by1', '1by1')], default='16by9', max_length=10),
        ),
    ]