# Generated by Django 5.2.2 on 2025-06-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_filmmoreinfo_youtube_trailer_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmcomment',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
