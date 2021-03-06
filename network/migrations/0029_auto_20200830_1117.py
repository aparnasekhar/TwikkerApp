# Generated by Django 3.0.8 on 2020-08-30 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0028_directmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectMessageClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('content', models.CharField(max_length=200)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_this', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_this', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='DirectMessage',
        ),
    ]
