# Generated by Django 3.0.8 on 2020-08-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_auto_20200815_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='userposts',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image/'),
        ),
    ]