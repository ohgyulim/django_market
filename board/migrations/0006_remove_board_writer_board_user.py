# Generated by Django 4.0.1 on 2022-02-11 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='writer',
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
